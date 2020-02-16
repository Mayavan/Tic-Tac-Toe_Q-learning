import numpy as np


data = np.genfromtxt('QTableMini.csv', delimiter=',')
data = np.zeros([6000, 10], dtype=float)
data[0][0] = 0.11111
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    data[0][i] = i
for i in range(5999):
    data[i+1][0] = 0.11
np.savetxt("QTableMini.csv", data, delimiter=",")
'''
from QTableDataHandler import DataHandler

ob = DataHandler()

print(ob.getRow(5.707299999999999596e-01))
'''
'''
a = [[6.69600000e+03, 9.00000000e-01, 6.68790000e+03, -1.00000000e+00,
      0.00000000e+00, 0.00000000e+00, 6.47190000e+03, 9.30690000e+03,
      - 1.00000000e+00, 0.00000000e+00]]
a=a[0][1:]
print(a)
'''