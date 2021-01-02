
from architectures.providers import _Azure


class _Security(_Azure):
    _service_type = "security"
    _icon_dir = "icons/azure/security"


class KeyVaults(_Security):
    _icon = "key-vaults.png"


class SecurityCenter(_Security):
    _icon = "security-center.png"


class Sentinel(_Security):
    _icon = "sentinel.png"


# Aliases
