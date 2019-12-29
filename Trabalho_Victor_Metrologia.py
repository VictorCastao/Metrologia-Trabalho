#Victor Gabriel Castão da Cruz - 11911ECP004
#Trabalho Metrologia

#Bibliotecas
import matplotlib.pyplot as plot
import statistics as stat
import math
import csv

#Dicionario com valores t de Student
TStudent = {
    1:[1.837,12.706,13.968,63.656,235.811],
    2:[1.321,4.303,4.527,9.925,19.206],
    3:[1.197,3.182,3.307,5.841,9.219],
    4:[1.142,2.776,2.869,4.604,6.620],
    5:[1.111,2.571,2.649,4.032,5.507],
    6:[1.091,2.447,2.517,3.707,4.904],
    7:[1.077,2.365,2.429,3.499,4.530],
    8:[1.067,2.306,2.366,3.355,4.277],
    9:[1.059,2.262,2.320,3.250,4.094],
    10:[1.053,2.228,2.284,3.169,3.957],
    11:[1.048,2.201,2.255,3.106,3.850],
    12:[1.043,2.179,2.231,3.055,3.764],
    13:[1.040,2.160,2.212,3.012,3.694],
    14:[1.037,2.145,2.195,2.977,3.636],
    15:[1.034,2.131,2.181,2.947,3.586],
    16:[1.032,2.120,2.169,2.921,3.544],
    17:[1.030,2.110,2.158,2.898,3.507],
    18:[1.029,2.101,2.149,2.878,3.475],
    19:[1.027,2.093,2.140,2.861,3.447],
    20:[1.026,2.086,2.133,2.845,3.422],
    25:[1.020,2.060,2.105,2.787,3.330],
    30:[1.017,2.042,2.087,2.750,3.270],
    35:[1.014,2.030,2.074,2.724,3.229],
    40:[1.013,2.021,2.064,2.704,3.199],
    50:[1.010,2.009,2.051,2.678,3.157],
    60:[1.008,2.000,2.043,2.660,3.130],
    70:[1.007,1.994,2.036,2.648,3.111],
    80:[1.006,1.990,2.032,2.639,3.097],
    90:[1.006,1.987,2.028,2.632,3.086],
    100:[1.005,1.984,2.025,2.626,3.077],
    150:[1.003,1.976,2.017,2.609,3.051],
    200:[1.003,1.972,2.013,2.601,3.038],
    1000:[1.000,1.962,2.003,2.581,3.008],
    10000:[1.000,1.960,2.000,2.576,3.001],
    100000:[1.000,1.960,2.000,2.576,3.000],
    }

##Variáveis utilizadas inicialmente
Casas_Decimais = 0
Precisao_Desejada = 0
Indicacoes = ()
Tipo_Medicao = 0
Tipo_Valores = 0
Correlacao = 0
Operacao = 0




##Funções a serem utilizadas
def Histograma(lista,intervalos,titulo,eixox,eixoy):
    plot.hist(lista, ec = "k", bins = intervalos)
    plot.title(titulo)
    plot.xlabel(eixox)
    plot.ylabel(eixoy)
    plot.savefig('./'+titulo+'.png')
    plot.close()

def achart(graus,precisao):
    retorno = 1
    p = 0
    g = 0
    if precisao == 68.27:
        p = 0
    if precisao == 95.00:
        p = 1
    if precisao == 95.45:
        p = 2
    if precisao == 99.00:
        p = 3
    if precisao == 99.73:
        p = 4
    if graus <= 20:
        g = graus
    if (graus > 20) and (graus < 25):
        g = 20
    if (graus >= 25) and (graus < 30):
        g = 25
    if (graus >= 30) and (graus < 35):
        g = 30
    if (graus >= 35) and (graus < 40):
        g = 35
    if (graus >= 40) and (graus < 50):
        g = 40
    if (graus >= 50) and (graus < 60):
        g = 50
    if (graus >= 60) and (graus < 70):
        g = 60
    if (graus >= 70) and (graus < 80):
        g = 70
    if (graus >= 80) and (graus < 90):
        g = 80
    if (graus >= 90) and (graus < 100):
        g = 90
    if (graus >= 100) and (graus < 150):
        g = 100
    if (graus >= 150) and (graus < 200):
        g = 150
    if (graus >= 200) and (graus < 1000):
        g = 200
    if (graus >= 1000) and (graus < 10000):
        g = 1000
    if (graus >= 10000) and (graus < 100000):
        g = 10000
    if (graus >= 100000):
        g = 100000
    retorno = TStudent[g][p]
    return retorno
    

