from numpy import ones, pi, array
from os.path import join
import matplotlib.pyplot as plt
from Tests import save_validation_path as save_path

from pyleecan.Classes.Simu1 import Simu1

from pyleecan.Classes.InputCurrent import InputCurrent
from pyleecan.Classes.InputFlux import InputFlux
from pyleecan.Classes.ImportGenVectLin import ImportGenVectLin
from pyleecan.Classes.ImportMatrixVal import ImportMatrixVal
from pyleecan.Classes.ImportMatlab import ImportMatlab

from pyleecan.Classes.MagFEMM import MagFEMM
from pyleecan.Classes.Output import Output
from Tests import TEST_DATA_DIR
import pytest

from pyleecan.Functions.load import load
from pyleecan.definitions import DATA_DIR

SPMSM_015 = load(join(DATA_DIR, "Machine", "SPMSM_015.json"))


@pytest.mark.long
@pytest.mark.validation
@pytest.mark.FEMM
def test_Magnetic_FEMM_sym():
    """Validation of outer rotor SPMSM 
    Open circuit (Null Stator currents)

    Machine B from Vu Xuan Hung thesis
    "Modeling of exterior rotor permanent magnet machines with concentrated windings" 
    Hanoi university of science and technology 2012 
    Test compute the Flux in FEMM, with and without symmetry
    and with MANATEE semi-analytical subdomain model
    """

    simu = Simu1(name="EM_SPMSM_NL_001", machine=SPMSM_015)

    # Definition of the enforced output of the electrical module
    Nr = ImportMatrixVal(value=ones(1) * 3000)
    Is = ImportMatrixVal(value=array([[0, 0, 0]]))
    time = ImportGenVectLin(start=0, stop=0, num=1, endpoint=True)
    angle = ImportGenVectLin(start=0, stop=2 * 2 * pi / 9, num=2043, endpoint=False)

    simu.input = InputCurrent(
        Is=Is,
        Ir=None,  # No winding on the rotor
        Nr=Nr,
        angle_rotor=None,
        time=time,
        angle=angle,
        angle_rotor_initial=0,
    )

    # Definition of the magnetic simulation (is_mmfr=False => no flux from the magnets)
    assert SPMSM_015.comp_sym() == (9, False)
    simu.mag = MagFEMM(
        type_BH_stator=0, type_BH_rotor=0, is_symmetry_a=True, is_mmfs=False, sym_a=9
    )
    simu.force = None
    simu.struct = None
    # Just load the Output and ends (we could also have directly filled the Output object)
    simu_load = Simu1(init_dict=simu.as_dict())
    simu_load.mag = None
    mat_file = join(TEST_DATA_DIR, "EM_SPMSM_NL_001_MANATEE_SDM.mat")
    Br = ImportMatlab(file_path=mat_file, var_name="Br")
    Bt = ImportMatlab(file_path=mat_file, var_name="Bt")
    angle2 = ImportGenVectLin(start=0, stop=2 * pi / 9, num=2048 / 9, endpoint=False)
    simu_load.input = InputFlux(time=time, angle=angle2, Br=Br, Bt=Bt)

    out = Output(simu=simu)
    out.post.legend_name = "Symmetry"
    simu.run()

    out3 = Output(simu=simu_load)
    out3.post.legend_name = "MANATEE SDM"
    out3.post.line_color = "r--"
    simu_load.run()

    plt.close("all")
    out.plot_B_space(out_list=[out3])

    fig = plt.gcf()
    fig.savefig(join(save_path, "test_EM_SPMSM_NL_001_SDM.png"))
