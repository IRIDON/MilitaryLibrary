from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.urlresolvers import reverse
from jinja2 import Environment
from django.conf import settings

from easy_thumbnails.files import get_thumbnailer

def get_thumb(file, name):
	return get_thumbnailer(file)[name].url
    
def environment(**options):
    env = Environment(**options)

    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
        'settings': settings,
        'get_thumb': get_thumb,
    })


    return env