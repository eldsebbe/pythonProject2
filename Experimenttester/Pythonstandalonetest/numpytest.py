import time
import numpy as np
import sys


dataset_digits = 8  #Scales exponentionally

dataset_size = 10 ** dataset_digits

# Generates with traditional python and numpy method
python_list= [1] * dataset_size
numpy_array = np.ones(dataset_size)

# Measure python time for multiplying each value by 1024
time_start = time.time()
python_list = [x * 1024 for x in python_list]

time_py = time.time() - time_start
py_size = sys.getsizeof(python_list) / 1000 #Size in mb
#print(python_list[:10])     #Data sample


#Measure numpy time for multiplying each value by 1024
numpy_array = numpy_array * 1024

time_np = time.time() - time_start
np_size = sys.getsizeof(numpy_array)/1000 #size in mb
#print(numpy_array[:10]) #data sample


print(f"Python computation time: {time_py}s")
print(f"Numpy computation time: {time_np}s")
print(f"Python list size: {py_size}mb")
print(f"Numpy list size: {np_size}mb")