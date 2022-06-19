"""data visualization"""

import csv
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('pomiary_2.csv', sep=';')

for x in range(1, 27):
    data[str(x)].plot(kind='hist')
    plt.show()

# to są histogramy dla każdego pomiaru 1 do 26, nie bierze pod uwagę typu gleby
