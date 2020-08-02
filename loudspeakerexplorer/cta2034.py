import pandas as pd

import loudspeakerexplorer as lsx

# As defined in CTA-2034A Appendix C
# See also:
#   https://www.audiosciencereview.com/forum/index.php?threads/master-preference-ratings-for-loudspeakers.11091/page-25#post-472599
_SOUND_POWER_WEIGHTS = (pd.Series({
    'On-Axis': 0.000604486,
    '10°':     0.004730189,
    '20°':     0.008955027,
    '30°':     0.012387354,
    '40°':     0.014989611,
    '50°':     0.016868154,
    '60°':     0.018165962,
    '70°':     0.019006744,
    '80°':     0.019477787,
    '90°':     0.019629373,
    '100°':    0.019477787,
    '110°':    0.019006744,
    '120°':    0.018165962,
    '130°':    0.016868154,
    '140°':    0.014989611,
    '150°':    0.012387354,
    '160°':    0.008955027,
    '170°':    0.004730189,
})
    .pipe(lambda semicircle: pd.concat([semicircle, semicircle.rename(
        lambda angle: '180°' if angle == 'On-Axis' else f'-{angle}')]))
    .pipe(lambda circle: pd.concat({
        'SPL Horizontal': circle,
        # 0° and 180° are the same measurement on both horizontal and vertical
        # planes. Don't count them twice.
        'SPL Vertical': circle.drop(['On-Axis', '180°']),
    })))


def listening_window(speaker_fr):
    # As defined in CTA-2034A §5.2
    return speaker_fr.loc[:, 'Sound Pessure Level [dB]'].loc[:, [
        ('SPL Horizontal', 'On-Axis'),
        ('SPL Vertical',   '-10°'),
        ('SPL Vertical',    '10°'),
        ('SPL Horizontal', '-10°'),
        ('SPL Horizontal',  '10°'),
        ('SPL Horizontal', '-20°'),
        ('SPL Horizontal',  '20°'),
        ('SPL Horizontal', '-30°'),
        ('SPL Horizontal',  '30°'),
    ]].pipe(lsx.fr.db_power_mean, axis='columns')


def floor_reflection(speaker_fr):
    # As defined in CTA-2034A §5.2
    return (speaker_fr.loc[:, ('Sound Pessure Level [dB]', 'SPL Vertical', [
        '-20°', '-30°', '-40°'])]
        .pipe(lsx.fr.db_power_mean, axis='columns'))


def ceiling_reflection(speaker_fr):
    # As defined in CTA-2034A §5.2
    return (speaker_fr.loc[:, ('Sound Pessure Level [dB]', 'SPL Vertical', [
        '40°', '50°', '60°'])]
        .pipe(lsx.fr.db_power_mean, axis='columns'))


def total_vertical_reflection(speaker_fr):
    # Not a standard curve, but included in the data, so we check it anyway.
    return (speaker_fr.loc[:, ('Sound Pessure Level [dB]', 'Vertical Reflections', [
        'Floor Reflection', 'Ceiling Reflection'])]
        .pipe(lsx.fr.db_power_mean, axis='columns'))


def front_wall_reflection(speaker_fr):
    # As defined in CTA-2034A §5.2
    return speaker_fr.loc[:, ('Sound Pessure Level [dB]', 'SPL Horizontal', [
        'On-Axis', '-10°', '10°', '-20°', '20°', '-30°', '30°',
    ])].pipe(lsx.fr.db_power_mean, axis='columns')


def side_wall_reflection(speaker_fr):
    # As defined in CTA-2034A §5.2
    return speaker_fr.loc[:, ('Sound Pessure Level [dB]', 'SPL Horizontal', [
        '-40°', '40°', '-50°', '50°', '-60°', '60°', '-70°', '70°',
        '-80°', '80°',
    ])].pipe(lsx.fr.db_power_mean, axis='columns')


def rear_wall_reflection(speaker_fr):
    # As defined in CTA-2034A §5.2
    # Note that there is ambiguity as to whether this should be an average of
    # all horizontal angles in the rear hemisphere, or if it should only be an
    # average of -90°, 90° and 180°. The correct answer is the former, as
    # explained here:
    #   https://www.audiosciencereview.com/forum/index.php?threads/spinorama-also-known-as-cta-cea-2034-but-that-sounds-dull-apparently.10862/page-3#post-343970
    return speaker_fr.loc[:, ('Sound Pessure Level [dB]', 'SPL Horizontal', [
        '-90°', '90°', '-100°', '100°', '-110°', '110°', '-120°', '120°',
        '-130°', '130°', '-140°', '140°', '-150°', '150°', '-160°', '160°',
        '-170°', '170°', '-150°', '150°', '-160°', '160°', '-170°', '170°',
        '180°',
    ])].pipe(lsx.fr.db_power_mean, axis='columns')


def alt_rear_wall_reflection(speaker_fr):
    # The *WRONG* way to calculate the Rear Reflections curve, using -90°, 90°
    # and 180° horizontal angles. This function only exists to check that the
    # input data is "consistently wrong". See:
    #   https://www.audiosciencereview.com/forum/index.php?threads/master-preference-ratings-for-loudspeakers.11091/page-26#post-473546
    return speaker_fr.loc[:, ('Sound Pessure Level [dB]', 'SPL Horizontal', [
        '-90°', '90°', '180°'])].pipe(lsx.fr.db_power_mean, axis='columns')


