def unpackaging(collection):
    """
    Removing nesting of list
    :param collection: a list object with an arbitrary nesting
    :return: generator object
    """
    assert isinstance(collection, (list, tuple)), "Входной аргумент должен быть списком или кортежем"

    for item in collection:
        if isinstance(item, (list, tuple)):
            for subitem in unpackaging(item):
                yield subitem
        else:
            yield item


def grouping(collection):
    """
    Group up objects in pairs.
    :param collection: symmetrical list with no nesting like ['a','b','1','2']
    :return: list with one-level nesting like [('a','1'), ('b','2')]
    """
    assert isinstance(collection, (list, tuple)), "Входной аргумент должен быть списком или кортежем"
    assert len(collection) % 2 == 0, "Список должен быть симметричным"

    return list(zip(collection[:len(collection)//2],
                    collection[len(collection)//2:]))
