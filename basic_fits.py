import numpy as np
import sys
import yaml
import matplotlib.pyplot as plt
from astropy.table import Table
from astropy.io import fits

def open_fits_file(name, file_type=None):
    if file_type is None:
        f = '_refined_events_ubv_I_Damineli16_'
    elif file_type == 'comp':
        f = '_refined_events_ubv_I_Damineli16_companions'
    else:
        raise ValueError('wrong file type: ' + str(file_type))  
    fits_table_name = name + f + 'rb.fits'
    with fits.open(fits_table_name) as hdus:
        t = Table(hdus[1].data)
        return t

if __name__ == '__main__':

    with open(sys.argv[1]) as in_file_1:
            params = yaml.safe_load(in_file_1)

    field_name = params["name"]
    data = open_fits_file(field_name)

#mask = (t['mass_L'] < 0.15) & (t['isMultiple_L'] == 1.0) & (t['N_companions_S'] == 0.0) & (t['N_companions_L'] == 1.0) & (t['sep_L'] > 0.1)
#t = t[mask]


#comp_list = t['companion_idx_list']
#t_E = t['t_E']
#u_0 = t['u0']
#sep_L = t['sep_L']

#with open('companions_sep.txt', 'w') as file1:
#    file1.writelines('comp_idx t_E u_0 sep_L \n')
#    for i in range(len(comp_list)):
#        file1.writelines('%s %f %f %f \n' %(comp_list[i], t_E[i], u_0[i], sep_L[i]))
