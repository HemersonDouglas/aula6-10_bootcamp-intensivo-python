import pandas as pd

class CsvPorcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None

    def carregar_csv(self):
        self.df = pd.read_csv(self.file_path)

    def filtrar_por(self, coluna, atributo):
        return self.df[self.df[coluna] == atributo]

# Caminho do arquivo CSV
arquivo_csv = "./exemplo.csv"
filtro = 'estado'
limite = 'SP'

# Criando a instância da classe e carregando o arquivo
arquivo_CSV = CsvPorcessor(arquivo_csv)
arquivo_CSV.carregar_csv()

# Filtrando os dados e imprimindo o resultado
print(arquivo_CSV.filtrar_por(filtro, limite))


arquivo_csv2 = "./exemplo.csv"
filtro2 = 'estado'
limite2 = 'DF'

# Criando a instância da classe e carregando o arquivo
arquivo_csv2 = CsvPorcessor(arquivo_csv2)
arquivo_CSV.carregar_csv()

# Filtrando os dados e imprimindo o resultado
print(arquivo_CSV.filtrar_por(filtro2, limite2))