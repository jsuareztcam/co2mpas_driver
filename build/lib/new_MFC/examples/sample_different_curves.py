import os
import numpy as np
import matplotlib.pyplot as plt
from new_MFC.common import curve_functions as mf
from new_MFC.common import reading_n_organizing as rno


def simple_run(db_name):
    # Database of vehicles with a unique id
    # db_name = '../db/EuroSegmentCar'
    car_id = 39393
    gs_style = 0.8  # gear shifting can take value from 0(timid driver)
    degree = 2

    # file path without extension of the file
    db_name = os.path.dirname(db_name) + '/' + \
              os.path.splitext(os.path.basename(db_name))[0]

    db = rno.load_db_to_dictionary(db_name)
    selected_car = rno.get_vehicle_from_db(db, car_id)

    curves, cs_acc_per_gear, start_stop, gs = mf.gear_curves_n_gs_from_poly(
        selected_car, gs_style, degree)

    for gear, curve in enumerate(curves):
        start = start_stop[0][gear]
        stop = min(start_stop[1][gear], 50)
        x = np.arange(start, stop, 1)
        y = curve(x)
        plt.plot(x, y)
    plt.show()

    return 0


if __name__ == '__main__':
    simple_run()