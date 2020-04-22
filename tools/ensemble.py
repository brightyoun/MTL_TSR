import numpy as np
import os

path = 'output/committee_ms1m/base/'
exps = ['base-nasnetasmall-lr0.1', 'base-irv2-lr0.1', 'base-densenet121-lr0.1', 'base-resnet101-lr0.1', 'base-resnet50-lr0.3']
output_exp = 'ensemble-top{}'.format(len(exps))
if not os.path.isdir(path + output_exp):
    os.makedirs(path + output_exp)
