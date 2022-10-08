import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

# ler a base de dados
turbina = pd.read_csv('T1.csv')
turbina.columns = ['Data/Hora','Potencia_ativa(kW)','velocidade_vento(m/s)','Curva_Teórica(kwh)','Direção_vento(°)'] # alterando o nome das colunas da tabela de dados
del turbina['Direção_vento(°)'] # deletando a coluna da direção dos ventos
turbina['Data/Hora'] = pd.to_datetime(turbina['Data/Hora'])
print(turbina)

# plotando o grafico dos dados reais da turbina
fig = sns.scatterplot(data= turbina,x = 'velocidade_vento(m/s)', y = 'Potencia_ativa(kW)')
fig.plot()
plt.show()

# plotando curva teorica do gerador
fig2 = sns.scatterplot(data= turbina,x = 'velocidade_vento(m/s)', y = 'Curva_Teórica(kwh)')
fig2.plot()
plt.show()

# criando limites para a potencia
pot_real = turbina['Potencia_ativa(kW)'].tolist()
pot_teorica = turbina['Curva_Teórica(kwh)'].tolist()
pot_max = []
pot_min = []
dentro_lim = []

for p in pot_teorica:
    pot_max.append(p*1.05)
    pot_min.append(p*0.95)

for i,pot in enumerate(pot_real):
    if pot >= pot_min[i] and pot<=pot_max[i]:
        dentro_lim.append('Dentro')
    elif pot == 0:
        dentro_lim.append('Zero')
    else:
        dentro_lim.append('Fora')

print('\n','O percentual de valores dentro dos limites de potência é {:.2f}%'.format(dentro_lim.count('Dentro')/len(dentro_lim)*100),'\n')

turbina['Dentro_limite'] = dentro_lim
print(turbina)

cores = {'Dentro':'blue','Zero':'orange','Fora':'red'}
fig3 = sns.scatterplot(data= turbina,x = 'velocidade_vento(m/s)', y = 'Potencia_ativa(kW)',hue ='Dentro_limite',s=1, palette=cores)
fig3.plot()
plt.show()