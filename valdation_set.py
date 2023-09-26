import os
import csv
from collections import defaultdict
import shutil

csv_path = 'LOC_val_solution.csv path'
val_path = 'validation path'
pt_path = 'validation packging path'

#make csv_dict
val_dict=defaultdict(list)
f = open(csv_path,mode='r',newline='')
rdr =csv.reader(f)
next(rdr)
for csv_img in rdr:
    val_value=csv_img[0]
    val_key = csv_img[1][:9]
    if not os.path.exists(os.path.join(pt_path,val_key)):
        os.makedirs(os.path.join(pt_path,val_key))
    for v in os.listdir(val_path):
        img = v[:-5]
        if img == val_value:
            shutil.copy(os.path.join(val_path, v), os.path.join(pt_path, val_key,v))