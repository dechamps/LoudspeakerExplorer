---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.3.4
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

<!-- #region id="view-in-github" colab_type="text" -->
<a href="https://colab.research.google.com/github/dechamps/LoudspeakerExplorer/blob/master/Loudspeaker_Explorer.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
<!-- #endregion -->

<!-- #region id="04RRpMNFkSxn" colab_type="text" -->
# The Loudspeaker Explorer

*By Etienne Dechamps (etienne@edechamps.fr)* - [ASR thread](https://www.audiosciencereview.com/forum/index.php?threads/loudspeaker-explorer-analyze-visualize-compare-speaker-data.11503/) - [GitHub](https://github.com/dechamps/LoudspeakerExplorer)

Welcome to the Loudspeaker Explorer, a speaker measurement visualization, analysis and comparison tool. This is an interactive [Colaboratory Notebook](https://colab.research.google.com/).

## How to use this notebook

To run the code and (re)generate the data, go to the **Runtime** menu and click **Run all** (CTRL+F9). **You will need to repeat this every time you change any of the settings or code** (e.g. if you enable or disable speakers).

**All the charts are interactive.** Use the mousewheel to zoom, and drag & drop to pan. Re-run the code block immediately above the graph ("play" icon) to reset the view.

**Charts can take a few seconds to load when scrolling**, especially if you're using the notebook for the first time. Be patient.

**Charts will not be generated if the section they're under is folded while the code runs.** To manually load a chart, click the Run (Play) icon next to the code block above it. Or use *Run all* again after unfolding the section.

## Acknowledgments

None of this would have been possible without [amirm](https://www.audiosciencereview.com/forum/index.php?members/amirm.2/)'s [tremendous work](https://www.audiosciencereview.com/forum/index.php?threads/announcement-asr-will-be-measuring-speakers.10725/) in measuring speakers. All the data used by this tool is from measurements made by amirm for [AudioScienceReview](https://www.audiosciencereview.com/). If you like what you see, [consider making a donation](https://www.audiosciencereview.com/forum/index.php?threads/how-to-support-audio-science-review.8150/).

## License

Loudspeaker Explorer is published under [MIT License](https://github.com/dechamps/LoudspeakerExplorer/blob/master/LICENSE.txt). Note that input data, including measurement data and pictures, is not part of Loudspeaker Explorer - it is published by third parties under potentially different licenses.
<!-- #endregion -->

<!-- #region id="ZOhKCU3Go26x" colab_type="text" -->
# Preliminary boilerplate
<!-- #endregion -->

```python id="NhdyLTvTovip" colab_type="code" colab={}
# https://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter/
import sys
!{sys.executable} -m pip install numpy pandas engarde yattag altair

from pathlib import Path
import numpy as np
import pandas as pd
import engarde.decorators as ed
import ipywidgets as widgets
from IPython.display import display
import yattag
import altair as alt
```

<!-- #region id="_xFyFEAhA_EB" colab_type="text" -->
# Speaker selection

Note that the following speakers, despite having been measured by amirm, are not (yet) available in this tool:

 - [**Kali IN-8 (damaged sample)**](https://www.audiosciencereview.com/forum/index.php?threads/kali-audio-in-8-studio-monitor-review.10897/): the raw data was not published. The data shown here is for the [good sample](https://www.audiosciencereview.com/forum/index.php?threads/kali-audio-in-8-studio-monitor-review.10897/page-29#post-318617).
 - [**Neumann KH80 (sample 2, low order)**](https://www.audiosciencereview.com/forum/index.php?threads/neumann-kh-80-dsp-speaker-measurements-take-two.11323/): the raw data was not published. The data shown here is from the [high order measurement](https://www.audiosciencereview.com/forum/index.php?threads/neumann-kh-80-dsp-speaker-measurements-take-two.11323/page-12#post-324456).
 - [**NHT Pro M-00**](https://www.audiosciencereview.com/forum/index.php?threads/nht-pro-m-00-powered-monitor-review.10859/): the raw data was not published.
 - [**Revel C52**](https://www.audiosciencereview.com/forum/index.php?threads/revel-c52-speaker-review-and-measurements.10934/): the raw data published is incomplete and does not come in the standard zipfile format that the tool expects.
 - [**Yamaha HS5**](https://www.audiosciencereview.com/forum/index.php?threads/yamaha-hs5-powered-monitor-review.10967/): the raw data published is incomplete and does not come in the standard zipfile format that the tool expects.

Also note that the datasets for **JBL 305P MkII** and **Neumann KH80 (sample 1)** are missing *Directivity Index* data. Due to a bug in the tool this also breaks the Spinorama charts unless another speaker is also selected.

**How to add a new speaker**: add a new variable in the "Enable/Disable speakers" code block, and repeat the pattern in the "Raw speaker specification" code block. That's it - everything else should take care of itself. Note that the tool expects a zipfile in the format that amirm publishes (which presumably is the Klippel analysis software export format). If you want to upload the zipfile manually instead of using `Data URL`, you can do that using the Colab file browser on the left - just make sure the name of the file matches the `Speaker` field in the raw specification so that the tool can find it.
<!-- #endregion -->

<!-- #region id="vbT7q38fvcLa" colab_type="text" -->
## Enable/Disable speakers

This is the most important setting. Here you can select the speakers you wish to analyze and compare. See the *Speaker list* section below for more information on each speaker. **Don't forget to use "Run all" after changing your selection.**
<!-- #endregion -->

```python id="laytqyKSBBUI" colab_type="code" colab={}
speaker_enable_AdamAudio_S2V = False #@param {type:"boolean"}
speaker_enable_DaytonAudio_B652AIR = True #@param {type:"boolean"}
speaker_enable_Elac_AdanteAS61 = True #@param {type:"boolean"}
speaker_enable_Emotiva_Airmotiv6s = False #@param {type:"boolean"}
speaker_enable_Harbeth_Monitor30_LowOrder = False #@param {type:"boolean"}
speaker_enable_Harbeth_Monitor30_HighOrder = False #@param {type:"boolean"}
speaker_enable_JBL_305PMkII = False #@param {type:"boolean"}
speaker_enable_JBL_Control1Pro = False #@param {type:"boolean"}
speaker_enable_JBL_OneSeries104 = False #@param {type:"boolean"}
speaker_enable_Kali_IN8 = False #@param {type:"boolean"}
speaker_enable_KEF_LS50 = False #@param {type:"boolean"}
speaker_enable_Klipsch_R41M = True #@param {type:"boolean"}
speaker_enable_Micca_RB42 = False #@param {type:"boolean"}
speaker_enable_Neumann_KH80_Sample1 = False #@param {type:"boolean"}
speaker_enable_Neumann_KH80_Sample2 = False #@param {type:"boolean"}
speaker_enable_Pioneer_SPBS22LR = False #@param {type:"boolean"}
speaker_enable_Realistic_MC1000 = False #@param {type:"boolean"}
speaker_enable_SelahAudio_RC3R = False #@param {type:"boolean"}
```

<!-- #region id="Xz_e10hWvhQs" colab_type="text" -->
## Raw speaker specification
<!-- #endregion -->

```python id="KxMbO72a7Dgh" colab_type="code" cellView="code" colab={}
speakers = pd.DataFrame([{
    'Speaker': 'Adam Audio S2V',
    'Enabled': speaker_enable_AdamAudio_S2V,
    'Data URL': 'https://www.audiosciencereview.com/forum/index.php?attachments/adam-s2v-spinorama-cea2034-zip.50119/',
    'Review URL': 'https://www.audiosciencereview.com/forum/index.php?threads/adam-s2v-studio-monitor-review.11455/',
    'Product URL': 'https://www.adam-audio.com/en/s-series/s2v/',
    'Picture URL': 'https://www.audiosciencereview.com/forum/index.php?attachments/adam-s2v-monitor-powered-studio-speaker-audio-review-jpg.50100/',
    'Active': True,
    'Price (Single, USD)': 875.00,
  }, {
    'Speaker': 'Dayton Audio B652-AIR',
    'Enabled': speaker_enable_DaytonAudio_B652AIR,
    'Data URL': 'https://www.audiosciencereview.com/forum/index.php?attachments/dayton-audio-b652-air-spinorama-zip.49763/',
    'Review URL': 'https://www.audiosciencereview.com/forum/index.php?threads/dayton-audio-b652-air-speaker-review.11410/',
    'Product URL': 'https://www.daytonaudio.com/product/1243/b652-air-6-1-2-2-way-bookshelf-speaker-with-amt-tweeter-pair',
    'Picture URL': 'https://www.audiosciencereview.com/forum/index.php?attachments/dayton-audio-b652-air-bookshelf-cheap-speakers-audio-review-jpg.49739/',
    'Active': False,
    'Price (Single, USD)': 39.00,
  }, {
    'Speaker': 'Elac Adante AS-61',
    'Enabled': speaker_enable_Elac_AdanteAS61,
    'Data URL': 'https://www.audiosciencereview.com/forum/index.php?attachments/elac-adante-as-61-cea-2034-spin-data-zip.50439/',
    'Review URL': 'https://www.audiosciencereview.com/forum/index.php?threads/elac-adante-as-61-speaker-review.11507/',
    'Picture URL': 'https://www.audiosciencereview.com/forum/index.php?attachments/elac-adante-as-61-bookshelf-speaker-audio-review-jpg.50415/',
    'Active': False,
    'Price (Single, USD)': 1250.00,
  }, {
    'Speaker': 'Emotiva Airmotiv 6s',
    'Enabled': speaker_enable_Emotiva_Airmotiv6s,
    'Data URL': 'https://www.audiosciencereview.com/forum/index.php?attachments/emotiva-airmotive-6s-spinorama-zip.48091/',
    'Review URL': 'https://www.audiosciencereview.com/forum/index.php?threads/emotiva-airmotiv-6s-powered-speaker-review.11185/',
    'Picture URL': 'https://www.audiosciencereview.com/forum/index.php?attachments/emotiva-airmotive-6s-powered-monitor-speaker-review-jpg.48017/',
    'Active': True,
    'Price (Single, USD)': 250.00,
  }, {
    'Speaker': 'Harbeth Monitor 30 (low order)',
    'Enabled': speaker_enable_Harbeth_Monitor30_LowOrder,
    'Data URL': 'https://www.audiosciencereview.com/forum/index.php?attachments/harbeth-monitor-ces2034-spinorama-zip.47527/',
    'Review URL': 'https://www.audiosciencereview.com/forum/index.php?threads/harbeth-monitor-30-speaker-review.11108/',
    'Picture URL': 'https://www.audiosciencereview.com/forum/index.php?attachments/harbeth-monitor-30-speaker-review-jpg.47512/',
    'Active': False,
    'Price (Single, USD)': 1600.00,
  }, {
    'Speaker': 'Harbeth Monitor 30 (high order)',
    'Enabled': speaker_enable_Harbeth_Monitor30_HighOrder,
    'Data URL': 'https://www.audiosciencereview.com/forum/index.php?attachments/harbeth-30-high-order-spin-data-zip.49385/',
    'Review URL': 'https://www.audiosciencereview.com/forum/index.php?threads/neumann-kh-80-dsp-speaker-measurements-take-two.11323/page-10#post-324345',
    'Picture URL': 'https://www.audiosciencereview.com/forum/index.php?attachments/harbeth-monitor-30-speaker-review-jpg.47512/',
    'Active': False,
    'Price (Single, USD)': 1600.00,
  }, {
    'Speaker': 'JBL 305P MkII',
    'Enabled': speaker_enable_JBL_305PMkII,
    # https://www.audiosciencereview.com/forum/index.php?threads/neumann-kh-80-dsp-monitor-review.11018/page-2#post-310325
    'Data URL': 'https://www.audiosciencereview.com/forum/index.php?attachments/jbl-305p-mark-ii-cea2034-zip.46835/',
    'Review URL': 'https://www.audiosciencereview.com/forum/index.php?threads/jbl-305p-mkii-and-control-1-pro-monitors-review.10811/',
    'Product URL': 'https://www.jbl.com/studio-monitors/305PMKII.html',
    'Picture URL': 'https://www.audiosciencereview.com/forum/index.php?attachments/jbl-305p-mkii-speaker-powered-monitor-review-jpg.45226/',
    'Active': True,
    'Price (Single, USD)': 150.00,
  }, {
    'Speaker': 'JBL Control 1 Pro',
    'Enabled': speaker_enable_JBL_Control1Pro,
    # https://www.audiosciencereview.com/forum/index.php?threads/jbl-305p-mkii-and-control-1-pro-monitors-review.10811/page-24#post-315827
    'Data URL': 'https://www.audiosciencereview.com/forum/index.php?attachments/jbl-control-1-pro-zip.47821/',
    'Review URL': 'https://www.audiosciencereview.com/forum/index.php?threads/jbl-305p-mkii-and-control-1-pro-monitors-review.10811/',
    'Product URL': 'https://jblpro.com/en/products/control-1-pro',
    'Picture URL': 'https://www.audiosciencereview.com/forum/index.php?attachments/jbl-control-1-pro-monitor-review-jpg.45228/',
    'Active': True,
    'Price (Single, USD)': 82.00,
  }, {
    'Speaker': 'JBL One Series 104',
    'Enabled': speaker_enable_JBL_OneSeries104,
    'Data URL': 'https://www.audiosciencereview.com/forum/index.php?attachments/jbl-104-spinorama-zip.47297/',
    'Review URL': 'https://www.audiosciencereview.com/forum/index.php?threads/jbl-one-series-104-powered-monitor-review.11076/',
    'Product URL': 'https://jblpro.com/en-US/products/104',
    'Picture URL': 'https://www.audiosciencereview.com/forum/index.php?attachments/jbl-one-series-104-powered-monitor-speaker-review-jpg.47273/',
    'Active': True,
    'Price (Single, USD)': 65.00,
  }, {
    'Speaker': 'Kali Audio IN-8',
    'Enabled': speaker_enable_Kali_IN8,
    'Data URL': 'https://www.audiosciencereview.com/forum/index.php?attachments/kali-in-8-spinorama-zip.48347/',
    'Review URL': 'https://www.audiosciencereview.com/forum/index.php?threads/kali-audio-in-8-studio-monitor-review.10897/page-29#post-318617',
    'Product URL': 'https://www.kaliaudio.com/independence',
    'Picture URL': 'https://www.audiosciencereview.com/forum/index.php?attachments/kali-audio-in-8-studio-monitor-powered-speaker-review-jpg.45827/',
    'Active': True,
    'Price (Single, USD)': 400.00,
  }, {
    'Speaker': 'KEF LS50',
    'Enabled': speaker_enable_KEF_LS50,
    'Data URL': 'https://www.audiosciencereview.com/forum/index.php?attachments/kef-ls50-ces2034-zip.47785/',
    'Review URL': 'https://www.audiosciencereview.com/forum/index.php?threads/kef-ls50-bookshelf-speaker-review.11144/',
    'Product URL': 'https://us.kef.com/catalog/product/view/id/1143/s/ls50-mini-monitor-speaker-pair/category/94/',
    'Picture URL': 'https://www.audiosciencereview.com/forum/index.php?attachments/kef-ls50-bookshelf-speaker-review-jpg.47768/',
    'Active': False,
    'Price (Single, USD)': 750.00,
  }, {
    'Speaker': 'Klipsch R-41M',
    'Enabled': speaker_enable_Klipsch_R41M,
    'Data URL': 'https://www.audiosciencereview.com/forum/index.php?attachments/klipsch-r41m-spin-data-zip.50860/',
    'Review URL': 'https://www.audiosciencereview.com/forum/index.php?threads/klipsch-r-41m-bookshelf-speaker-review.11566/',
    'Product URL': 'https://www.klipsch.com/products/r-41m-bookshelf-speaker-blk-gnm',
    'Picture URL': 'https://www.audiosciencereview.com/forum/index.php?attachments/klipsch-r-41m-booksehlf-speaker-audio-review-jpg.50841/',
    'Active': False,
    'Price (Single, USD)': 75.00,
  }, {
    'Speaker': 'Micca RB42',
    'Enabled': speaker_enable_Micca_RB42,
    'Data URL': 'https://www.audiosciencereview.com/forum/index.php?attachments/micca-rb42-cea2034-spinorama-zip.48638/',
    'Review URL': 'https://www.audiosciencereview.com/forum/index.php?threads/micca-rb42-bookshelf-speaker-review.11267/',
    'Product URL': 'https://www.miccatron.com/micca-rb42-reference-bookshelf-speakers/',
    'Picture URL': 'https://www.audiosciencereview.com/forum/index.php?attachments/micca-rb42-bookshelf-budget-speaker-review-jpg.48623/',
    'Active': False,
    'Price (Single, USD)': 75.00,
  }, {
    'Speaker': 'Neumann KH 80 DSP (sample 1)',
    'Enabled': speaker_enable_Neumann_KH80_Sample1,
    'Data URL': 'https://www.audiosciencereview.com/forum/index.php?attachments/neumann-kh-80-cea2034-zip.46824/',
    'Review URL': 'https://www.audiosciencereview.com/forum/index.php?threads/neumann-kh-80-dsp-monitor-review.11018/',
    'Product URL': 'https://www.neumann.com/homestudio/en/kh-80',
    'Picture URL': 'https://www.audiosciencereview.com/forum/index.php?attachments/neumann-kh-80-dsp-monitor-active-studio-pro-speaker-audio-review-jpg.46803/',
    'Active': True,
    'Price (Single, USD)': 500.00,
  }, {
    'Speaker': 'Neumann KH 80 DSP (sample 2)',
    'Enabled': speaker_enable_Neumann_KH80_Sample2,
    # https://www.audiosciencereview.com/forum/index.php?threads/neumann-kh-80-dsp-speaker-measurements-take-two.11323/page-12#post-324456
    'Data URL': 'https://www.audiosciencereview.com/forum/index.php?attachments/neumann-kh80-dsp-1000-point-order-20-spin-datra-zip.49443/',
    'Review URL': 'https://www.audiosciencereview.com/forum/index.php?threads/neumann-kh-80-dsp-speaker-measurements-take-two.11323/',
    'Product URL': 'https://www.neumann.com/homestudio/en/kh-80',
    'Picture URL': 'https://www.audiosciencereview.com/forum/index.php?attachments/neumann-kh-80-dsp-monitor-active-studio-pro-speaker-audio-review-jpg.46803/',
    'Active': True,
    'Price (Single, USD)': 500.00,
  }, {
    'Speaker': 'Pioneer SP-BS22-LR',
    'Enabled': speaker_enable_Pioneer_SPBS22LR,
    'Data URL': 'https://www.audiosciencereview.com/forum/index.php?attachments/pioneer-sp-bs22-lr-spinorama-2-zip.49024/',
    'Review URL': 'https://www.audiosciencereview.com/forum/index.php?threads/pioneer-sp-bs22-lr-bookshelf-speaker-review.11303/',
    'Product URL': 'https://intl.pioneer-audiovisual.com/products/speakers/sp-bs22-lr/',
    'Picture URL': 'https://www.audiosciencereview.com/forum/index.php?attachments/pioneer-sp-bs22-lr-budget-bookshelf-speaker-review-jpg.48945/',
    'Active': False,
    'Price (Single, USD)': 80.00,
  }, {
    'Speaker': 'Realistic MC-1000',
    'Enabled': speaker_enable_Realistic_MC1000,
    'Data URL': 'https://www.audiosciencereview.com/forum/index.php?attachments/realistic-mc-1000-spinorama-zip.48797/',
    'Review URL': 'https://www.audiosciencereview.com/forum/index.php?threads/mc-1000-best-speaker-in-the-world.11283/',
    'Picture URL': 'https://www.audiosciencereview.com/forum/index.php?attachments/realistic-mc-1000-radio-shack-2-way-vintage-speaker-listing-jpg.48786/',
    'Active': False,
    'Price (Single, USD)': 120.00,  # $30 in 1978, adjusted for inflation
  }, {
    'Speaker': 'Selah Audio RC3R',
    'Enabled': speaker_enable_SelahAudio_RC3R,
    'Data URL': 'https://www.audiosciencereview.com/forum/index.php?attachments/selah-audio-rc3r-spinorama-zip.48264/',
    'Review URL': 'https://www.audiosciencereview.com/forum/index.php?threads/selah-audio-rc3r-3-way-speaker-review.11218/',
    'Product URL': 'http://www.selahaudio.com/monitors',
    'Picture URL': 'https://www.audiosciencereview.com/forum/index.php?attachments/selah-audio-rc3r-3-way-speaker-review-jpg.48249/',
    'Active': False,
    'Price (Single, USD)': 650.00,
  },
]).set_index('Speaker')
```

```python id="_TAZfS40gN1l" colab_type="code" colab={}
def speaker_list_html():
  doc, tag, text, line = yattag.Doc().ttl()
  for speaker_name in speakers.index:
    speaker = speakers.loc[speaker_name, :]
    with tag('h2', style='clear: left; padding-top: 20px'):
      text(speaker_name + (' (ENABLED)' if speaker['Enabled'] else ''))
    doc.stag('img', src=speaker['Picture URL'], width=200, style='float: left; margin-right: 20px')
    product_url = speaker['Product URL']
    if not pd.isna(product_url):
      line('a', 'Product page', href=speaker['Product URL'])
      text(' - ')
    line('a', 'Review', href=speaker['Review URL'])
    text(' - ')
    line('a', 'Data package', href=speaker['Data URL'])
    doc.stag('br')
    with tag('b'): text('Active' if speaker['Active'] else 'Passive')
    doc.stag('br')
    with tag('b'): text('Price: ')
    text('${:.0f} (single)'.format(speaker['Price (Single, USD)']))
  return doc.getvalue()
```

<!-- #region id="hwvM09h0voNa" colab_type="text" -->
## Speaker list
<!-- #endregion -->

```python id="Z8DFJB6wflUQ" colab_type="code" colab={}
speakers.loc[:, ['Enabled', 'Active', 'Price (Single, USD)']]
```

```python id="Ohnl5ExgvtGs" colab_type="code" colab={}
widgets.HTML(speaker_list_html())
```

<!-- #region id="LrJkGq6Qi6F3" colab_type="text" -->
# Data intake
<!-- #endregion -->

<!-- #region id="OvN7MtmnofOx" colab_type="text" -->
## Download and unpack

This downloads and unpacks speaker measurement data for each *enabled* speaker using the URL specified in `data_url`. This step is skipped if the files already exist in the `speaker_data` folder.
<!-- #endregion -->

```python id="byzTXpiEgEZm" colab_type="code" cellView="both" colab={}
Path('speaker_data').mkdir(exist_ok=True)
for speaker_name, speaker_data_url in speakers.loc[speakers['Enabled'], 'Data URL'].items():
  if not (Path('speaker_data') / speaker_name).exists():
    if not (Path('speaker_data') / (speaker_name + '.zip')).exists():
      !wget -O "speaker_data/{speaker_name}.zip" "{speaker_data_url}"
    !unzip "speaker_data/{speaker_name}.zip" -d "speaker_data/{speaker_name}"
```

<!-- #region id="feKcX-dQo8i3" colab_type="text" -->
## Load

This loads all data from all speakers into a single, massive `speaker_fr_raw`
DataFrame. The DataFrame index is arranged by speaker name, then frequency. All
data files for each speaker are merged to form the columns of the DataFrame.
<!-- #endregion -->

```python id="swQuvz41m84M" colab_type="code" colab={}
# pd.read_table() expects the following multi-level column headers:
#   A, A, A, A, B, B, B, B
#   I, I, J, J, K, K, L, L
#   X, Y, X, Y, X, Y, X, Y
# But the data we have uses the following header format instead:
#   A, B
#   I, J, K, L
#   X, Y, X, Y, X, Y, X, Y
# When confronted with this header, pd.read_table() gets confused and generates
# the following multi-level column index:
#   A, _, _, _, B, _, _, _
#   I, _, J, _, K, _, L, _
#   X, Y, X, Y, X, Y, X, Y
# Where "_" is some autogenerated column name in the form: "Unnamed: 1_level_0"
# This function restores the correct column names by replacing every "Unnamed"
# column with the name of the last known column on that level.
def fix_unnamed_columns(columns):
  last_names = [None] * columns.nlevels
  def fix_column(column):
    for level, label in enumerate(column):
      if not label.startswith('Unnamed: '):
        last_names[level] = label
    return tuple(last_names)
  return pd.MultiIndex.from_tuples(fix_column(column) for column in columns.values)

# Expects input in the following form:
#   (Additional top column levels)
#   FR1                     FR2
#   "Frequency [Hz]" value  "Frequency [Hz]" value
#   42.42            1.234  42.42            2.345
#   43.43            3.456  43.43            5.678
# And reindexes it by the "Frequency [Hz]" column, producing:
#          value
#          (Additional top column labels)
#          FR1    FR2
#   42.42  1.234  2.345
#   43.43  3.456  5.678
def index_by_frequency(data):
  preserve_column_level = list(range(data.columns.nlevels - 1))
  return (data
    # Move all columns levels except the bottommost one into the index
    .stack(level=preserve_column_level)
    # Drop the topmost (default) index level as it's not useful anymore
    .reset_index(level=0, drop=True)
    # Use the frequency as the new bottommost index level
    .set_index('Frequency [Hz]', append=True)
    # Move all other index levels back to columns
    .unstack(level=preserve_column_level))

def load_fr(file):
  fr = pd.read_table(file, header=[0,1,2], thousands=',')
  fr.columns = fix_unnamed_columns(fr.columns)
  return fr.pipe(index_by_frequency)

# If the none_missing() assertion fires, it likely means something is wrong or
# corrupted in the data files of the speaker (e.g. some frequencies present in
# some columns/files but not others)
@ed.none_missing()
def load_speaker(dir):
  return pd.concat((load_fr(file) for file in dir.iterdir()), axis='columns')

speakers_fr_raw = pd.concat(
  {speaker.Index: load_speaker(Path('speaker_data') / speaker.Index) for speaker in speakers[speakers['Enabled']].itertuples()},
  names=['Speaker'], axis='rows')
speakers_fr_raw
```

<!-- #region id="0sxZSHE8e8qV" colab_type="text" -->
# Raw data summary

Basic information about loaded data, including frequency bounds and resolution.
<!-- #endregion -->

```python id="Aj572tr9e-g1" colab_type="code" colab={}
speakers_frequencies = (speakers_fr_raw
  .index
  .to_frame()
  .reset_index(drop=True)
  .groupby('Speaker'))
speakers_frequency_count = speakers_frequencies.count()
speakers_min_frequency = speakers_frequencies.min()
speakers_max_frequency = speakers_frequencies.max()
speakers_octaves = (speakers_max_frequency / speakers_min_frequency).apply(np.log2)
speakers_points_per_octave = speakers_frequency_count / speakers_octaves
pd.concat([
  speakers_frequency_count.rename(columns={'Frequency [Hz]': 'Frequencies'}),
  speakers_min_frequency.rename(columns={'Frequency [Hz]': 'Min Frequency (Hz)'}),
  speakers_max_frequency.rename(columns={'Frequency [Hz]': 'Max Frequency (Hz)'}),
  speakers_octaves.rename(columns={'Frequency [Hz]': 'Extent (octaves)'}),
  speakers_points_per_octave.rename(columns={'Frequency [Hz]': 'Resolution (freqs/octave)'})
], axis='columns')
```

<!-- #region id="E-_wPWN6w7FG" colab_type="text" -->
# Sensitivity

This calculates a single sensitivity value for each speaker using the **mean on-axis SPL** in a configurable frequency band. The result can then be used as the basis for normalization (see next section).


<!-- #endregion -->

<!-- #region id="wdCEUnXk7BFR" colab_type="text" -->
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
<!-- #endregion -->

```python id="QhGjOxtVw955" colab_type="code" cellView="both" colab={}
sensitivity_first_frequency_hz = 200 #@param
sensitivity_last_frequency_hz = 400 #@param
```

```python id="zKWRxJ8WxgQN" colab_type="code" colab={}
sensitivity_input_column = ('Sound Pessure Level [dB]  / [2.83V 1m] ', 'CEA2034', 'On Axis')
speakers_sensitivity = (speakers_fr_raw
  .loc[speakers_fr_raw.index.to_frame()['Frequency [Hz]'].between(sensitivity_first_frequency_hz, sensitivity_last_frequency_hz), sensitivity_input_column]
  .mean(level='Speaker'))
speakers_sensitivity.to_frame()
```

<!-- #region id="HvqJh6mEhWWr" colab_type="text" -->
# Normalization

This step normalizes *all* SPL frequency response data (on-axis, spinorama, off-axis, estimated in-room response, etc.) according to the `normalization_mode` variable, which can take the following values:

 - **None**: raw absolute SPL values are carried over as-is.
 - **Equal sensitivity** (recommended): sensitivity values calculated in the previous section are subtracted from all SPL values of each speaker, such that all speakers have 0 dB sensitivity. Improves readability and makes it easier to compare speakers.
 - **Flat on-axis**: the on-axis SPL value is subtracted to itself as well as every other SPL variable at each frequency. In other words this simulates EQ'ing every speaker to be perfectly flat on-axis. Use this mode to focus solely on directivity data.

The normalized data is stored in the `speakers_fr_splnorm` variable, which is used as the input of most graphs and calculations that follow. Note that this variable only contains the columns that actually underwent normalization, i.e. absolute SPL columns - in particular it doesn't include the directivity indices.
<!-- #endregion -->

```python id="7qCapMbNhZk6" colab_type="code" cellView="both" colab={}
normalization_mode = 'Equal sensitivity' #@param ["None", "Equal sensitivity", "Flat on-axis"]
```

```python id="Qf6dvIYEURdz" colab_type="code" colab={}
speakers_fr_splnorm = speakers_fr_raw.loc[:, 'Sound Pessure Level [dB]  / [2.83V 1m] ']
if normalization_mode == 'Equal sensitivity':
  speakers_fr_splnorm = speakers_fr_splnorm.sub(
      speakers_sensitivity, axis='index', level='Speaker')
if normalization_mode == 'Flat on-axis':
  speakers_fr_splnorm = speakers_fr_splnorm.sub(
      speakers_fr_raw.loc[:, ('Sound Pessure Level [dB]  / [2.83V 1m] ', 'CEA2034', 'On Axis')], axis='index')
speakers_fr_splnorm
```

<!-- #region id="C12-wV0U7M-y" colab_type="text" -->
# Plot settings

Here you can customize some parameters related to the charts.
<!-- #endregion -->

```python id="FlfHUnsr7TCi" colab_type="code" cellView="form" colab={}
#@markdown Dimensions for standalone charts
standalone_chart_width =  800#@param {type:"integer"}
standalone_chart_height =  400#@param {type:"integer"}
#@markdown Dimensions for side-by-side charts
sidebyside_chart_width = 600 #@param {type:"integer"}
sidebyside_chart_height = 300 #@param {type:"integer"}
```

```python id="ENSOjscP7Tui" colab_type="code" cellView="both" colab={}
alt.data_transformers.disable_max_rows()

# Prepares DataFrame `df` for charting using alt.Chart().
#
# Altair doesn't use the index, so we move it into columns. Then columns are
# renamed according to the `columns_mapper` dict. (This is necessary because
# Altair doesn't work well with verbose column names, and it doesn't support 
# multi-level columns anyway.) Columns that don't appear in the dict are
# dropped.
#
# Note: contrary to DataFrame.rename(), in the case of MultiIndex columns,
# `columns_mapper` keys are matched against the full column name (i.e. a tuple),
# not individual per-level labels. 
def prepare_alt_chart(df, columns_mapper):
  df = df.reset_index().loc[:, list(columns_mapper.keys())]
  df.columns = df.columns.map(mapper=columns_mapper)
  return df

def frequency_response_chart(data, sidebyside=False):
  return (alt.Chart(data)
    .properties(
      width=sidebyside_chart_width if sidebyside else standalone_chart_width,
      height=sidebyside_chart_height if sidebyside else standalone_chart_height)
    .mark_line(clip=True, interpolate='monotone')
    .encode(frequency_xaxis('frequency')))

def frequency_xaxis(shorthand):
  return alt.X(shorthand, title='Frequency (Hz)', scale=alt.Scale(type='log', base=10, nice=False), axis=alt.Axis(format='s'))

def sound_pressure_yaxis(shorthand, title='Relative Sound Pressure (dB)', scale_domain=None):
  if scale_domain is None:
    scale_domain = (55, 105) if normalization_mode == 'None' else (-40, 10)
  return alt.Y(shorthand, title=title, scale=alt.Scale(domain=scale_domain), axis=alt.Axis(grid=True))

# Given a DataFrame with some of the columns in the following format:
#   'On-Axis' '10°' '20°' '-10°' ...
# Converts the above column labels to the following:
#   0.0 10.0 20.0 -10.0
def convert_angles(df):
  def convert_label(label):
    if label == 'On-Axis':
      return 0.0
    stripped_label = label.strip('°')
    if stripped_label == label:
      return label
    try:
      return float(stripped_label)
    except ValueError:
      return label
  return df.rename(columns=convert_label)
```

<!-- #region id="k3AcxFuKZbwt" colab_type="text" -->
# Measurements

Note that all the data shown in this section is a direct representation of the input data after normalization. No complex processing is done. In particular, data for derived metrics such as *Listening Window*, *Early Reflections*, *Sound Power*, Directivity Indices and even *Estimated In-Room Response* come directly from the input - they are not derived by this code.
<!-- #endregion -->

<!-- #region id="VcfgDHv2ZjxS" colab_type="text" -->
## Spinorama

The famous CEA/CTA-2034 charts, popularized by Dr. Floyd Toole. These provide a good summary of the measurements from a perceptual perspective. Speakers are presented side-by-side for easy comparison.

Remember:
 - **All the charts are interactive.** Use the mousewheel to zoom, and drag & drop to pan. Re-run the code block to reset the view.
 - **Charts are not computed if the section they're under is folded while the code runs.** To manually load a chart, click the Run (Play) icon next to the code block above it.
<!-- #endregion -->

```python id="hdspzIUlFuWe" colab_type="code" colab={}
spinorama_chart_common = (frequency_response_chart(sidebyside=speakers_fr_splnorm.index.unique('Speaker').size > 1, data=
  pd.concat([speakers_fr_splnorm, speakers_fr_raw.loc[:, '[dB] Directivity Index ']], axis='columns')
    .pipe(prepare_alt_chart, {
      ('Speaker', ''): 'speaker',
      ('Frequency [Hz]', ''): 'frequency',
      ('CEA2034', 'On Axis'): 'On Axis',
      ('CEA2034', 'Listening Window'): 'Listening Window',
      ('CEA2034', 'Early Reflections'): 'Early Reflections',
      ('CEA2034', 'Sound Power'): 'Sound Power',
      ('Directivity Index', 'Early Reflections DI'): 'Early Reflections DI',
      ('Directivity Index', 'Sound Power DI'): 'Sound Power DI',
    }).melt(['speaker', 'frequency']))
  .encode(alt.Color('variable', title=None, sort=None)))

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
(alt.layer(
    spinorama_chart_common
      .encode(sound_pressure_yaxis('value'))
      .transform_filter(alt.FieldOneOfPredicate(field='variable', oneOf=['On Axis', 'Listening Window', 'Early Reflections', 'Sound Power']))
      .interactive(),
    spinorama_chart_common
      .encode(sound_pressure_yaxis('value', title='Directivity Index (dB)', scale_domain=(-10, 40)))
      .transform_filter(alt.FieldOneOfPredicate(field='variable', oneOf=['Early Reflections DI', 'Sound Power DI']))
      .interactive())
    .resolve_scale(y='independent')
    .facet(alt.Column('speaker', title=None))
    .resolve_scale(y='independent'))
```

<!-- #region id="R_AuSbae0CE2" colab_type="text" -->
## On-axis response
<!-- #endregion -->

```python id="BIxJJclZ0Krk" colab_type="code" colab={}
(frequency_response_chart(speakers_fr_splnorm
  .pipe(prepare_alt_chart, {
      ('Speaker', ''): 'speaker',
      ('Frequency [Hz]', ''): 'frequency',
      ('CEA2034', 'On Axis'): 'on_axis',
    }))
  .encode(
    alt.Color('speaker', title='Speaker'),
    sound_pressure_yaxis('on_axis', title='On Axis Relative Sound Pressure (dB)'))
  .interactive())
```

<!-- #region id="vgRM35OrpvW1" colab_type="text" -->
## Off-axis responses
<!-- #endregion -->

<!-- #region id="bjP3nPUZx_9w" colab_type="text" -->
Note that this chart can be particularly taxing on your browser due to the sheer number of points.
<!-- #endregion -->

```python id="fh4AJa4kuyMZ" colab_type="code" colab={}
(frequency_response_chart(sidebyside=speakers_fr_splnorm.index.unique('Speaker').size > 1, data=speakers_fr_splnorm
    .loc[:, ['SPL Horizontal', 'SPL Vertical']]
    .pipe(convert_angles)
    .rename_axis(columns=['Direction', 'Angle'])
    .rename(columns={'SPL Horizontal': 'Horizontal', 'SPL Vertical': 'Vertical'}, level='Direction')
    .stack(level=['Direction', 'Angle'])
    .reset_index()
    .pipe(prepare_alt_chart, {
        'Speaker': 'speaker',
        'Direction': 'direction',
        'Angle': 'angle',
        'Frequency [Hz]': 'frequency',
        0: 'value',
      }))
  .encode(
      alt.Column('speaker', title=None),
      alt.Row('direction', title=None),
      alt.Color('angle', title='Angle (°)', scale=alt.Scale(scheme='sinebow')),
      sound_pressure_yaxis('value'))
    .interactive()
)
```

<!-- #region id="zS17Y0dMApUY" colab_type="text" -->
## Listening Window response
<!-- #endregion -->

```python id="48iUY8H-AsHI" colab_type="code" colab={}
(frequency_response_chart(speakers_fr_splnorm
  .pipe(prepare_alt_chart, {
      ('Speaker', ''): 'speaker',
      ('Frequency [Hz]', ''): 'frequency',
      ('CEA2034', 'Listening Window'): 'listening_window',
    }))
  .encode(
    alt.Color('speaker', title='Speaker'),
    sound_pressure_yaxis('listening_window', title='Listening Window Relative Sound Pressure (dB)'))
  .interactive())
```

<!-- #region id="4Xyimer4A1oJ" colab_type="text" -->
## Early Reflections response
<!-- #endregion -->

```python id="yuPM6GmIA5q3" colab_type="code" colab={}
(frequency_response_chart(speakers_fr_splnorm
  .pipe(prepare_alt_chart, {
      ('Speaker', ''): 'speaker',
      ('Frequency [Hz]', ''): 'frequency',
      ('CEA2034', 'Early Reflections'): 'early_reflections',
    }))
  .encode(
    alt.Color('speaker', title='Speaker'),
    sound_pressure_yaxis('early_reflections', title='Early Reflections Relative Sound Pressure (dB)'))
  .interactive())
```

<!-- #region id="0itIlvlIBBAv" colab_type="text" -->
## Sound Power response
<!-- #endregion -->

```python id="Javo9oSnBDsQ" colab_type="code" colab={}
(frequency_response_chart(speakers_fr_splnorm
  .pipe(prepare_alt_chart, {
      ('Speaker', ''): 'speaker',
      ('Frequency [Hz]', ''): 'frequency',
      ('CEA2034', 'Sound Power'): 'sound_power',
    }))
  .encode(
    alt.Color('speaker', title='Speaker'),
    sound_pressure_yaxis('sound_power', title='Sound Power Relative Sound Pressure (dB)'))
  .interactive())
```

<!-- #region id="OmpSXvLwB9Zo" colab_type="text" -->
## Early Reflections Directivity Index
<!-- #endregion -->

```python id="JU5pMDYMCBwY" colab_type="code" colab={}
(frequency_response_chart(speakers_fr_raw
  .pipe(prepare_alt_chart, {
      ('Speaker', '', ''): 'speaker',
      ('Frequency [Hz]', '', ''): 'frequency',
      ('[dB] Directivity Index ', 'Directivity Index', 'Early Reflections DI'): 'early_reflections_di',
    }))
  .encode(
    alt.Color('speaker', title='Speaker'),
    sound_pressure_yaxis('early_reflections_di', title='Early Reflections Directivity Index (dB)', scale_domain=(-5, 10)))
  .interactive())
```

<!-- #region id="ZIF8B_hCDSho" colab_type="text" -->
## Sound Power Directivity Index
<!-- #endregion -->

```python id="ZPrJ2pOXDVL3" colab_type="code" colab={}
(frequency_response_chart(speakers_fr_raw
  .pipe(prepare_alt_chart, {
      ('Speaker', '', ''): 'speaker',
      ('Frequency [Hz]', '', ''): 'frequency',
      ('[dB] Directivity Index ', 'Directivity Index', 'Sound Power DI'): 'sound_power_di',
    }))
  .encode(
    alt.Color('speaker', title='Speaker'),
    sound_pressure_yaxis('sound_power_di', title='Sound Power Directivity Index (dB)', scale_domain=(-10, 20)))
  .interactive())
```

<!-- #region id="xsMdN7q6D1NP" colab_type="text" -->
## Estimated In-Room Response

<!-- #endregion -->

```python id="-RuTb_A7Ehgf" colab_type="code" colab={}
(frequency_response_chart(speakers_fr_splnorm
  .pipe(prepare_alt_chart, {
      ('Speaker', ''): 'speaker',
      ('Frequency [Hz]', ''): 'frequency',
      ('Estimated In-Room Response', 'Estimated In-Room Response'): 'estimated_inroom_response',
    }))
  .encode(
    alt.Color('speaker', title='Speaker'),
    sound_pressure_yaxis('estimated_inroom_response', title='Estimated In-Room Response Relative Sound Pressure (dB)'))
  .interactive())
```