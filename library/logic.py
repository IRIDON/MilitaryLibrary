from django.template.defaultfilters import slugify
from translitua import translit, RussianSimple


def filter_items(Model, last=False):
    date_filter = '-pub_date' if last else 'pub_date'

    return Model.objects.filter(visible=True).order_by(date_filter)

def _get_unique_slug(text, Model):
    slug = translit(text, RussianSimple)
    slug = slugify(slug)

    unique_slug = slug
    num = 1

    while Model.objects.filter(slug=unique_slug).exists():
        unique_slug = '{}-{}'.format(slug, num)
        num += 1

    return unique_slug