def Media (indicacoes):
    resultado = stat.mean(indicacoes)
    return resultado


def Incerteza_Padrao (indicacoes):
    resultado = stat.stdev(indicacoes)
    return resultado


def Graus_de_Liberdade (indicacoes):
    resultado = len(indicacoes) - 1
    return resultado


def inc_comb_soma_e_sub (indicacao1,indicacao2):
    u1 = Incerteza_Padrao(indicacao1)
    u2 = Incerteza_Padrao(indicacao2)
    soma = math.sqrt((math.pow(u1,2))+(math.pow(u2,2)))
    return soma


def MIENC(indic,vv,alg,prob):
    n = int (input("Informe o número de fontes de incerteza presentes: "))
    if n == 1:
        indicacoes = [float(i) for i in indic.split(";")]
        media = Media(indicacoes)
        inc_p = Incerteza_Padrao(indicacoes)
        gl = Graus_de_Liberdade(indicacoes)
        tstudent = achart(gl,prob)
        precisao = tstudent * inc_p
        correcao = (media - vv) * -1
        erro = correcao + precisao
        print ("\nMédia: " + str(round(media,alg)))
        print ("Incerteza: " + str(round(inc_p, alg)))
        print ("Erro Máximo: " + str(round (erro,alg)))
        print ("Precisão: " + str(round(precisao,alg)))
        print ("Valor Verdadeiro: " + str(vv))
        print ("RM: " + str(round(media, alg)) + " +- " + str(round (erro,alg)))
        with open('Dados Obtidos.csv', 'w', newline='') as dados:
            valores = csv.writer(dados)
            valores.writerow(["Medidas","Indicações 1"])
            for i in range (len(indicacoes)):
                valores.writerow([str(i+1),str(indicacoes[i])])
            valores.writerow(["",""])
            valores.writerow(["Média",str(round(media,alg))])
            valores.writerow(["Incerteza",str(round(inc_p,alg))])
            valores.writerow(["Precisão",str(round(precisao,alg))])
            valores.writerow(["Erro Máximo",str(round(erro,alg))])
            valores.writerow(["Valor Verdadeiro",str(vv)])
            valores.writerow(["RM",str(round((media),alg))+" +- " + str(round((erro),alg))])
        
    else:
        indicacoes = [float(i) for i in indic.split(";")]
        media = Media (indicacoes)
        auxinc = input("Informe as incertezas: ")
        incertezas = [float(i) for i in auxinc.split(";")]
        auxgl = input("Informe os graus de liberdade: ")
        grausl = [int(i) for i in auxgl.split(";")]
        auxcc = input("Informe as correcoes: ")
        correcoes = [float(i) for i in auxcc.split(";")]
        correcao_combinada = 0
        incerteza_combinada = 0
        graus_efetivos = 0
        for i in correcoes:
            correcao_combinada += i
        for i in incertezas:
            incerteza_combinada += i**2
        incerteza_combinada **= 0.5
        soma_graus = 0
        for i in range (n):
            soma_graus += ((incertezas[i] ** 4) / grausl[i])
        graus_efetivos = (incerteza_combinada**4) / soma_graus
        tstud = achart(int (graus_efetivos) , prob)
        precisao = tstud * incerteza_combinada
        erro = correcao_combinada + precisao
        print ("\nMédia: " + str(round(media,alg)))
        print ("Incerteza: " + str(round(incerteza_combinada, alg)))
        print ("Precisão: " + str(round(precisao,alg)))
        print ("Correção Combinada: " + str(round(correcao_combinada,alg)))
        print ("Valor Verdadeiro: " + str(vv))
        print ("Erro Máximo: " + str(round (erro,alg)))
        print ("RM: " + str(round(media,alg)) + " +- " + str(round(erro,alg)))        
        with open('Dados Obtidos.csv', 'w', newline='') as dados:
            valores = csv.writer(dados)
            valores.writerow(["Medidas","Indicações 1"])
            for i in range (len(indicacoes)):
                valores.writerow([str(i+1),str(indicacoes[i])])
            valores.writerow(["",""])
            valores.writerow(["Fonte de Erro","Incertezas","Correção","Graus de Liberdade"])
            for i in range (len(incertezas)):
                valores.writerow([str(i+1),str(incertezas[i]),str(correcoes[i]),(str(grausl[i]))])
            valores.writerow(["",""])
            valores.writerow(["Média",str(round(media,alg))])
            valores.writerow(["Incerteza Combinada",str(round(incerteza_combinada,alg))])
            valores.writerow(["Precisão",str(round(precisao,alg))])
            valores.writerow(["Correção Combinada",str(round(correcao_combinada,alg))])
            valores.writerow(["Erro Máximo",str(round(erro,alg))])
            valores.writerow(["Valor Verdadeiro",str(vv)])
            valores.writerow(["RM",str(round((media),alg))+" +- " + str(round((erro),alg))])
            

