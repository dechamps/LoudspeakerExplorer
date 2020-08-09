import itertools

import pandas as pd

import loudspeakerexplorer as lsx

# As defined in CTA-2034A §5.2
_FLOOR_REFLECTION_VERTICAL_ANGLES = ['-20°', '-30°', '-40°']
_CEILING_REFLECTION_VERTICAL_ANGLES = ['40°', '50°', '60°']
_FRONT_WALL_REFLECTION_HORIZONTAL_ANGLES = [
    'On-Axis', '-10°', '10°', '-20°', '20°', '-30°', '30°']
_SIDE_WALL_REFLECTION_HORIZONTAL_ANGLES = [
    '-40°', '40°', '-50°', '50°', '-60°', '60°', '-70°', '70°',
    '-80°', '80°']
# Note that there is ambiguity as to whether the rear wall reflection should be
# an average of all horizontal angles in the rear hemisphere, or if it should
# only be an average of -90°, 90° and 180°. The correct answer is the former, as
# explained here:
#   https://www.audiosciencereview.com/forum/index.php?threads/spinorama-also-known-as-cta-cea-2034-but-that-sounds-dull-apparently.10862/page-3#post-343970
_REAR_WALL_REFLECTION_HORIZONTAL_ANGLES = [
    '-90°', '90°', '-100°', '100°', '-110°', '110°', '-120°', '120°',
    '-130°', '130°', '-140°', '140°', '-150°', '150°', '-160°', '160°',
    '-170°', '170°', '-150°', '150°', '-160°', '160°', '-170°', '170°',
    '180°']
# What follows is the *WRONG* way to calculate the Rear Reflections curve, using
# -90°, 90° and 180° horizontal angles. See:
#   https://www.audiosciencereview.com/forum/index.php?threads/master-preference-ratings-for-loudspeakers.11091/page-26#post-473546
_ALT_REAR_WALL_REFLECTION_HORIZONTAL_ANGLES = ['-90°', '90°', '180°']

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

# As defined in CTA-2034A §13
_ESTIMATED_IN_ROOM_WEIGHTS = pd.Series({
    'Listening Window': 0.12,
    'Early Reflections': 0.44,
    'Sound Power': 0.44,
})


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
    return (speaker_fr.loc[:, ('Sound Pessure Level [dB]', 'SPL Vertical',
                               _FLOOR_REFLECTION_VERTICAL_ANGLES)]
            .pipe(lsx.fr.db_power_mean, axis='columns'))


def ceiling_reflection(speaker_fr):
    # As defined in CTA-2034A §5.2
    return (speaker_fr.loc[:, ('Sound Pessure Level [dB]', 'SPL Vertical',
                               _CEILING_REFLECTION_VERTICAL_ANGLES)]
            .pipe(lsx.fr.db_power_mean, axis='columns'))


def total_vertical_reflection(speaker_fr):
    # Not a standard curve, but included in the data, so we check it anyway.
    return (speaker_fr.loc[:, ('Sound Pessure Level [dB]', 'SPL Vertical',
                               _FLOOR_REFLECTION_VERTICAL_ANGLES +
                               _CEILING_REFLECTION_VERTICAL_ANGLES)]
            .pipe(lsx.fr.db_power_mean, axis='columns'))


def front_wall_reflection(speaker_fr):
    # As defined in CTA-2034A §5.2
    return (speaker_fr.loc[:, ('Sound Pessure Level [dB]', 'SPL Horizontal',
                               _FRONT_WALL_REFLECTION_HORIZONTAL_ANGLES)]
            .pipe(lsx.fr.db_power_mean, axis='columns'))


def side_wall_reflection(speaker_fr):
    # As defined in CTA-2034A §5.2
    return (speaker_fr.loc[:, ('Sound Pessure Level [dB]', 'SPL Horizontal',
                               _SIDE_WALL_REFLECTION_HORIZONTAL_ANGLES)]
            .pipe(lsx.fr.db_power_mean, axis='columns'))


