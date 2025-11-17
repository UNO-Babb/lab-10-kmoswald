#MapPlot.py
#Name:Kaitlyn Oswald
#Date:11/16/25
#Assignment: Lab 10


import coffee
import pandas
import matplotlib.pyplot as plt

coffee = coffee.get_coffee()


#print(coffee[0]["Data"]["Scores"]["Total"])
years = []
scores = []
for bean in coffee:
    year = bean["Year"]
    score = bean["Data"]["Scores"]["Total"]
    if score != 0:
        years.append(year)
        scores.append(score)
    #print(year,score)

df = pandas.DataFrame({"Year": years,
                       "Score": scores})


print(df)
df.plot(kind = 'scatter', x = 'Year', y = 'Score')

plt.savefig("output")