def MIEC(n,ind,prob,alsig):
    vv = float (input("Digite o valor verdadeiro: "))
    indicacoes = [float(i) for i in ind.split(";")]
    numero_medicoes = len(ind)
    media = Media(indicacoes)

    if n == 1:
        gl = Graus_de_Liberdade(ind)
        tendencia = media - vv
        correcao = (-1) * tendencia
        ip = Incerteza_Padrao(indicacoes)
        tstud = achart(gl,prob)
        precisao = tstud * ip
        precisao /= (math.pow(numero_medicoes,0.5))
        resultado_medicao = str(round((media + correcao),alsig)) + " +- " + str(round(precisao,alsig))
        print ("\nMédia: " + str(round(media,alsig)))
        print ("Incerteza: " + str(round(ip, alsig)))
        print ("Correção: " + str(round (correcao,alsig)))
        print ("Precisão: " + str(round(precisao,alsig)))
        print ("RM: " + resultado_medicao)
        with open('Dados Obtidos.csv', 'w', newline='') as dados:
            valores = csv.writer(dados)
            valores.writerow(["Medidas","Indicações 1"])
            for i in range (len(indicacoes)):
                valores.writerow([str(i+1),str(indicacoes[i])])
            valores.writerow(["",""])
            valores.writerow(["Média",str(round(media,alsig))])
            valores.writerow(["Incerteza",str(round(ip,alsig))])
            valores.writerow(["Precisão",str(round(precisao,alsig))])
            valores.writerow(["Correção",str(round(correcao,alsig))])
            valores.writerow(["RM",str(round((media+correcao),alsig))+" +- " + str(round((precisao),alsig))])
    else:
        auxcor = input("Informe as correções: ")
        correcoes = [float(i) for i in auxcor.split(";")]
        auxinc = input("Informe as incertezas: ")
        incertezas = [float(i) for i in auxinc.split(";")]
        auxgl = input("Informe os graus de liberdade: ")
        grausl = [int(i) for i in auxgl.split(";")]
        correcao_combinada = 0
        incerteza_combinada = 0
        graus_efetivos = 0
        for i in correcoes:
            correcao_combinada += i
        for i in incertezas:
            incerteza_combinada += i**2
        incerteza_combinada **= 0.5
        soma_graus = 0
        for i in range (n):
            soma_graus += ((incertezas[i] ** 4) / grausl[i])
        graus_efetivos = (incerteza_combinada**4) / soma_graus
        tstud = achart(int (graus_efetivos) , prob)
        precisao = tstud * incerteza_combinada
        precisao /= (math.pow(numero_medicoes,0.5))
        resultado_medicao = str(round((media + correcao_combinada),alsig)) + " +- " + str(round(precisao,alsig))
        print ("\nMédia: " + str(round(media,alsig)))
        print ("Incerteza: " + str(round(incerteza_combinada, alsig)))
        print ("Correção: " + str(round (correcao_combinada,alsig)))
        print ("Precisão: " + str(round(precisao,alsig)))
        print ("Valor Verdadeiro: " + str(vv))
        print ("RM: " + resultado_medicao)
        with open('Dados Obtidos.csv', 'w', newline='') as dados:
            valores = csv.writer(dados)
            valores.writerow(["Medidas","Indicações 1"])
            for i in range (len(indicacoes)):
                valores.writerow([str(i+1),str(indicacoes[i])])
            valores.writerow(["",""])
            valores.writerow(["Fonte de Erro","Incertezas","Correção","Graus de Liberdade"])
            for i in range (len(incertezas)):
                valores.writerow([str(i+1),str(incertezas[i]),str(correcoes[i]),(str(grausl[i]))])
            valores.writerow(["",""])
            valores.writerow(["Média",str(round(media,alsig))])
            valores.writerow(["Incerteza Combinada",str(round(incerteza_combinada,alsig))])
            valores.writerow(["Precisão",str(round(precisao,alsig))])
            valores.writerow(["Correção Combinada",str(round(correcao_combinada,alsig))])
            valores.writerow(["Valor Verdadeiro",str(vv)])
            valores.writerow(["RM",str(round((media+correcao_combinada),alsig))+" +- " + str(round((precisao),alsig))])
        


