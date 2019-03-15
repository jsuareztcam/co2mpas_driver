import generic_co2mpas as lco
import matplotlib.pyplot as plt
import reading_n_organizing as rno
import curve_functions as mf

db_name = '../db/EuroSegmentCar'
car_id = 35135

db = rno.load_db_to_dictionary(db_name)

my_car = rno.get_vehicle_from_db(db, car_id, lco = True)

# Curves, cs_acc_per_gear, StartStop = mf.gear_curves(my_car)

sp = [0.075647222, 0.138130556, 0.165027778, 0.093338889, 0.050647222, 0.073841667, 0.067722222, 0.041172222,
      0.094272222, 0.240147222, 0.421988889, 0.601022222, 0.805477778, 1.067511111, 1.360083333, 1.650283333, 1.913175,
      2.176333333, 2.444797222, 2.700288889, 2.946313889, 3.189297222, 3.448358333, 3.704702778, 3.940416667,
      4.130133333, 4.260580556, 4.3409, 4.388002778, 4.426941667, 4.455319444, 4.476166667, 4.515033333, 4.539722222,
      4.54225, 4.563194444, 4.616366667, 4.794819444, 4.925277778, 5.010258333, 5.270727778, 5.526880556, 5.698258333,
      5.863777778, 6.025444444, 6.178002778, 6.320294444, 6.455533333, 6.586655556, 6.7208, 6.850394444, 6.973597222,
      7.076808333, 7.125569444, 7.125688889, 7.095327778, 7.045141667, 6.987052778, 6.942780556, 6.943469444,
      6.972669444, 6.987636111, 6.995147222, 7.01125, 7.034722222, 7.064722222, 7.095263889, 7.144930556, 7.228544444,
      7.351388889, 7.516902778, 7.705436111, 7.912636111, 8.142141667, 8.384738889, 8.638480556, 8.896288889,
      9.157808333, 9.427988889, 9.695, 9.931672222, 10.09765, 10.17970556, 10.211575, 10.22029444, 10.21634444,
      10.22308056, 10.25685278, 10.32316667, 10.43054444, 10.55200833, 10.67687222, 10.81433889, 10.94932778,
      11.08748889, 11.23079444, 11.37732778, 11.52675278, 11.67602222, 11.83357778, 11.99132222, 12.127225, 12.217525,
      12.27826111, 12.33689444, 12.41279167, 12.52231944, 12.648375, 12.78034722, 12.91521111, 13.04194444, 13.16066111,
      13.28333333, 13.40571944, 13.53175556, 13.64644444, 13.75571111, 13.8666, 13.93222222, 13.95751111, 13.96354444,
      13.95462222, 13.92623333, 13.89566111, 13.88161111, 13.90078611, 13.92424167, 13.95039722, 13.98454444,
      14.02729722, 14.07866111, 14.15, 14.24663333, 14.3537, 14.45984444, 14.58112778, 14.7043, 14.83035556,
      14.96040278, 15.09104722, 15.22573889, 15.36123611, 15.49455833, 15.63419444, 15.77003889, 15.90303333,
      16.04134167, 16.17628056, 16.30461111, 16.4286, 16.54910556, 16.66977778, 16.77255278, 16.85622222, 16.94144444,
      17.02344444, 17.09977778, 17.17553056, 17.24705278, 17.31889444, 17.39001389, 17.44721389]
gs = [5.715589018826222, 10.974960637586783, 16.396951475513028, 22.832902038337586]
sim_step = 0.1

fp = lco.light_co2mpas_series(my_car, sp, gs, sim_step)

plt.plot(fp)
# plt.plot(fp2)
plt.show()

# print(fp)
#
# plt.plot(fp)
# plt.plot(sp)
# plt.show()
