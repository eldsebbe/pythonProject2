import os
import pandas as pd
import lib

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))

biology_path= CURR_DIR_PATH + "/data/biology_data.csv"      #skickar in

#lib.biology_combine()
#lib.herbology_combine()
#lib.math_combine()
#lib.pe_combine()
#lib.physics_combine()

#lib.combine_names(biology_path)
#lib.is_late(biology_path)

biology_df = pd.read_csv(biology_path)



print(biology_df)