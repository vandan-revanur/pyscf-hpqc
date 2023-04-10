#!/usr/bin/env python
import pyscf
from pyscf.tools.go_db import get_xyz
import requests

if __name__ == '__main__':
    VERBOSITY = 9
    CONV_TOL = 1e-7
    BASIS = 'sto-3g'
    FROZEN = 4
    url = 'https://raw.githubusercontent.com/HPQC-LABS/goDatabase/master/benchmark_sets/gw5000.txt'
    mol_name = 'C10H15NO2S2:GW5000.v0'

    page = requests.get(url)
    data = page.text

    molecule_xyz = get_xyz(data, mol_name)

    print(molecule_xyz)

    neut_mol = pyscf.M(atom=molecule_xyz, basis=BASIS, verbose=VERBOSITY, spin=0, charge=0)

    print(neut_mol)