def MVENC(indic, alg,prob,erro):
    n = int (input ("Informe a quantidade de fontes de incertezas: "))
    if n == 1:
        indicacoes = [float(i) for i in indic.split(";")]
        media = Media(indicacoes)
        inc_p = Incerteza_Padrao(indicacoes)
        gl = Graus_de_Liberdade(indicacoes)
        tstudent = achart(gl,prob)
        precisao = tstudent * inc_p
        print ("\nMédia: " + str(round(media,alg)))
        print ("Incerteza: " + str(round(inc_p, alg)))
        print ("Erro Máximo: " + str(round (erro,alg)))
        print ("Precisão: " + str(round(precisao,alg)))
        print ("RM: " + str(round(media, alg)) + " +- " + str(round ((erro+precisao),alg)))
        with open('Dados Obtidos.csv', 'w', newline='') as dados:
            valores = csv.writer(dados)
            valores.writerow(["Medidas","Indicações 1"])
            for i in range (len(indicacoes)):
                valores.writerow([str(i+1),str(indicacoes[i])])
            valores.writerow(["",""])
            valores.writerow(["Média",str(round(media,alg))])
            valores.writerow(["Incerteza",str(round(inc_p,alg))])
            valores.writerow(["Precisão",str(round(precisao,alg))])
            valores.writerow(["Erro Máximo",str(round(erro,alg))])
            valores.writerow(["RM",str(round(media,alg))+" +- " + str(round((erro+precisao),alg))])
    else:
        indicacoes = [float(i) for i in indic.split(";")]
        auxinc = input("Informe as incertezas: ")
        incertezas = [float(i) for i in auxinc.split(";")]
        auxgl = input("Informe os graus de liberdade: ")
        grausl = [int(i) for i in auxgl.split(";")]
        media = Media(indicacoes)
        soma_graus = 0
        incerteza_combinada = 0
        for i in incertezas:
            incerteza_combinada += i**2
        incerteza_combinada**0.5
        for i in range (n):
            soma_graus += ((incertezas[i] ** 4) / grausl[i])
        graus_efetivos = (incerteza_combinada**4) / soma_graus
        tstud = achart(int (graus_efetivos) , prob)
        precisao = tstud * incerteza_combinada
        print ("\nMédia: " + str(round(media,alg)))
        print ("Erro Máximo: " + str(round (erro,alg)))
        print ("Precisão: " + str(round(precisao,alg)))
        print ("RM: " + str(round(media, alg)) + " +- " + str(round ((erro+precisao),alg)))                
        with open('Dados Obtidos.csv', 'w', newline='') as dados:
            valores = csv.writer(dados)
            valores.writerow(["Medidas","Indicações 1"])
            for i in range (len(indicacoes)):
                valores.writerow([str(i+1),str(indicacoes[i])])
            valores.writerow(["",""])
            valores.writerow(["Fonte de Erro","Incertezas","Graus de Liberdade"])
            for i in range (len(incertezas)):
                valores.writerow([str(i+1),str(incertezas[i]),str(grausl[i])])
            valores.writerow(["",""])
            valores.writerow(["Média",str(round(media,alg))])
            valores.writerow(["Incerteza Combinada",str(round(incerteza_combinada,alg))])
            valores.writerow(["Precisão",str(round(precisao,alg))])
            valores.writerow(["Erro Máximo",str(round(erro,alg))])
            valores.writerow(["RM",str(round(media,alg))+" +- " + str(round((erro+precisao),alg))])

            
