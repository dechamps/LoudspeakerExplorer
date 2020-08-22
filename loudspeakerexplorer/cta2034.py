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


def early_reflections(speaker_fr):
    # Note that CTA-2034A §5.2 is ambiguous as to whether the Early Reflections
    # curve should be an average of all early reflection angles, or an
    # average of the early reflection curves (i.e. an average of averages).
    # This was clarified to be the latter:
    #   https://www.audiosciencereview.com/forum/index.php?threads/spinorama-also-known-as-cta-cea-2034-but-that-sounds-dull-apparently.10862/#post-312191
    return (speaker_fr
            .loc[:, ('Sound Pessure Level [dB]', 'Early Reflections')]
            .loc[:, [
                'Floor Bounce', 'Ceiling Bounce', 'Front Wall Bounce',
                'Side Wall Bounce', 'Rear Wall Bounce',
            ]]
            .pipe(lsx.fr.db_power_mean, axis='columns'))


def alt_early_reflections(speaker_fr):
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


def sound_power_directivity_index(speaker_fr):
    return (speaker_fr
            .loc[:, ('Sound Pessure Level [dB]', 'CEA2034')]
            .pipe(lambda cea2034: cea2034.loc[:, 'Listening Window'] - cea2034.loc[:, 'Sound Power']))


def early_reflections_directivity_index(speaker_fr):
    return (speaker_fr
            .loc[:, ('Sound Pessure Level [dB]', 'CEA2034')]
            .pipe(lambda cea2034: cea2034.loc[:, 'Listening Window'] - cea2034.loc[:, 'Early Reflections']))


