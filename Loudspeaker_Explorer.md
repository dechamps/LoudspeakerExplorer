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

This notebook is powered by amazing software: [Google Colaboratory](https://colab.research.google.com/), [Jupyter](https://jupyter.org/), [Jupytext](https://github.com/mwouts/jupytext), [Pandas](https://pandas.pydata.org/), and [Altair](https://altair-viz.github.io/).

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
import yattag
import altair as alt
import yaml

import loudspeakerexplorer as lsx
```

```python
settings = lsx.Settings(pathlib.Path('settings.json'))

prerender_mode = bool(os.environ.get('LOUDSPEAKER_EXPLORER_PRERENDER', default=False))

def form(widget):
    form_banner = widgets.HTML()
    def set_form_banner(contents):
        form_banner.value = '<div style="text-align: left; padding-left: 1ex; border: 2px solid red; background-color: #eee">' + contents + '</div>'
    if prerender_mode:
        set_form_banner('<strong>Settings disabled</strong> because the notebook is not running. Run the notebook (in Colab, "Runtime" → "Run All") to change settings.')
        def disable_widget(widget):
            widget.disabled = True
        lsx.util.recurse_attr(widget, 'children', disable_widget)
    lsx.util.recurse_attr(widget, 'children',
        lambda widget: widget.observe(
            lambda change: set_form_banner('<strong>Settings have changed.</strong> Run the notebook again (in Colab, "Runtime" → "Run All") for the changes to take effect.'), names='value'))
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
 - [**NHT Pro M-00**](https://www.audiosciencereview.com/forum/index.php?threads/nht-pro-m-00-powered-monitor-review.10859/): the raw data was not published.
 - [**Yamaha HS5**](https://www.audiosciencereview.com/forum/index.php?threads/yamaha-hs5-powered-monitor-review.10967/): the raw data published is incomplete and does not come in the standard zipfile format that the tool expects.

Also note that the datasets for **JBL 305P MkII** and **Neumann KH80 (sample 1)** are missing *Directivity Index* data. Due to a bug in the tool this also breaks the Spinorama charts unless another speaker is also selected.

Also note that a [measurement artefact](https://www.audiosciencereview.com/forum/index.php?threads/klipsch-r-41m-bookshelf-speaker-review.11566/page-3#post-332136) in the form of a slight [ripple in high frequencies](https://www.audiosciencereview.com/forum/index.php?threads/neumann-kh-80-dsp-speaker-measurements-take-two.11323/page-10#post-324189) (above 4 kHz or so) is present in all measurements made before 2020-02-23. This was [fixed](https://www.audiosciencereview.com/forum/index.php?threads/genelec-8341a-sam%E2%84%A2-studio-monitor-review.11652/#post-335109) starting from the Genelec 8341A measurement.

Also note that the **Revel F35** measurement suffers from [numerical computation issues](https://www.audiosciencereview.com/forum/index.php?threads/revel-f35-speaker-review.12053/page-20#post-354889) that cause erroneous spikes around 1 kHz.

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
        return checkbox

    def img():
        doc = yattag.Doc()
        doc.stag('img', src=speaker.loc['Picture URL'])
        box = widgets.Box([widgets.HTML(doc.getvalue())])
        box.layout.height = '150px'
        box.layout.width = '100px'
        return box
    
    def info():
        doc, tag, text, line = yattag.Doc().ttl()
        product_url = speaker.loc['Product URL']
        if not pd.isna(product_url):
            line('a', 'Product page', href=product_url, target='_blank')
            text(' - ')
        line('a', 'Review', href=speaker.loc['Review URL'], target='_blank')
        doc.stag('br')
        text('Active' if speaker.loc['Active'] else 'Passive')
        doc.stag('br')
        text('${:.0f} (single)'.format(speaker.loc['Price (Single, USD)']))
        doc.stag('br')
        text('Measured ' + str(speaker.loc['Measurement Date'].date()))
        return widgets.HTML(doc.getvalue())

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

speakers_box = widgets.HBox(list(speakers.apply(speaker_box, axis='columns')))
speakers_box.layout.flex_flow = 'row wrap'
form(speakers_box)
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

```python
speakers_fr_annotated = (speakers_fr_raw
    .unstack(level='Frequency [Hz]')
    .pipe(lsx.pd.join_index, speakers_freqs_per_octave.to_frame())
    .stack()
)
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
speakers_fr_splnorm = speakers_fr_annotated.loc[:, 'Sound Pessure Level [dB]']
speakers_fr_dinorm = speakers_fr_annotated.loc[:, '[dB] Directivity Index ']
spl_axis_label = ['Absolute Sound Pressure Level (dB SPL)']
di_axis_label = ['Directivity Index (dBr)']
spl_domain = (55, 105)
di_domain = (-5, 10)
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
    if detrend_individually.value:
        speakers_fr_splnorm = speakers_fr_splnorm.sub(speakers_fr_splnorm
            .groupby('Speaker')
            .apply(lsx.fr.smooth, detrend_octaves.value))
        spl_axis_label = ['Sound Pressure (dBr)', detrend_octaves_label + ' detrended']
        spl_domain = (-25, 25)
        speakers_fr_dinorm = speakers_fr_dinorm.sub(speakers_fr_dinorm
            .groupby('Speaker')
            .apply(lsx.fr.smooth, detrend_octaves.value))
        di_axis_label = ['Directivity Index (dBr)', detrend_octaves_label + ' detrended']
        di_domain = (-7.5, 7.5)
    else:
        speakers_fr_splnorm = speakers_fr_splnorm.sub(speakers_fr_splnorm.loc[:, ('CEA2034', detrend_reference.value)]
            .groupby('Speaker')                     
            .apply(lsx.fr.smooth, detrend_octaves.value), axis='index')
        spl_axis_label = ['Sound Pressure (dBr)', 'relative to {} smoothed {} (dBr)'.format(detrend_octaves_label, detrend_reference.value)]
        spl_domain = (-40, 10)
        
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
# Appends a new index level with all identical values.
def append_constant_index(df, value=pd.NA, name=None):
    return df.set_index(pd.Index([value] * df.shape[0], name=name), append=True)

speakers_fr_smoothed = (speakers_fr_norm
    .unstack(level='Frequency [Hz]')
    .pipe(append_constant_index, 'No smoothing', name='Smoothing')
    .stack()
)
if smoothing_enabled.value:
    speakers_fr_smoothed_only = (speakers_fr_norm
        .groupby('Speaker')
        .apply(lsx.fr.smooth, smoothing_octaves.value)
        .unstack(level='Frequency [Hz]')
        .pipe(append_constant_index,
              lsx.widgets.lookup_option_label(smoothing_octaves) + ' smoothing',
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

form(widgets.VBox([
    widgets.HBox([speaker_offset_enabled, speaker_offset_db]),
    widgets.HBox([standalone_chart_width, standalone_chart_height]),
    widgets.HBox([sidebyside_chart_width, sidebyside_chart_height]),
]))
```

```python
# Rearranges the index, folding metadata such as resolution and smoothing into the "Speaker" index level.
def fold_speakers_info(speakers_fr):
    return (speakers_fr
        .unstack(level='Frequency [Hz]')
        .pipe(lambda df: df
              .pipe(lsx.pd.set_index, df
                  .index
                  .to_frame()
                  .apply(
                      # Ideally this should be on multiple lines, but it's not clear if that's feasible: https://github.com/vega/vega-lite/issues/5994
                      lambda speaker: pd.Series({'Speaker': '; '.join(speaker)}),
                      axis='columns')
                  .pipe(pd.MultiIndex.from_frame)))
        .stack())

(speakers_fr_ready, common_title) = (speakers_fr_smoothed
    .rename(
        level='Mean resolution (freqs/octave)',
        index=lambda freqs_per_octave: 'Mean {:.2g} pts/octave'.format(freqs_per_octave))
    .rename_axis(index={'Mean resolution (freqs/octave)': 'Resolution'})
    .pipe(lsx.pd.extract_common_index_levels)
)
single_speaker_mode = speakers_fr_ready.index.names == ['Frequency [Hz]']
if single_speaker_mode:
    # Re-add an empty Speaker index level.
    # The alternative would be to handle this case specially in every single graph, which gets annoying fast.
    speakers_fr_ready = (speakers_fr_ready
        .pipe(append_constant_index, '', name='Speaker')
        .swaplevel(0, -1)
    )
else:
    speakers_fr_ready = fold_speakers_info(speakers_fr_ready)
common_title = alt.TitleParams(
    text='; '.join(common_title.to_list()),
    anchor='start')

speaker_offsets = (speakers_fr_ready.index
    .get_level_values('Speaker')
    .drop_duplicates()
    .to_frame()
    .reset_index(drop=True)
    .reset_index()
    .set_index('Speaker')
    .loc[:, 'index']
    * (speaker_offset_db.value if speaker_offset_enabled.value else 0)
)
def relabel_speaker_with_offset(speaker_name):
    speaker_offset = speaker_offsets.loc[speaker_name]
    return speaker_name + ('' if speaker_offset == 0 else ' [{:+.0f} dB]'.format(speaker_offsets.loc[speaker_name]))
speakers_fr_ready_offset = (speakers_fr_ready
    # Arguably it would cleaner to use some kind of "Y offset" encoding channel in charts, but that doesn't seem to be supported yet: https://github.com/vega/vega-lite/issues/4703
    .add(speaker_offsets, axis='index', level='Speaker')
    .rename(relabel_speaker_with_offset, level='Speaker')
)

speakers_license = speakers.loc[
    speakers_fr_smoothed.index.get_level_values('Speaker').drop_duplicates(),
    'Data License']
credits = ['Data: amirm, AudioScienceReview.com - Plotted by Loudspeaker Explorer']
if speakers_license.nunique(dropna=False) == 1:
    (unique_license,) = speakers_license.unique()
    if (pd.notna(unique_license)):
        credits.append('Data licensed under {}'.format(unique_license))
else:
    for speaker, license in speakers_license.dropna().items():
        credits.append('{} data licensed under {}'.format(speaker, license))

alt.data_transformers.disable_max_rows()

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
    sidebyside=False,
    alter_tooltips=lambda tooltips: tooltips):
    return lsx.util.pipe(data
        .rename_axis(index={
            'Frequency [Hz]': 'frequency',
            'Speaker': 'speaker',
        })
        .reset_index('frequency')
        .pipe(lsx.alt.make_chart, title=common_title),
        lambda chart:
            set_chart_dimensions(chart, sidebyside)
            .encode(
                frequency_xaxis('frequency'),
                tooltip=alter_tooltips([frequency_tooltip()])))

def frequency_response_db_chart(data, additional_tooltips=[], *kargs, **kwargs):
    return frequency_response_chart(
        data, *kargs,
        alter_tooltips=lambda tooltips: additional_tooltips + tooltips + [value_db_tooltip()],
        **kwargs)

def standalone_speaker_frequency_response_db_chart(column, yaxis):
    return lsx.util.pipe(
        speakers_fr_ready
            .loc[:, column]
            .rename('value')
            .to_frame(),
        lambda data: frequency_response_db_chart(data,
            additional_tooltips=
                [alt.Tooltip('speaker', type='nominal', title='Speaker')]
                if data.index.get_level_values('Speaker').nunique() > 1 else [])
            .encode(y=yaxis),
        lambda chart: lsx.alt.interactive_line(chart, speaker_color()),
        speaker_input,
        postprocess_chart)

def frequency_xaxis(shorthand):
    return alt.X(
        shorthand, type='quantitative', title='Frequency (Hz)',
        scale=alt.Scale(type='log', base=10, nice=False),
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
        legend=None if single_speaker_mode else alt.Legend(
            orient='top', direction='vertical', labelLimit=600, symbolType='stroke'),
        **kwargs)

def speaker_facet(chart):
    return chart.facet(
        alt.Column('speaker', title=None, type='nominal'),
        title=common_title)

def speaker_input(chart):
    speakers = list(speakers_fr_ready.index.get_level_values('Speaker').drop_duplicates().values)
    if len(speakers) < 2: return chart
    selection = alt.selection_single(
            fields=['speaker'],
            bind=alt.binding_select(
                name='Speaker: ', options=[None] + speakers, labels=['All'] + speakers))
    return chart.transform_filter(selection).add_selection(selection)

def postprocess_chart(chart):
    # Altair/Vega-Lite doesn't provide a way to set multiple titles or just display arbitrary text.
    # We hack around that limitation by concatenating with a dummy chart that has a title.
    # See https://github.com/vega/vega-lite/issues/5997
    return (alt.vconcat(
        chart,
        alt.Chart(title=alt.TitleParams(
            credits, fontSize=10, fontWeight='lighter', color='gray', anchor='start'),
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
lsx.util.pipe(
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
    lambda data: frequency_response_chart(
        data, alter_tooltips=lambda tooltips:
        ([alt.Tooltip('speaker', title='Speaker')]
            if speakers_fr_ready.index.get_level_values('Speaker').nunique() > 1 else []) +
        tooltips +
        [alt.Tooltip('value', type='quantitative', title='Resolution (points/octave)', format='.2f')])
        .encode(alt.Y('value', type='quantitative', title='Resolution (points/octave)', axis=alt.Axis(grid=True))),
    lambda chart: lsx.alt.interactive_line(chart, speaker_color()),
    speaker_input,
    postprocess_chart)
```

# Standard measurements

Note that all the data shown in this section is a direct representation of the input data after normalization. No complex processing is done. In particular, data for derived metrics such as *Listening Window*, *Early Reflections*, *Sound Power*, Directivity Indices and even *Estimated In-Room Response* come directly from the input - they are not derived by this code.


## Spinorama

The famous CEA/CTA-2034 charts, popularized by Dr. Floyd Toole. These provide a good summary of the measurements from a perceptual perspective. Speakers are presented side-by-side for easy comparison.

Remember:
 - **All the charts are interactive.** Use the mousewheel to zoom, and drag & drop to pan. Click on a legend entry to highlight a single response; hold shift to highlight multiple responses. Double-click to reset the view. (PROTIP: to quickly switch back and forth between speakers, select the speaker dropdown, then use the left-right arrow keys on your keyboard.)
 - **Charts will not be generated if the section they're under is folded while the notebook is running.** To manually load a chart after running the notebook, click on the square to the left of the *Show Code* button. Or simply use *Run all* again after unfolding the section.

```python
speakers_fr_spinorama = speakers_fr_ready.pipe(lsx.pd.remap_columns, {
    ('CEA2034', 'On Axis'): 'On Axis',
    ('CEA2034', 'Listening Window'): 'Listening Window',
    ('CEA2034', 'Early Reflections'): 'Early Reflections',
    ('CEA2034', 'Sound Power'): 'Sound Power',
    ('Directivity Index', 'Early Reflections DI'): 'Early Reflections DI',
    ('Directivity Index', 'Sound Power DI'): 'Sound Power DI',
})

spinorama_chart_common = lsx.util.pipe(
    speakers_fr_spinorama,
    lambda data: frequency_response_db_chart(data,
        sidebyside=True,
        additional_tooltips=[alt.Tooltip('key', type='nominal', title='Response')])
        .transform_fold(speakers_fr_spinorama.columns.values))

# Note that there are few subtleties here because of Altair/Vega quirks:
# - To make the Y axes independent, `.resolve_scale()` has to be used *before
#   and after* `.facet()`. (In Vega terms, there needs to be a Resolve property
#   in *every* view composition specification.)
#   - If the first `.resolve_scale()` is removed from the layer spec, the axes
#     are not made independent.
#   - If the second `.resolve_scale()` is removed from the facet spec, Vega
#     throws a weird `Unrecognized scale name: "child_layer_0_y"` error.
# - To make the two axes zoom and pan at the same time, `.interactive()` has to
#   be used on each encoding, not on the overall view. Otherwise only the left
#   axis will support zoom & pan.
lsx.util.pipe(
    alt.layer(
        lsx.util.pipe(
            spinorama_chart_common
                .encode(sound_pressure_yaxis())
                .transform_filter(alt.FieldOneOfPredicate(field='key', oneOf=['On Axis', 'Listening Window', 'Early Reflections', 'Sound Power'])),
            lambda chart: lsx.alt.interactive_line(chart, key_color())),
        lsx.util.pipe(
            spinorama_chart_common
                .encode(directivity_index_yaxis(scale_domain=(-10, 40)))
                .transform_filter(alt.FieldOneOfPredicate(field='key', oneOf=['Early Reflections DI', 'Sound Power DI'])),
            lambda chart: lsx.alt.interactive_line(chart, key_color())))
        .resolve_scale(y='independent'),
    speaker_facet, speaker_input,
    lambda chart: chart.resolve_scale(y='independent'),
    postprocess_chart)
```

## On-axis response

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
    off_axis_angle_selection = alt.selection_single(
        fields=['angle'],
        bind=alt.binding_range(min=-170, max=180, step=10, name=direction + ' angle selector (°)'),
        clear='dblclick')
    speakers_fr_angles = (speakers_fr_ready
            .loc[:, 'SPL ' + direction]
            .pipe(lsx.data.convert_angles)
            .pipe(lambda df: df.pipe(lsx.pd.set_columns, df.columns.map(mapper=lambda column: f'{column:+.0f}')))
            .rename_axis(columns='Angle'))
    return lsx.util.pipe(
        speakers_fr_angles,
        lambda data: frequency_response_db_chart(data,
            sidebyside=True,
            additional_tooltips=[alt.Tooltip('key', type='nominal', title=direction + ' angle (°)')])
            .transform_fold(speakers_fr_angles.columns.values)
            .transform_calculate(angle=alt.expr.toNumber(alt.datum.key))
            .transform_filter(off_axis_angle_selection)
            .encode(sound_pressure_yaxis()),
        lambda chart: lsx.alt.interactive_line(
            chart, legend_channel=alt.Color(
                'angle', title=direction + ' angle (°)', type='quantitative',
                scale=alt.Scale(scheme='sinebow', domain=(-180, 180)),
                # We have to explicitly set the legend type to 'gradient' because of https://github.com/vega/vega-lite/issues/6258
                legend=alt.Legend(type='gradient', gradientLength=300, values=list(range(-180, 180+10, 10)))))
            .add_selection(off_axis_angle_selection),
        speaker_facet, speaker_input,
        postprocess_chart)

off_axis_angles_chart('Horizontal')
```

```python
off_axis_angles_chart('Vertical')
```

<!-- #region heading_collapsed=true -->
## Horizontal reflection responses
<!-- #endregion -->

```python
def reflection_responses_chart(axis):
    fr = (speakers_fr_ready
        .loc[:, f'{axis} Reflections']
        .rename_axis(columns=['Direction'])
        .rename(columns=lambda column:
                re.sub(f' ?{axis} ?', '', re.sub(' ?Reflection ?', '', column))))
    
    return lsx.util.pipe(
        fr,
        lambda data: frequency_response_db_chart(data,
            sidebyside=True,
            additional_tooltips=[alt.Tooltip('key', type='nominal', title='Direction')])
            .transform_fold(fr.columns.values)
            .encode(sound_pressure_yaxis()),
        lambda chart: lsx.alt.interactive_line(chart, key_color()),
        speaker_facet, speaker_input,
        postprocess_chart)

reflection_responses_chart('Horizontal')
```

<!-- #region heading_collapsed=true -->
## Vertical reflection responses
<!-- #endregion -->

```python
reflection_responses_chart('Vertical')
```

## Listening Window response

```python
standalone_speaker_frequency_response_db_chart(
    ('CEA2034', 'Listening Window'),
    sound_pressure_yaxis(title_prefix='Listening Window'))
```

## Early Reflections response

```python
standalone_speaker_frequency_response_db_chart(
    ('CEA2034', 'Early Reflections'),
    sound_pressure_yaxis(title_prefix='Early Reflections'))
```

## Sound Power response

```python
standalone_speaker_frequency_response_db_chart(
    ('CEA2034', 'Sound Power'),
    sound_pressure_yaxis(title_prefix='Sound Power'))
```

## Early Reflections Directivity Index

```python
standalone_speaker_frequency_response_db_chart(
    ('Directivity Index', 'Early Reflections DI'),
    directivity_index_yaxis(title_prefix='Early Reflections'))
```

## Sound Power Directivity Index

```python
standalone_speaker_frequency_response_db_chart(
    ('Directivity Index', 'Sound Power DI'),
    directivity_index_yaxis(title_prefix='Sound Power'))
```

## Estimated In-Room Response

```python
standalone_speaker_frequency_response_db_chart(
    ('Estimated In-Room Response', 'Estimated In-Room Response'),
    sound_pressure_yaxis(title_prefix='Estimated In-Room Response'))
```

# Other measurements



## Listening Window detail

The Listening Window is defined by CTA-2034-A as the average of on-axis, ±10° vertical responses, and ±10º, ±20º and ±30º horizontal responses. Averages can be misleading as they can hide significant variation between angles.

This chart provides more detail by including each individual angle that is used in the Listening Window average. This can be used to assess the consistency of the response within the Listening Window.

```python
speakers_fr_listening_window = speakers_fr_ready.pipe(lsx.pd.remap_columns, {
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
})

lsx.util.pipe(
    speakers_fr_listening_window,
    lambda data: frequency_response_db_chart(data,
        sidebyside=True,
        additional_tooltips=[alt.Tooltip('key', type='nominal', title='Response')])
        .transform_fold(speakers_fr_listening_window.columns.values)
        .encode(sound_pressure_yaxis())
        .encode(strokeWidth=alt.condition(alt.FieldOneOfPredicate(
            field='key', oneOf=['Listening Window', 'On Axis']),
            if_true=alt.value(2), if_false=alt.value(1.5))),
    lambda chart: lsx.alt.interactive_line(chart,
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
        ]))),
    speaker_facet, speaker_input,
    postprocess_chart)
```

<!-- #region heading_collapsed=true -->
# Olive Preference Score (work in progress)
<!-- #endregion -->

This section describes the calculation of a loudspeaker preference score based on [research by Sean Olive](http://www.aes.org/e-lib/browse.cfm?elib=12847) (also available as a [patent](https://patents.google.com/patent/US20050195982A1)).

This research involves 268 listeners evaluating 70 loudspeakers in rigorous controlled conditions. Statistical methods were used to correlate subjective ratings with the speakers anechoic measurement data. The result is a statistical model in the form of a formula that can be used to fairly accurately predict loudspeaker preference ratings from spinorama data alone. This research is widely considered to be the state of the art when it comes to assessing speakers based on measurements.

**This section is a work in progress. It does not yet include a complete score calculation.**

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

def curve_selection(init):
    return alt.selection_single(
        fields=['curve'], init={'curve': init},
        bind=alt.binding_select(
            name='Curve: ',
            options=list(olive_curve_labels.keys()),
            labels=[f'{curve} {label}' for curve, label in olive_curve_labels.items()]))

def curve_input(chart, init):
    selection = curve_selection(init)
    return chart.transform_filter(selection).add_selection(selection)
```

## Narrow Band Deviation (NBD)

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


The paper is ambiguous as to where the _½-octave bands between 100 Hz and 12 kHz_ actually lie. Specifically, it is not clear if *100 Hz* and *12 kHz* are meant as *boundaries*, or if they refer to the *center frequencies* of the first and last bands. (For more debate on this topic, see [this](https://www.audiosciencereview.com/forum/index.php?threads/speaker-equivalent-sinad-discussion.10818/page-3#post-303034), [this](https://www.audiosciencereview.com/forum/index.php?threads/speaker-equivalent-sinad-discussion.10818/page-4#post-303834), [this](https://www.audiosciencereview.com/forum/index.php?threads/speaker-equivalent-sinad-discussion.10818/page-7#post-306831), [this](https://www.audiosciencereview.com/forum/index.php?threads/speaker-equivalent-sinad-discussion.10818/page-10#post-308515), and [this](https://www.audiosciencereview.com/forum/index.php?threads/yamaha-hs5-powered-monitor-review.10967/page-6#post-309021).) In his [score calculations](https://docs.google.com/spreadsheets/d/e/2PACX-1vRVN63daR6Ph8lxhCDUEHxWq_gwV0wEjL2Q1KRDA0J4i_eE1JS-JQYSZy7kCQZMKtRnjTOn578fYZPJ/pubhtml), [MZKM](https://www.audiosciencereview.com/forum/index.php?members/mzkm.4645/) uses 114 Hz as the center frequency of the first band and deduces the rest from there. For consistency's sake, Loudspeaker Explorer does the same, resulting in the following bands:

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
            .pipe(append_constant_index, name='Frequency [Hz]')
    }, names=['Dataset']))

# We can't use curve_input() because, for some reason, the chart doesn't work if the filtering is done at the top level.
nbd_fr_curve_selection = curve_selection('ON')

nbd_fr_chart_base = lsx.util.pipe(
    nbd_fr_chart_data,
    lambda data: frequency_response_db_chart(data, sidebyside=True)
    .transform_fold(nbd_fr_chart_data.columns.values, ['curve', 'value'])
    .transform_filter(nbd_fr_curve_selection))

nbd_fr_chart_color = alt.Color(
    'layer',
    type='nominal', title=None,
    legend=alt.Legend(symbolType='stroke'),
    scale=alt.Scale(range=[
        '#2ca02c',  # category10[2]: Band Mean
        '#ff7f0e',  # category10[1]: Deviation
        '#1f77b4',  # category10[0]: Curve
    ]))

lsx.util.pipe(
    alt.layer(
        lsx.util.pipe(nbd_fr_chart_base
                .transform_filter(alt.FieldEqualPredicate(field='Dataset', equal='Curve'))
                .transform_calculate(layer='datum.curve + " Curve"')
                .encode(sound_pressure_yaxis(), strokeWidth=alt.value(0.5)),
            lambda chart: lsx.alt.interactive_line(chart, nbd_fr_chart_color)),
        lsx.util.pipe(nbd_fr_chart_base
                .transform_filter(alt.FieldEqualPredicate(field='Dataset', equal='Band Mean'))
                .transform_calculate(layer='"NBD_" + datum.curve + " Band Mean"')
                .transform_calculate(frequency='datum.band_info.start_frequency')
                .encode(
                    sound_pressure_yaxis(), alt.X2('band_info.end_frequency'),
                    tooltip=[
                        alt.Tooltip('Band'),
                        frequency_tooltip('band_info.start_frequency', 'Start Frequency'),
                        frequency_tooltip('band_info.center_frequency', 'Center Frequency'),
                        frequency_tooltip('band_info.end_frequency', 'End Frequency'),
                        value_db_tooltip(title='Mean'),
                    ]
                ),
            lambda chart: lsx.alt.interactive_line(
                chart, nbd_fr_chart_color, add_mark=lambda chart: chart.mark_rule())
                .interactive()),
        lsx.util.pipe(nbd_fr_chart_base
                .transform_filter(alt.FieldEqualPredicate(field='Dataset', equal='Curve'))
                .transform_calculate(band_mean=
                    'isValid(datum.speaker_band_mean.band_mean[datum.Band]) ? datum.speaker_band_mean.band_mean[datum.Band][datum.curve] : NaN')
                .transform_filter(alt.FieldValidPredicate(field='band_mean', valid=True))
                .transform_calculate(layer='"NBD_" + datum.curve + " Deviation"')
                .transform_calculate(deviation='abs(datum.band_mean - datum.value)')
                .encode(
                    sound_pressure_yaxis(), alt.Y2('band_mean'),
                    strokeWidth=alt.value(2),
                    tooltip=[
                        frequency_tooltip(),
                        value_db_tooltip(),
                        alt.Tooltip('Band'),
                        value_db_tooltip('deviation', title='Deviation'),
                    ]),
            lambda chart: lsx.alt.interactive_line(
                chart, nbd_fr_chart_color, add_mark=lambda chart: chart.mark_rule())))
    # Lookups are done here. If they are done in nbd_fr_chart_base, Altair seems to generate an invalid spec.
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
    .add_selection(nbd_fr_curve_selection),
    speaker_facet, speaker_input,
    postprocess_chart)
```

```python
# We can't use curve_input() because, for some reason, the chart doesn't work if the filtering is done after facet().
nbd_curve_selection = curve_selection('ON')
nbd_chart_base = lsx.alt.make_chart(speakers_nbd_band)
lsx.util.pipe(
    alt.layer(
        nbd_chart_base
            .mark_bar()
            .transform_calculate(band_label=
                'datum.Band + " (" + format(datum.band_info.start_frequency, ".02s") + " - " + format(datum.band_info.end_frequency, ".02s") + " Hz)"')
            .encode(
                alt.X('value', type='quantitative', title=['Narrow Band Deviation (NBD)', 'lower is better']),
                alt.Color('band_label', type='nominal', sort=None, title='Band'),
                alt.Order('Band'),
                tooltip=[
                        alt.Tooltip('Speaker', title='Speaker'),
                        alt.Tooltip('Band'),
                        frequency_tooltip('band_info.start_frequency', 'Start Frequency'),
                        frequency_tooltip('band_info.center_frequency', 'Center Frequency'),
                        frequency_tooltip('band_info.end_frequency', 'End Frequency'),
                        alt.Tooltip('value', type='quantitative', title='Band NBD', format='.3f'),
                    ]),
        nbd_chart_base
            .mark_text(align='left', dx=3)
            .encode(
                alt.X('value', type='quantitative', aggregate='sum'),
                alt.Text('value', type='quantitative', aggregate='sum', format='.2f')))
    .transform_fold(speakers_nbd_band.columns.values, ['curve', 'value'])
    .transform_filter(nbd_curve_selection)
    .transform_lookup(lookup='curve', as_='curve_info', from_=alt.LookupData(
        key='curve', data=pd.Series(olive_curve_labels)
            .rename_axis('curve')
            .rename('label')
            .reset_index()))
    .transform_calculate(curve_label='datum.curve + " " + datum.curve_info.label')
    .transform_lookup(lookup='Band', as_='band_info', from_=alt.LookupData(
        key='Band', data=nbd_bands
            .pipe(lsx.pd.remap_columns, {
                'Start Frequency (Hz)': 'start_frequency',
                'Center Frequency (Hz)': 'center_frequency',
                'End Frequency (Hz)': 'end_frequency',
            })
            .reset_index()))
    .encode(alt.Y('Speaker', title=None))
    .facet(
        alt.Column('curve_label', type='nominal', title=None),
        title=common_title)
    .add_selection(nbd_curve_selection),
    postprocess_chart)
```
