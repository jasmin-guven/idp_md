import matplotlib.pyplot as plt
import numpy as np
import MDAnalysis as mda 
import MDAnalysis.auxiliary 


potential_file = "../potential.xvg"
reader = mda.auxiliary.XVG.XVGReader(potential_file)
print(reader)