def MVEC(indic,vv,alg,prob):
    n = int (input("Informe o número de fontes de incertezas: "))
    if n == 1:
        indicacoes = [float(i) for i in indic.split(";")]
        media = Media(indicacoes)
        inc_p = Incerteza_Padrao(indicacoes)
        gl = Graus_de_Liberdade(indicacoes)
        tstudent = achart(gl,prob)
        precisao = tstudent * inc_p
        correcao = (media - vv) * -1
        print ("\nMédia: " + str(round(media,alg)))
        print ("Incerteza: " + str(round(inc_p, alg)))
        print ("Precisão: " + str(round(precisao,alg)))
        print ("RM: " + str(round(media+correcao, alg)) + " +- " + str(round (precisao,alg)))
        with open('Dados Obtidos.csv', 'w', newline='') as dados:
            valores = csv.writer(dados)
            valores.writerow(["Medidas","Indicações 1"])
            for i in range (len(indicacoes)):
                valores.writerow([str(i+1),str(indicacoes[i])])
            valores.writerow(["",""])
            valores.writerow(["Média",str(round(media,alg))])
            valores.writerow(["Valor Verdadeiro",str(vv)])
            valores.writerow(["Correção",str(round(correcao,alg))])
            valores.writerow(["Incerteza",str(round(inc_p,alg))])
            valores.writerow(["Precisão",str(round(precisao,alg))])
            valores.writerow(["RM",str(round((media+correcao),alg))+" +- " + str(round(precisao,alg))])
    else:
        indicacoes = [float(i) for i in indic.split(";")]
        media = Media(indicacoes)
        auxinc = input("Informe as incertezas: ")
        incertezas = [float(i) for i in auxinc.split(";")]
        auxcc = input("Informe as correções: ")
        cc = [float(i) for i in auxcc.split(";")]
        auxgl = input("Informe os graus de liberdade: ")
        grausl = [int(i) for i in auxgl.split(";")]
        inc_c = 0
        correcomb = 0
        for i in cc:
            correcomb += i
        for i in incertezas:
            inc_c += i**2
        inc_c **= 0.5
        soma_graus = 0
        for i in range (n):
            soma_graus += ((incertezas[i] ** 4) / grausl[i])
        graus_efetivos = (inc_c**4) / soma_graus
        tstud = achart(int (graus_efetivos) , prob)
        precisao = tstud * inc_c
        print ("\nMédia: " + str(round(media,alg)))
        print ("Correção: " + str(round(correcomb,alg)))
        print ("Incerteza: " + str(round(inc_c, alg)))
        print ("Precisão: " + str(round(precisao,alg)))
        print ("RM: " + str(round((media + correcomb), alg)) + " +- " + str(round(precisao,alg)))        
        with open('Dados Obtidos.csv', 'w', newline='') as dados:
            valores = csv.writer(dados)
            valores.writerow(["Medidas","Indicações 1"])
            for i in range (len(indicacoes)):
                valores.writerow([str(i+1),str(indicacoes[i])])
            valores.writerow(["",""])
            valores.writerow(["Fonte de Erro","Incertezas","Correções","Graus de Liberdade"])
            for i in range (len(incertezas)):
                valores.writerow([str(i+1),str(incertezas[i]),str(cc[i]),str(grausl[i])])
            valores.writerow(["","",""])
            valores.writerow(["Média",str(round(media,alg))])
            valores.writerow(["Correção Combinada",str(round(correcomb,alg))])
            valores.writerow(["Incerteza Combinada",str(round(inc_c,alg))])
            valores.writerow(["Precisão",str(round(precisao,alg))])
            valores.writerow(["RM",str(round((media+correcomb),alg))+" +- " + str(round(precisao,alg))])

