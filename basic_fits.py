import numpy as np
import sys
import yaml
import matplotlib.pyplot as plt
from astropy.table import Table
from astropy.io import fits

def open_fits_file(settings_file, file_type=None):
    with open(settings_file) as in_file_1:
        input_ = yaml.safe_load(in_file_1)
def open_fits_file(settings_file, file_type=None):
    name = input_["name"]
    if file_type is None:
        f = '_refined_events_ubv_I_Damineli16_'
    elif file_type is comp:
        f = '_refined_events_ubv_I_Damineli16_companions'
    elif file_type is peaks:
        f = '_refined_events_ubv_I_Damineli16_companions'
    elif file_type is lc:



        f = '_refined_events_ubv_I_Damineli16_lightcurves'
    else:
        raise ValueError('wrong file type: ' + str(file_type))
    fits_table_name = name + f + 'rb.fits'

mask = (t['mass_L'] < 0.15) & (t['isMultiple_L'] == 1.0) & (t['N_companions_S'] == 0.0) & (t['N_companions_L'] == 1.0) & (t['sep_L'] > 0.1)
t = t[mask]


comp_list = t['companion_idx_list']
t_E = t['t_E']
u_0 = t['u0']
sep_L = t['sep_L']

with open('companions_sep.txt', 'w') as file1:
    file1.writelines('comp_idx t_E u_0 sep_L \n')
    for i in range(len(comp_list)):
        file1.writelines('%s %f %f %f \n' %(comp_list[i], t_E[i], u_0[i], sep_L[i]))
