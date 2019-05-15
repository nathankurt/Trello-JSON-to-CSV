#!/usr/bin/env python3
#DON'T GET RID OF ^

##Be sure file is in the same folder as script

import pandas as pd

f_name = input("Enter File Name: ")
with open(f_name, encoding='utf-8-sig') as f_input:
    df = pd.read_json(f_input)

new_file_name = f_name.split(".")[0] + ".csv"
df.to_csv(f_name, encoding='utf-8', index=False)