def MNC(indicacoes1,indicacoes2,casasdec,op):
    media1 = Media(indicacoes1)
    media2 = Media(indicacoes2)
    incerteza1 = Incerteza_Padrao(indicacoes1)
    incerteza2 = Incerteza_Padrao(indicacoes2)
    inc_result = inc_comb_soma_e_sub (indicacoes1,indicacoes2)
    print("\nIncerteza Total: " + str(round(inc_result,casasdec)))
    print("Média 1: " + str(round(media1,casasdec)))
    print("Média 2: " + str(round(media2,casasdec)))
    resultado_medicao = 0
    if op == 1:
        resultado_medicao = media1+media2
    if op == 2:
        resultado_medicao = media1-media2
    if op == 3:
        resultado_medicao = media1*media2
    if op == 4:
        resultado_medicao = media1/media2
    print("RM: " + str(round(resultado_medicao,casasdec)) + " +- " + str(round(inc_result,casasdec)))
    with open('Dados Obtidos.csv', 'w', newline='') as dados:
        valores = csv.writer(dados)
        valores.writerow(["Medidas","Indicações 1","Indicações 2"])
        for i in range (len(indicacoes1)):
            valores.writerow([str(i+1),str(indicacoes1[i]),str(indicacoes2[i])])
        valores.writerow(["","",""])
        valores.writerow(["Médias",str(round(media1,casasdec)),str(round(media2,casasdec))])
        valores.writerow(["Incertezas",str(round(incerteza1,casasdec)),str(round(incerteza2,casasdec))])
        valores.writerow(["","",""])
        valores.writerow(["RM",str(round(resultado_medicao,casasdec))+" +- " + str(round(inc_result,casasdec))])

def MDC(indicacoes1,indicacoes2,casasdec,Operacao):
    media1 = Media(indicacoes1)
    media2 = Media(indicacoes2)
    incerteza1 = Incerteza_Padrao(indicacoes1)
    incerteza2 = Incerteza_Padrao(indicacoes2)
    incerteza_resultante = 0
    if Operacao == 1 or Operacao == 3:
        incerteza_resultante = incerteza1 + incerteza2
    if Operacao == 2 or Operacao == 4:
        incerteza_resultante = incerteza1 - incerteza2
        if incerteza_resultante < 0:
            incerteza_resultante *= -1
    print("\nIncerteza Total: " + str(round(incerteza_resultante,casasdec)))
    print("Média 1: " + str(round(media1,casasdec)))
    print("Média 2: " + str(round(media2,casasdec)))
    resultado_medicao = 0
    if Operacao == 1:
        resultado_medicao = media1+media2
    if Operacao == 2:
        resultado_medicao = media1-media2
    if Operacao == 3:
        resultado_medicao = media1*media2
    if Operacao == 4:
        resultado_medicao = media1/media2
    print("RM: " + str(round(resultado_medicao,casasdec)) + " +- " + str(round(incerteza_resultante,casasdec)))
    with open('Dados Obtidos.csv', 'w', newline='') as dados:
        valores = csv.writer(dados)
        valores.writerow(["Medidas","Indicações 1","Indicações 2"])
        for i in range (len(indicacoes1)):
            valores.writerow([str(i+1),str(indicacoes1[i]),str(indicacoes2[i])])
        valores.writerow(["","",""])
        valores.writerow(["Médias",str(round(media1,casasdec)),str(round(media2,casasdec))])
        valores.writerow(["Incertezas",str(round(incerteza1,casasdec)),str(round(incerteza2,casasdec))])
        valores.writerow(["","",""])
        valores.writerow(["RM",str(round(resultado_medicao,casasdec))+" +- " + str(round(incerteza_resultante,casasdec))])


