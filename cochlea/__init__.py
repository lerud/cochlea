from __future__ import division
from __future__ import print_function


import numpy as np

from cochlea.zilany2009.zilany2009 import run_zilany2009
from cochlea.zilany2009.zilany2009_human import run_zilany2009_human
from cochlea.holmberg2007 import run_holmberg2007




def set_dbspl(signal, dbspl):
    p0 = 20e-6
    rms = np.sqrt( np.sum(signal**2) / signal.size )

    scalled = signal * 10**(dbspl/20) * p0 / rms

    return scalled


def set_dba_isolet(signal, dba):
    p0 = 20e-6
    rms_dba = 0.02972401089     # value from miclib (precalculated for
                                # all ISOLET files)

    scaled = signal * 10**(dba/20) * p0 / rms_dba

    return scaled