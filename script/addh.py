import glob as glob
import numpy as np
import re
import warnings
from openmm.app import *
from openmm import *
from openmm.unit import *
from openmm.app import PDBFile
from pdbfixer import PDBFixer


file = "rna_noh.pdb"
fixer = PDBFixer(filename=file)
fixer.findMissingResidues()
fixer.findNonstandardResidues()
fixer.replaceNonstandardResidues()
fixer.removeHeterogens(True)
fixer.findMissingAtoms()
fixer.addMissingHydrogens(7.0)

PDBFile.writeFile(fixer.topology, fixer.positions, open('pdbfixer.pdb', 'w'))