import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
%matplotlib inline


data = pd.read_csv('/Users/sachinprabhuram/Desktop/Data Analysis/LaLigaTable.csv')
data = data.iloc[::-1]

teamColours = ['#EF0107','#F5F5F5','#004D98','#D00027',
              '#0067B1', '#0BB363', '#FFE667', '#8AC3EE',
              '#A61B2B', '#EE2523', '#AD8F1F', '#fde607',
              '#D18816', '#B4053F', '#005999', '#0761AF',
               '#05642c', '#cf122d', '#921B88','#0C2D69'
              ]

plt.hlines(y=np.arange(1,21), xmin = 0, xmax = data['Pts'], color=teamColours)
plt.plot(data['Pts'], np.arange(1,21), "o")
plt.yticks(np.arange(1,21), data['Squad'])

plt.xlabel('Points')

plt.title('La Liga Table 20/21')
plt.savefig('LaLigaTableLollipop.png')
