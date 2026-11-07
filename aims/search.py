def search_by_category(dvds, category):
    return [
        dvd for dvd in dvds
        if category.lower() in dvd.category.lower()
    ]


def search_by_title(dvds, title):
    return [
        dvd for dvd in dvds
        if title.lower() in dvd.title.lower()
    ]