import html

import IPython


def display_css(css):
    return IPython.display.display(IPython.display.HTML(
        '<style>' + html.escape(css) + '</style>'))
