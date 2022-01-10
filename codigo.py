import numpy as np
import pandas as pd
import matplotlib.pyplot as plotar

dados2010 = pd.read_csv('C:/Users/Railson Martins/Documents/9 Período/Tópicos/Trabalho final/arquivos csv/chegadas_2010.csv', delimiter=';')
dados2011 = pd.read_csv('C:/Users/Railson Martins/Documents/9 Período/Tópicos/Trabalho final/arquivos csv/chegadas_2011.csv', delimiter=';')
dados2012 = pd.read_csv('C:/Users/Railson Martins/Documents/9 Período/Tópicos/Trabalho final/arquivos csv/chegadas_2012.csv', delimiter=';')
dados2013 = pd.read_csv('C:/Users/Railson Martins/Documents/9 Período/Tópicos/Trabalho final/arquivos csv/chegadas_2013.csv', delimiter=';')
dados2014 = pd.read_csv('C:/Users/Railson Martins/Documents/9 Período/Tópicos/Trabalho final/arquivos csv/chegadas_2014.csv', delimiter=';')
dados2015 = pd.read_csv('C:/Users/Railson Martins/Documents/9 Período/Tópicos/Trabalho final/arquivos csv/chegadas_2015.csv', delimiter=';')
dados2016 = pd.read_csv('C:/Users/Railson Martins/Documents/9 Período/Tópicos/Trabalho final/arquivos csv/chegadas_2016.csv', delimiter=';')
dados2017 = pd.read_csv('C:/Users/Railson Martins/Documents/9 Período/Tópicos/Trabalho final/arquivos csv/chegadas_2017.csv', delimiter=';')
dados2018 = pd.read_csv('C:/Users/Railson Martins/Documents/9 Período/Tópicos/Trabalho final/arquivos csv/chegadas_2018.csv', delimiter=';')
dados2019 = pd.read_csv('C:/Users/Railson Martins/Documents/9 Período/Tópicos/Trabalho final/arquivos csv/chegadas_2019.csv', delimiter=';')

relacaoColunas = {'cod continente':'Ordem continente', 'cod pais': 'Ordem país', 'ano':'Ano', 'cod via':'Ordem via de acesso', 'cod mes':'Ordem mês', 'cod uf':'Ordem UF', 'Via':'Via de acesso'}

dados2010 = dados2010.rename(columns = relacaoColunas) 
dados2011 = dados2011.rename(columns = relacaoColunas) 
dados2012 = dados2012.rename(columns = relacaoColunas) 
dados2013 = dados2013.rename(columns = relacaoColunas) 
dados2014 = dados2014.rename(columns = relacaoColunas) 
dados2015 = dados2015.rename(columns = relacaoColunas) 
dados2016 = dados2016.rename(columns = relacaoColunas) 
dados2017 = dados2017.rename(columns = relacaoColunas) 
dados2018 = dados2018.rename(columns = relacaoColunas) 
dados2019 = dados2019.rename(columns = relacaoColunas) 

dados = pd.concat([dados2010,dados2011,dados2012,dados2013,dados2014,dados2015,dados2016,dados2017,dados2018,dados2019])

dados = dados.drop(columns=['Unnamed: 12'])

def numChegEstado():
    Amazonas = dados[(dados['UF'] == 'Amazonas')]
    Amazonas = Amazonas['Chegadas']
    Amazonas = Amazonas.sum(axis=0)

    Bahia = dados[(dados['UF'] == 'Bahia')]
    Bahia = Bahia['Chegadas']
    Bahia = Bahia.sum(axis=0)

    Ceara = dados[(dados['UF'] == 'Ceará')]
    Ceara = Ceara['Chegadas']
    Ceara = Ceara.sum(axis=0)

    DF = dados[(dados['UF'] == 'Distrito Federal')]
    DF = DF['Chegadas']
    DF = DF.sum(axis=0)

    MG = dados[(dados['UF'] == 'Minas Gerais')]
    MG = MG['Chegadas']
    MG = MG.sum(axis=0)
    
    OUF = dados[(dados['UF'] == 'Outras Unidades da Federação')]
    OUF = OUF['Chegadas']
    OUF = OUF.sum(axis=0)

    Para = dados[(dados['UF'] == 'Pará')]
    Para = Para['Chegadas']
    Para = Para.sum(axis=0)

    Pernambuco = dados[(dados['UF'] == 'Pernambuco')]
    Pernambuco = Pernambuco['Chegadas']
    Pernambuco = Pernambuco.sum(axis=0)

    Parana = dados[(dados['UF'] == 'Parana')]
    Parana = Parana['Chegadas']
    Parana = Parana.sum(axis=0)

    Rio = dados[(dados['UF'] == 'Rio de Janeiro')]
    Rio = Rio['Chegadas']
    Rio = Rio.sum(axis=0)

    RioNorte = dados[(dados['UF'] == 'Rio Grande do Norte')]
    RioNorte = RioNorte['Chegadas']
    RioNorte = RioNorte.sum(axis=0)

    RioSul = dados[(dados['UF'] == 'Rio Grande do Sul')]
    RioSul = RioSul['Chegadas']
    RioSul = RioSul.sum(axis=0)

    SantaCatarina = dados[(dados['UF'] == 'Santa Catarina')]
    SantaCatarina = SantaCatarina['Chegadas']
    SantaCatarina = SantaCatarina.sum(axis=0)

    SaoPaulo = dados[(dados['UF'] == 'São Paulo')]
    SaoPaulo = SaoPaulo['Chegadas']
    SaoPaulo = SaoPaulo.sum(axis=0)

    MGS = dados[(dados['UF'] == 'Mato Grosso do Sul')]
    MGS = MGS['Chegadas']
    MGS = MGS.sum(axis=0)

    Acre = dados[(dados['UF'] == 'Acre')]
    Acre = Acre['Chegadas']
    Acre = Acre.sum(axis=0)

    Amapa = dados[(dados['UF'] == 'Amapá')]
    Amapa = Amapa['Chegadas']
    Amapa = Amapa.sum(axis=0)

    Roraima = dados[(dados['UF'] == 'Roraima')]
    Roraima = Roraima['Chegadas']
    Roraima = Roraima.sum(axis=0)

    estados = ['Amaz' ,'Ba' ,'Ce', 'DF' ,'MG',
    'OUF', 'Pará', 'Per' ,'Paraná',
    'Rio', 'RioNorte' ,'RioSul',
    'San', 'SP', 'MGS', 'Acr', 'Amap',
    'Ro']
    valores = [Amazonas, Bahia, Ceara, DF, MG, OUF, Para, Pernambuco, Parana, Rio, RioNorte, RioSul, SantaCatarina, SaoPaulo, MGS, Acre, Amapa, Roraima]

    plotar.plot(estados,valores)

    plotar.show()

