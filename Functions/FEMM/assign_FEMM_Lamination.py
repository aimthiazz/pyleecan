# -*- coding: utf-8 -*-
"""@package assign_FEMM_Lamination
@date Created on août 01 17:06 2018
@author franco_i
"""
import femm
from pyleecan.Functions.FEMM import GROUP_RC, GROUP_SC


def assign_FEMM_Lamination(surf, prop, mesh_dict):
    """Assign the property of Lamination

    Parameters
    ----------
    surf : Surface
        The surface to assign
    prop : str
        the property to assign
    FEMM_dict : dict
        Dictionnary containing the main parameters of FEMM

    Returns
    -------
    None
    
    """
    point_ref = surf.point_ref

    femm.mi_addblocklabel(point_ref.real, point_ref.imag)
    femm.mi_selectlabel(point_ref.real, point_ref.imag)
    femm.mi_setblockprop(
        prop, mesh_dict["automesh"], mesh_dict["meshsize"], 0, 0, mesh_dict["group"], 0
    )
    femm.mi_clearselected()