def rear_wall_reflection(speaker_fr):
    # As defined in CTA-2034A §5.2
    return (speaker_fr.loc[:, ('Sound Pessure Level [dB]', 'SPL Horizontal',
                               _REAR_WALL_REFLECTION_HORIZONTAL_ANGLES)]
            .pipe(lsx.fr.db_power_mean, axis='columns'))


def alt_rear_wall_reflection(speaker_fr):
    # This function only exists to check that the input data is "consistently
    # wrong", and should not be used for any other purpose.
    return (speaker_fr.loc[:, ('Sound Pessure Level [dB]', 'SPL Horizontal',
                               _ALT_REAR_WALL_REFLECTION_HORIZONTAL_ANGLES)]
            .pipe(lsx.fr.db_power_mean, axis='columns'))


def total_horizontal_reflection(speaker_fr):
    # Not a standard curve, but included in the data, so we check it anyway.
    return (speaker_fr.loc[:, ('Sound Pessure Level [dB]', 'SPL Horizontal',
                               _FRONT_WALL_REFLECTION_HORIZONTAL_ANGLES +
                               _SIDE_WALL_REFLECTION_HORIZONTAL_ANGLES +
                               _REAR_WALL_REFLECTION_HORIZONTAL_ANGLES)]
            .pipe(lsx.fr.db_power_mean, axis='columns'))


def sound_power(speaker_fr):
    return (speaker_fr.loc[:, 'Sound Pessure Level [dB]'].loc[:, _SOUND_POWER_WEIGHTS.index]
            .pipe(lsx.fr.db_power_mean, weights=_SOUND_POWER_WEIGHTS, axis='columns'))


def alt_early_reflections(speaker_fr):
    # Note that this is *NOT* the correct way to compute the Early Reflections
    # curve. The Early Reflections curve is supposed to be an average of
    # averages, not an average of individual angles. The CTA-2034A standard is
    # ambiguous in that regard, but clarifications have been provided elsewhere:
    #   https://www.audiosciencereview.com/forum/index.php?threads/spinorama-also-known-as-cta-cea-2034-but-that-sounds-dull-apparently.10862/#post-312191
    # This function only exists to check that the input data is "consistently
    # wrong", and should not be used for any other purpose.
    return speaker_fr.loc[:, 'Sound Pessure Level [dB]'].loc[:, itertools.chain(
        (('SPL Vertical', angle)
         for angle in _FLOOR_REFLECTION_VERTICAL_ANGLES),
        (('SPL Vertical', angle)
         for angle in _CEILING_REFLECTION_VERTICAL_ANGLES),
        (('SPL Horizontal', angle)
         for angle in _FRONT_WALL_REFLECTION_HORIZONTAL_ANGLES),
        (('SPL Horizontal', angle)
         for angle in _SIDE_WALL_REFLECTION_HORIZONTAL_ANGLES),
        (('SPL Horizontal', angle) for angle in _ALT_REAR_WALL_REFLECTION_HORIZONTAL_ANGLES))
    ].pipe(lsx.fr.db_power_mean, axis='columns')


def estimated_in_room(speaker_fr):
    return (speaker_fr
            .loc[:, ('Sound Pessure Level [dB]', 'CEA2034')]
            .loc[:, _ESTIMATED_IN_ROOM_WEIGHTS.index]
            .pipe(lsx.fr.db_power_mean, weights=_ESTIMATED_IN_ROOM_WEIGHTS, axis='columns'))


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
    validate_spatial_average(
        ('Sound Pessure Level [dB]',
         'Horizontal Reflections', 'Total Horizontal Reflection'),
        total_horizontal_reflection)
    validate_spatial_average(
        ('Sound Pessure Level [dB]', 'Early Reflections', 'Rear Wall Bounce'),
        alt_rear_wall_reflection)
    validate_spatial_average(
        ('Sound Pessure Level [dB]', 'CEA2034', 'Early Reflections'),
        alt_early_reflections)
    validate_spatial_average(
        ('Sound Pessure Level [dB]', 'CEA2034', 'Sound Power'),
        sound_power)
    validate_spatial_average(
        ('Sound Pessure Level [dB]',
         'Estimated In-Room Response', 'Estimated In-Room Response'),
        estimated_in_room)
    # TODO: add Directivity Index
