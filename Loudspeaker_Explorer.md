---
jupyter:
  colab:
    name: Loudspeaker Explorer
    toc_visible: true
  hide_input: true
  jupytext:
    cell_metadata_filter: heading_collapsed,id,tags,scrolled,-hidden
    notebook_metadata_filter: colab,-jupytext.text_representation.jupytext_version,hide_input,toc.toc_window_display,toc
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
  toc:
    toc_window_display: true
---

<!-- #region id="view-in-github" -->
<!-- The "view-in-github" magic section ID is handled specially by Colab, which will not show its contents. Note that this only seems to work if this is the first section. -->
**You are viewing the source version of the Loudspeaker Explorer notebook.** You can also open the ready-to-use, published version in [Colab]((https://colab.research.google.com/github/dechamps/LoudspeakerExplorer-rendered/blob/master/Loudspeaker_Explorer.ipynb)).

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/dechamps/LoudspeakerExplorer-rendered/blob/master/Loudspeaker_Explorer.ipynb)
<!-- #endregion -->

<!-- #region tags=["buildinfo"] -->

# The Loudspeaker Explorer

_By [Etienne Dechamps](https://www.audiosciencereview.com/forum/index.php?members/edechamps.4453/) (etienne@edechamps.fr)_ - [ASR thread](https://www.audiosciencereview.com/forum/index.php?threads/loudspeaker-explorer-analyze-visualize-compare-speaker-data.11503/) - [GitHub](https://github.com/dechamps/LoudspeakerExplorer)<!--BUILDINFO-->

**All data provided by [amirm](https://www.audiosciencereview.com/forum/index.php?members/amirm.2/) from [AudioScienceReview](https://www.audiosciencereview.com/). Consider [making a donation](https://www.audiosciencereview.com/forum/index.php?threads/how-to-support-audio-science-review.8150/) if you enjoy the use of this data.**

Welcome to the [Loudspeaker Explorer](https://colab.research.google.com/github/dechamps/LoudspeakerExplorer-rendered/blob/master/Loudspeaker_Explorer.ipynb), a speaker measurement visualization, analysis and comparison tool. This is an interactive [Colaboratory Notebook](https://colab.research.google.com/).

## How to use this notebook

To run the code and (re)generate the data, go to the **Runtime** menu and click **Run all** (CTRL+F9). **You will need to repeat this every time you change any of the settings or code** (e.g. if you enable or disable speakers).

**All the charts are interactive.** Use the mousewheel to zoom, and drag & drop to pan. Click on a legend entry to highlight a single response; hold shift to highlight multiple responses. Double-click to reset the view. (PROTIP: to quickly switch back and forth between speakers, select the speaker dropdown, then use the left-right arrow keys on your keyboard.)

**Charts can take a few seconds to load when scrolling**, especially if you're using the notebook for the first time. Be patient.

**Charts will not be generated if the section they're under is folded while the notebook is running.** To manually load a chart after running the notebook, click on the square to the left of the *Show Code* button. Or simply use *Run all* again after unfolding the section.

### Other ways to run this notebook

If you don't have a Google account, or don't want to use Colab for any other reason, the following alternatives are available:

- **[Binder](https://mybinder.org/v2/gh/dechamps/LoudspeakerExplorer/master?filepath=Loudspeaker_Explorer.ipynb)**: similar to Colab. Can take a (very) long time to load the first time; be patient. To run the notebook after it's loaded, go to the **Kernel** menu and click **Restart & Run All**.
- **[Run locally](https://github.com/dechamps/LoudspeakerExplorer#developer-information)**: clone the Github repository and follow the developer instructions to run the Notebook on your local machine. This is not an easy option as it requires you to set up a Python environment. This is useful if you want maximum performance, if you want to make significant changes to the code, or if you want to contribute to Loudspeaker Explorer.

## Acknowledgments

None of this would have been possible without [amirm](https://www.audiosciencereview.com/forum/index.php?members/amirm.2/)'s [tremendous work](https://www.audiosciencereview.com/forum/index.php?threads/announcement-asr-will-be-measuring-speakers.10725/) in measuring speakers. All the data used by this tool is from measurements made by amirm for [AudioScienceReview](https://www.audiosciencereview.com/). If you like what you see, [consider making a donation](https://www.audiosciencereview.com/forum/index.php?threads/how-to-support-audio-science-review.8150/).

This notebook is powered by amazing software: [Google Colaboratory](https://colab.research.google.com/), [Jupyter](https://jupyter.org/), [Jupytext](https://github.com/mwouts/jupytext), [Pandas](https://pandas.pydata.org/), [Altair](https://altair-viz.github.io/), and [statsmodels](https://www.statsmodels.org/).

## License

The *code* and accompanying text of Loudspeaker Explorer is published under [MIT License](https://github.com/dechamps/LoudspeakerExplorer/blob/master/LICENSE.txt).

The *measurement data* is not part of Loudspeaker Explorer - it is published by Audio Science Review LLC under the [Creative Commons BY-NC-SA 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/). Because this is a "share alike" license, **all data generated by Loudspeaker Explorer, including the charts, is de facto licensed under these terms as well**. Note that these license terms do not apply to measurements published before 2020-03-02, as these do not come with a clear license.

## Other tools

You might also be interested in:

 - [pozz](https://www.audiosciencereview.com/forum/index.php?members/pozz.7752/)'s [ASR Speaker Review and Measurement Index](https://www.audiosciencereview.com/forum/index.php?pages/SpeakerTestData/)
 - [MZKM](https://www.audiosciencereview.com/forum/index.php?members/mzkm.4645/)'s [Preference Rating data](https://docs.google.com/spreadsheets/d/e/2PACX-1vRVN63daR6Ph8lxhCDUEHxWq_gwV0wEjL2Q1KRDA0J4i_eE1JS-JQYSZy7kCQZMKtRnjTOn578fYZPJ/pubhtml)
 - [pierre](https://www.audiosciencereview.com/forum/index.php?members/pierre.344/)'s [Spinorama visualizations](https://pierreaubert.github.io/spinorama/)
<!-- #endregion -->
<!-- #region heading_collapsed=true -->
# Preliminary boilerplate
<!-- #endregion -->

```python
LOUDSPEAKER_EXPLORER_PRERENDERED_GIT_SHA = None
###INJECT_LOUDSPEAKER_EXPLORER_PRERENDERED_GIT_SHA###  # Variable assignment injected by continuous integration process

import sys
import os
import shutil
import pathlib
import re

if LOUDSPEAKER_EXPLORER_PRERENDERED_GIT_SHA is not None and 'COLAB_GPU' in os.environ:
    def read_git_sha(directory):
        try:
            with open(directory / '.loudspeaker_explorer_git_sha', mode='r') as git_sha_file:
                return git_sha_file.read()
        except FileNotFoundError:
            return None

    current_git_sha = read_git_sha(pathlib.Path('.'))
    if current_git_sha is None:
        current_git_sha = read_git_sha(pathlib.Path('LoudspeakerExplorer'))
        if current_git_sha is not None:
            os.chdir('LoudspeakerExplorer')
            
    if current_git_sha != LOUDSPEAKER_EXPLORER_PRERENDERED_GIT_SHA:
        if current_git_sha is not None:
            # An already running Colab instance has opened a different version of the notebook.
            # (It's not clear if this can actually happen in practice, but err on the safe side nonetheless…)
            os.chdir('..')
            shutil.rmtree('LoudspeakerExplorer')
        os.mkdir('LoudspeakerExplorer')
        os.chdir('LoudspeakerExplorer')
        !curl --location -- 'https://github.com/dechamps/LoudspeakerExplorer/tarball/{LOUDSPEAKER_EXPLORER_PRERENDERED_GIT_SHA}' | tar --gzip --extract --strip-components=1
        # https://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter/
        !{sys.executable} -m pip install --requirement requirements.txt --progress-bar=off
        with open('.loudspeaker_explorer_git_sha', mode='w') as git_sha_file:
            git_sha_file.write(LOUDSPEAKER_EXPLORER_PRERENDERED_GIT_SHA)

import numpy as np
import pandas as pd
import IPython
import ipywidgets as widgets
import dominate
import altair as alt
import yaml
import statsmodels.formula.api as smf

import loudspeakerexplorer as lsx
```

```python
settings = lsx.Settings(pathlib.Path('settings.json'))

prerender_mode = bool(os.environ.get('LOUDSPEAKER_EXPLORER_PRERENDER', default=False))

def banner(*children):
    banner = dominate.tags.div(
            style='text-align: left; padding: 0.5ex 1ex; padding-left: 1ex; border: 2px solid red; background-color: #eee')
    banner.add(*children)
    return banner

def form(widget):
    form_banner = widgets.HTML()
    def set_form_banner(*children):
        form_banner.value = str(banner(children))
    if prerender_mode:
        form_banner.value = str(banner(
            dominate.tags.strong('Settings disabled'),
            dominate.util.text(' because the notebook is not running. Run the notebook (in Colab, "Runtime" → "Run All") to change settings.')))
        def disable_widget(widget):
            widget.disabled = True
        lsx.util.recurse_attr(widget, 'children', disable_widget)
    lsx.util.recurse_attr(widget, 'children',
        lambda widget: widget.observe(
            lambda change: set_form_banner(
                dominate.tags.strong('Settings have changed.'),
                dominate.util.text(' Run the notebook again (in Colab, "Runtime" → "Run All") for the changes to take effect.'))))
    lsx.ipython.display_css('''
        .widget-checkbox *, .widget-radio-box * { cursor: pointer; }
    ''')
    if prerender_mode:
        lsx.ipython.display_css('''
            /*
                Don't show the broken chain "disconnected" icon as it messes up the form layouts, and it's redundant with the banner.
                We only hide it in pre-render - in live runs, we do want the user to notice if the kernel is disconnected.
            */
            .jupyter-widgets-disconnected::before { content: none; }
        ''')
    return widgets.VBox([form_banner, widget])

if LOUDSPEAKER_EXPLORER_PRERENDERED_GIT_SHA is not None:
    print('Prerendered from Git commit', LOUDSPEAKER_EXPLORER_PRERENDERED_GIT_SHA)
print(settings)
```

# Speaker selection

This is the most important setting. Here you can select the speakers you wish to analyze and compare. See below for more information on each speaker. **You will have to run the notebook by clicking "Runtime" → "Run all" before you can change the selection.**

Note that the following speakers, despite having been measured by amirm, are not (yet) available in this tool:

 - [**Buchardt S400 (sample 2)**](https://www.audiosciencereview.com/forum/index.php?threads/buchardt-s400-speaker-review.12844/page-13#post-382821): the raw data was not published. The data shown here is for the [first sample](https://www.audiosciencereview.com/forum/index.php?threads/buchardt-s400-speaker-review.12844/).
 - [**Genelec 8341A (before treble ripple issue fix)**](https://www.audiosciencereview.com/forum/index.php?threads/genelec-8341a-sam%E2%84%A2-studio-monitor-review.11652/page-2#post-335133): the raw data was [not published](https://www.audiosciencereview.com/forum/index.php?threads/genelec-8341a-sam%E2%84%A2-studio-monitor-review.11652/page-5#post-335291). The data shown here is from the [fixed](https://www.audiosciencereview.com/forum/index.php?threads/genelec-8341a-sam%E2%84%A2-studio-monitor-review.11652/#post-335109) [measurement](https://www.audiosciencereview.com/forum/index.php?threads/genelec-8341a-sam%E2%84%A2-studio-monitor-review.11652/).
 - [**Kali IN-8 (damaged sample)**](https://www.audiosciencereview.com/forum/index.php?threads/kali-audio-in-8-studio-monitor-review.10897/): the raw data was not published. The data shown here is for the [good sample](https://www.audiosciencereview.com/forum/index.php?threads/kali-audio-in-8-studio-monitor-review.10897/page-29#post-318617).
 - [**Neumann KH80 (sample 2, low order)**](https://www.audiosciencereview.com/forum/index.php?threads/neumann-kh-80-dsp-speaker-measurements-take-two.11323/): the raw data was not published. The data shown here is from the [high order measurement](https://www.audiosciencereview.com/forum/index.php?threads/neumann-kh-80-dsp-speaker-measurements-take-two.11323/page-12#post-324456).
 - [**NHT Pro M-00**](https://www.audiosciencereview.com/forum/index.php?threads/nht-pro-m-00-powered-monitor-review.10859/): the [raw data published](https://www.audiosciencereview.com/forum/index.php?threads/speaker-equivalent-sinad-discussion.10818/page-7#post-306521) is [incomplete](https://www.audiosciencereview.com/forum/index.php?threads/speaker-equivalent-sinad-discussion.10818/page-14#post-424713).
 - [**Yamaha HS5**](https://www.audiosciencereview.com/forum/index.php?threads/yamaha-hs5-powered-monitor-review.10967/): the raw data published is incomplete.
 
Also keep in mind the following known issues with the measurements:

 - **[Low frequency measurement errors](https://www.audiosciencereview.com/forum/index.php?threads/jbl-hdi-3600-speaker-review.13027/page-2#post-389147)** (below 100 Hz or so) are present in measurements made before 2020-05-03. This was [fixed](https://www.audiosciencereview.com/forum/index.php?threads/jbl-hdi-3600-speaker-review.13027/) in the JBL HDI-3600 measurement.
 - A [measurement artefact](https://www.audiosciencereview.com/forum/index.php?threads/klipsch-r-41m-bookshelf-speaker-review.11566/page-3#post-332136) in the form of a slight **[ripple in high frequencies](https://www.audiosciencereview.com/forum/index.php?threads/neumann-kh-80-dsp-speaker-measurements-take-two.11323/page-10#post-324189)** (above 4 kHz or so) is present in all measurements made before 2020-02-23. This was [fixed](https://www.audiosciencereview.com/forum/index.php?threads/genelec-8341a-sam%E2%84%A2-studio-monitor-review.11652/#post-335109) starting from the Genelec 8341A measurement.
 - Klippel uses slightly wrong weights to compute the **Early Reflections** and **Estimated In-Room Response** curves. See the Early Reflections and Estimated In-Room Response sections, below, for details. Loudspeaker Explorer displays the Klippel data as-is and does not (yet) attempt to correct it.
 - Datasets for **JBL 305P MkII** and **Neumann KH80 (sample 1)** are missing *Directivity Index* data. Due to a bug in the tool this also breaks the Spinorama charts unless another speaker is also selected.
 - The **Revel F35** measurement suffers from [numerical computation issues](https://www.audiosciencereview.com/forum/index.php?threads/revel-f35-speaker-review.12053/page-20#post-354889) that cause erroneous spikes around 1 kHz.
 - The **Sony SS-CS5** measurement is inaccurate at high frequencies because [an erroneous measurement axis was used](https://www.audiosciencereview.com/forum/index.php?threads/sony-ss-cs5-3-way-speaker-review.13562/page-5#post-409981).
 - The very first measurements (**JBL Control 1 Pro** and **JBL 305P MkII**) were only published in 10 points/octave resolution. [This is also the case](https://www.audiosciencereview.com/forum/index.php?threads/revel-f208-tower-speaker-review.13192/page-7#post-394941) for the **Revel F208**.

```python scrolled=false
speakers = {}
for speaker_dir in pathlib.Path('speaker_data').iterdir():
    try:
        with (speaker_dir / 'speaker_metadata.yaml').open(mode='r') as speaker_metadata_file:
            speakers[speaker_dir.name] = yaml.safe_load(speaker_metadata_file)
    except (FileNotFoundError, NotADirectoryError):
        continue
speakers = (pd.DataFrame.from_dict(speakers, orient='index')
    .rename_axis('Speaker'))

speakers = speakers.iloc[speakers.index.to_series().str.casefold().argsort()]

speakers.loc[:, 'Measurement Date'] = pd.to_datetime(speakers.loc[:, 'Measurement Date'])

speakers.loc[:, 'Enabled'] = speakers.index.isin(
    speakers.loc[:, 'Measurement Date'].nlargest(3).index)

speaker_checkboxes = []
def speaker_box(speaker):
    box = widgets.VBox()
    
    def checkbox():
        speaker_copy = speaker.copy()
        def speaker_change(new):
            speakers.loc[speaker_copy.name, 'Enabled'] = new
            if new:
                box.add_class('lsx-speaker-enabled')
            else:
                box.remove_class('lsx-speaker-enabled')
        checkbox = settings.track_widget(
            ('speakers', 'enabled', speaker_copy.name),
            widgets.Checkbox(value=speaker_copy.loc['Enabled'], description=speaker_copy.name, style={'description_width': 'initial'}),
            speaker_change)
        checkbox.add_class('lsx-speaker-checkbox')
        speaker_checkboxes.append(checkbox)
        return checkbox

    def img():
        box = widgets.Box([widgets.HTML(str(
            dominate.tags.img(src=speaker.loc['Picture URL'])))])
        box.layout.height = '150px'
        box.layout.width = '100px'
        return box
    
    def info():
        span = dominate.tags.span()
        with span:
            product_url = speaker.loc['Product URL']
            if not pd.isna(product_url):
                dominate.tags.a('Product page', href=product_url, target='_blank')
                dominate.util.text(' - ')
            dominate.tags.a('Review', href=speaker.loc['Review URL'], target='_blank')
            dominate.tags.br()
            dominate.util.text('Active' if speaker.loc['Active'] else 'Passive')
            dominate.tags.br()
            dominate.util.text('${:.0f} (single)'.format(speaker.loc['Price (Single, USD)']))
            dominate.tags.br()
            dominate.util.text('Measured ' + str(speaker.loc['Measurement Date'].date()))
        return widgets.HTML(str(span))

    box.children = (
        checkbox(),
        # Note: not using widgets.Image() because Colab doesn't support that. See https://github.com/googlecolab/colabtools/issues/587
        widgets.HBox([img(), info()])
    )
    box.add_class('lsx-speaker')
    box.layout.margin = '5px'
    box.layout.padding = '5px'
    return box

# Colab does not recognize the scrolled=false cell metadata.
# Simulate it using the technique described at https://github.com/googlecolab/colabtools/issues/541
# Note that this only has an effect in Colab. The reason we don't add that line as part of Continuous Integration is because the Javascript to be present in prerender *and* run.
IPython.display.display(IPython.display.Javascript('''
    try { google.colab.output.setIframeHeight(0, true, {maxHeight: 5000}) }
    catch (e) {}
'''))

lsx.ipython.display_css('''
    .lsx-speaker { background-color: #f6f6f6; }
    .lsx-speaker * {
        /* required in Colab to avoid scrollbars on images */
        overflow: hidden;
    }
    .lsx-speaker label { font-weight: bold; }
    .lsx-speaker-enabled { background-color: #dcf5d0; }
    .lsx-speaker-checkbox label { width: 100%; }
    .lsx-speaker img {
        max-height: 100%;
        max-width: 100%;  /* required in Colab */
    }
''')

def speakers_set_all_button(enabled, **kwargs):
    button = widgets.Button(**kwargs)
    def set_all(_):
        for checkbox in speaker_checkboxes:
            checkbox.value = enabled
    button.on_click(set_all)
    button.style.font_weight = 'bold'
    return button

speakers_box = widgets.HBox(list(speakers.apply(speaker_box, axis='columns')))
speakers_box.layout.flex_flow = 'row wrap'
form(widgets.VBox([
    widgets.HBox([
        speakers_set_all_button(True, description='Select all'),
        speakers_set_all_button(False, description='Unselect all'),
    ]),
    speakers_box,
]))
```

<!-- #region heading_collapsed=true -->
# Data intake
<!-- #endregion -->

This loads all data from all speakers into a single, massive `speaker_fr_raw`
DataFrame. The DataFrame index is arranged by speaker name, then frequency. All
data files for each speaker are merged to form the columns of the DataFrame.

```python
speakers_fr_raw = pd.concat(
  {speaker.Index: lsx.data.load_speaker(pathlib.Path('speaker_data') / speaker.Index) for speaker in speakers[speakers['Enabled']].itertuples()},
  names=['Speaker'], axis='rows')
speakers_fr_raw
```

<!-- #region heading_collapsed=true -->
# Raw data summary

Basic information about loaded data, including frequency bounds and resolution.
<!-- #endregion -->

```python
speakers_frequencies = speakers_fr_raw.pipe(lsx.pd.index_as_columns).groupby('Speaker')
speakers_frequency_count = speakers_frequencies.count().loc[:, 'Frequency [Hz]'].rename('Frequencies')
speakers_min_frequency = speakers_frequencies.min().loc[:, 'Frequency [Hz]'].rename('Min Frequency (Hz)')
speakers_max_frequency = speakers_frequencies.max().loc[:, 'Frequency [Hz]'].rename('Max Frequency (Hz)')
speakers_octaves = (speakers_max_frequency / speakers_min_frequency).apply(np.log2).rename('Extent (octaves)')
speakers_freqs_per_octave = (speakers_frequency_count / speakers_octaves).rename('Mean resolution (freqs/octave)')
pd.concat([
  speakers_frequency_count,
  speakers_min_frequency,
  speakers_max_frequency,
  speakers_octaves,
  speakers_freqs_per_octave
], axis='columns')
```

<!-- #region heading_collapsed=true -->
# Sensitivity

This calculates a single sensitivity value for each speaker using the **mean on-axis SPL** in a configurable frequency band. The result can then be used as the basis for normalization (see next section).
<!-- #endregion -->

The recommended frequency band is **200-400 Hz**, as it appears to be the most appropriate for normalization - c.f. [Olive](http://www.aes.org/e-lib/online/browse.cfm?elib=12847) (section 3.2.1):

> The use of a reference band of 200-400 Hz is based
> on an observation made in Part One (see section 4.8
> of Part 1). When asked to judge the spectral balance of
> each loudspeaker across 6 frequency bands, listeners
> referenced or anchored their judgments to the band
> centered around 200 Hz. One plausible explanation is
> that many of the fundamentals of instruments,
> including voice, fall within 200-400 Hz, and the
> levels of the higher harmonics are referenced to it.

Note that in other contexts a band centered around 1 kHz is often used.

**CAUTION:** take the numbers in the below table with a grain of salt. Indeed the raw measurement data is using the wrong absolute scale for some speakers, especially active ones.

```python
def frequency_slider(**kwargs):
    return widgets.FloatLogSlider(base=10, min=np.log10(20), max=np.log10(20000), step=0.1, readout_format='.2s', layout=widgets.Layout(width='90%'), **kwargs)

sensitivity_first_frequency_hz = settings.track_widget(
    ('sensitivity', 'first_frequency_hz'),
    frequency_slider(value=200, description='First frequency (Hz)', style={'description_width': 'initial'}))
sensitivity_last_frequency_hz = settings.track_widget(
    ('sensitivity', 'last_frequency_hz'),
    frequency_slider(value=400, description='Last frequency (Hz)', style={'description_width': 'initial'}))

form(widgets.VBox([sensitivity_first_frequency_hz, sensitivity_last_frequency_hz]))
```

```python
sensitivity_input_column = ('Sound Pessure Level [dB]', 'CEA2034', 'On Axis')
speakers_sensitivity = (speakers_fr_raw
  .loc[speakers_fr_raw.index.to_frame()['Frequency [Hz]'].between(sensitivity_first_frequency_hz.value, sensitivity_last_frequency_hz.value), sensitivity_input_column]
  .mean(level='Speaker'))
speakers_sensitivity.to_frame()
```

<!-- #region heading_collapsed=true -->
# Normalization & detrending

This step normalizes *all* SPL frequency response data (on-axis, spinorama, off-axis, estimated in-room response, etc.).
<!-- #endregion -->

The data is normalized according to the `normalization_mode` variable, which can take the following values:

 - **None**: raw absolute SPL values are carried over as-is.
 - **Equal sensitivity** (recommended): sensitivity values calculated in the previous section are subtracted from all SPL values of each speaker, such that all speakers have 0 dB sensitivity. Improves readability and makes it easier to compare speakers.
 - **Flat on-axis**: the on-axis SPL value is subtracted to itself as well as every other SPL variable at each frequency. In other words this simulates EQ'ing every speaker to be perfectly flat on-axis. Use this mode to focus solely on directivity data.
 - **Flat listening window**: same as above, using the Listening Window average instead of On-Axis.
 - **Detrend**: for each speaker, computes a smoothed response (using the same mechanism as described in the *Smoothing* section below), then subtracts it from the original responses. In other words, this is the opposite of smoothing. Useful for removing trends (e.g. overall bass/treble balance) to focus solely on local variations.
 
## Detrending settings
 
If **Detrend each response individually** is checked, individual responses are smoothed and subtracted independently of each other, *including* directivity indices. Otherwise, a smoothed version of the **Detrending reference** will be subtracted to all responses for that speaker, *excluding* directivity indices.

The **Detrending strength** is the strength of the smoothing applied to the subtracted response.

```python
detrend_reference = settings.track_widget(
    ('normalization', 'detrend', 'reference'),
    widgets.RadioButtons(
        description='Detrending reference',
        options=['On Axis', 'Listening Window', 'Early Reflections', 'Sound Power'], value='On Axis',
        style={'description_width': 'initial'},
        layout={'width': 'max-content'}))
detrend_individually = settings.track_widget(
    ('normalization', 'detrend', 'individually'),
    widgets.Checkbox(
        description='Detrend each response individually',
        value=False,
        style={'description_width': 'initial'}),
    on_new_value=lambda value: lsx.widgets.display(detrend_reference, not value))
detrend_octaves = settings.track_widget(
    ('normalization', 'detrend', 'octaves'),
    widgets.SelectionSlider(
        description='Detrending strength',
        options=[
            ('2/1-octave', 2/1),
            ('1/1-octave', 1/1),
            ('1/2-octave', 1/2),
            ('1/3-octave', 1/3),
            ('1/6-octave', 1/6),
        ], value=1/1,
        style={'description_width': 'initial'}))
detrend = widgets.VBox([detrend_individually, detrend_reference, detrend_octaves])

normalization_mode = settings.track_widget(
    ('normalization', 'mode'),
    widgets.RadioButtons(
        description='Normalization mode',
        options=[
            ('None', 'none'),
            ('Equal sensitivity', 'sensitivity'),
            ('Flat on-axis', 'on_axis'),
            ('Flat listening window', 'listening_window'),
            ('Detrend', 'detrend'),
        ], value='sensitivity',
        style={'description_width': 'initial'}),
    on_new_value=lambda value: lsx.widgets.display(detrend, value == 'detrend'))

form(widgets.HBox([normalization_mode, detrend]))
```

```python
speakers_fr_splnorm = speakers_fr_raw.loc[:, 'Sound Pessure Level [dB]']
speakers_fr_dinorm = speakers_fr_raw.loc[:, '[dB] Directivity Index ']
spl_axis_label = ['Absolute Sound Pressure Level (dB SPL)']
di_axis_label = ['Directivity Index (dBr)']
spl_domain = (55, 105)
di_domain = (-5, 10)
detrending_info = None
if normalization_mode.value == 'sensitivity':
    speakers_fr_splnorm = speakers_fr_splnorm.sub(
        speakers_sensitivity, axis='index', level='Speaker')
    spl_axis_label = ['Relative Sound Pressure (dBr)']
    spl_domain = (-40, 10)
if normalization_mode.value == 'on_axis':
    speakers_fr_splnorm = speakers_fr_splnorm.sub(
        speakers_fr_raw.loc[:, ('Sound Pessure Level [dB]', 'CEA2034', 'On Axis')], axis='index')
    spl_axis_label = ['Sound Pressure (dBr)', 'relative to on-axis']
    spl_domain = (-40, 10)
if normalization_mode.value == 'listening_window':
    speakers_fr_splnorm = speakers_fr_splnorm.sub(
        speakers_fr_raw.loc[:, ('Sound Pessure Level [dB]', 'CEA2034', 'Listening Window')], axis='index')
    spl_axis_label = ['Sound Pressure (dBr)', 'relative to listening window']
    spl_domain = (-40, 10)
if normalization_mode.value == 'detrend':
    detrend_octaves_label = lsx.widgets.lookup_option_label(detrend_octaves)
    def smooth(fr):
        return (fr
            .groupby('Speaker')
            .apply(lambda speaker: lsx.fr.smooth(
                speaker, speakers_freqs_per_octave.loc[speaker.name] * detrend_octaves.value)))
    if detrend_individually.value:
        speakers_fr_splnorm = speakers_fr_splnorm.sub(smooth(speakers_fr_splnorm))
        spl_axis_label = ['Sound Pressure (dBr)', detrend_octaves_label + ' detrended']
        spl_domain = (-25, 25)
        speakers_fr_dinorm = speakers_fr_dinorm.sub(smooth(speakers_fr_dinorm))
        di_axis_label = ['Directivity Index (dBr)', detrend_octaves_label + ' detrended']
        di_domain = (-7.5, 7.5)
        detrending_info = f'Each curve individually {detrend_octaves_label} detrended'
    else:
        speakers_fr_splnorm = speakers_fr_splnorm.sub(
            smooth(speakers_fr_splnorm.loc[:, ('CEA2034', detrend_reference.value)]),
            axis='index')
        spl_axis_label = ['Sound Pressure (dBr)', f'relative to {detrend_octaves_label} smoothed {detrend_reference.value} (dBr)']
        spl_domain = (-40, 10)
        detrending_info = f'Curves relative to {detrend_octaves_label} smoothed {detrend_reference.value}'

speakers_fr_norm = pd.concat([speakers_fr_splnorm, speakers_fr_dinorm], axis='columns')
speakers_fr_norm
```

<!-- #region heading_collapsed=true -->
# Smoothing

All responses (including directivity indices) are smoothed according to the settings below.
<!-- #endregion -->

Smoothing is done by applying an [exponential moving average (EMA)](https://en.wikipedia.org/wiki/Moving_average#Exponential_moving_average) with a "span" or "N" corresponding to the number of octaves chosen (since points in the input are already equally spaced in log-frequency). EMA was chosen over a simple moving average because it gracefully handles the case where N is not an integer, as is often the case here.

Note that the current algorithm makes the implicit assumption that the input data is equally log-spaced in frequency (see "Data Check", "Resolution" below). With recent datasets this assumption tends to break down below ~100 Hz, where points are further apart than expected, leading to excessive smoothing.

```python
smoothing_octaves = settings.track_widget(
    ('smoothing', 'octaves'),
    widgets.SelectionSlider(
        description='Smoothing strength',
        options=[
            ('1/1-octave', 1/1),
            ('1/2-octave', 1/2),
            ('1/3-octave', 1/3),
            ('1/6-octave', 1/6),
            ('1/12-octave', 1/12),
        ], value=1/1,
        style={'description_width': 'initial'}))
smoothing_preserve_original = settings.track_widget(
    ('smoothing', 'preserve_original'),
    widgets.RadioButtons(
        options=[
            ('Display smoothed data alongside unsmoothed data', True),
            ('Drop unsmoothed data', False),
        ], value=True,
        layout={'width': 'max-content'}))
smoothing_params = widgets.VBox([smoothing_octaves, smoothing_preserve_original])
smoothing_enabled = settings.track_widget(
    ('smoothing', 'enabled'),
    widgets.Checkbox(
        description='Enable smoothing',
        value=False,
        style={'description_width': 'initial'}),
    on_new_value=lambda value: lsx.widgets.display(smoothing_params, value))

form(widgets.HBox([smoothing_enabled, smoothing_params]))
```

```python
speakers_fr_smoothed = (speakers_fr_norm
    .unstack(level='Frequency [Hz]')
    .pipe(lsx.pd.append_constant_index, 'None', name='Smoothing')
    .stack()
)
if smoothing_enabled.value:
    speakers_fr_smoothed_only = (speakers_fr_norm
        .groupby('Speaker')
        .apply(lambda speaker: lsx.fr.smooth(
            speaker, speakers_freqs_per_octave.loc[speaker.name] * smoothing_octaves.value))
        .unstack(level='Frequency [Hz]')
        .pipe(lsx.pd.append_constant_index,
              lsx.widgets.lookup_option_label(smoothing_octaves),
              name='Smoothing')
        .stack())
    speakers_fr_smoothed = (
        pd.concat([speakers_fr_smoothed, speakers_fr_smoothed_only])
        if smoothing_preserve_original.value else speakers_fr_smoothed_only)
speakers_fr_smoothed
```

<!-- #region heading_collapsed=true -->
# Plot settings

Here you can customize some parameters related to the charts.
<!-- #endregion -->

```python
speaker_offset_db = settings.track_widget(
    ('speaker_offset', 'db'),
    widgets.FloatText(value=-10, description='Offset (dB):'))
speaker_offset_enabled = settings.track_widget(
    ('speaker_offset', 'enabled'),
    widgets.Checkbox(
        description='Offset speaker traces', value=False,
        style={'description_width': 'initial'}),
    on_new_value=lambda value: lsx.widgets.display(speaker_offset_db, value))

standalone_chart_width = settings.track_widget(
    ('chart_size', 'standalone', 'width'),
    widgets.IntText(
        description='Standalone chart width:', value=800, min=0,
        style={'description_width': 'initial'}))
standalone_chart_height = settings.track_widget(
    ('chart_size', 'standalone', 'height'),
    widgets.IntText(
        description='height:', value=400, min=0))
sidebyside_chart_width = settings.track_widget(
    ('chart_size', 'sidebyside', 'width'),
    widgets.IntText(
        description='Side-by-side chart width:', value=600, min=0,
        style={'description_width': 'initial'}))
sidebyside_chart_height = settings.track_widget(
    ('chart_size', 'sidebyside', 'height'),
    widgets.IntText(
        description='height:', value=300, min=0))

bar_chart_width = settings.track_widget(
    ('chart_size', 'bar', 'width'),
    widgets.IntText(
        description='Bar chart width:', value=600, min=0,
        style={'description_width': 'initial'}))

form(widgets.VBox([
    widgets.HBox([speaker_offset_enabled, speaker_offset_db]),
    widgets.HBox([standalone_chart_width, standalone_chart_height]),
    widgets.HBox([sidebyside_chart_width, sidebyside_chart_height]),
    bar_chart_width
]))
```

```python
speakers_count = (speakers_fr_smoothed
    .index
    .get_level_values('Speaker')
    .nunique())                  

speakers_properties = (pd.concat([
        speakers_fr_smoothed
            .index
            .droplevel('Frequency [Hz]')
            .drop_duplicates()
            .to_frame()
            .reset_index(drop=True)
            .set_index('Speaker'),
        speakers_freqs_per_octave
            .rename('Mean resolution')
            .apply(lambda resolution: f'{resolution:.3g} pts/octave'),
        speakers.loc[:, 'Data License'],
    ], axis='columns', join='inner')
    .dropna(axis='columns', how='all'))
speakers_specific_properties = (speakers_properties
    .pipe(lambda speakers_properties: speakers_properties.loc[:,
        speakers_properties.groupby('Speaker').nunique(dropna=False).eq(1).all()])
    .groupby('Speaker')
    .apply(lambda speaker_properties: speaker_properties.apply(
        lambda speaker_property: speaker_property.unique().squeeze())))

single_speaker_mode = speakers_properties.index.nunique() <= 1

db_chart_fineprint = (speakers_specific_properties
    .pipe(lsx.pd.rollup, lambda speakers_property:
        [f'{speakers_property.name}: {speakers_property.unique().squeeze()}']
        if speakers_property.nunique(dropna=False) == 1
        else [f'{speakers_property.name}:'] + list('- ' + speakers_property
            .dropna()
            .reset_index()
            .apply(
                lambda speaker_property: speaker_property.str.cat(sep=': '),
                axis='columns')))
    .sum() + ['Data: amirm, AudioScienceReview.com - Plotted by Loudspeaker Explorer'])
chart_fineprint = ([] if detrending_info is None else [f'Detrending: {detrending_info}']) + db_chart_fineprint

speakers_fr_ready = speakers_fr_smoothed.copy()
speakers_fr_ready.index = (speakers_fr_ready.index
    .droplevel(
        speakers_specific_properties.columns
        .intersection(speakers_fr_ready.index.names)
        .to_list())
    .to_frame()
    .reset_index(drop=True)
    .set_index(['Speaker', 'Frequency [Hz]'])
    .apply(lambda speakers_property: speakers_property.name + ': ' + speakers_property)
    .reset_index('Speaker')
    .apply(lambda speaker: speaker.str.cat(sep='; '), axis='columns')
    .rename('Speaker')
    .to_frame()
    .set_index('Speaker', append=True)
    .swaplevel(0, -1)
    .index)

speaker_offsets = (speakers_fr_ready.index
    .get_level_values('Speaker')
    .drop_duplicates()
    .to_series()
    .groupby('Speaker')
    .ngroup()
    .mul(speaker_offset_db.value if speaker_offset_enabled.value else 0)
)
speakers_fr_ready_offset = (speakers_fr_ready
    # Arguably it would cleaner to use some kind of "Y offset" encoding channel in charts, but that doesn't seem to be supported yet: https://github.com/vega/vega-lite/issues/4703
    .add(speaker_offsets, axis='index', level='Speaker')
    .rename(lambda speaker_name: speaker_name +
        (lambda speaker_offset: '' if speaker_offset == 0 else f' [{speaker_offset:+.0f} dB]')(
            speaker_offsets.loc[speaker_name]),
        level='Speaker')
)

alt.data_transformers.disable_max_rows()
# In Altair 4.1.0, alt.datum[foo][bar] doesn't work. That was fixed in Altair commit bdef95b,
# but that's not released yet. In the mean time, dynamically patch the method as a workaround.
if alt.expr.Expression.__getitem__ == alt.utils.schemapi.SchemaBase.__getitem__:
    alt.expr.core.Expression.__getitem__ = lambda self, val: alt.expr.core.GetItemExpression(self, val)
    alt.expr.core.GetItemExpression.__repr__ = lambda self: '{}[{!r}]'.format(self.group, self.name)
    
max_standalone_speaker_count = 10
max_sidebyside_speaker_count = 6
def conditional_chart(max_speaker_count, make_chart):
    if speakers_count > max_speaker_count:
        return IPython.core.display.HTML(str(banner(
            dominate.util.text('This chart is not displayed because there are too many speakers selected (currently '),
            dominate.tags.strong(speakers_count),
            dominate.util.text(', max '),
            dominate.tags.strong(max_speaker_count),
            dominate.util.text(').'))))
    return make_chart()

def set_chart_dimensions(chart, sidebyside=False):
    if single_speaker_mode:
        sidebyside = False
    return chart.properties(
        width=sidebyside_chart_width.value if sidebyside else standalone_chart_width.value,
        height=sidebyside_chart_height.value if sidebyside else standalone_chart_height.value)

def frequency_tooltip(shorthand='frequency', title='Frequency', **kwargs):
    return alt.Tooltip(
        shorthand, type='quantitative',
        title=f'{title} (Hz)', format='.03s',
        **kwargs)

def value_db_tooltip(shorthand='value', title='Value', **kwargs):
    return alt.Tooltip(
        shorthand, type='quantitative',
        title=f'{title} (dB)', format='.2f',
        **kwargs)

def frequency_response_chart(
    data,
    process_before=lambda chart: chart,
    process_after=lambda chart: chart,
    fold=None,
    sidebyside=False,
    alter_tooltips=lambda tooltips: tooltips,
    fineprint=chart_fineprint):
    return lsx.util.pipe(data
        .rename_axis(index={
            'Frequency [Hz]': 'frequency',
            'Speaker': 'speaker',
        })
        .reset_index('frequency')
        .pipe(lsx.alt.make_chart,
            process_before=lambda chart: lsx.util.pipe(chart
                .interactive(),
                lambda chart: chart if fold is None else chart.transform_fold(data.columns.values, **fold),
                lambda chart: set_chart_dimensions(chart, sidebyside)
                .encode(
                    frequency_xaxis('frequency'),
                    tooltip=alter_tooltips([frequency_tooltip()])),
                process_before),
            process_after=process_after),
        lambda chart: postprocess_chart(chart, fineprint=fineprint))

def frequency_response_db_chart(*kargs, additional_tooltips=[], fineprint=db_chart_fineprint, **kwargs):
    return frequency_response_chart(
        *kargs,
        alter_tooltips=lambda tooltips: additional_tooltips + tooltips + [value_db_tooltip()],
        fineprint=fineprint,
        **kwargs)

def standalone_speaker_frequency_response_db_chart(column, yaxis):
    def make_chart():
        data = (speakers_fr_ready_offset
            .loc[:, column]
            .rename('value')
            .to_frame())
        return frequency_response_db_chart(
            data,
            lambda chart: lsx.util.pipe(chart
                .encode(speaker_color(), y=yaxis),
                speaker_input),
            lambda chart: lsx.alt.interactive_line(chart),
            additional_tooltips=
                [alt.Tooltip('speaker', type='nominal', title='Speaker')]
                if data.index.get_level_values('Speaker').nunique() > 1 else [])
    return conditional_chart(max_standalone_speaker_count, make_chart)

def frequency_xaxis(shorthand):
    return alt.X(
        shorthand, type='quantitative', title='Frequency (Hz)',
        scale=alt.Scale(type='log', base=10, domain=[20, 20000], nice=False),
        axis=alt.Axis(format='s'))

def sound_pressure_yaxis(title_prefix=None):
    return alt.Y(
        'value', type='quantitative',
        title=[(title_prefix + ' ' if title_prefix else '') + spl_axis_label[0]] + spl_axis_label[1:],
        scale=alt.Scale(domain=spl_domain),
        axis=alt.Axis(grid=True))

def directivity_index_yaxis(title_prefix=None, scale_domain=di_domain):
    return alt.Y(
        'value', type='quantitative',
        title=[(title_prefix + ' ' if title_prefix else '') + di_axis_label[0]] + di_axis_label[1:],
        scale=alt.Scale(domain=scale_domain), axis=alt.Axis(grid=True))

def key_color(**kwargs):
    return alt.Color(
        'key', type='nominal', title=None, sort=None,
        legend=alt.Legend(symbolType='stroke'),
        **kwargs)
 
def speaker_color(**kwargs):
    return alt.Color(
        'speaker', type='nominal', title=None,
        legend=alt.Legend(
            orient='top', direction='vertical', labelLimit=600, symbolType='stroke'),
        **kwargs)

def speaker_facet(chart):
    return chart.facet(alt.Column('speaker', title=None, type='nominal'))

def speaker_input(chart):
    speakers = list(speakers_fr_ready.index.get_level_values('Speaker').drop_duplicates().values)
    if len(speakers) < 2: return chart
    selection = alt.selection_single(
            fields=['speaker'],
            bind=alt.binding_select(
                name='Speaker: ', options=[None] + speakers, labels=['All'] + speakers))
    return chart.transform_filter(selection).add_selection(selection)

def postprocess_chart(chart, fineprint=chart_fineprint):
    # Altair/Vega-Lite doesn't provide a way to set multiple titles or just display arbitrary text.
    # We hack around that limitation by concatenating with a dummy chart that has a title.
    # See https://github.com/vega/vega-lite/issues/5997
    return (alt.vconcat(
        chart,
        alt.Chart(title=alt.TitleParams(
            fineprint, fontSize=10, fontWeight='lighter', color='gray', anchor='start'),
            width=600, height=1)
            .mark_text())
        .resolve_legend(color='independent')
        .configure_view(opacity=0))
```

<!-- #region heading_collapsed=true -->
# Data check

The charts in these section can be used to sanity check the input data. They are not particularly useful unless you suspect a problem with the data.
<!-- #endregion -->

## Resolution

This chart shows the resolution of the input data at each frequency. For each point, resolution is calculated by looking at the distance from the previous point. The larger the distance, the lower the resolution.

A straight, horizontal line means that resolution is constant throughout the spectrum, or in other words, points are equally spaced in log-frequency. Some Loudspeaker Explorer features, especially smoothing and detrending, implicitly assume that this is the case, and might produce inaccurate results otherwise.

```python
conditional_chart(max_standalone_speaker_count, lambda: frequency_response_chart(
    speakers_fr_ready
        .pipe(lsx.pd.index_as_columns)
        .set_index('Speaker')
        .set_index('Frequency [Hz]', append=True, drop=False)
        .groupby('Speaker').apply(lambda frequencies: frequencies / frequencies.shift(1))
        .pipe(np.log2)
        .pow(-1)
        .rename(columns={'Frequency [Hz]': 'Resolution (points/octave)'})
        .pipe(lsx.pd.remap_columns, {
            'Resolution (points/octave)': 'value',
        }),
    lambda chart: lsx.util.pipe(chart
        .encode(
            alt.Y('value', type='quantitative', title='Resolution (points/octave)', axis=alt.Axis(grid=True)),
            speaker_color()),
        speaker_input),
    lambda chart: lsx.alt.interactive_line(chart),
    alter_tooltips=lambda tooltips:
        ([alt.Tooltip('speaker', title='Speaker')]
            if speakers_fr_ready.index.get_level_values('Speaker').nunique() > 1 else []) +
        tooltips +
        [alt.Tooltip('value', type='quantitative', title='Resolution (points/octave)', format='.2f')]
))
```

# Standard measurements

Note that all the data shown in this section is a direct representation of the input data after normalization. No complex processing is done. In particular, data for derived metrics such as *Listening Window*, *Early Reflections*, *Sound Power*, Directivity Indices and even *Estimated In-Room Response* come directly from the input - they are not derived by this code.


## Spinorama

The famous CEA/CTA-2034 charts, popularized by Dr. Floyd Toole. These provide a good summary of the measurements from a perceptual perspective. Speakers are presented side-by-side for easy comparison.

The curves that make up this chart are described in more detail in the following sections.

Remember:
 - **All the charts are interactive.** Use the mousewheel to zoom, and drag & drop to pan. Click on a legend entry to highlight a single response; hold shift to highlight multiple responses. Double-click to reset the view. (PROTIP: to quickly switch back and forth between speakers, select the speaker dropdown, then use the left-right arrow keys on your keyboard.)
 - **Charts will not be generated if the section they're under is folded while the notebook is running.** To manually load a chart after running the notebook, click on the square to the left of the *Show Code* button. Or simply use *Run all* again after unfolding the section.

```python
conditional_chart(max_sidebyside_speaker_count, lambda: frequency_response_db_chart(
    speakers_fr_ready.pipe(lsx.pd.remap_columns, {
        ('CEA2034', 'On Axis'): 'On Axis',
        ('CEA2034', 'Listening Window'): 'Listening Window',
        ('CEA2034', 'Early Reflections'): 'Early Reflections',
        ('CEA2034', 'Sound Power'): 'Sound Power',
        ('Directivity Index', 'Early Reflections DI'): 'Early Reflections DI',
        ('Directivity Index', 'Sound Power DI'): 'Sound Power DI',
    }),
    lambda chart: lsx.util.pipe(chart
        .encode(key_color()),
        # To make the Y axes independent, `.resolve_scale()` has to be used *before
        # and after* `.facet()`. (In Vega terms, there needs to be a Resolve property
        # in *every* view composition specification.)
        #  - If the first `.resolve_scale()` is removed from the layer spec, the axes
        #    are not made independent.
        #  - If the second `.resolve_scale()` is removed from the facet spec, Vega
        #    throws a weird `Unrecognized scale name: "child_layer_0_y"` error.
        lambda chart: chart.resolve_scale(y='independent'),
        speaker_facet, speaker_input,
        lambda chart: chart.resolve_scale(y='independent')),
    lambda chart: alt.layer(
        lsx.util.pipe(lsx.alt.interactive_line(chart)
            .transform_filter(alt.FieldOneOfPredicate(field='key', oneOf=[
                'On Axis', 'Listening Window', 'Early Reflections', 'Sound Power']))
            .encode(sound_pressure_yaxis())),
        lsx.util.pipe(lsx.alt.interactive_line(chart)
            .transform_filter(alt.FieldOneOfPredicate(field='key', oneOf=[
                'Early Reflections DI', 'Sound Power DI']))
            .encode(directivity_index_yaxis(scale_domain=(-10, 40)))
            .interactive())),  # Required, otherwise only left axis scales.
    fold={},
    additional_tooltips=[alt.Tooltip('key', type='nominal', title='Response')],
    sidebyside=True))
```

## On-axis response


On-axis (**ON**) is is the response at a 0° horizontal and vertical angle, i.e. on the reference axis of measurement. Note that in all measurements done thus far, the reference axis is the same as the tweeter axis.

```python
standalone_speaker_frequency_response_db_chart(
    ('CEA2034', 'On Axis'),
    sound_pressure_yaxis(title_prefix='On Axis'))
```

<!-- #region heading_collapsed=true -->
## Off-axis responses

Note that this chart can be particularly taxing on your browser due to the sheer number of points.
<!-- #endregion -->

Use the slider at the bottom to focus on a specific angle. Note that the slider can be slow to respond, especially if there are many speakers. Double-click the chart to reset.

Keep in mind that these graphs can be shown normalized to flat on-axis by changing the settings in the *Normalization* section above.

```python
def off_axis_angles_chart(direction):
    return conditional_chart(4, lambda: frequency_response_db_chart(
        speakers_fr_ready
            .loc[:, 'SPL ' + direction]
            .pipe(lsx.data.convert_angles)
            .pipe(lambda df: df.pipe(lsx.pd.set_columns, df.columns.map(mapper=lambda column: f'{column:+.0f}')))
            .rename_axis(columns='Angle'),
        lambda chart: lsx.util.pipe(chart
            .transform_calculate(angle=alt.expr.toNumber(alt.datum['key'])),
            lambda chart: lsx.alt.filter_selection(chart, alt.selection_single(
                fields=['angle'],
                bind=alt.binding_range(min=-170, max=180, step=10, name=direction + ' angle selector (°)'),
                clear='dblclick'))
            .encode(
                sound_pressure_yaxis(),
                alt.Color(
                    'angle', title=direction + ' angle (°)', type='quantitative',
                    scale=alt.Scale(scheme='sinebow', domain=(-180, 180)),
                    # We have to explicitly set the legend type to 'gradient' because of https://github.com/vega/vega-lite/issues/6258
                    legend=alt.Legend(type='gradient', gradientLength=300, values=list(range(-180, 180+10, 10))))),
            speaker_facet, speaker_input),
        lambda chart: lsx.alt.interactive_line(chart),
        fold={},
        additional_tooltips=[alt.Tooltip('key', type='nominal', title=direction + ' angle (°)')],
        sidebyside=True
    ))

off_axis_angles_chart('Horizontal')
```

```python
off_axis_angles_chart('Vertical')
```

<!-- #region heading_collapsed=true -->
## Horizontal reflection responses
<!-- #endregion -->

[ANSI-CTA-2034-A](https://shop.cta.tech/products/standard-method-of-measurement-for-in-home-loudspeakers) section 5.2 defines the following Horizontal Reflection curves as the power average of the responses at the following horizontal angles:

- **Front**: ±0-30°
- **Side**: ±40-80°
- **Rear**: ±90-180° (i.e. rear semicircle)

```python
def reflection_responses_chart(axis):
    return conditional_chart(max_sidebyside_speaker_count, lambda: frequency_response_db_chart(
        speakers_fr_ready
            .loc[:, f'{axis} Reflections']
            .rename_axis(columns=['Direction'])
            .rename(columns=lambda column:
                    re.sub(f' ?{axis} ?', '', re.sub(' ?Reflection ?', '', column))),
        lambda chart: lsx.util.pipe(chart
            .encode(sound_pressure_yaxis(), key_color()),
            speaker_facet, speaker_input),
        lambda chart: lsx.alt.interactive_line(chart),
        fold={},
        additional_tooltips=[alt.Tooltip('key', type='nominal', title='Direction')],
        sidebyside=True))

reflection_responses_chart('Horizontal')
```

<!-- #region heading_collapsed=true -->
## Vertical reflection responses
<!-- #endregion -->

[ANSI-CTA-2034-A](https://shop.cta.tech/products/standard-method-of-measurement-for-in-home-loudspeakers) section 5.2 defines the following Vertical Reflection curves as the power average of the responses at the following vertical angles:

- **Floor**: -20° to -40°
- **Ceiling**: +40° to +60°

```python
reflection_responses_chart('Vertical')
```

## Listening Window response


[ANSI-CTA-2034-A](https://shop.cta.tech/products/standard-method-of-measurement-for-in-home-loudspeakers) section 5.2 defines the Listening Window (**LW**) curve as the power average of the responses at **±0-10° vertical and ±0-30° horizontal angles**.

```python
standalone_speaker_frequency_response_db_chart(
    ('CEA2034', 'Listening Window'),
    sound_pressure_yaxis(title_prefix='Listening Window'))
```

## Early Reflections response


[ANSI-CTA-2034-A](https://shop.cta.tech/products/standard-method-of-measurement-for-in-home-loudspeakers) section 5.2 defines the Early Reflections (**ER**) curve as the average of all Reflection curves described previously (**Floor**, **Ceiling**, **Front**, **Side**, **Rear**).

**Note:** CTA-2034-A is actually ambiguous as to the definition of this curve - the text could also be interpreted to refer to the average of the *individual responses* from all the angles that make up the aforementioned curves. A clearer definition can be found in the [seminal paper](http://www.aes.org/e-lib/browse.cfm?elib=11234) the standard is based on, which does define the Early Reflections curve as an average of averages, and this was [confirmed by Todd Welti](https://www.audiosciencereview.com/forum/index.php?threads/spinorama-also-known-as-cta-cea-2034-but-that-sounds-dull-apparently.10862/page-3#post-343970) who worked with the author of the paper. **Sadly, Klippel uses the wrong definition (average of individual responses), and for that reason, the data shown here is slightly wrong.** For details, see [this](https://www.audiosciencereview.com/forum/index.php?threads/spinorama-also-known-as-cta-cea-2034-but-that-sounds-dull-apparently.10862/page-2#post-323270), [this](https://www.audiosciencereview.com/forum/index.php?threads/master-preference-ratings-for-loudspeakers.11091/page-16#post-395073), [this](https://www.audiosciencereview.com/forum/index.php?threads/master-preference-ratings-for-loudspeakers.11091/page-18#post-397135) and [this](https://www.audiosciencereview.com/forum/index.php?threads/erinsaudiocorner.11219/page-14#post-421640).

```python
standalone_speaker_frequency_response_db_chart(
    ('CEA2034', 'Early Reflections'),
    sound_pressure_yaxis(title_prefix='Early Reflections'))
```

## Sound Power response


[ANSI-CTA-2034-A](https://shop.cta.tech/products/standard-method-of-measurement-for-in-home-loudspeakers) section 5.2 defines the Sound Power (**SP**) curve as the power average of the responses at all horizontal and vertical angles, weighted according to the portion of the spherical surface they represent.

```python
standalone_speaker_frequency_response_db_chart(
    ('CEA2034', 'Sound Power'),
    sound_pressure_yaxis(title_prefix='Sound Power'))
```

## Early Reflections Directivity Index


[ANSI-CTA-2034-A](https://shop.cta.tech/products/standard-method-of-measurement-for-in-home-loudspeakers) section 5.2 defines the Early Reflections Directivity Index (**ERDI**) curve as the Listening Window curve minus the Early Reflection Curve. An ERDI of 0 dB means early reflections are as loud as the direct sound.

```python
standalone_speaker_frequency_response_db_chart(
    ('Directivity Index', 'Early Reflections DI'),
    directivity_index_yaxis(title_prefix='Early Reflections'))
```

## Sound Power Directivity Index


[ANSI-CTA-2034-A](https://shop.cta.tech/products/standard-method-of-measurement-for-in-home-loudspeakers) section 5.2 defines the Sound Power Directivity Index (**SPDI**) curve as the Listening Window curve minus the Sound Power Curve. An SPDI of 0 dB means the speaker is effectively omnidirectional.

```python
standalone_speaker_frequency_response_db_chart(
    ('Directivity Index', 'Sound Power DI'),
    directivity_index_yaxis(title_prefix='Sound Power'))
```

## Estimated In-Room Response


[ANSI-CTA-2034-A](https://shop.cta.tech/products/standard-method-of-measurement-for-in-home-loudspeakers) section 13 defines the Estimated In-Room Response curve, also known as the Predicted In-Room Response or PIR, as a weighted average of the following curves:

- **12% Listening Window**
- **44% Early Reflections**
- **44% Sound Power**

It [has been shown](http://www.aes.org/e-lib/browse.cfm?elib=12847) (section 6) that, in practice, there is good agreement between the Estimated In-Room Response curve and the In-Situ Response, i.e. the response that would be picked up by an omnidirectional measurement microphone at a typical listener location in a typical room, between 300 Hz and 10 kHz.

**Note:** because the Predicted In-Room Response curve is calculated using the Early Reflections curve, it suffers from the same problem described in the Early Reflection section, meaning that the data shown here is [slightly wrong](https://www.audiosciencereview.com/forum/index.php?threads/speaker-equivalent-sinad-discussion.10818/page-12#post-389656).

```python
standalone_speaker_frequency_response_db_chart(
    ('Estimated In-Room Response', 'Estimated In-Room Response'),
    sound_pressure_yaxis(title_prefix='Estimated In-Room Response'))
```

# Other measurements



## Listening Window detail

[ANSI-CTA-2034-A](https://shop.cta.tech/products/standard-method-of-measurement-for-in-home-loudspeakers) section 5.2 defines the Listening Window curve as the average of the responses at ±0-10° vertical and ±0-30° horizontal angles. Averages can be misleading as they can hide significant variation between angles.

This chart provides more detail by including each individual angle that is used in the Listening Window average. This can be used to assess the consistency of the response within the Listening Window.

```python
conditional_chart(max_sidebyside_speaker_count, lambda: frequency_response_db_chart(
    speakers_fr_ready
        .pipe(lsx.pd.remap_columns, {
            ('SPL Vertical', '-10°'): '-10° Vertical',
            ('SPL Vertical',  '10°'): '+10° Vertical',
            ('SPL Horizontal', '-10°'): '-10° Horizontal',
            ('SPL Horizontal',  '10°'): '+10° Horizontal',
            ('SPL Horizontal', '-20°'): '-20° Horizontal',
            ('SPL Horizontal',  '20°'): '+20° Horizontal',
            ('SPL Horizontal', '-30°'): '-30° Horizontal',
            ('SPL Horizontal',  '30°'): '+30° Horizontal',
            ('CEA2034', 'Listening Window'): 'Listening Window',
            ('CEA2034', 'On Axis'): 'On Axis',
        }),
    lambda chart: lsx.util.pipe(chart
        .encode(
            sound_pressure_yaxis(),
            key_color(scale=alt.Scale(range=[
                # Vertical ±10°: purples(2)
                '#796db2', '#aeadd3', 
                # Horizontal ±10°: browns(2)
                '#c26d43', '#e1a360',
                # Horizontal ±20°: blues(2)
                '#3887c0', '#86bcdc',
                # Horizontal ±30°: greys(2)
                '#686868', '#aaaaaa',
                # Listening Window: category10(1)
                '#ff7f0e',
                # On Axis: category10(2)
                '#2ca02c',
            ])),
            strokeWidth=alt.condition(alt.FieldOneOfPredicate(
                field='key', oneOf=['Listening Window', 'On Axis']),
                if_true=alt.value(2), if_false=alt.value(1.5))),
        speaker_facet, speaker_input),
    lambda chart: lsx.alt.interactive_line(chart),
    fold={},
    additional_tooltips=[alt.Tooltip('key', type='nominal', title='Response')],
    sidebyside=True))
```

# Olive Preference Rating


This section describes the calculation of a loudspeaker preference score based on [research by Sean Olive](http://www.aes.org/e-lib/browse.cfm?elib=12847), also available as a [patent](https://patents.google.com/patent/US20050195982A1).

This research involves 268 listeners evaluating 70 loudspeakers in rigorous controlled conditions. Statistical methods were used to correlate subjective ratings with the speakers anechoic measurement data. The result is a statistical model in the form of a formula that can be used to fairly accurately predict loudspeaker preference ratings from spinorama data alone. This research is widely considered to be the state of the art when it comes to assessing speakers based on measurements.

**Note that scores are calculated based on post-processed data. For example, if smoothing or detrending are enabled, they will affect the calculated scores.**

```python
# Remap columns according to the curves selected in the Olive paper.
speakers_fr_olive = speakers_fr_ready.pipe(lsx.pd.remap_columns, {
    ('CEA2034', 'On Axis'): 'ON',
    ('CEA2034', 'Listening Window'): 'LW',
    ('CEA2034', 'Early Reflections'): 'ER',
    ('Estimated In-Room Response', 'Estimated In-Room Response'): 'PIR',
    ('CEA2034', 'Sound Power'): 'SP',
    ('Directivity Index', 'Sound Power DI'): 'SPDI',
    ('Directivity Index', 'Early Reflections DI'): 'ERDI',
}).rename_axis(columns='Curve')

olive_variable_labels = {
    'NBD': 'Narrow Band Deviation',
}
olive_curve_labels = {
    'ON': 'On Axis',
    'LW': 'Listening Window',
    'ER': 'Early Reflections',
    'PIR': 'Predicted In-Room Response',
    'SP': 'Sound Power',
    'SPDI': 'Sound Power Directivity Index',
    'ERDI': 'Early Reflections Directivity Index',
}

def expand_olive_curve_label(curve):
    return f'{curve} {olive_curve_labels[curve]}'

def expand_olive_label(variable, curve):
    return f'{variable}_{curve} {olive_curve_labels[curve]} {olive_variable_labels[variable]}'

def curve_input(chart, init):
    return lsx.alt.filter_selection(chart, alt.selection_single(
        fields=['curve'], init={'curve': init},
        bind=alt.binding_select(
            name='Curve: ',
            options=list(olive_curve_labels.keys()),
            labels=[f'{curve} {label}' for curve, label in olive_curve_labels.items()])))

def value_yaxis(title_prefix=None):
    return alt.Y(
        'value', type='quantitative', title='Curve value (dB)',
        scale=alt.Scale(domain=spl_domain),
        axis=alt.Axis(grid=True))
```

<!-- #region heading_collapsed=true -->
## Narrow Band Deviation (NBD)
<!-- #endregion -->

<!-- #region heading_collapsed=true -->
### Calculation
<!-- #endregion -->

This metric is defined in section 3.2.2 of the [paper](http://www.aes.org/e-lib/browse.cfm?elib=12847) and section 0068 of the [patent](https://patents.google.com/patent/US20050195982A1). Loudspeaker Explorer uses the following interpretation:

$$\mathit{NBD} =
    \left(\sum_{n=1}^{N} \frac{\sum_{b=1}^{B_{n}} |y_{n,b} - \overline{y}_{n}|}{B_{n}}\right) \div N$$
    
Where:

- $\mathit{NBD}$ is the Narrow Band Deviation in dB. Lower is better.
- $N$ is the number of ½-octave bands between 100 Hz and 12 kHz.
- $B_{n}$ is the number of measurement points within the $n$th ½-octave band. The model assumes $B_{n} = 10$.
- $y_{n,b}$ is the amplitude of the $b$th measurement point within the $n$th ½-octave band in dB. Points should be equally spaced in log-frequency.
- $\overline{y}_{n}$ is the mean amplitude within the $n$th ½-octave band in dB, i.e. $\overline{y}_{n} = \left(\sum_{b=1}^{B_{n}} y_{n,b}\right) \div B_{n}$

In plain English, NBD takes the mean absolute deviation from the mean SPL within each ½-octave band, and then takes the mean of these bands.

The formula that appears in the paper is somewhat different as it does not include the division by $B_{n}$, i.e. it uses the sum of deviations within each ½-octave band, as opposed to their mean. It is [believed](https://www.audiosciencereview.com/forum/index.php?threads/speaker-equivalent-sinad-discussion.10818/page-12#post-376370) that this is an oversight in the paper and that the formula above is the one Olive actually meant.


The paper is ambiguous as to where the _½-octave bands between 100 Hz and 12 kHz_ actually lie. Specifically, it is not clear if *100 Hz* and *12 kHz* are meant as *boundaries*, or if they refer to the *center frequencies* of the first and last bands. (For more debate on this topic, see [this](https://www.audiosciencereview.com/forum/index.php?threads/speaker-equivalent-sinad-discussion.10818/page-3#post-303034), [this](https://www.audiosciencereview.com/forum/index.php?threads/speaker-equivalent-sinad-discussion.10818/page-4#post-303834), [this](https://www.audiosciencereview.com/forum/index.php?threads/speaker-equivalent-sinad-discussion.10818/page-7#post-306831), [this](https://www.audiosciencereview.com/forum/index.php?threads/speaker-equivalent-sinad-discussion.10818/page-10#post-308515), [this](https://www.audiosciencereview.com/forum/index.php?threads/yamaha-hs5-powered-monitor-review.10967/page-6#post-309021) and [this](https://www.audiosciencereview.com/forum/index.php?threads/master-preference-ratings-for-loudspeakers.11091/page-19#post-401344).) In his [score calculations](https://docs.google.com/spreadsheets/d/e/2PACX-1vRVN63daR6Ph8lxhCDUEHxWq_gwV0wEjL2Q1KRDA0J4i_eE1JS-JQYSZy7kCQZMKtRnjTOn578fYZPJ/pubhtml), [MZKM](https://www.audiosciencereview.com/forum/index.php?members/mzkm.4645/) uses 114 Hz as the center frequency of the first band and deduces the rest from there. For consistency's sake, Loudspeaker Explorer does the same, resulting in the following bands:

```python
nbd_bands = (pd.Series(range(0, 14)).rpow(2**(1/2))*114).rename('Center Frequency (Hz)')
nbd_bands = pd.concat([
    (nbd_bands / (2**(1/4))).rename('Start Frequency (Hz)'),
    nbd_bands,
    (nbd_bands * (2**(1/4))).rename('End Frequency (Hz)'),
], axis='columns').rename_axis('Band').rename(index=lambda i: i+1)
nbd_bands
```

```python
frequency_nbd_band = (speakers_fr_olive
    .pipe(lsx.pd.index_as_columns)
    .set_index('Speaker')
    .set_index('Frequency [Hz]', append=True, drop=False)
    .reindex(columns=nbd_bands.index))
frequency_nbd_band.loc[:, :] = frequency_nbd_band.index.get_level_values('Frequency [Hz]').values[:, None]
frequency_nbd_band = ((
    (frequency_nbd_band >= nbd_bands.loc[:, 'Start Frequency (Hz)']) &
    (frequency_nbd_band <  nbd_bands.loc[:, 'End Frequency (Hz)']))
    .stack())
frequency_nbd_band = (frequency_nbd_band
    .loc[frequency_nbd_band]
    .pipe(lsx.pd.index_as_columns)
    .set_index(['Speaker', 'Frequency [Hz]']))

speakers_fr_band = (speakers_fr_olive
    .pipe(lsx.pd.join_index, frequency_nbd_band)
    .swaplevel('Frequency [Hz]', 'Band'))
speakers_nbd_mean = speakers_fr_band.groupby(['Speaker', 'Band']).mean()
speakers_nbd_mean
```

```python
speakers_nbd_deviation = speakers_fr_band - speakers_nbd_mean
speakers_nbd_deviation
```

```python
speakers_nbd_deviation_band = speakers_nbd_deviation.abs().groupby(['Speaker', 'Band'])
speakers_nbd_band = speakers_nbd_deviation_band.mean() / len(nbd_bands.index)
speakers_nbd_band
```

```python
speakers_nbd = speakers_nbd_band.groupby(['Speaker']).sum()
speakers_nbd
```

### Results

```python
nbd_fr_chart_data = (pd.concat({
        'Curve': pd.concat([speakers_fr_olive, frequency_nbd_band], axis='columns')
            .pipe(lambda df: df.set_index(df.loc[:, 'Band'].fillna(0).astype(int), append=True))
            .drop(columns='Band')
            .swaplevel('Frequency [Hz]', 'Band'),
        'Band Mean': speakers_nbd_mean
            .pipe(lsx.pd.append_constant_index, name='Frequency [Hz]')
    }, names=['Dataset']))

conditional_chart(max_sidebyside_speaker_count, lambda: frequency_response_db_chart(
    nbd_fr_chart_data,
    lambda chart: lsx.util.pipe(chart
        .transform_lookup(lookup='Band', as_='band_info', from_=alt.LookupData(
            key='Band', data=nbd_bands
                .pipe(lsx.pd.remap_columns, {
                    'Start Frequency (Hz)': 'start_frequency',
                    'Center Frequency (Hz)': 'center_frequency',
                    'End Frequency (Hz)': 'end_frequency',
                })
                .reset_index()))
        .transform_lookup(lookup='speaker', as_='speaker_band_mean', from_=alt.LookupData(
            key='Speaker', data=speakers_nbd_mean
                .groupby('Speaker')
                .apply(lambda df: df
                    .reset_index('Speaker', drop=True)
                    .to_dict(orient='index'))
                .rename('band_mean')
                .reset_index()))
        .encode(
            value_yaxis(),
            alt.Color(
                'layer',
                type='nominal', title=None,
                legend=alt.Legend(symbolType='stroke'),
                scale=alt.Scale(range=[
                    # TODO: this doesn't quite work, presumably because the input is not interleaved in this way.
                    # Revisit once https://github.com/vega/vega-lite/issues/6392 is fixed.
                    '#2ca02c',  # category10[2]: Band Mean
                    '#ff7f0e',  # category10[1]: Deviation
                    '#1f77b4',  # category10[0]: Curve
                ]))),
        lambda chart: curve_input(chart, 'ON'),
        speaker_facet, speaker_input),
    lambda chart: alt.layer(
        lsx.util.pipe(lsx.alt.interactive_line(chart)
            .transform_filter(alt.datum['Dataset'] == 'Curve')
            .transform_calculate(layer=alt.datum['curve'] + ' Curve')
            .encode(strokeWidth=alt.value(0.5))),
        lsx.util.pipe(lsx.alt.interactive_line(
                chart, add_mark=lambda chart: chart.mark_rule())
            .transform_filter(alt.datum['Dataset'] == 'Band Mean')
            .transform_calculate(layer='NBD_' + alt.datum['curve'] + ' Band Mean')
            .transform_calculate(frequency=alt.datum['band_info']['start_frequency'])
            .encode(
                alt.X2('band_info.end_frequency'),
                tooltip=[
                    alt.Tooltip('Band'),
                    frequency_tooltip('band_info.start_frequency', 'Start Frequency'),
                    frequency_tooltip('band_info.center_frequency', 'Center Frequency'),
                    frequency_tooltip('band_info.end_frequency', 'End Frequency'),
                    value_db_tooltip(title='Mean'),
                ]
            )),
        lsx.util.pipe(lsx.alt.interactive_line(
                chart, add_mark=lambda chart: chart.mark_rule())
            .transform_filter(alt.datum['Dataset'] == 'Curve')
            .transform_calculate(band_mean=lsx.util.pipe(
                alt.datum['speaker_band_mean']['band_mean'][alt.datum['Band']],
                lambda band: alt.expr.if_(alt.expr.isObject(band), band[alt.datum['curve']], alt.expr.NaN)))
            .transform_filter(alt.FieldValidPredicate(field='band_mean', valid=True))
            .transform_calculate(layer='NBD_' + alt.datum['curve'] + ' Deviation')
            .transform_calculate(deviation=alt.expr.abs(alt.datum['band_mean'] - alt.datum['value']))
            .encode(
                alt.Y2('band_mean'),
                strokeWidth=alt.value(2),
                tooltip=[
                    frequency_tooltip(),
                    value_db_tooltip(),
                    alt.Tooltip('Band'),
                    value_db_tooltip('deviation', title='Deviation'),
                ]))),
    fold={'as_': ['curve', 'value']},
    sidebyside=True, fineprint=chart_fineprint))
```

```python
lsx.alt.make_chart(
    speakers_nbd_band
        .reset_index('Band'),
    lambda chart: lsx.util.pipe(chart
        .properties(width=bar_chart_width.value)
        .transform_fold(speakers_nbd_band.columns.values, ['curve', 'value'])
        .transform_lookup(lookup='curve', as_='curve_info', from_=alt.LookupData(
            key='curve', data=pd.Series(olive_curve_labels)
                .rename_axis('curve')
                .rename('label')
                .reset_index()))
        .transform_calculate(curve_label=alt.datum['curve'] + ' ' + alt.datum['curve_info']['label'])
        .transform_lookup(lookup='Band', as_='band_info', from_=alt.LookupData(
            key='Band', data=nbd_bands
                .pipe(lsx.pd.remap_columns, {
                    'Start Frequency (Hz)': 'start_frequency',
                    'Center Frequency (Hz)': 'center_frequency',
                    'End Frequency (Hz)': 'end_frequency',
                })
                .reset_index()))
        .encode(alt.Y('Speaker', title=None, axis=alt.Axis(orient='right', labelLimit=0))),
        lambda chart: curve_input(chart, 'ON')
        .facet(alt.Column('curve_label', type='nominal', title=None)),
        postprocess_chart),
    lambda chart: alt.layer(
        lsx.util.pipe(chart
            .mark_bar()
            .transform_calculate(band_label=
                alt.datum['Band'] + ' (' +
                alt.expr.format(alt.datum['band_info']['start_frequency'], '.02s') + ' - ' +
                alt.expr.format(alt.datum['band_info']['end_frequency'], '.02s') + ' Hz)')
            .encode(
                alt.X(
                    'value', type='quantitative',
                    scale=alt.Scale(reverse=True, domain=alt.DomainUnionWith([0, 1])),
                    title=['Narrow Band Deviation (NBD)', 'lower is better']),
                alt.Color('band_label', type='nominal', sort=None, title='Band'),
                alt.Order('Band', sort='descending'),
                tooltip=[
                    alt.Tooltip('Band'),
                    frequency_tooltip('band_info.start_frequency', 'Start Frequency'),
                    frequency_tooltip('band_info.center_frequency', 'Center Frequency'),
                    frequency_tooltip('band_info.end_frequency', 'End Frequency'),
                    alt.Tooltip('Speaker', title='Speaker'),
                    alt.Tooltip('value', type='quantitative', title='Band NBD', format='.3f'),
                ]),
            lambda chart: lsx.alt.highlight_mouseover(chart, fields=['Band'])),
        chart
            .mark_text(align='right', dx=-3)
            .encode(
                alt.X('value', type='quantitative', aggregate='sum'),
                alt.Text('value', type='quantitative', aggregate='sum', format='.2f'))))
```

```python
speakers_nbd
```

<!-- #region heading_collapsed=true -->
## Slope
<!-- #endregion -->

<!-- #region heading_collapsed=true -->
### Calculation
<!-- #endregion -->

Slope is discussed in section 3.2.3 of the [paper](http://www.aes.org/e-lib/browse.cfm?elib=12847) and section 0073 of the [patent](https://patents.google.com/patent/US20050195982A1). It involves computing an [Ordinary Least Squares (OLS)](https://en.wikipedia.org/wiki/Ordinary_least_squares) linear regression over the frequency response curve. More precisely, in the following model, $a$ and $b$ are chosen to minimize the sum of squared Y residuals among all measurement points between 100 Hz and 16 kHz:

$$Y = b\ln(x) + a$$

Where:

- $Y$ is the predicted amplitude in dB.
- $x$ is the frequency in Hz.
- $b$ is the slope in $\ln(2)$dB/octave (multiply by $\ln(2) \approx 0.7$ to get dB/octave).
- $a$ is the intercept, i.e. the prediction for $x$ = 1 Hz, in dB.

Loudspeaker Explorer computes the above linear regression because that is a prerequisite for computing SM. The actual slope variable (SL) discussed in the paper is not computed because it isn't used in the final model.

```python
speakers_slope_min_frequency_hz = 100
speakers_slope_max_frequency_hz = 16000

speakers_fr_slope = speakers_fr_olive.loc[lsx.util.pipe(
    speakers_fr_olive.index.get_level_values('Frequency [Hz]'),
    lambda freqs: (freqs >= speakers_slope_min_frequency_hz) & (freqs <= speakers_slope_max_frequency_hz))]

speakers_slope_regression = (speakers_fr_slope
    .groupby('Speaker')
    .apply(lambda speaker: lsx.pd.apply_notna(speaker, lambda curve: smf.ols(
            data=curve
                .rename('value_db')
                .reset_index('Frequency [Hz]')
                .reset_index(drop=True)
                .rename(columns={'Frequency [Hz]': 'frequency_hz'}),
            formula='value_db ~ np.log(frequency_hz)').fit())))

speakers_slope_b = speakers_slope_regression.pipe(lsx.pd.applymap_notna, lambda regression_results:
    regression_results.params.loc['np.log(frequency_hz)'])
speakers_slope_b
```

### Results

```python
def speakers_slope_value_at_frequency(frequency_hz):
    return (speakers_slope_regression
        .pipe(lsx.pd.applymap_notna, lambda regression_results:
              regression_results.predict({'frequency_hz': frequency_hz}).squeeze())
        .pipe(lsx.pd.append_constant_index, frequency_hz, name='Frequency [Hz]'))

conditional_chart(max_sidebyside_speaker_count, lambda: frequency_response_db_chart(
    pd.concat({
        'Curve': speakers_fr_olive,
        'Slope': pd.concat([
            speakers_slope_value_at_frequency(speakers_slope_min_frequency_hz),
            speakers_slope_value_at_frequency(speakers_slope_max_frequency_hz),
        ])
    }, names=['Dataset']),
    lambda chart: lsx.util.pipe(chart
        .transform_lookup(lookup='speaker', as_='speaker_b', from_=alt.LookupData(
            key='Speaker', data=speakers_slope_b
                .apply(lambda df: df.to_dict(), axis='columns')
                .rename('b')
                .to_frame()
                .reset_index()))
        .transform_calculate(layer=alt.datum['curve'] + ' ' + alt.datum['Dataset'])
        .encode(
            value_yaxis(),
            alt.Color(
                'layer', type='nominal', title=None,
                legend=alt.Legend(symbolType='stroke'))),
        lambda chart: curve_input(chart, 'PIR'),
        speaker_facet, speaker_input),
    lambda chart: alt.layer(
        lsx.alt.interactive_line(chart)
            .transform_filter(alt.datum['Dataset'] == 'Curve'),
        lsx.alt.interactive_line(chart, add_mark=lambda chart: chart.mark_line(clip=True))
            .transform_filter(alt.datum['Dataset'] == 'Slope')
            .transform_calculate(b=alt.datum['speaker_b']['b'][alt.datum['curve']])
            .transform_calculate(db_per_octave=alt.datum['b'] * alt.expr.LN2)
            .encode(tooltip=[
                    alt.Tooltip('b', title='b (ln(2)dB/octave)', type='quantitative', format='.2f'),
                    alt.Tooltip('db_per_octave', title='Slope (dB/octave)', type='quantitative', format='.2f'),
                ])),
    fold={'as_': ['curve', 'value']},
    sidebyside=True, fineprint=chart_fineprint))
```

<!-- #region heading_collapsed=true -->
## SM
<!-- #endregion -->

**CAUTION: interpreting SM is very tricky and fraught with peril.** The Olive paper describes SM as the "smoothness" of the response, which is misleading at best. The real meaning of SM as mathematically defined in the paper is way more subtle and hard to describe. In reality, SM describes how much of the curve deviation from a flat, *horizontal* line can be explained by the overall slope (as opposed to just jagginess). This leads to some counter-intuitive results - for example, a roughly horizontal curve with negligible deviations can have an SM of zero! (For more debate on this topic, see [this](https://www.audiosciencereview.com/forum/index.php?threads/speaker-equivalent-sinad-discussion.10818/page-8#post-308028), [this](https://www.audiosciencereview.com/forum/index.php?threads/selah-audio-rc3r-3-way-speaker-review.11218/page-4#post-320082), [this](https://www.audiosciencereview.com/forum/index.php?threads/master-preference-ratings-for-loudspeakers.11091/page-7#post-322879), [this](https://www.audiosciencereview.com/forum/index.php?threads/master-preference-ratings-for-loudspeakers.11091/page-8#post-325872) and especially [this](https://www.audiosciencereview.com/forum/index.php?threads/master-preference-ratings-for-loudspeakers.11091/page-14#post-377457) and [this](https://www.audiosciencereview.com/forum/index.php?threads/sony-ss-cs5-3-way-speaker-review.13562/page-13#post-411179).)

<!-- #region heading_collapsed=true -->
### Calculation
<!-- #endregion -->


SM is discussed in section 3.2.3 of the [paper](http://www.aes.org/e-lib/browse.cfm?elib=12847) and section 0071 of the [patent](https://patents.google.com/patent/US20050195982A1). Loudspeaker Explorer uses an interpretation in which SM is the [coefficient of determination](https://en.wikipedia.org/wiki/Coefficient_of_determination) ($r^2$) of the linear regression model computed in the previous Slope section. Higher is better.

```python
speakers_sm = speakers_slope_regression.pipe(lsx.pd.applymap_notna, lambda regression_results:
    regression_results.rsquared)
speakers_sm
```

### Results


See [here](https://www.audiosciencereview.com/forum/index.php?threads/master-preference-ratings-for-loudspeakers.11091/page-20#post-409739) for a guided tour on how SM works and how to interpret the following charts.

```python
def compensate_mean(speakers_fr):
    return speakers_fr.sub(speakers_fr_slope
        .groupby('Speaker')
        .mean())

def compensate_slope(speakers_fr):
    return speakers_fr.sub(speakers_fr
        .groupby('Speaker')
        .apply(lambda speaker: lsx.pd.apply_notna(speaker, lambda curve:
                speakers_slope_regression
                    .loc[speaker.name, curve.name]
                    .predict({'frequency_hz': curve
                        .index
                        .get_level_values('Frequency [Hz]')
                        .to_series()}))))

conditional_chart(max_sidebyside_speaker_count, lambda: frequency_response_db_chart(
    pd.concat({
        'Mean': compensate_mean(speakers_fr_olive),
        'Slope': compensate_slope(speakers_fr_olive),
    }, names=['reference']),
    lambda chart: lsx.util.pipe(chart
        .transform_calculate(layer=alt.datum['curve'] + ' relative to ' + alt.datum['reference'])
        .encode(
            alt.Y(
                'value', type='quantitative',
                title='Deviation (dBr)',
                scale=alt.Scale(domain=[-40, 10]),
                axis=alt.Axis(grid=True)),
            alt.Color(
                'layer', type='nominal', title=None,
                legend=alt.Legend(symbolType='stroke'))),
        lambda chart: curve_input(chart, 'PIR'),
        speaker_facet, speaker_input),
    lambda chart: lsx.alt.interactive_line(chart),
    fold={'as_': ['curve', 'value']},
    additional_tooltips=[alt.Tooltip('reference', title='Relative to', type='nominal')],
    sidebyside=True, fineprint=chart_fineprint))
```

```python
conditional_chart(max_sidebyside_speaker_count, lambda: frequency_response_chart(
    pd.concat({
        'Mean': compensate_mean(speakers_fr_slope),
        'Slope': compensate_slope(speakers_fr_slope),
    }, names=['reference']),
    lambda chart: lsx.util.pipe(chart
        .transform_calculate(layer=
            # This can't be expressed using an Altair expression due to https://github.com/altair-viz/altair/issues/2194
            '[datum.curve + " relative to " + datum.reference + ";",' +
            '(datum.reference == "Mean" ? "TSS (Total Sum of Squares)" : "RSS (Residual Sum of Squares)"),'
            '"contribution"]')
        .transform_calculate(deviation=alt.datum['value'])
        .transform_calculate(deviation_squared=alt.datum['deviation'] ** 2)
        .transform_calculate(value=alt.datum['deviation_squared'] * alt.expr.if_(alt.datum['reference'] == 'Slope', -1, 1))
        .encode(
            alt.Y(
                'value', type='quantitative',
                title='Squared deviation (dB²)',
                scale=alt.Scale(domain=[-30, 30]),
                axis=alt.Axis(grid=True)),
            alt.Color(
                'layer', type='nominal', title=None,
                legend=alt.Legend(symbolType='square'))),
        lambda chart: curve_input(chart, 'PIR'),
        speaker_facet, speaker_input),
    lambda chart: lsx.alt.interactive_line(
        chart, lambda chart: chart.mark_bar().encode(size=alt.value(2))),
    fold={'as_': ['curve', 'value']},
    alter_tooltips=lambda tooltips:
        [alt.Tooltip('reference', title='Relative to', type='nominal')] +
        tooltips +
        [
            value_db_tooltip('deviation', title='Deviation'),
            alt.Tooltip('deviation_squared', title='Squared deviation (dB²)', type='quantitative', format='.2f'),
        ],
    sidebyside=True))
```

```python
conditional_chart(max_sidebyside_speaker_count, lambda: frequency_response_chart(
    pd.concat({
        'mean': compensate_mean(speakers_fr_slope),
        'slope': compensate_slope(speakers_fr_slope),
    }, names=['reference']),
    lambda chart: lsx.util.pipe(chart
        .transform_calculate(deviation=alt.datum['value'])
        .transform_calculate(value=alt.datum['deviation'] ** 2)
        .transform_pivot(pivot='reference', groupby=['speaker', 'curve', 'frequency'], value='value')
        .transform_joinaggregate(tss='sum(mean)', groupby=['speaker', 'curve'])
        .transform_joinaggregate(count='count(mean)', groupby=['speaker', 'curve'])
        .transform_calculate(sm=-alt.datum['slope'] / alt.datum['tss'])
        .transform_calculate(value=alt.datum['sm'] * alt.datum['count'])
        .encode(
            alt.Color(
                'curve', type='nominal',
                title=None, legend=alt.Legend(symbolType='square')), 
            alt.Y(
                'value', type='quantitative',
                title=[
                    'Scaled SM-1 contribution',
                    'Scaled -RSS/TSS contribution',
                    'Scaled fraction of variance explained contribution'],
                scale=alt.Scale(domain=[-5, 0]))),
        lambda chart: curve_input(chart, 'PIR'),
        speaker_facet, speaker_input),
    lambda chart: lsx.alt.interactive_line(
        chart, lambda chart: chart.mark_bar().encode(size=alt.value(2))),
    fold={'as_': ['curve', 'value']},
    alter_tooltips=lambda tooltips:
        [alt.Tooltip('tss', title='TSS (dB²)', type='quantitative', format='.2f')] +
        tooltips +
        [
            alt.Tooltip('slope', title='RSS (dB²)', type='quantitative', format='.2f'),
            alt.Tooltip('sm', title='SM-1 contribution', type='quantitative', format='.4f'),
            alt.Tooltip('value', title='Scaled SM-1 contribution', type='quantitative', format='.2f'),
        ],
    sidebyside=True))
```

```python
lsx.alt.make_chart(
    speakers_sm,
    lambda chart: lsx.util.pipe(chart
        .properties(width=bar_chart_width.value)
        .transform_fold(speakers_sm.columns.values, ['curve', 'value'])
        .transform_lookup(lookup='curve', as_='curve_info', from_=alt.LookupData(
            key='curve', data=pd.Series(olive_curve_labels)
                .rename_axis('curve')
                .rename('label')
                .reset_index()))
        .transform_calculate(curve_label=alt.datum['curve'] + ' ' + alt.datum['curve_info']['label'])
        .encode(alt.Y('Speaker', title=None, axis=alt.Axis(labelLimit=0))),
        lambda chart: curve_input(chart, 'PIR')
        .facet(alt.Column('curve_label', type='nominal', title=None)),
        postprocess_chart),
    lambda chart: alt.layer(
        lsx.util.pipe(chart
            .mark_bar()
            .encode(
                alt.X(
                    'value', type='quantitative',
                    title='SM (higher is better)',
                    scale=alt.Scale(domain=[0, 1])),
                tooltip=[
                    alt.Tooltip('Speaker'),
                    alt.Tooltip('value', title='SM', type='quantitative', format='.2f')
                ]),
            lsx.alt.highlight_mouseover),
        chart
            .mark_text(align='left', dx=3)
            .encode(
                alt.X('value', type='quantitative'),
                alt.Text('value', type='quantitative', format='.2f'))))
```

```python
speakers_sm
```

<!-- #region heading_collapsed=true -->
## Low Frequency Extension (LFX)
<!-- #endregion -->

<!-- #region heading_collapsed=true -->
### Calculation
<!-- #endregion -->


LFX is discussed in section 3.2.4 of the [paper](http://www.aes.org/e-lib/browse.cfm?elib=12847) and section 0078 of the [patent](https://patents.google.com/patent/US20050195982A1). Loudspeaker Explorer uses the following formula:

$$\mathrm{LFX} = \log_{10} \min \{ x_i : SP_{i+1} \gt \overline{LW}-6 \}$$

Where:

 - $\mathrm{LFX}$ is the low frequency extension in $\log_{10}\mathrm{Hz}$. Bring $10$ to the power of $\mathrm{LFX}$ to get the cutoff frequency in Hz.
 - $x_i$ is the frequency of the $i$th measurement point (in increasing frequency order).
 - $SP_i$ is the sound pressure of the Sound Power curve in dB at the $i$th measurement point.
 - $\overline{LW}$ is the mean sound pressure of the Listening Window curve in dB between 300 Hz and 10 kHz.
 
In plain English, given the first measurement point whose Sound Power is above the -6 dB point (based on the Listening Window average between 300 and 10 kHz), LFX is the logarithm base 10 of the frequency of the previous measurement point.

For some debate on the definition of this metric, see [this](https://www.audiosciencereview.com/forum/index.php?threads/speaker-equivalent-sinad-discussion.10818/page-7#post-306831), [this](https://www.audiosciencereview.com/forum/index.php?threads/speaker-equivalent-sinad-discussion.10818/page-8#post-307638) and [this](https://www.audiosciencereview.com/forum/index.php?threads/speaker-equivalent-sinad-discussion.10818/page-9#post-308320). Note that the Loudspeaker Explorer formula differs somewhat from the original formula in the paper. This is because the formula in the paper did not seem to anticipate pathological Sound Power curves like the [Ocean Way Audio HR5](https://www.audiosciencereview.com/forum/index.php?threads/ocean-way-hr5-studio-monitor-review.13925/#post-424729) that dip below the -6 dB point multiple times below 300 Hz. The "improved" formula Loudspeaker Explorer uses returns a more sensible result for such speakers, but still returns the same result as the original formula for "well-behaved" Sound Power curves.

```python
lfx_reference_curve = 'LW'
lfx_reference_min_frequency = 300
lfx_reference_max_frequency = 10000

speakers_lfx_reference = (speakers_fr_olive
    .loc[:, lfx_reference_curve]
    .pipe(lambda speakers_reference: speakers_reference.loc[lsx.util.pipe(speakers_reference
        .index
        .get_level_values('Frequency [Hz]'),
        lambda freqs: (freqs >= lfx_reference_min_frequency) & (freqs <= lfx_reference_max_frequency))])
    .groupby('Speaker')
    .mean())
speakers_lfx_reference.rename(f'{lfx_reference_curve} average (dB)').to_frame()
```

```python
lfx_curve = 'SP'
lfx_cutoff_threshold = -6

speakers_lfx_cutoff = (speakers_fr_olive
    .loc[:, lfx_curve]
    .reset_index('Frequency [Hz]')
    .groupby('Speaker')
    .apply(lambda speaker: speaker.iloc[
        speaker.loc[:, lfx_curve].gt(speakers_lfx_reference.loc[speaker.name] + lfx_cutoff_threshold).argmax()-1]))
speakers_lfx_cutoff
```

```python
speakers_lfx = (speakers_lfx_cutoff
    .pipe(lsx.pd.remap_columns, {'Frequency [Hz]': 'LFX'})
    .pipe(np.log10))
speakers_lfx
```

### Results


Note that the LFX cutoff frequency can appear slightly below the threshold in the following chart. That's because the calculation is made on the set of measurement points in their original resolution, not the interpolated curve that is drawn on the chart.

```python
conditional_chart(max_sidebyside_speaker_count, lambda: frequency_response_db_chart(
    speakers_fr_olive.loc[:, [lfx_curve, lfx_reference_curve]],
    lambda chart: lsx.util.pipe(chart
        .transform_lookup(lookup='speaker', as_='speaker_cutoff', from_=alt.LookupData(
                    key='Speaker', data=speakers_lfx_cutoff
                        .pipe(lsx.pd.remap_columns, {
                            'Frequency [Hz]': 'frequency',
                            lfx_curve: 'value',
                        })
                        .reset_index()))
        .transform_lookup(lookup='curve', as_='curve_info', from_=alt.LookupData(
            key='curve', data=pd.Series(olive_curve_labels)
                .rename_axis('curve')
                .rename('label')
                .reset_index()))
        .encode(
            sound_pressure_yaxis(),
            alt.Color(
                'curve_label', type='nominal', title=None,
                legend=alt.Legend(symbolType='stroke')),
            strokeDash=alt.condition(
                (alt.datum['curve'] == lfx_reference_curve) | alt.datum['is_reference'],
                alt.value([4, 2]), alt.value([1, 0])),
            strokeWidth=alt.condition(
                alt.datum['curve'] == lfx_reference_curve,
                alt.value(1), alt.value(2))),
        speaker_facet, speaker_input),
    lambda chart: alt.layer(
        lsx.alt.interactive_line(chart)
            .transform_calculate(curve_label=alt.datum['curve'] + ' ' + alt.datum['curve_info']['label']),
        (lambda chart: chart
        .transform_filter(
            (alt.datum['curve'] == lfx_reference_curve) &
            alt.expr.inrange(alt.datum['frequency'], [lfx_reference_min_frequency, lfx_reference_max_frequency]))
        .transform_aggregate(
            value='mean(value)', groupby=['reference_curve', 'speaker', 'speaker_cutoff']))(alt.layer(
            lsx.alt.interactive_line(chart, add_mark=lambda chart: chart.mark_rule())
                .transform_calculate(is_reference=alt.expr.toBoolean(True))
                .transform_calculate(curve_label=alt.expr.toString('Reference'))
                .transform_calculate(frequency=alt.expr.toNumber(lfx_reference_min_frequency))
                .transform_calculate(max_frequency=alt.expr.toNumber(lfx_reference_max_frequency))
                .encode(
                    alt.X2('max_frequency'), strokeWidth=alt.value(2),
                    tooltip=[value_db_tooltip(title='Reference level (dB)')]),
            lsx.alt.interactive_line(chart, add_mark=lambda chart: chart.mark_rule())
                .transform_calculate(curve_label=alt.expr.toString('LFX Cutoff threshold'))
                .transform_calculate(frequency='MIN_VALUE')
                .transform_calculate(max_frequency='MAX_VALUE')
                .transform_calculate(value=alt.datum['value'] + lfx_cutoff_threshold)
                .encode(
                    alt.X2('max_frequency'), strokeWidth=alt.value(2),
                    tooltip=[value_db_tooltip(title='LFX Cutoff threshold')]
                ),
            lsx.alt.interactive_line(chart, add_mark=lambda chart: chart.mark_point(shape='triangle', size=200, opacity=1, filled=True))
                .transform_calculate(curve_label=alt.expr.toString('LFX Cutoff'))
                .transform_calculate(frequency=alt.datum['speaker_cutoff']['frequency'])
                .transform_calculate(value=alt.datum['speaker_cutoff']['value'])
                .transform_calculate(lfx=alt.expr.log(alt.datum['frequency']) / alt.expr.LN10)
                .encode(tooltip=[
                    value_db_tooltip(title='LFX Cutoff Level'),
                    frequency_tooltip(title='LFX Cutoff Frequency'),
                    alt.Tooltip('lfx', type='quantitative', title='LFX', format='.02f')])))),
    fold={'as_': ['curve', 'value']},
    additional_tooltips=[alt.Tooltip('curve_label', title='Curve', type='nominal')],
    sidebyside=True))
```

```python
lsx.alt.make_chart(speakers_lfx_cutoff
        .pipe(lsx.pd.remap_columns, {
            'Frequency [Hz]': 'frequency',
            lfx_curve: 'cutoff',
        }),
    lambda chart: lsx.util.pipe(chart
        .properties(width=bar_chart_width.value)
        .transform_calculate(value=alt.expr.log(alt.datum['frequency']) / alt.expr.LN10)
        .transform_calculate(min_value=alt.expr.toNumber(np.log10(20)))
        .encode(alt.Y('Speaker', title=None, axis=alt.Axis(orient='right', labelLimit=0))),
        postprocess_chart),
    lambda chart: alt.layer(
        lsx.util.pipe(chart
            .mark_bar()
            .encode(
                alt.X(
                    'value', type='quantitative',
                    title='LFX (lower is better)',
                    scale=alt.Scale(domain=alt.DomainUnionWith([np.log10(20), np.log10(100)]), reverse=True)),
                alt.X2('min_value'),  # https://github.com/vega/vega-lite/issues/6655
                tooltip=[
                    alt.Tooltip('Speaker'),
                    value_db_tooltip('cutoff', title='LFX Cutoff Level'),
                    frequency_tooltip(title='LFX Cutoff Frequency'),
                    alt.Tooltip('value', title='LFX', type='quantitative', format='.2f'),
                ]),
            lsx.alt.highlight_mouseover),
        chart
            .mark_text(align='right', dx=-3)
            .encode(
                alt.X('value', type='quantitative'),
                alt.Text('value', type='quantitative', format='.2f'))))
```

## Preference Rating

<!-- #region heading_collapsed=true -->
### Calculation
<!-- #endregion -->

The definition of the final preference rating is discussed in section 5.3 of the [paper](http://www.aes.org/e-lib/browse.cfm?elib=12847) and section 0101 of the [patent](https://patents.google.com/patent/US20050195982A1). It is a simple linear combination of some of the variables that were computed in the previous sections:

$$\mathrm{PR} = 12.69-2.49\cdot\mathrm{NBD}_\mathrm{ON}-2.99\cdot\mathrm{NBD}_\mathrm{PIR}+2.32\cdot\mathrm{SM}_\mathrm{PIR}-4.31\cdot\mathrm{LFX}$$

```python
speakers_olive_components = pd.concat({
    'NBD': [-2.49, -2.99] * speakers_nbd.loc[:, ['ON', 'PIR']],
    'SM': +2.32 * speakers_sm.loc[:, ['PIR']],
    'LFX': -4.31 * speakers_lfx.loc[:, 'LFX'],
}, axis='columns').rename_axis(columns=['Variable', 'Curve'])
speakers_olive_components
```

```python
speakers_olive_curves = (speakers_olive_components
    .groupby('Curve', axis='columns')
    .sum())
speakers_olive_curves
```

```python
speakers_olive = (
    speakers_olive_curves
    .sum(axis='columns')
    .add(12.69)
    .rename('Olive Preference Rating'))
speakers_olive.to_frame()
```

### Results


In the following chart, $\mathrm{NBD}_\mathrm{PIR}$ and $\mathrm{SM}_\mathrm{PIR}$ are summed into a single $\mathrm{PIR}$ metric. This makes the numbers easier to reason about, as $\mathrm{SM}_\mathrm{PIR}$ is difficult to interpret in isolation.

To make the below chart more readable, the LFX scale has been adjusted to be relative to a speaker with a low frequency extension of 40 Hz ($\mathrm{LFX} \approx 1.60$, scaled $\mathrm{LFX} \approx -6.90$).

```python
lsx.alt.make_chart(
    speakers_olive_curves,
    lambda chart: lsx.util.pipe(chart
        .properties(width=bar_chart_width.value)
        .transform_fold(speakers_olive_curves.columns.values, ['curve', 'raw_value'])
        .transform_lookup(lookup='curve', as_='curve_info', from_=alt.LookupData(
            key='curve', data=pd.Series({**olive_curve_labels, **{'LFX': 'Low Frequency Extension'}})
                .rename_axis('curve')
                .rename('label')
                .reset_index()))
        .transform_calculate(curve_label=alt.datum['curve'] + ' ' + alt.datum['curve_info']['label'])
        .transform_calculate(value=alt.datum['raw_value'] + alt.expr.if_(alt.datum['curve'] == 'LFX', 4.31 * np.log(40) / np.log(10), 0))
        .encode(
            alt.X(
                    'value', type='quantitative',
                    title='Scaled Olive Preference Rating contribution (higher is better)',
                    scale=alt.Scale(domain=alt.DomainUnionWith([-3, 1]))),
            alt.Y('Speaker', type='nominal', title=None, axis=alt.Axis(labelLimit=0)))
        .facet(row=alt.Row('curve', title=None, type='nominal')),
        postprocess_chart),
    lambda chart: alt.layer(
        lsx.util.pipe(chart
            .mark_bar()
            .encode(
                tooltip=[
                    alt.Tooltip('Speaker'),
                    alt.Tooltip('curve_label', title='Curve', type='nominal'),
                    alt.Tooltip('raw_value', title='Scaled rating contribution', type='quantitative', format='.2f')
                ]),
            lsx.alt.highlight_mouseover),
        chart
            .transform_filter(alt.datum['value'] < 0)
            .mark_text(align='right', dx=-3)
            .encode(
                alt.Text('raw_value', type='quantitative', format='.2f')),
        chart
            .transform_filter(alt.datum['value'] >= 0)
            .mark_text(align='left', dx=3)
            .encode(
                alt.Text('raw_value', type='quantitative', format='.2f'))))
```

The following [box plot](https://en.wikipedia.org/wiki/Box_plot) should be read in the following way:

- The **box** (±0.5) indicates the **50%** [prediction interval](https://en.wikipedia.org/wiki/Prediction_interval) of the rating. In other words: there is a 50% chance that the average listener will give this speaker a rating that falls within the box.
- The **lines (whiskers)** (±0.9) are similar to boxes but with a **75%** interval.

A mathematically equivalent, and perhaps more useful, way of looking at this plot is the following:

- If **boxes barely overlap** (predicted score differs by 1.0), there is a **91%** chance that the average listener will prefer the higher-rated speaker.
- If **lines (whiskers) barely overlap** (predicted score differs by 1.8), the probability is **99%**.

These numbers were [derived](https://www.audiosciencereview.com/forum/index.php?threads/master-preference-ratings-for-loudspeakers.11091/page-23#post-429503) from section 5.3 of the [paper](http://www.aes.org/e-lib/browse.cfm?elib=12847) and section 0111 of the [patent](https://patents.google.com/patent/US20050195982A1), which states that the model error follows a normal distribution with a standard error of **0.8**.

**Disclaimer: the above reasoning assumes that the speakers being rated are "typical" relative to the speakers used in the original study. Extrapolated preference ratings for speakers that are very different from the sample used in the study should be taken with a larger grain of salt than these prediction intervals indicate. For example, scores above 7 [carry more uncertainty](https://www.audiosciencereview.com/forum/index.php?threads/vanatoo-transparent-zero-speaker-review.13717/page-7#post-417999).**

```python
lsx.alt.make_chart(
    speakers_olive
        .rename('value')
        .to_frame(),
    lambda chart: lsx.util.pipe(chart
        .properties(width=bar_chart_width.value)
        .transform_calculate(rating=alt.datum['value'])
        .encode(
            alt.X(
                'value', type='quantitative',
                title='Olive Predicted Preference Rating (higher is better)',
                scale=alt.Scale(domain=alt.DomainUnionWith([0, 10]))),
            alt.Y(
                'Speaker', type='nominal', title=None,
                axis=alt.Axis(labelLimit=0, tickMinStep=10),
                sort=alt.SortField('rating', order='descending')),
            tooltip=[
                alt.Tooltip('Speaker'),
                alt.Tooltip('rating', title='Predicted rating', type='quantitative', format='.2f')
            ]),
        lambda chart: postprocess_chart(chart,
            fineprint=['Prediction intervals: 50% (boxes), 75% (whiskers)'] + chart_fineprint)),
    lambda chart: alt.layer(
        chart
            # See https://en.wikipedia.org/wiki/Normal_distribution#Quantile_function
            .transform_calculate(value='quantileNormal((0.75+1)/2, datum.rating,  0.8)')
            .transform_calculate(end  ='quantileNormal((0.75+1)/2, datum.rating, -0.8)')
            .mark_rule(strokeWidth=1)
            .encode(alt.X2('end')),
        chart
            .transform_calculate(value ='quantileNormal((0.50+1)/2, datum.rating,  0.8)')
            .transform_calculate(end   ='quantileNormal((0.50+1)/2, datum.rating, -0.8)')
            .mark_bar(stroke='black', size=16)
            .encode(alt.X2('end'),
                alt.Color(
                    'rating', type='quantitative',
                    scale=alt.Scale(scheme='redyellowgreen', domain=[0, 10]), legend=None)),
        chart
            .mark_text(fontWeight='bold')
            .encode(
                alt.Text('value', type='quantitative', format='.1f'))))
```

```python
olive_matrix_selection_x = alt.selection_single(
    on='mouseover', clear='mouseout', encodings=['x'])
olive_matrix_selection_y = alt.selection_single(
    on='mouseover', clear='mouseout', encodings=['y'])

lsx.alt.make_chart(
    speakers_olive
        .rename('value')
        .to_frame()
        .pipe(lsx.pd.append_constant_index, 0, 'dummy_key'),
    lambda chart: lsx.util.pipe(chart
        .properties(title='Probability that the average listener will prefer speaker A to speaker B (%)')
        # Vega Lite doesn't seem to have a way to do do cartesian products,
        # but we can emulate that by inserting the whole dataset into every datum using lookup(),
        # and then we expand that into multiple datums using flatten().
        .transform_lookup(lookup='dummy_key', from_=alt.LookupData(
            key='dummy_key', fields=['VsSpeakerInfo'], data=pd.DataFrame(
                {'dummy_key': 0, 'VsSpeakerInfo': [speakers_olive
                    .rename('value')
                    .reset_index()
                    .to_dict(orient='records')]})))
        .transform_flatten(['VsSpeakerInfo'])
        .transform_calculate(VsSpeaker=alt.datum['VsSpeakerInfo']['Speaker'])
        .transform_calculate(VsValue=alt.datum['VsSpeakerInfo']['value'])
        .transform_calculate(diff=alt.datum['value'] - alt.datum['VsValue'])
        .transform_calculate(percent='(1 - cumulativeNormal(0, datum.diff, 0.8)) * 100')
        .encode(
            alt.Y(
                'Speaker', type='nominal', title='Speaker A',
                sort=alt.SortField('value', order='descending')),
            alt.X(
                'VsSpeaker', type='nominal', title='Speaker B',
                sort=alt.SortField('VsValue', order='ascending')),
            tooltip=[
                alt.Tooltip('Speaker', type='nominal', title='Speaker A'),
                alt.Tooltip('VsSpeaker', type='nominal', title='Speaker B'),
                alt.Tooltip('value', type='nominal', title='Speaker A Score', format='.1f'),
                alt.Tooltip('VsValue', type='nominal', title='Speaker B Score', format='.1f'),
                alt.Tooltip('diff', type='nominal', title='Score difference (A-B)', format='.1f'),
                alt.Tooltip('percent', type='nominal', title='Probability of A>B (%)', format='.0f'),
            ]),
        postprocess_chart),
    lambda chart: alt.layer(
        lsx.util.pipe(chart
            .mark_rect()
            .add_selection(olive_matrix_selection_x)
            .add_selection(olive_matrix_selection_y)
            .encode(
                color=alt.Color(
                    'percent', type='quantitative',
                    scale=alt.Scale(scheme='redyellowgreen', domain=[0, 100]), legend=None),
                fillOpacity=alt.condition(
                    olive_matrix_selection_x | olive_matrix_selection_y,
                    alt.value(1), alt.value(0.2)))),
        chart
            .mark_text()
            .encode(alt.Text('percent', type='quantitative', format='.0f'))))
```
