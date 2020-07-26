import numpy as np

import loudspeakerexplorer as lsx


def db_power_mean(frs, *kargs, **kwargs):
    # Like DataFrame.mean(), but does a power mean (assuming decibel input)
    # instead of the usual mean. "Power mean" means a root-mean-square (RMS)
    # mean applied in linear scale (i.e. Pascals, in the case of sound
    # pressure), as opposed to the logarithmic (decibel) scale. This is
    # consistent with CTA-2034A for computing spatial averages on loudspeaker
    # frequency response curves.
    return (frs
            .pipe(lsx.db.dbspl_to_pascals)
            .pipe(np.square)
            .mean(*kargs, **kwargs)
            .pipe(np.sqrt)
            .pipe(lsx.db.pascals_to_dbspl))


def smooth(fr, frequency_span):
    if frequency_span <= 1:
        # Data resolution is lower than requested smoothing - nothing to do.
        return fr
    return (
        fr
        # Ensure the input to ewm() is sorted by frequency, otherwise things
        # will get weird fast. This should already be the case, but make sure
        # regardless.
        .sort_index()
        # Note that this assumes points are equally spaced in log-frequency.
        .ewm(span=frequency_span).mean()
    )
