
from architectures.providers import _Azure


class _Migration(_Azure):
    _service_type = "migration"
    _icon_dir = "icons/azure/migration"


class DatabaseMigrationServices(_Migration):
    _icon = "database-migration-services.png"


class MigrationProjects(_Migration):
    _icon = "migration-projects.png"


class RecoveryServicesVaults(_Migration):
    _icon = "recovery-services-vaults.png"


# Aliases
