# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 17:20:16 2019

@author: boidiyv
"""

import os.path
import sys
import argparse
parser = argparse.ArgumentParser(description='Process some integers.')
#print(len(sys.path))
#sys.path.remove('C:/Users/boidiyv/Documents/tes_squad_model/document-qa-master')
print(sys.path)
for arg in sys.argv:
    print('sys arg',arg)
args = parser.parse_args()
print(args._get_args)