# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np

path = '/home/darshind/Workspace/code/python_intermediate_project/data/ipl_matches_small.csv'
read_ipl_data_csv = np.genfromtxt(path,delimiter=',',dtype='|S50',skip_header=1)

# Enter Code Here
def get_unique_teams_set():
    Count = np.unique(read_ipl_data_csv[:,3:5])
    

    return set(Count)
print get_unique_teams_set()
