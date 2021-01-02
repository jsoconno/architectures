
from architectures.providers import _Azure


class _Ml(_Azure):
    _service_type = "ml"
    _icon_dir = "icons/azure/ml"


class BatchAI(_Ml):
    _icon = "batch-ai.png"


class BotServices(_Ml):
    _icon = "bot-services.png"


class CognitiveServices(_Ml):
    _icon = "cognitive-services.png"


class GenomicsAccounts(_Ml):
    _icon = "genomics-accounts.png"


class MachineLearningServiceWorkspaces(_Ml):
    _icon = "machine-learning-service-workspaces.png"


class MachineLearningStudioWebServicePlans(_Ml):
    _icon = "machine-learning-studio-web-service-plans.png"


class MachineLearningStudioWebServices(_Ml):
    _icon = "machine-learning-studio-web-services.png"


class MachineLearningStudioWorkspaces(_Ml):
    _icon = "machine-learning-studio-workspaces.png"


# Aliases
