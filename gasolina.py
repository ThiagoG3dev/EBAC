import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./gasolina.csv')

df['venda'].plot()
plt.xlabel('!DIA!')
plt.ylabel('!PREÇO!')
plt.title('Preço da Gasolina:')

plt.savefig('precogasolina.png', format='png')