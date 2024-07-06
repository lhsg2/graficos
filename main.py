import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Categoria':['População Total','Celulares','Usuários de Internet','Usuários de Redes Sociais'],
    'Quantidade(bilhões)': [8.08,5.61,5.35,5.04]
}
df = pd.DataFrame(data)
plt.figure(figsize=(10,6))
plt.bar(df['Categoria'],df['Quantidade(bilhões)'],color=['purple','yellow','orange','red'])
plt.xlabel('Categoria')
plt.ylabel('Quantidade(bilhões)')
plt.title('Dados Globais')
plt.ylim(0,9)

for i,value in enumerate(df['Quantidade(bilhões)']):
  plt.text(i,value+0.2,f'{value}B',ha='center')
  
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()