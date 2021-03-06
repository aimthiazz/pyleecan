# -*- coding: utf-8 -*-

import numpy as np
from numpy import int32


def get_all_connectivity(self, group=None):
    """Return the connectivity and tags for a selected group of elements

    Parameters
    ----------
    self : ElementMat
        an ElementMat object
    group : numpy.array
        one or several group number

    Returns
    -------
    connect_select: ndarray
        Selected connectivity
    tag_select: ndarray
        Selected element tags

    """

    connect = self.connectivity
    elem_groups = self.group
    elem_tags = self.tag
    connect_select = np.array([], dtype=int)
    tag_select = np.array([], dtype=int)

    if group is not None:
        group = int32(group)
        if isinstance(group, (int, int32, float, complex)):
            group = np.array([group], dtype=int)

        if type(group) is list or type(group) is np.ndarray:
            for grp in group:
                Ipos_select = np.where(elem_groups == grp)[0]
                tag_select = np.concatenate([tag_select, elem_tags[Ipos_select]])
                k = 0
                for Ipos in Ipos_select:
                    if k == 0:
                        connect_select = np.append(
                            connect_select, connect[Ipos, :], axis=0
                        )
                        k += 1
                    else:
                        connect_select = np.vstack((connect_select, connect[Ipos, :]))
                        k += 1

    elif group is None:
        connect_select = connect
        tag_select = elem_tags

    else:
        return None, None

    return connect_select, tag_select