def MIC(indicacoes1,indicacoes2,casasdec,Operacao):
    media1 = Media(indicacoes1)
    media2 = Media(indicacoes2)
    incerteza1 = Incerteza_Padrao(indicacoes1)
    incerteza2 = Incerteza_Padrao(indicacoes2)
    incerteza_resultante = 0
    if Operacao == 2 or Operacao == 4:
        incerteza_resultante = incerteza1 + incerteza2
    if Operacao == 1 or Operacao == 3:
        incerteza_resultante = incerteza1 - incerteza2
        if incerteza_resultante < 0:
            incerteza_resultante *= -1
    print("\nIncerteza Total: " + str(round(incerteza_resultante,casasdec)))
    print("Média 1: " + str(round(media1,casasdec)))
    print("Média 2: " + str(round(media2,casasdec)))
    resultado_medicao = 0
    if Operacao == 1:
        resultado_medicao = media1+media2
    if Operacao == 2:
        resultado_medicao = media1-media2
    if Operacao == 3:
        resultado_medicao = media1*media2
    if Operacao == 4:
        resultado_medicao = media1/media2
    print("RM: " + str(round(resultado_medicao,casasdec)) + " +- " + str(round(incerteza_resultante,casasdec)))
    with open('Dados Obtidos.csv', 'w', newline='') as dados:
        valores = csv.writer(dados)
        valores.writerow(["Medidas","Indicações 1","Indicações 2"])
        for i in range (len(indicacoes1)):
            valores.writerow([str(i+1),str(indicacoes1[i]),str(indicacoes2[i])])
        valores.writerow(["","",""])
        valores.writerow(["Médias",str(round(media1,casasdec)),str(round(media2,casasdec))])
        valores.writerow(["Incertezas",str(round(incerteza1,casasdec)),str(round(incerteza2,casasdec))])
        valores.writerow(["","",""])
        valores.writerow(["RM",str(round(resultado_medicao,casasdec))+" +- " + str(round(incerteza_resultante,casasdec))])


        
    


##Interação com usuário
print("Bem vindo ao ID Calc!")
print("Caso algum valor seja inserido incorretamente, reinicie todo o procedimento.\n\n")
print("Inicialmente, digite o número correspondente ao tipo de sua medição:")
print("1 - Medição Direta")
print("2 - Medição Indireta\n")
Tipo_Medicao = int(input("Opção:"))
print("\n")

