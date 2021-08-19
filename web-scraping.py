from bs4 import BeautifulSoup
import requests

# faz uma requisição do tipo get e atruibui o conteúdo da página à variável
# page = requests.get("https://www.climatempo.com.br/brasil").content  # nova versão do site retorna campos em branco
page = requests.get("https://www.climadobrasil.com.br/").content

# cria objeto da classe BeautifulSoup e passa como parâmetro o conteúdo da página e seu tipo
soup = BeautifulSoup(page, "html.parser")
# print(soup.prettify())

# o request não retornou o resultado desejado, então... usando o BS para coletar todos os links da página
with open("links.csv", "w+") as links_file:
    for link in soup.find_all("a"):
        href = str(link.get("href"))
        if href[:4] == "http":
            links_file.write(href + "\n")
            print(href)
    
