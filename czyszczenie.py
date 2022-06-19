"""clearing data"""

from numpy import genfromtxt
import numpy as np
from numpy import savetxt

my_data = genfromtxt('wszystkie_pomiary.csv', delimiter=';')
# print(my_data)

my_data_del_first_row = np.delete(my_data, 0, 0)
my_data_del_last_col = np.delete(my_data_del_first_row, 26, 1)
# print(my_data_del_last_col)

data_mean = np.mean(my_data_del_last_col, 0)
# print(data_mean)

bonzai = my_data_del_last_col[0::4][:]
universal = my_data_del_last_col[1::4][:]
palm = my_data_del_last_col[2::4][:]
herbs = my_data_del_last_col[3::4][:]

bonzai_mean = np.mean(bonzai, 0)
universal_mean = np.mean(universal, 0)
palm_mean = np.mean(palm, 0)
herbs_mean = np.mean(herbs, 0)

# print(bonzai_mean)
# print(universal_mean)
# print(palm_mean)
# print(herbs_mean)

bonzai_std = np.std(bonzai, 0)
universal_std = np.std(universal, 0)
palm_std = np.std(palm, 0)
herbs_std = np.std(herbs, 0)

# print("Odchylenie standardowe: ")
# print(bonzai_std)
# print(universal_std)
# print(palm_std)
# print(herbs_std)

bonzai_var = np.var(bonzai, 0)
universal_var = np.var(universal, 0)
palm_var = np.var(palm, 0)
herbs_var = np.var(herbs, 0)

bonzai_sig = np.sqrt(bonzai_var)
universal_sig = np.sqrt(universal_var)
palm_sig = np.sqrt(palm_var)
herbs_sig = np.sqrt(herbs_var)

# print(bonzai_sig)
# print(universal_sig)
# print(palm_sig)
# print(herbs_sig)

# bonzai_max = np.amax(bonzai, 0)
# universal_max = np.amax(universal, 0)
# palm_max = np.amax(palm, 0)
# herbs_max = np.amax(herbs, 0)
#
# bonzai_min = np.amin(bonzai, 0)
# universal_min = np.amin(universal, 0)
# palm_min = np.amin(palm, 0)
# herbs_min = np.amin(herbs, 0)
#
# print("--------")
# print(bonzai_max)
# print(universal_max)
# print(palm_max)
# print(herbs_max)
#
# print("--------")
# print(bonzai_min)
# print(universal_min)
# print(palm_min)
# print(herbs_min)
#
# print(bonzai.shape)
# print(universal.shape)
# print(palm.shape)
# print(herbs.shape)

sigma_multiplayer = 3

for i in range(0, 26):
    bonzai = bonzai[bonzai[:, i] < (bonzai_mean[i] + sigma_multiplayer * bonzai_sig[i])]
    universal = universal[universal[:, i] < (universal_mean[i] + sigma_multiplayer * universal_sig[i])]
    palm = palm[palm[:, i] < (palm_mean[i] + sigma_multiplayer * palm_sig[i])]
    herbs = herbs[herbs[:, i] < (herbs_mean[i] + sigma_multiplayer * herbs_sig[i])]

for i in range(0, 26):
    bonzai = bonzai[bonzai[:, i] > (bonzai_mean[i] - sigma_multiplayer * bonzai_sig[i])]
    universal = universal[universal[:, i] > (universal_mean[i] - sigma_multiplayer * universal_sig[i])]
    palm = palm[palm[:, i] > (palm_mean[i] - sigma_multiplayer * palm_sig[i])]
    herbs = herbs[herbs[:, i] > (herbs_mean[i] - sigma_multiplayer * herbs_sig[i])]

# print(bonzai.shape)
# print(universal.shape)
# print(palm.shape)
# print(herbs.shape)


bonzai = np.c_[bonzai, np.full((bonzai.shape[0], 1), 0)]
universal = np.c_[universal[:], np.full((universal.shape[0], 1), 1)]
palm = np.c_[palm[:], np.full((palm.shape[0], 1), 2)]
herbs = np.c_[herbs[:], np.full((herbs.shape[0], 1), 3)]


cleaned_data = np.concatenate((bonzai, universal, palm, herbs))
cleaned_data = cleaned_data.astype(int)
# print(cleaned_data)

np.random.shuffle(cleaned_data)

savetxt('cleaned_data.csv', cleaned_data, delimiter=';', fmt='%d')