# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Aws

class _Enablement(_Aws):
    _service_type = "enablement"
    _icon_dir = "icons/aws/enablement"

class ManagedServices(_Enablement):
    _icon = "managed-services.png"
    _default_label = "Managed Services"

class Support(_Enablement):
    _icon = "support.png"
    _default_label = "Support"

class Iq(_Enablement):
    _icon = "iq.png"
    _default_label = "Iq"

class ProfessionalServices(_Enablement):
    _icon = "professional-services.png"
    _default_label = "Professional Services"