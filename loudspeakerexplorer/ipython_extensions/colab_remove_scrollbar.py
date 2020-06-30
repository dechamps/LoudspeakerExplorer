import IPython


def _remove_scrollbar():
    # Prevents the current Colab output cell from scrolling.

    # Colab does not recognize the scrolled=false cell metadata.
    # Simulate it using the technique described at https://github.com/googlecolab/colabtools/issues/541
    # Note that this only has an effect in Colab.
    IPython.display.display(IPython.display.Javascript('''
        try { google.colab.output.setIframeHeight(0, true, {maxHeight: 50000}) }
        catch (e) {}
    '''))


def load_ipython_extension(ipython):
    ipython.events.register('pre_run_cell', _remove_scrollbar)


def unload_ipython_extension(ipython):
    ipython.events.unregister('pre_run_cell', _remove_scrollbar)
