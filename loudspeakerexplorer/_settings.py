import json
import os

import loudspeakerexplorer as lsx


class Settings:
    def __init__(self, path):
        self._path = path
        self._settings = {}
        self._load()

    def track_widget(self, path, widget, on_new_value=lambda x: None):
        try:
            widget.value = lsx.util.get_nested(self._settings, path)
        except KeyError:
            pass

        def on_change(change):
            lsx.util.set_nested(self._settings, path, change['new'])
            self._save()
            return on_new_value(change['new'])
        on_new_value(widget.value)
        widget.observe(on_change, names='value')
        return widget

    def __str__(self):
        return json.dumps(self._settings, indent=4, sort_keys=True)

    def _load(self):
        try:
            with self._path.open(mode='r') as file:
                self._settings = json.load(file)
        except FileNotFoundError:
            pass

    def _save(self):
        new_path = self._path.with_name(self._path.name + '.new')
        with new_path.open(mode='w') as file:
            json.dump(self._settings, file, indent=4, sort_keys=True)
        new_path.rename(self._path)
