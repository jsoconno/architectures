from architectures.providers import _Azure

class _AI(_Azure):
    _type = "ai"
    _icon_dir = "icons/azure/ai"

class BatchAI(_AI):
    _icon = "batch-ai.png"