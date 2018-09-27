'''
    File name: Mayavi surface visualization
    Author: minhnc
    Date created(MM/DD/YYYY): 9/28/2018
    Last modified(MM/DD/YYYY HH:MM): 9/28/2018 6:33 AM
    Python Version: 3.5
    Other modules: [tensorflow-gpu 1.3.0]
    Reference: [Guide](https://www.scipy-lectures.org/advanced/3d_plotting/index.html#id4)

    Copyright = Copyright (C) 2017 of NGUYEN CONG MINH
    Credits = [None] # people who reported bug fixes, made suggestions, etc. but did not actually write the code
    License = None
    Version = 0.9.0.1
    Maintainer = [None]
    Email = minhnc.edu.tw@gmail.com
    Status = Prototype # "Prototype", "Development", or "Production"
    Code Style: http://web.archive.org/web/20111010053227/http://jaynes.colorado.edu/PythonGuidelines.html#module_formatting
'''

#==============================================================================
# Imported Modules
#==============================================================================
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import os.path
import sys
import time

import numpy as np
from mayavi import mlab

#==============================================================================
# Constant Definitions
#==============================================================================

#==============================================================================
# Function Definitions
#==============================================================================

#==============================================================================
# Main function
#==============================================================================
def main(argv=None):
    print('Hello! This is Mayavi surface visualization Program')

    # Create surface data
    from numpy import pi, sin, cos, mgrid
    dphi, dtheta = pi/250.0, pi/250.0
    [phi,theta] = mgrid[0:pi+dphi*1.5:dphi,0:2*pi+dtheta*1.5:dtheta]
    m0 = 4; m1 = 3; m2 = 2; m3 = 3; m4 = 6; m5 = 2; m6 = 6; m7 = 4;
    r = sin(m0*phi)**m1 + cos(m2*phi)**m3 + sin(m4*theta)**m5 + cos(m6*theta)**m7
    x = r*sin(phi)*cos(theta)
    y = r*cos(phi)
    z = r*sin(phi)*sin(theta)

    # Build surface s then Visualize
    s = mlab.mesh(x, y, z)
    mlab.show()


if __name__ == '__main__':
    main()
