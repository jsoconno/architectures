# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Aws

class _Robotics(_Aws):
    _service_type = "robotics"
    _icon_dir = "icons/aws/robotics"

class RobomakerSimulator(_Robotics):
    _icon = "robomaker-simulator.png"
    _default_label = "Robomaker Simulator"

class Robomaker(_Robotics):
    _icon = "robomaker.png"
    _default_label = "Robomaker"

class Robotics(_Robotics):
    _icon = "robotics.png"
    _default_label = "Robotics"