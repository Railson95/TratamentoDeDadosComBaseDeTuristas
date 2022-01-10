import pandas as pd
import matplotlib.pyplot as plotar

df = pd.DataFrame({'Aluno' : ["Wilfred", "Abbie", "Harry", "Julia", "Carrie"],
                   'Faltas' : [3,4,2,1,4],
                   'Prova' : [2,7,5,10,6],
                   'Seminário': [8.5,7.5,9.0,7.5,8.0]})

print(df.head())

df["Faltas"].value_counts().plot.bar()

plotar.show()