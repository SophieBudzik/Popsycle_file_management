import numpy as np
import sys
import yaml
import matplotlib.pyplot as plt
from astropy.table import Table
from astropy.io import fits

with open(sys.argv[1]) as in_file_1:
    "opens the yaml file with input names"
    input_ = yaml.safe_load(in_file_1)
name = input_["output_root"]
file_type = '_refined_events_ubv_I_Damineli16_'
basic = name + file_type + 'rb.fits'


with fits.open(basic) as hdus:
    t = Table(hdus[1].data)


mask = (t['mass_L'] < 0.3) & (t['mass_L'] > 0.15) & (t['isMultiple_L'] == 1.0) & (t['N_companions_S'] == 0.0)
t = t[mask]


comp_list = t['companion_idx_list']
print(comp_list)

with open('companions.txt', 'w') as file1:
    for i in range(len(comp_list)):
        file1.writelines('%s \n' %(comp_list[i]))
