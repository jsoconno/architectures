
from architectures.providers import _Azure


class _Identity(_Azure):
    _service_type = "identity"
    _icon_dir = "icons/azure/identity"


class AccessReview(_Identity):
    _icon = "access-review.png"


class ActiveDirectoryConnectHealth(_Identity):
    _icon = "active-directory-connect-health.png"


class ActiveDirectory(_Identity):
    _icon = "active-directory.png"


class ADB2C(_Identity):
    _icon = "ad-b2c.png"


class ADDomainServices(_Identity):
    _icon = "ad-domain-services.png"


class ADIdentityProtection(_Identity):
    _icon = "ad-identity-protection.png"


class ADPrivilegedIdentityManagement(_Identity):
    _icon = "ad-privileged-identity-management.png"


class AppRegistrations(_Identity):
    _icon = "app-registrations.png"


class ConditionalAccess(_Identity):
    _icon = "conditional-access.png"


class EnterpriseApplications(_Identity):
    _icon = "enterprise-applications.png"


class IdentityGovernance(_Identity):
    _icon = "identity-governance.png"


class InformationProtection(_Identity):
    _icon = "information-protection.png"


class ManagedIdentities(_Identity):
    _icon = "managed-identities.png"


# Aliases