def _curve_descriptors(for_generation=False, alt_mode=False):
    def copy_of(destination, source):
        return [destination, lambda speaker_fr: speaker_fr.loc[:, source], 0]

    def copy_of_early_reflection(axis, reflection, early_reflection):
        return copy_of(
            ('Sound Pessure Level [dB]',
             'Early Reflections', early_reflection),
            ('Sound Pessure Level [dB]', f'{axis} Reflections', reflection))

    def spatial_average(destination, generate):
        # Should be accurate within rounding error of the input curves. See
        #   https://www.audiosciencereview.com/forum/index.php?threads/master-preference-ratings-for-loudspeakers.11091/page-25#post-472599
        return [destination, generate, 0.001]

    def cea2034_directivity_index(name):
        return [
            ('Sound Pessure Level [dB]', 'CEA2034', f'{name} DI'),
            lambda speaker_fr: speaker_fr.loc[:, (
                '[dB] Directivity Index ', 'Directivity Index', f'{name} DI')] +
            speaker_fr.loc[:, ('Sound Pessure Level [dB]',
                               'CEA2034', 'DI offset')],
            0.001]

    return pd.DataFrame(([
        copy_of(
            ('Sound Pessure Level [dB]', 'SPL Vertical', 'On-Axis'),
            ('Sound Pessure Level [dB]', 'SPL Horizontal', 'On-Axis')),
        copy_of(
            ('Sound Pessure Level [dB]', 'SPL Vertical', '180°'),
            ('Sound Pessure Level [dB]', 'SPL Horizontal', '180°')),
    ] if not for_generation else []) + [
        spatial_average(
            ('Sound Pessure Level [dB]',
             'Vertical Reflections', 'Floor Reflection'),
            floor_reflection),
        spatial_average(
            ('Sound Pessure Level [dB]',
             'Vertical Reflections', 'Ceiling Reflection'),
            ceiling_reflection),
        spatial_average(
            ('Sound Pessure Level [dB]',
             'Vertical Reflections', 'Total Vertical Reflection'),
            total_vertical_reflection),
        spatial_average(
            ('Sound Pessure Level [dB]', 'Horizontal Reflections', 'Front'),
            front_wall_reflection),
        spatial_average(
            ('Sound Pessure Level [dB]', 'Horizontal Reflections', 'Side'),
            side_wall_reflection),
        spatial_average(
            ('Sound Pessure Level [dB]', 'Horizontal Reflections', 'Rear'),
            rear_wall_reflection),
        spatial_average(
            ('Sound Pessure Level [dB]',
             'Horizontal Reflections', 'Total Horizontal Reflection'),
            total_horizontal_reflection),
        copy_of_early_reflection(
            'Vertical', 'Floor Reflection', 'Floor Bounce'),
        copy_of_early_reflection(
            'Vertical', 'Ceiling Reflection', 'Ceiling Bounce'),
        copy_of_early_reflection(
            'Horizontal', 'Front', 'Front Wall Bounce'),
        copy_of_early_reflection(
            'Horizontal', 'Side', 'Side Wall Bounce'),
        # https://www.audiosciencereview.com/forum/index.php?threads/master-preference-ratings-for-loudspeakers.11091/page-25#post-472466
        spatial_average(
            ('Sound Pessure Level [dB]',
             'Early Reflections', 'Rear Wall Bounce'),
            alt_rear_wall_reflection if alt_mode else rear_wall_reflection),
        spatial_average(
            ('Sound Pessure Level [dB]',
             'Early Reflections', 'Total Early Reflection'),
            alt_early_reflections if alt_mode else early_reflections),
        copy_of(
            ('Sound Pessure Level [dB]', 'CEA2034', 'On Axis'),
            ('Sound Pessure Level [dB]', 'SPL Horizontal', 'On-Axis')),
        spatial_average(
            ('Sound Pessure Level [dB]', 'CEA2034', 'Listening Window'),
            listening_window),
        copy_of(
            ('Sound Pessure Level [dB]', 'CEA2034', 'Early Reflections'),
            ('Sound Pessure Level [dB]',
             'Early Reflections', 'Total Early Reflection')),
        spatial_average(
            ('Sound Pessure Level [dB]', 'CEA2034', 'Sound Power'),
            sound_power),
        spatial_average(
            ('Sound Pessure Level [dB]',
             'Estimated In-Room Response', 'Estimated In-Room Response'),
            estimated_in_room),
        spatial_average(
            ('[dB] Directivity Index ', 'Directivity Index', 'Sound Power DI'),
            sound_power_directivity_index),
        spatial_average(
            ('[dB] Directivity Index ', 'Directivity Index', 'Early Reflections DI'),
            early_reflections_directivity_index),
    ] + ([
        cea2034_directivity_index('Sound Power'),
        cea2034_directivity_index('Early Reflections'),
    ] if not for_generation else []), columns=['Curve', 'Generator', 'Tolerance']).set_index('Curve')


def validate(speakers_fr, alt_mode=False):
    # Validates that all derived curves in the input (i.e. reflections, CTA2034,
    # DI, etc.) are consistent with the "SPL Horizontal" and "SPL Vertical" raw
    # angle data. In other words, verifies that the input is self-consistent.

    for curve_name, curve_descriptor in _curve_descriptors(
            alt_mode=alt_mode).iterrows():
        try:
            lsx.util.assert_similar(
                speakers_fr.loc[:, curve_name],
                curve_descriptor.loc['Generator'](speakers_fr),
                curve_descriptor.loc['Tolerance'])
        except:
            raise AssertionError(curve_name)


def generate(speakers_fr, alt_mode=False):
    # Generates derived curves (i.e. reflections, CTA2034, DI, etc.) based on
    # the "SPL Horizontal" and "SPL Vertical" raw angle data in the input.
    # Derived curves already present in the input are thrown away.

    speakers_fr = speakers_fr.loc[:, ('Sound Pessure Level [dB]', [
        'SPL Horizontal', 'SPL Vertical'])]
    for curve_name, curve_descriptor in _curve_descriptors(
            for_generation=True, alt_mode=alt_mode).iterrows():
        curve = curve_descriptor.loc['Generator'](speakers_fr)
        curve.name = curve_name
        # Assigning to speakers_fr.loc[:, curve_name] leads to a Pandas
        # SettingWithCopyError, so we use concat() instead.
        speakers_fr = pd.concat([speakers_fr, curve], axis='columns')
    return speakers_fr
