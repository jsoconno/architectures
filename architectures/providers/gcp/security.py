# Do not modify this file directly. It is auto-generated with Python.

from architectures.providers import _Gcp

class _Security(_Gcp):
    _service_type = "security"
    _icon_dir = "icons/gcp/security"

class SecurityCommandCenter(_Security):
    _icon = "security-command-center.png"
    _default_label = "Security Command Center"

class Iap(_Security):
    _icon = "iap.png"
    _default_label = "Iap"

class Iam(_Security):
    _icon = "iam.png"
    _default_label = "Iam"

class SecurityScanner(_Security):
    _icon = "security-scanner.png"
    _default_label = "Security Scanner"

class KeyManagementService(_Security):
    _icon = "key-management-service.png"
    _default_label = "Key Management Service"

class ResourceManager(_Security):
    _icon = "resource-manager.png"
    _default_label = "Resource Manager"