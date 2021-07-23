import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

LLtable = pd.read_csv('/Users/sachinprabhuram/Desktop/Data Analysis/Data/LaLigaTable.csv')
Squad_list = LLtable["Squad"].to_list()

teamColours = ['#EF0107','#F5F5F5','#004D98','#D00027',
              '#0067B1', '#0BB363', '#FFE667', '#8AC3EE',
              '#A61B2B', '#EE2523', '#AD8F1F', '#fde607',
              '#D18816', '#B4053F', '#005999', '#0761AF',
               '#05642c', '#cf122d', '#921B88','#0C2D69'
              ]

fig, ax = plt.subplots() 

fig.set_size_inches(21,10)
ax.scatter(LLtable['GF'], LLtable['GA'], s=40, c=teamColours)
plt.plot([LLtable['GF'].mean(),LLtable['GF'].mean()],[90,20],'k-', linestyle = ":", lw=1)
plt.plot([20,90],[LLtable['GA'].mean(),LLtable['GA'].mean()],'k-', linestyle = ":", lw=1)

for i in range(LLtable.shape[0]):
     plt.text(x=LLtable.GF[i]+0.3,y=LLtable.GA[i]+0.3,s=LLtable.Squad[i], 
          fontdict=dict(color='red',size=9),
          bbox=dict(facecolor='yellow',alpha=0.2))
        
# Set chart title and label axes. 
plt.title(' La Liga Goals Scored vs Goals Conceded', fontsize=21) 
ax.set_xlabel('Goals Scored', fontsize=14) 
ax.set_ylabel('Goals Conceded', fontsize=14)
ax.spines['top'].set_color('white')
ax.spines['bottom'].set_color('white')

ax.text(18,90,"Poor attack, poor defense",color="red",size="12")
ax.text(75,20,"Strong attack, strong defense",color="red",size="12")
ax.text(18,20,"Poor attack, strong defense",color="red",size="12")
ax.text(75,90,"Strong attack, poor defense",color="red",size="12")

# Set scale of axes, and size of tick labels. 
ax.tick_params(axis='both', labelsize=14)

plt.savefig('LaLigaScatter2.png') 