if Tipo_Medicao == 1:
    print("Digite, agora, a características de seus valores:\n")
    print("1 - Mensurando invariável com erros não compensados\n")
    print("2 - Mensurando variável com erros não compensados\n")
    print("3 - Mensurando invariável com erros compensados\n")
    print("4 - Mensurando variável com erros compensados\n")

    Tipo_Valores = int(input("Opção:"))

    if Tipo_Valores == 1:
        indic1 = input("Informe as indicações: ")
        vv = float (input("Digite o valor verdadeiro: "))
        alg = int (input("Informe as casas decimais desejadas no resultado: "))
        prob = float (input("Informe a probabilidade de abrangência: "))
        MIENC(indic1,vv,alg,prob)
        indicacoes1 = [float(i) for i in indic1.split(";")]
        colunas = int (input("\nOs histogramas das indicações inseridas serão salvos na pasta onde esse arquivo se encontra. Insira o número de intervalos desejados no gráfico: ")) 
        Histograma(indicacoes1,colunas,"Histograma das Indicações","Indicações","Frequência")
        
    if Tipo_Valores == 2:
        indic2 = input("Informe as indicações: ")
        alg = int (input("Informe as casas decimais desejadas no resultado: "))
        prob = float (input("Informe a probabilidade de abrangência: "))
        erro = float (input("Informe o erro máximo: "))
        MVENC(indic2,alg,prob,erro)
        indicacoes1 = [float(i) for i in indic2.split(";")]
        colunas = int (input("\nOs histogramas das indicações inseridas serão salvos na pasta onde esse arquivo se encontra. Insira o número de intervalos desejados no gráfico: ")) 
        Histograma(indicacoes1,colunas,"Histograma das Indicações","Indicações","Frequência")

    if Tipo_Valores == 3:
        indic3 = input("Informe as indicações: ")
        alg = int (input("Informe as casas decimais desejadas no resultado: "))
        prob = float (input("Informe a probabilidade de abrangência: "))
        n = int (input("Informe o número de fontes de incerteza: "))
        MIEC(n,indic3,prob,alg)
        indicacoes1 = [float(i) for i in indic3.split(";")]
        colunas = int (input("\nOs histogramas das indicações inseridas serão salvos na pasta onde esse arquivo se encontra. Insira o número de intervalos desejados no gráfico: ")) 
        Histograma(indicacoes1,colunas,"Histograma das Indicações","Indicações","Frequência")
        
    if Tipo_Valores == 4:
        indic4 = input("Informe as indicações: ")
        vv = float (input("Digite o valor verdadeiro: "))
        alg = int (input("Informe as casas decimais desejadas no resultado: "))
        prob = float (input("Informe a probabilidade de abrangência: "))
        MVEC(indic4,vv,alg,prob)
        indicacoes1 = [float(i) for i in indic4.split(";")]
        colunas = int (input("\nOs histogramas das indicações inseridas serão salvos na pasta onde esse arquivo se encontra. Insira o número de intervalos desejados no gráfico: ")) 
        Histograma(indicacoes1,colunas,"Histograma das Indicações","Indicações","Frequência")
    

if Tipo_Medicao == 2:
    print("Digite a relação de correlação entre suas variáveis:\n")
    print("1 - Medidas indiretas correlacionadas\n")
    print("2 - Medidas diretas correlacionadas\n")
    print("3 - Medidas não-correlacionadas\n")
    Correlacao = int(input("Opção:"))
    print("\n")
    print("Digite a operação:\n")
    print("1 - Soma \n")
    print("2 - Subtração\n")
    print("3 - Multiplicação\n")
    print("4 - Divisão\n")
    Operacao = int(input("Opção:"))
    print("\n")
    print("A partir das opções, informe as indicações na ordem da operação escolhida, com os valores separados por ;\n")
    aux1 = input("Indicações 1: ")
    aux2 = input("Indicações 2: ")
    indicacoes1 = [float(i) for i in aux1.split(";")]                 
    indicacoes2 = [float(i) for i in aux2.split(";")]                 
    casasdec = int(input("Informe o número de casas decimais desejadas no resultado: "))
    if Correlacao == 3:
        MNC(indicacoes1,indicacoes2,casasdec,Operacao)
    if Correlacao == 2:
        MDC(indicacoes1,indicacoes2,casasdec,Operacao)
    if Correlacao == 1:
        MIC(indicacoes1,indicacoes2,casasdec,Operacao)
    colunas = int (input("\nOs histogramas das indicações inseridas serão salvos na pasta onde esse arquivo se encontra. Insira o número de intervalos desejados no gráfico: ")) 
    Histograma(indicacoes1,colunas,"Histograma das Indicações 1","Indicações","Frequência")
    Histograma(indicacoes2,colunas,"Histograma das Indicações 2","Indicações","Frequência")
    
