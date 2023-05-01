import numpy as np
import os

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
speed_measurement_path = CURR_DIR_PATH + "/03-speed_measurements.txt"

#speed_data = np.genfromtxt(speed_measurement_path, delimiter=",")

speed_data = np.genfromtxt(
    speed_measurement_path,
    delimiter=",",
    dtype="str",
    autostrip=True
)

speed_list = np.array(speed_data[:,0], dtype=float)
plate_list = np.array(speed_data[:,1])
color_list = np.array(speed_data[:,2])
time_list = np.array(speed_data[:,3])

SPEED_LIMIT = 50

speedster_count= np.count_nonzero(speed_list > SPEED_LIMIT)
#print(f"{speedster_count} out of {speed_list.size} are speeding")

speeder_list = speed_data[np.where(speed_list > (SPEED_LIMIT + 2))]
#print(speeder_list)

c_uniques,c_count = np.unique(color_list, return_counts=True)

for color, count in zip(c_uniques, c_count):
    print(f"{color}: {count}")





