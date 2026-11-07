def search_by_title(dvds, title):
    keyword = title.casefold()

    return [
        dvd for dvd in dvds
        if keyword in dvd.title.casefold()
    ]
