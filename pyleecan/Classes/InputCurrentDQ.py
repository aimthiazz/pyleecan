# -*- coding: utf-8 -*-
"""File generated according to Generator/ClassesRef/Simulation/InputCurrentDQ.csv
WARNING! All changes made in this file will be lost!
"""

from os import linesep
from logging import getLogger
from ._check import check_var, raise_
from ..Functions.get_logger import get_logger
from ..Functions.save import save
from .Input import Input

# Import all class method
# Try/catch to remove unnecessary dependencies in unused method
try:
    from ..Methods.Simulation.InputCurrentDQ.gen_input import gen_input
except ImportError as error:
    gen_input = error


from ._check import InitUnKnowClassError
from .Import import Import
from .ImportMatrixVal import ImportMatrixVal


class InputCurrentDQ(Input):
    """Input to set the electrical module output"""

    VERSION = 1

    # cf Methods.Simulation.InputCurrentDQ.gen_input
    if isinstance(gen_input, ImportError):
        gen_input = property(
            fget=lambda x: raise_(
                ImportError(
                    "Can't use InputCurrentDQ method gen_input: " + str(gen_input)
                )
            )
        )
    else:
        gen_input = gen_input
    # save method is available in all object
    save = save

    # generic copy method
    def copy(self):
        """Return a copy of the class
        """
        return type(self)(init_dict=self.as_dict())

    # get_logger method is available in all object
    get_logger = get_logger

    def __init__(
        self,
        Is=None,
        Ir=None,
        angle_rotor=None,
        Nr=None,
        rot_dir=-1,
        angle_rotor_initial=0,
        time=-1,
        angle=-1,
        init_dict=None,
        init_str=None,
    ):
        """Constructor of the class. Can be use in three ways :
        - __init__ (arg1 = 1, arg3 = 5) every parameters have name and default values
            for Matrix, None will initialise the property with an empty Matrix
            for pyleecan type, None will call the default constructor
        - __init__ (init_dict = d) d must be a dictionnary with every properties as keys
        - __init__ (init_str = s) s must be a string
        s is the file path to load

        ndarray or list can be given for Vector and Matrix
        object or dict can be given for pyleecan Object"""

        if Is == -1:
            Is = Import()
        if Ir == -1:
            Ir = Import()
        if angle_rotor == -1:
            angle_rotor = Import()
        if Nr == -1:
            Nr = Import()
        if time == -1:
            time = ImportMatrixVal()
        if angle == -1:
            angle = ImportMatrixVal()
        if init_str is not None:  # Initialisation by str
            from ..Functions.load import load

            assert type(init_str) is str
            # load the object from a file
            obj = load(init_str)
            assert type(obj) is type(self)
            Is = obj.Is
            Ir = obj.Ir
            angle_rotor = obj.angle_rotor
            Nr = obj.Nr
            rot_dir = obj.rot_dir
            angle_rotor_initial = obj.angle_rotor_initial
            time = obj.time
            angle = obj.angle
        if init_dict is not None:  # Initialisation by dict
            assert type(init_dict) is dict
            # Overwrite default value with init_dict content
            if "Is" in list(init_dict.keys()):
                Is = init_dict["Is"]
            if "Ir" in list(init_dict.keys()):
                Ir = init_dict["Ir"]
            if "angle_rotor" in list(init_dict.keys()):
                angle_rotor = init_dict["angle_rotor"]
            if "Nr" in list(init_dict.keys()):
                Nr = init_dict["Nr"]
            if "rot_dir" in list(init_dict.keys()):
                rot_dir = init_dict["rot_dir"]
            if "angle_rotor_initial" in list(init_dict.keys()):
                angle_rotor_initial = init_dict["angle_rotor_initial"]
            if "time" in list(init_dict.keys()):
                time = init_dict["time"]
            if "angle" in list(init_dict.keys()):
                angle = init_dict["angle"]
        # Initialisation by argument
        # Is can be None, a Import object or a dict
        if isinstance(Is, dict):
            # Check that the type is correct (including daughter)
            class_name = Is.get("__class__")
            if class_name not in [
                "Import",
                "ImportGenMatrixSin",
                "ImportGenToothSaw",
                "ImportGenVectLin",
                "ImportGenVectSin",
                "ImportMatlab",
                "ImportMatrix",
                "ImportMatrixVal",
                "ImportMatrixXls",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for Is"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.Is = class_obj(init_dict=Is)
        elif isinstance(Is, str):
            from ..Functions.load import load

            Is = load(Is)
            # Check that the type is correct (including daughter)
            class_name = Is.__class__.__name__
            if class_name not in [
                "Import",
                "ImportGenMatrixSin",
                "ImportGenToothSaw",
                "ImportGenVectLin",
                "ImportGenVectSin",
                "ImportMatlab",
                "ImportMatrix",
                "ImportMatrixVal",
                "ImportMatrixXls",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for Is"
                )
            self.Is = Is
        else:
            self.Is = Is
        # Ir can be None, a Import object or a dict
        if isinstance(Ir, dict):
            # Check that the type is correct (including daughter)
            class_name = Ir.get("__class__")
            if class_name not in [
                "Import",
                "ImportGenMatrixSin",
                "ImportGenToothSaw",
                "ImportGenVectLin",
                "ImportGenVectSin",
                "ImportMatlab",
                "ImportMatrix",
                "ImportMatrixVal",
                "ImportMatrixXls",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for Ir"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.Ir = class_obj(init_dict=Ir)
        elif isinstance(Ir, str):
            from ..Functions.load import load

            Ir = load(Ir)
            # Check that the type is correct (including daughter)
            class_name = Ir.__class__.__name__
            if class_name not in [
                "Import",
                "ImportGenMatrixSin",
                "ImportGenToothSaw",
                "ImportGenVectLin",
                "ImportGenVectSin",
                "ImportMatlab",
                "ImportMatrix",
                "ImportMatrixVal",
                "ImportMatrixXls",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for Ir"
                )
            self.Ir = Ir
        else:
            self.Ir = Ir
        # angle_rotor can be None, a Import object or a dict
        if isinstance(angle_rotor, dict):
            # Check that the type is correct (including daughter)
            class_name = angle_rotor.get("__class__")
            if class_name not in [
                "Import",
                "ImportGenMatrixSin",
                "ImportGenToothSaw",
                "ImportGenVectLin",
                "ImportGenVectSin",
                "ImportMatlab",
                "ImportMatrix",
                "ImportMatrixVal",
                "ImportMatrixXls",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for angle_rotor"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.angle_rotor = class_obj(init_dict=angle_rotor)
        elif isinstance(angle_rotor, str):
            from ..Functions.load import load

            angle_rotor = load(angle_rotor)
            # Check that the type is correct (including daughter)
            class_name = angle_rotor.__class__.__name__
            if class_name not in [
                "Import",
                "ImportGenMatrixSin",
                "ImportGenToothSaw",
                "ImportGenVectLin",
                "ImportGenVectSin",
                "ImportMatlab",
                "ImportMatrix",
                "ImportMatrixVal",
                "ImportMatrixXls",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for angle_rotor"
                )
            self.angle_rotor = angle_rotor
        else:
            self.angle_rotor = angle_rotor
        # Nr can be None, a Import object or a dict
        if isinstance(Nr, dict):
            # Check that the type is correct (including daughter)
            class_name = Nr.get("__class__")
            if class_name not in [
                "Import",
                "ImportGenMatrixSin",
                "ImportGenToothSaw",
                "ImportGenVectLin",
                "ImportGenVectSin",
                "ImportMatlab",
                "ImportMatrix",
                "ImportMatrixVal",
                "ImportMatrixXls",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for Nr"
                )
            # Dynamic import to call the correct constructor
            module = __import__("pyleecan.Classes." + class_name, fromlist=[class_name])
            class_obj = getattr(module, class_name)
            self.Nr = class_obj(init_dict=Nr)
        elif isinstance(Nr, str):
            from ..Functions.load import load

            Nr = load(Nr)
            # Check that the type is correct (including daughter)
            class_name = Nr.__class__.__name__
            if class_name not in [
                "Import",
                "ImportGenMatrixSin",
                "ImportGenToothSaw",
                "ImportGenVectLin",
                "ImportGenVectSin",
                "ImportMatlab",
                "ImportMatrix",
                "ImportMatrixVal",
                "ImportMatrixXls",
            ]:
                raise InitUnKnowClassError(
                    "Unknow class name " + class_name + " in init_dict for Nr"
                )
            self.Nr = Nr
        else:
            self.Nr = Nr
        self.rot_dir = rot_dir
        self.angle_rotor_initial = angle_rotor_initial
        # Call Input init
        super(InputCurrentDQ, self).__init__(time=time, angle=angle)
        # The class is frozen (in Input init), for now it's impossible to
        # add new properties

    def __str__(self):
        """Convert this objet in a readeable string (for print)"""

        InputCurrentDQ_str = ""
        # Get the properties inherited from Input
        InputCurrentDQ_str += super(InputCurrentDQ, self).__str__()
        if self.Is is not None:
            tmp = self.Is.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            InputCurrentDQ_str += "Is = " + tmp
        else:
            InputCurrentDQ_str += "Is = None" + linesep + linesep
        if self.Ir is not None:
            tmp = self.Ir.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            InputCurrentDQ_str += "Ir = " + tmp
        else:
            InputCurrentDQ_str += "Ir = None" + linesep + linesep
        if self.angle_rotor is not None:
            tmp = (
                self.angle_rotor.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            )
            InputCurrentDQ_str += "angle_rotor = " + tmp
        else:
            InputCurrentDQ_str += "angle_rotor = None" + linesep + linesep
        if self.Nr is not None:
            tmp = self.Nr.__str__().replace(linesep, linesep + "\t").rstrip("\t")
            InputCurrentDQ_str += "Nr = " + tmp
        else:
            InputCurrentDQ_str += "Nr = None" + linesep + linesep
        InputCurrentDQ_str += "rot_dir = " + str(self.rot_dir) + linesep
        InputCurrentDQ_str += (
            "angle_rotor_initial = " + str(self.angle_rotor_initial) + linesep
        )
        return InputCurrentDQ_str

    def __eq__(self, other):
        """Compare two objects (skip parent)"""

        if type(other) != type(self):
            return False

        # Check the properties inherited from Input
        if not super(InputCurrentDQ, self).__eq__(other):
            return False
        if other.Is != self.Is:
            return False
        if other.Ir != self.Ir:
            return False
        if other.angle_rotor != self.angle_rotor:
            return False
        if other.Nr != self.Nr:
            return False
        if other.rot_dir != self.rot_dir:
            return False
        if other.angle_rotor_initial != self.angle_rotor_initial:
            return False
        return True

    def as_dict(self):
        """Convert this objet in a json seriable dict (can be use in __init__)
        """

        # Get the properties inherited from Input
        InputCurrentDQ_dict = super(InputCurrentDQ, self).as_dict()
        if self.Is is None:
            InputCurrentDQ_dict["Is"] = None
        else:
            InputCurrentDQ_dict["Is"] = self.Is.as_dict()
        if self.Ir is None:
            InputCurrentDQ_dict["Ir"] = None
        else:
            InputCurrentDQ_dict["Ir"] = self.Ir.as_dict()
        if self.angle_rotor is None:
            InputCurrentDQ_dict["angle_rotor"] = None
        else:
            InputCurrentDQ_dict["angle_rotor"] = self.angle_rotor.as_dict()
        if self.Nr is None:
            InputCurrentDQ_dict["Nr"] = None
        else:
            InputCurrentDQ_dict["Nr"] = self.Nr.as_dict()
        InputCurrentDQ_dict["rot_dir"] = self.rot_dir
        InputCurrentDQ_dict["angle_rotor_initial"] = self.angle_rotor_initial
        # The class name is added to the dict fordeserialisation purpose
        # Overwrite the mother class name
        InputCurrentDQ_dict["__class__"] = "InputCurrentDQ"
        return InputCurrentDQ_dict

    def _set_None(self):
        """Set all the properties to None (except pyleecan object)"""

        if self.Is is not None:
            self.Is._set_None()
        if self.Ir is not None:
            self.Ir._set_None()
        if self.angle_rotor is not None:
            self.angle_rotor._set_None()
        if self.Nr is not None:
            self.Nr._set_None()
        self.rot_dir = None
        self.angle_rotor_initial = None
        # Set to None the properties inherited from Input
        super(InputCurrentDQ, self)._set_None()

    def _get_Is(self):
        """getter of Is"""
        return self._Is

    def _set_Is(self, value):
        """setter of Is"""
        check_var("Is", value, "Import")
        self._Is = value

        if self._Is is not None:
            self._Is.parent = self

    # Stator dq-currents as a function of time to import
    # Type : Import
    Is = property(
        fget=_get_Is,
        fset=_set_Is,
        doc=u"""Stator dq-currents as a function of time to import""",
    )

    def _get_Ir(self):
        """getter of Ir"""
        return self._Ir

    def _set_Ir(self, value):
        """setter of Ir"""
        check_var("Ir", value, "Import")
        self._Ir = value

        if self._Ir is not None:
            self._Ir.parent = self

    # Rotor currents as a function of time to import
    # Type : Import
    Ir = property(
        fget=_get_Ir,
        fset=_set_Ir,
        doc=u"""Rotor currents as a function of time to import""",
    )

    def _get_angle_rotor(self):
        """getter of angle_rotor"""
        return self._angle_rotor

    def _set_angle_rotor(self, value):
        """setter of angle_rotor"""
        check_var("angle_rotor", value, "Import")
        self._angle_rotor = value

        if self._angle_rotor is not None:
            self._angle_rotor.parent = self

    # Rotor angular position as a function of time (if None computed according to Nr) to import
    # Type : Import
    angle_rotor = property(
        fget=_get_angle_rotor,
        fset=_set_angle_rotor,
        doc=u"""Rotor angular position as a function of time (if None computed according to Nr) to import""",
    )

    def _get_Nr(self):
        """getter of Nr"""
        return self._Nr

    def _set_Nr(self, value):
        """setter of Nr"""
        check_var("Nr", value, "Import")
        self._Nr = value

        if self._Nr is not None:
            self._Nr.parent = self

    # Rotor speed as a function of time to import
    # Type : Import
    Nr = property(
        fget=_get_Nr,
        fset=_set_Nr,
        doc=u"""Rotor speed as a function of time to import""",
    )

    def _get_rot_dir(self):
        """getter of rot_dir"""
        return self._rot_dir

    def _set_rot_dir(self, value):
        """setter of rot_dir"""
        check_var("rot_dir", value, "float", Vmin=-1, Vmax=1)
        self._rot_dir = value

    # Rotation direction of the rotor 1 trigo, -1 clockwise
    # Type : float, min = -1, max = 1
    rot_dir = property(
        fget=_get_rot_dir,
        fset=_set_rot_dir,
        doc=u"""Rotation direction of the rotor 1 trigo, -1 clockwise""",
    )

    def _get_angle_rotor_initial(self):
        """getter of angle_rotor_initial"""
        return self._angle_rotor_initial

    def _set_angle_rotor_initial(self, value):
        """setter of angle_rotor_initial"""
        check_var("angle_rotor_initial", value, "float")
        self._angle_rotor_initial = value

    # Initial angular position of the rotor at t=0
    # Type : float
    angle_rotor_initial = property(
        fget=_get_angle_rotor_initial,
        fset=_set_angle_rotor_initial,
        doc=u"""Initial angular position of the rotor at t=0""",
    )
