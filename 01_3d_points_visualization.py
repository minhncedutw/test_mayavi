'''
    File name: Mayavi 3D points visualization
    Author: minhnc
    Date created(MM/DD/YYYY): 9/28/2018
    Last modified(MM/DD/YYYY HH:MM): 9/28/2018 5:18 AM
    Python Version: 3.5
    Other modules: []
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
    print('Hello! This is Mayavi 3D points visualization Program')

    # View 3D points
    x, y, z = np.random.random((3, 40))
    color = (np.random.randint(0, 5, (40)) + 90)/100 # create different label to be different color but similar size
    mlab.points3d(x, y, z, color, scale_factor=0.1)
    mlab.show()


if __name__ == '__main__':
    main()
