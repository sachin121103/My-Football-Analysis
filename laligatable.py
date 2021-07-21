#Import Modules

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
%matplotlib qt
from collections import Counter

# Read Data

data = pd.read_csv('LaLigaTable.csv')

squad = data['Squad']
pts = data['Pts']

squads = list(squad)
squads.reverse()

points = list(pts)
points.reverse()

# Team Colours

teamColours = ['#EF0107','#F5F5F5','#004D98','#D00027',
              '#0067B1', '#0BB363', '#FFE667', '#8AC3EE',
              '#A61B2B', '#EE2523', '#AD8F1F', '#fde607',
              '#D18816', '#B4053F', '#005999', '#0761AF',
               '#05642c', '#cf122d', '#921B88','#0C2D69'
              ]

teamColours.reverse()

#Plot data

plt.style.use('ggplot')
plt.title("La Liga 20/21 Table")
plt.xlabel("Points", fontsize=14)


plt.barh(squads, points, color=teamColours)
plt.ylim(-1, 21)

plt.rcParams['figure.figsize'] = [15, 10]

plt.grid(True)

plt.show()
