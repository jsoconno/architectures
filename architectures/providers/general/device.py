# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _General

class _Device(_General):
    _service_type = "device"
    _icon_dir = "icons/general/device"

class Tablet(_Device):
    _icon = "tablet.png"
    _default_label = "Tablet"

class Mobile(_Device):
    _icon = "mobile.png"
    _default_label = "Mobile"