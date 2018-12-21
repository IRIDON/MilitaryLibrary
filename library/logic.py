from django.conf import settings
from django.template.defaultfilters import slugify
from translitua import translit, RussianSimple


def filter_items(Model, last=False):
    date_filter = '-pub_date' if last else 'pub_date'

    return Model.objects.filter(visible=True).order_by(date_filter)

def _get_file_type(link):
    ext = re.search('\.[a-zA-Z0-9]+$', str(link))
    ext = ext.group(0).replace('.', '')
    ext = ext.encode('utf-8')

    if settings.ALLOWED_BOOK_FORMATS.index(ext) != -1:
        return ext

    return None

def _get_unique_slug(text, Model):
    slug = translit(text, RussianSimple)
    slug = slugify(slug)

    if len(slug) > settings.SLUG_MAX_LENGTH:
        slug = slug[:settings.SLUG_MAX_LENGTH - 1]

    unique_slug = slug
    num = 1

    while Model.objects.filter(slug=unique_slug).exists():
        unique_slug = '{}-{}'.format(slug, num)
        num += 1

    return unique_slug
