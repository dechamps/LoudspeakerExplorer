import altair as alt
import numpy as np

import loudspeakerexplorer as lsx


def make_chart(
        data,
        process_before=lambda chart: chart,
        process_after=lambda chart: chart,
        *kargs, **kwargs):
    # Semantically equivalent to:
    #   base = alt.Chart(data.reset_index(), *kargs, **kwargs)
    #   process_before(process_after(base))
    #
    # Improves readability by making it possible to write the top layer
    # processing code *before* the sublayers, which matches the order in which
    # Vega processes the spec. This is especially important when it comes to
    # the order in which transforms run.
    #
    # Optimizes for minimum Vega spec size by packing unique index values
    # together and rounding long floating point numbers.

    data = (data
            # Round numbers like 0.999999999999 to prevent them from
            # unnecessarily increasing spec size.
            .apply(lambda column: np.around(column, 3), raw=True)
            .pipe(lsx.pd.implode))
    return lsx.util.pipe(
        alt.Chart(data.reset_index(), *kargs, **kwargs),
        process_after,
        lambda chart: chart.transform_flatten(data.columns.values),
        process_before)


def encode_selection(chart, selection, channel_type, selected, unselected):
    return (chart
            .add_selection(selection)
            .encode(**{channel_type: alt.condition(selection, selected, unselected)}))


def filter_selection(chart, selection):
    return (chart
            .add_selection(selection)
            .transform_filter(selection))


def interactive_line(
        chart,
        add_mark=lambda chart: chart.mark_line(clip=True, interpolate='monotone')):
    # Note that the channels should explicitly override the legend symbolType to
    #  'stroke', otherwise it gets set to 'circle' from the hidden layer, which
    # is wrong. A clear way to avoid this problem would be to make the legends
    # independent and disable the legend on the hidden layer, but that causes
    # problems with faceted charts, see:
    #   https://github.com/vega/vega-lite/issues/6261

    # This is equivalent to using the `point` line mark property.
    # The reason why we don't simply do that is because tooltips wouldn't work
    # as well due to this Vega-lite bug:
    #   https://github.com/vega/vega-lite/issues/6107
    return alt.layer(
        # Note: order is important. If the points chart comes first, legend selection doesn't work.
        lsx.util.pipe(
            chart,
            add_mark,
            lambda chart: encode_selection(
                chart, alt.selection_multi(encodings=['color'], bind='legend'),
                'opacity', alt.value(1), alt.value(0.2))),
        lsx.util.pipe(
            chart
            .mark_circle(clip=True, size=100),
            # We don't use legend_selection for points. If we do, it seems to
            # break legend interactivity in weird ways on non-faceted charts.
            lambda chart: encode_selection(chart, alt.selection_single(
                on='mouseover', clear='mouseout', empty='none',
                # We explicitly specify the encodings, as the defaults might not take
                # new fields added by transforms into account. See:
                #   https://github.com/vega/vega-lite/issues/6389
                encodings=['x', 'y']),
                'fillOpacity', alt.value(0.3), alt.value(0))
            .interactive()))
