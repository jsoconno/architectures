
from architectures.providers import _Azure


class _Mobile(_Azure):
    _service_type = "mobile"
    _icon_dir = "icons/azure/mobile"


class AppServiceMobile(_Mobile):
    _icon = "app-service---mobile.png"


class MobileEngagement(_Mobile):
    _icon = "mobile-engagement.png"


class NotificationHubs(_Mobile):
    _icon = "notification-hubs.png"


# Aliases
