import numpy as np
import os
import random

def gen_and_save(dir, n_var):

    n_data = 2 ** n_var
    save_dir = dir+"truth_table_"+str(n_var)+".csv"

    f = open(save_dir, 'w')

    for i in range(n_data):
        f.write("{0:b}".format(i).zfill(n_var)+",")
        f.write(str(random.randint(0,1)) + "\n")
    
for n_var in range(15):
    gen_and_save(dir="datasets/", n_var=n_var)




