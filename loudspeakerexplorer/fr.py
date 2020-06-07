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