def sound_power(speaker_fr):
    return (speaker_fr.loc[:, 'Sound Pessure Level [dB]'].loc[:, _SOUND_POWER_WEIGHTS.index]
            .pipe(lsx.fr.db_power_mean, weights=_SOUND_POWER_WEIGHTS, axis='columns'))


def validate_early_reflections(speaker_fr):
    # Verifies that the data in "Horizontal Reflections" and "Vertical
    # Reflections" is identical to the data in "Early Reflections".

    def validate_early_reflection(axis, reflection, early_reflection):
        lsx.util.assert_similar(
            speaker_fr.loc[:, ('Sound Pessure Level [dB]',
                               f'{axis} Reflections', reflection)],
            speaker_fr.loc[:, ('Sound Pessure Level [dB]',
                               'Early Reflections', early_reflection)])

    validate_early_reflection('Vertical', 'Floor Reflection', 'Floor Bounce')
    validate_early_reflection(
        'Vertical', 'Ceiling Reflection', 'Ceiling Bounce')
    validate_early_reflection(
        'Horizontal', 'Front', 'Front Wall Bounce')
    validate_early_reflection(
        'Horizontal', 'Side', 'Side Wall Bounce')
    # Rear deliberately left out because the data in "Early Reflections" is
    # known to be wrong. See:
    #   https://www.audiosciencereview.com/forum/index.php?threads/master-preference-ratings-for-loudspeakers.11091/page-25#post-472466


def validate_common_angles(speaker_fr):
    # Verifies that redundant single-angle data, e.g. On-Axis, is the same
    # everywhere in the input.

    def assert_similar_curve(index1, index2):
        lsx.util.assert_similar(
            speaker_fr.loc[:, index1], speaker_fr.loc[:, index2])

    assert_similar_curve(
        ('Sound Pessure Level [dB]', 'SPL Horizontal', 'On-Axis'),
        ('Sound Pessure Level [dB]', 'SPL Vertical', 'On-Axis'))
    assert_similar_curve(
        ('Sound Pessure Level [dB]', 'SPL Horizontal', '180°'),
        ('Sound Pessure Level [dB]', 'SPL Vertical', '180°'))
    assert_similar_curve(
        ('Sound Pessure Level [dB]', 'CEA2034', 'On Axis'),
        ('Sound Pessure Level [dB]', 'SPL Horizontal', 'On-Axis'))
    assert_similar_curve(
        ('Sound Pessure Level [dB]', 'CEA2034', 'Early Reflections'),
        ('Sound Pessure Level [dB]', 'Early Reflections', 'Total Early Reflection'))


def validate_spatial_averages(speaker_fr):
    # Verifies that the CTA2034 spatial average curves in `speaker_fr` are
    # consistent with the individual angle frequency responses.

    def validate_spatial_average(curve, generate_spatial_average):
        lsx.util.assert_similar(
            speaker_fr.loc[:, curve],
            generate_spatial_average(speaker_fr),
            # Should be accurate within rounding error of the input curves. See
            #   https://www.audiosciencereview.com/forum/index.php?threads/master-preference-ratings-for-loudspeakers.11091/page-25#post-472599
            tolerance=0.001)

    validate_spatial_average(
        ('Sound Pessure Level [dB]', 'CEA2034', 'Listening Window'),
        listening_window)
    validate_spatial_average(
        ('Sound Pessure Level [dB]',
         'Vertical Reflections', 'Floor Reflection'),
        floor_reflection)
    validate_spatial_average(
        ('Sound Pessure Level [dB]',
         'Vertical Reflections', 'Ceiling Reflection'),
        ceiling_reflection)
    validate_spatial_average(
        ('Sound Pessure Level [dB]',
         'Vertical Reflections', 'Total Vertical Reflection'),
        total_vertical_reflection)
    validate_spatial_average(
        ('Sound Pessure Level [dB]', 'Horizontal Reflections', 'Front'),
        front_wall_reflection)
    validate_spatial_average(
        ('Sound Pessure Level [dB]', 'Horizontal Reflections', 'Side'),
        side_wall_reflection)
    validate_spatial_average(
        ('Sound Pessure Level [dB]', 'Horizontal Reflections', 'Rear'),
        rear_wall_reflection)
    # Not validating "Total Horizontal Reflection" because it's not clear how
    # it's computed - the obvious choices of (Front+Side+Rear) or
    # (Front+Side+Rear Wall Bounce) don't work.
    validate_spatial_average(
        ('Sound Pessure Level [dB]', 'Early Reflections', 'Rear Wall Bounce'),
        alt_rear_wall_reflection)
    validate_spatial_average(
        ('Sound Pessure Level [dB]', 'CEA2034', 'Sound Power'),
        sound_power)
    # TODO: add Early Reflections
    # TODO: add Directivity Index
    # TODO: add Predicted In-Room Response
