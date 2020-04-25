import altair as alt

import loudspeakerexplorer as lsx


def interactive_line(
        chart, legend_channel,
        add_mark=lambda chart: chart.mark_line(clip=True, interpolate='monotone')):
    # Note that `legend_channel` should explicitly override the legend
    # symbolType to 'stroke', otherwise it gets set to 'circle' from the hidden
    # layer, which is wrong. A clear way to avoid this problem would be to make
    # the legends independent and disable the legend on the hidden layer, but
    # that causes problems with faceted charts, see:
    #   https://github.com/vega/vega-lite/issues/6261

    mouseover_selection = alt.selection_single(
        on='mouseover', empty='none',
        # We explicitly specify the encodings, as the defaults might not take
        # new fields added by transforms into account. See:
        #   https://github.com/vega/vega-lite/issues/6389
        encodings=['x', 'y'])
    legend_selection = alt.selection_multi(encodings=['color'], bind='legend')
    # This is equivalent to using the `point` line mark property.
    # The reason why we don't simply do that is because tooltips wouldn't work
    # as well due to this Vega-lite bug:
    #   https://github.com/vega/vega-lite/issues/6107
    return alt.layer(
        # Note: order is important. If the points chart comes first, legend selection doesn't work.
        add_mark(chart)
        .add_selection(legend_selection)
        .encode(
            legend_channel,
            opacity=alt.condition(
                legend_selection, alt.value(1), alt.value(0.2))
        ),
        chart
        .mark_circle(clip=True, size=100)
        .add_selection(mouseover_selection)
        .encode(
            # We don't use legend_selection for points. If we do, it seems to
            # break legend interactivity in weird ways on non-faceted charts.
            legend_channel,
            fillOpacity=alt.condition(
                mouseover_selection, alt.value(0.3), alt.value(0)))
        .interactive())
