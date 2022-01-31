import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

site = requests.get("https://www.otempo.com.br/tempo/medianeira-pr")
soup = BeautifulSoup(site.content,"html.parser")#analisar a pagina em html
#dias da semana
dias_semana = soup.find_all(class_ = 'cell nome-dia')
dias_semana = [(d.getText()).strip() for d in dias_semana]
dias_semana[0] = "Hoje"
#temperaturas por dia da semana
min_max = soup.find_all(class_ = 'graus')
min_max = [t.getText() for t in min_max]
#chance de chuva por dia da semana
chance_chuva = soup.find_all(class_ = 'cell porcentagem')
chance_chuva = [t.getText() for t in chance_chuva]
#formata os dados para criar a tabela
tabela = ({"Dia da semana":[i for i in dias_semana],"Temperatura máxima e mínima":[i for i in min_max],"Chance de chuva":[i for i in chance_chuva]})
#formata os dados em uma tabela bonita 
print(tabulate(tabela,headers="keys",tablefmt="pretty"))
