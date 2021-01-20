# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Aws

class _Engagement(_Aws):
    _service_type = "engagement"
    _icon_dir = "icons/aws/engagement"

class Pinpoint(_Engagement):
    _icon = "pinpoint.png"
    _default_label = "Pinpoint"

class Connect(_Engagement):
    _icon = "connect.png"
    _default_label = "Connect"

class SimpleEmailServiceSes(_Engagement):
    _icon = "simple-email-service-ses.png"
    _default_label = "Simple Email Service Ses"