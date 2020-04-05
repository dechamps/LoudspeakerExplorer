def pipe(data, *funcs):
    # Equivalent to the (deprecated) alt.pipe(), or toolz.curried.pipe()
    # (but without the extra dependency)
    for func in funcs:
        data = func(data)
    return data


def get_nested(dic, path):
    # Shamelessly stolen from https://stackoverflow.com/a/37704379/172594
    for key in path:
        dic = dic[key]
    return dic


def set_nested(dic, path, value):
    # Shamelessly stolen from https://stackoverflow.com/a/37704379/172594
    for key in path[:-1]:
        dic = dic.setdefault(key, {})
    dic[path[-1]] = value
