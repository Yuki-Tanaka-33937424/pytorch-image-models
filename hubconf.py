dependencies = ['torch']
from timm_new.models import registry

globals().update(registry._model_entrypoints)
