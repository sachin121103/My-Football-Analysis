from matplotlib import pyplot as plt
%matplotlib qt

wins = [13, 7, 6, 6, 5]
teams = ['Real Madrid', 'AC Milan', 'Liverpool', 'Bayern Munich', 'Barcelona']
colors = ['#FEBE10', '#FB090B', '#C8102E', '#DC052D', '#004D98']

def autopct_format(values):
    def my_format(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{v:d}'.format(v=val)
    return my_format
  
plt.style.use('fivethirtyeight')

plt.pie(wins, labels=teams, autopct=autopct_format(wins), colors=colors,
        shadow=True, startangle=90,wedgeprops={'edgecolor':'black'})
plt.title("Champions League Winners")
plt.show()
