import numpy as np


_ZERO_DBSPL_IN_PASCALS = 0.00002


def dbspl_to_pascals(dbspl):
    return _ZERO_DBSPL_IN_PASCALS * np.power(10, dbspl / 20)


def pascals_to_dbspl(pascals):
    return 20 * np.log10(pascals / _ZERO_DBSPL_IN_PASCALS)