def numChegViaAcesso():
    Aerea = dados[(dados['Via de acesso'] == 'Aérea')]
    Aerea = Aerea['Chegadas']
    Aerea = Aerea.sum(axis=0)

    Maritima = dados[(dados['Via de acesso'] == 'Marítima')]
    Maritima = Maritima['Chegadas']
    Maritima = Maritima.sum(axis=0)

    Terrestre = dados[(dados['Via de acesso'] == 'Terrestre')]
    Terrestre = Terrestre['Chegadas']
    Terrestre = Terrestre.sum(axis=0)

    Fluvial = dados[(dados['Via de acesso'] == 'Fluvial')]
    Fluvial = Fluvial['Chegadas']
    Fluvial = Fluvial.sum(axis=0)

    viaAcesso = ['Aerea', 'Maritima', 'Terrestre', 'Fluvial']
    valores = [Aerea, Maritima, Terrestre, Fluvial]

    plotar.plot(viaAcesso, valores)

    plotar.show()


#Número de chegadas em relação aos meses
def numChegMes():
    
    #Número de chegadas no mes de janeiro
    janeiro = dados[(dados['Mês'] == 'janeiro')]
    janeiro = janeiro['Chegadas']
    janeiro = janeiro.sum(axis=0)

    print(janeiro)

    #Número de chegadas no mes de fevereiro
    fevereiro = dados[(dados['Mês'] == 'fevereiro')]
    fevereiro = fevereiro['Chegadas']
    fevereiro = fevereiro.sum(axis=0)

    #Número de chegadas no mes de março
    marco = dados[(dados['Mês'] == 'março')]
    marco = marco['Chegadas']
    marco = marco.sum(axis=0)

    #Número de chegadas no mes de abril
    abril = dados[(dados['Mês'] == 'abril')]
    abril = abril['Chegadas']
    abril = abril.sum(axis=0)

    #Número de chegadas no mes de maio
    maio = dados[(dados['Mês'] == 'maio')]
    maio = maio['Chegadas']
    maio = maio.sum(axis=0)

    #Número de chegadas no mes de junho
    junho = dados[(dados['Mês'] == 'junho')]
    junho = junho['Chegadas']
    junho = junho.sum(axis=0)

    #Número de chegadas no mes de julho
    julho = dados[(dados['Mês'] == 'julho')]
    julho = julho['Chegadas']
    julho = julho.sum(axis=0)

    #Número de chegadas no mes de agosto
    agosto = dados[(dados['Mês'] == 'agosto')]
    agosto = agosto['Chegadas']
    agosto = agosto.sum(axis=0)

    #Número de chegadas no mes de setembro
    setembro = dados[(dados['Mês'] == 'setembro')]
    setembro = setembro['Chegadas']
    setembro = setembro.sum(axis=0)

    #Número de chegadas no mes de outubro
    outubro = dados[(dados['Mês'] == 'outubro')]
    outubro = outubro['Chegadas']
    outubro = outubro.sum(axis=0)

    #Número de chegadas no mes de novembro
    novembro = dados[(dados['Mês'] == 'outubro')]
    novembro = novembro['Chegadas']
    novembro = novembro.sum(axis=0)

    #Número de chegadas no mes de dezembro
    dezembro = dados[(dados['Mês'] == 'dezembro')]
    dezembro = dezembro['Chegadas']
    dezembro = dezembro.sum(axis=0)

    meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
    valores = [janeiro, fevereiro, marco, abril, maio, junho, julho, agosto, setembro, outubro, novembro, dezembro]

    plotar.plot(meses,valores)

    plotar.show()

numChegMes()
numChegEstado()
numChegViaAcesso()