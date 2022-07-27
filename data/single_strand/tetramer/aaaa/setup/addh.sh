#/bin/bash

grep -v "   H" rna.pdb | grep ATOM > rna_noh.pdb
python ../../../../../script/addh.py