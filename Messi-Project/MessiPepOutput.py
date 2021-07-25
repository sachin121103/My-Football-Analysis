colors = ['#EDBB00', '#004D98', '#A50044', '#DB0030']
seasons = ['2008/09', '2009/10', '2010/11', '2011/12']

goals_per_90 = [0.84, 1.00, 0.99, 1.35]
assists_per_90 = [0.42, 0.21, 0.51, 0.44]
SOT_per_90 = [1.78, 3.18, 2.54, 3.19]
dribbles_per_90 = [7.0, 7.2, 7.2, 6.8]

fig, ax = plt.subplots(2, 2, sharex='col', sharey='row')

fig.set_size_inches(18.5, 10.5)

ax[0,0].barh(seasons, goals_per_90, color=colors[0])
ax[0,1].barh(seasons, SOT_per_90, color=colors[1])
ax[1,0].barh(seasons, assists_per_90, color=colors[2])
ax[1,1].barh(seasons, dribbles_per_90, color=colors[3])

ax[0,0].tick_params(labelbottom=True)
ax[0,1].tick_params(labelbottom=True)
ax[0,1].tick_params(labelleft=True)
ax[1,1].tick_params(labelleft=True)

ax[0, 0].text(0.7, 3.8, "Goals per 90", ha='center', fontsize=16)
ax[0, 1].text(4, 3.8, "Shots on Target per 90", ha='center', fontsize=16)
ax[1, 0].text(0.7, 3.8, "Assists per 90", ha='center', fontsize=16)
ax[1, 1].text(4, 3.8, "Dribbles per 90", ha='center', fontsize=16)

plt.show()
