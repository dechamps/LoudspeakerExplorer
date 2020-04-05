def display(widget, value):
    widget.layout.display = None if value else 'none'


def lookup_option_label(widget):
    return {value: label for label, value in widget.options}[widget.value]
