"""clearing data"""

from numpy import genfromtxt
import numpy as np
import matplotlib.pyplot as plt
from numpy import savetxt

# my_data = genfromtxt('pomiary_2_sigma.csv', delimiter=';')
my_data = genfromtxt('pomiary_2_sigma_test_set.csv', delimiter=';')

bonzai = []
universal = []
palm = []
herbs = []

for row in my_data:
    if row[26] == 0:
        bonzai.append(row)
    if row[26] == 1:
        universal.append(row)
    if row[26] == 2:
        palm.append(row)
    if row[26] == 3:
        herbs.append(row)

bonzai = np.array(bonzai)
universal = np.array(universal)
palm = np.array(palm)
herbs = np.array(herbs)

bonzai = np.delete(bonzai, 26, 1)
universal = np.delete(universal, 26, 1)
palm = np.delete(palm, 26, 1)
herbs = np.delete(herbs, 26, 1)

bonzai_mean = []
universal_mean = []
palm_mean = []
herbs_mean = []

bonzai_mean = np.array(bonzai_mean)
universal_mean = np.array(universal_mean)
palm_mean = np.array(palm_mean)
herbs_mean = np.array(herbs_mean)

for i in range(0, 26):
    bonzai_mean = np.append(bonzai_mean, np.mean(bonzai[:, i]))
    universal_mean = np.append(universal_mean, np.mean(universal[:, i]))
    palm_mean = np.append(palm_mean, np.mean(palm[:, i]))
    herbs_mean = np.append(herbs_mean, np.mean(herbs[:, i]))

x_axis = list(range(0, 26))

# TYLKO ŚREDNIE
plt.plot(x_axis, bonzai_mean, label="do bonzai")
plt.plot(x_axis, universal_mean, label="uniwersalna")
plt.plot(x_axis, palm_mean, label="do palm")
plt.plot(x_axis, herbs_mean, label="do ziół")

# WSZYSTKIE POMIARY
# for i in range(len(bonzai)):
#     plt.plot(x_axis, bonzai[i], color='green')
#
# for i in range(len(universal)):
#     plt.plot(x_axis, universal[i], color='yellow')
#
# for i in range(len(palm)):
#     plt.plot(x_axis, palm[i], color='red')
#
# for i in range(len(herbs)):
#     plt.plot(x_axis, herbs[i], color='blue')

plt.xlabel('godzina pomiaru')
plt.ylabel('wartość pomiaru')
plt.title('Średnie charakterystyki wysychania gleb')
plt.legend()

plt.show()
