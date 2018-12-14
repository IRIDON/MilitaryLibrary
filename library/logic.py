def filter_items(Model, last=False):
    date_filter = '-pub_date' if last else 'pub_date'

    return Model.objects.filter(visible=True).order_by(date_filter)
