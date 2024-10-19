import pandas as pd 
import numpy as np 

# como na plataforma não tem como importar um arquivo, vou ter que simular um
with open('Academy_Candidates.txt', 'w') as file:
    file.write('Wagner;Desenvolvedor Back-end;34;Pará\n')
    file.write('Lorena;Desenvolvedor Front-end;29;Pará\n')
    file.write('Paula;Analista de Qualidade;25;Santa Catarina\n')
    file.write('ana;Analista de Qualidade;25;Santa Catarina\n')
    file.write('Jeovane;Data Scientist;30;Pará\n')
    file.write('Marcela;DevOps Engineer;28;Rio de Janeiro\n')
    file.write('Carlos;Desenvolvedor Back-end;35;Bahia\n')
    file.write('Fernanda;Analista de Qualidade;26;Paraná\n')
    file.write('Pedro;Engenheiro de Dados;32;Santa Catarina\n')
    file.write('Beatriz;Desenvolvedor Front-end;24;Distrito Federal\n')
    file.write('Rafaela;Administradora de Sistemas;29;Pernambuco\n')
    file.write('Lucas Costa;Mobile;30;Piauí\n')

#lendo o arquivo "Academy_Candidates.txt"
df = pd.read_csv('Academy_Candidatos.txt', sep=';', header=None, names=['Nome', 'Vaga', 'Idade', 'Estado'])

#percentual de candidatos por vagas
vaga_porcentagem = df['Vaga'].value_counts(normalize=True)*100
print("Proporção de candidatos por vaga (porcentagem):\n", vaga_porcentagem)

#idade média dos candidatos por Vaga
idade_media_por_vaga = df.groupby('Vaga')['Idade'].mean()
print("\nIdade média dos candidatos por vaga:\n", idade_media_por_vaga)

#idade do candidato mais velho inscrito em cada vaga
idade_mais_velho_por_vaga = df.groupby('Vaga').agg({'Idade': 'max', 'Nome':'first'})
print("\nIdade do candidato mais velho por vaga:\n", idade_mais_velho_por_vaga)

#idade do candidato mais novo inscrito em cada vaga
idade_mais_novo_por_vaga = df.groupby('Vaga').agg({'Idade': 'min', 'Nome': 'first'})
print("\nIdade do candidato mais novo por vaga:\n", idade_mais_novo_por_vaga)

#soma das idades de todos os candidatos por vaga
soma_idade_por_vaga = df.groupby('Vaga')['Idade'].sum()
print("\nSoma das idades dos candidatos por vaga:\n", soma_idade_por_vaga)

#Numeros de Estados Distintos
estados_distintos = df['Estado'].nunique()
print("\nNúmero de estados distintos entre os candidatos:", estados_distintos)

#criando um arquivo csv
df_sorted = df.sort_values(by='Nome')
df_sorted.to_csv('Sorted_Academy_Candidates.csv', index=False)
print("\nArquivo 'Sorted_Academy_Candidates.csv' foi criado.")


# Descobrir o instrutor de QA
qa_candidatos = df[(df['Vaga'] == 'Analista de Qualidade') & (df['Estado'] == 'Santa Catarina')].copy()
qa_candidatos.loc[:, 'Quadrado_Perfeito'] = qa_candidatos['Idade'].apply(lambda x: np.sqrt(x).is_integer())

# Verificar se o primeiro nome é um palíndromo
qa_instrutor = qa_candidatos[
    qa_candidatos['Quadrado_Perfeito'] & 
    qa_candidatos['Nome'].apply(lambda x: x.split()[0] == x.split()[0][::-1])
]
print("\nNome do instrutor de QA descoberto:\n", qa_instrutor['Nome'].values[0] if not qa_instrutor.empty else 'Nenhum encontrado')

# Descobrir o instrutor de Mobile com base nas pistas
mobile_candidatos = df[(df['Vaga'] == 'Mobile') & (df['Estado'] == 'Piauí')].copy()
mobile_candidatos.loc[:, 'Idade_Par'] = mobile_candidatos['Idade'].apply(lambda x: x % 2 == 0)

# Verificação se o nome contém pelo menos dois componentes (primeiro e sobrenome)
mobile_instrutor = mobile_candidatos[
    mobile_candidatos['Idade_Par'] & 
    mobile_candidatos['Nome'].apply(lambda x: len(x.split()) > 1 and x.split()[1].startswith('C'))
]
print("\nNome do instrutor de Mobile descoberto:\n", mobile_instrutor['Nome'].values[0] if not mobile_instrutor.empty else 'Nenhum encontrado')
