import pandas as pd


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


def recurse_attr(obj, attr, fn):
    for child in getattr(obj, attr, []):
        recurse_attr(child, attr, fn)
    fn(obj)


def assert_similar(s1, s2, tolerance=0):
    deviation = s1.sub(s2).abs()
    idxmax = deviation.idxmax()
    if pd.isna(idxmax):
        return
    max = deviation.loc[idxmax]
    if max > tolerance:
        raise AssertionError(idxmax, s1.loc[idxmax], s2.loc[idxmax], max)
