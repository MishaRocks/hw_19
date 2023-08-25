from django.conf import settings
from django.core.cache import cache


def get_some_cache(model):
    if settings.CACHE_ENABLED:
        key = 'model_list'
        model_list = cache.get(key)
        if model_list is None:
            model_list = model.objects.all()
            cache.set(key, model_list)
    else:
        model_list = model.objects.all()

    return model_list

