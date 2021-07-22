# Top Goalscorers plot

import squarify
import matplotlib as mpt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
%matplotlib qt

data = pd.read_csv('/Users/sachinprabhuram/Desktop/Data Analysis/Data/Barcadetails.csv')

Goalsdata = data[data["Gls"]>0]
normalized = mpt.colors.Normalize(vmin=min(Goalsdata.Gls), vmax=max(Goalsdata.Gls))
colors = [mpt.cm.Blues(normalized(value)) for value in Goalsdata.Gls]

fig = mpt.pyplot.gcf()
ax = fig.add_subplot()
squarify.plot(label=Goalsdata.Player,sizes=Goalsdata.Gls, color = colors, alpha=.6)
fig.set_size_inches(12, 8)
plt.title("Barcelona Goals contributions",fontsize=21,fontweight="bold")
plt.axis('off')

plt.show()

# Top Assisters Plot

import squarify
import matplotlib as mpt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
%matplotlib qt

data = pd.read_csv('/Users/sachinprabhuram/Desktop/Data Analysis/Data/Barcadetails.csv')

AssistData = data[data["Ast"]>0]

normalized = mpt.colors.Normalize(vmin=min(AssistData.Ast), vmax=max(AssistData.Ast))
colors = [mpt.cm.Reds(normalized(value)) for value in AssistData.Ast]

fig = mpt.pyplot.gcf()
ax = fig.add_subplot()
squarify.plot(label=AssistData.Player,sizes=AssistData.Ast, color = colors, alpha=.6)
fig.set_size_inches(12, 8)
plt.title("Barcelona Assist contributions",fontsize=21,fontweight="bold")
plt.axis('off')

plt.show()
