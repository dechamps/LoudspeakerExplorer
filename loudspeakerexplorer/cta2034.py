import loudspeakerexplorer as lsx


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
    # TODO: add Rear Wall Bounce


def validate_spatial_averages(speaker_fr):
    # Verifies that the CTA2034 spatial average curves in `speaker_fr` are
    # consistent with the individual angle frequency responses.

    def validate_spatial_average(curve, generate_spatial_average):
        lsx.util.assert_similar(
            speaker_fr.loc[:, curve],
            generate_spatial_average(speaker_fr),
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
        ('Sound Pessure Level [dB]', 'Horizontal Reflections', 'Front'),
        front_wall_reflection)
    validate_spatial_average(
        ('Sound Pessure Level [dB]', 'Horizontal Reflections', 'Side'),
        side_wall_reflection)
    # TODO: add Rear Wall Bounce
    # TODO: add Sound Power
    # TODO: add Early Reflections
    # TODO: add Directivity Index
    # TODO: add Predicted In-Room Response
