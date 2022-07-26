import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def BoxPlots(Data, N_Columna):
    ColumnaMainData = Data.columns[N_Columna]
    fig, ejes = plt.subplots(10,3, sharex = True, sharey=False, figsize = [30,50])
    sns.boxplot(data = Data[Data.Year == 1990], x = ColumnaMainData, ax = ejes[0,0])
    sns.boxplot(data = Data[Data.Year == 1991], x = ColumnaMainData, ax = ejes[1,0])
    sns.boxplot(data = Data[Data.Year == 1992], x = ColumnaMainData, ax = ejes[2,0])
    sns.boxplot(data = Data[Data.Year == 1993], x = ColumnaMainData, ax = ejes[3,0])
    sns.boxplot(data = Data[Data.Year == 1994], x = ColumnaMainData, ax = ejes[4,0])
    sns.boxplot(data = Data[Data.Year == 1995], x = ColumnaMainData, ax = ejes[5,0])
    sns.boxplot(data = Data[Data.Year == 1996], x = ColumnaMainData, ax = ejes[6,0])
    sns.boxplot(data = Data[Data.Year == 1997], x = ColumnaMainData, ax = ejes[7,0])
    sns.boxplot(data = Data[Data.Year == 1998], x = ColumnaMainData, ax = ejes[8,0])
    sns.boxplot(data = Data[Data.Year == 1999], x = ColumnaMainData, ax = ejes[9,0])
    sns.boxplot(data = Data[Data.Year == 2000], x = ColumnaMainData, ax = ejes[0,1])
    sns.boxplot(data = Data[Data.Year == 2001], x = ColumnaMainData, ax = ejes[1,1])
    sns.boxplot(data = Data[Data.Year == 2002], x = ColumnaMainData, ax = ejes[2,1])
    sns.boxplot(data = Data[Data.Year == 2003], x = ColumnaMainData, ax = ejes[3,1])
    sns.boxplot(data = Data[Data.Year == 2004], x = ColumnaMainData, ax = ejes[4,1])
    sns.boxplot(data = Data[Data.Year == 2005], x = ColumnaMainData, ax = ejes[5,1])
    sns.boxplot(data = Data[Data.Year == 2006], x = ColumnaMainData, ax = ejes[6,1])
    sns.boxplot(data = Data[Data.Year == 2007], x = ColumnaMainData, ax = ejes[7,1])
    sns.boxplot(data = Data[Data.Year == 2008], x = ColumnaMainData, ax = ejes[8,1])
    sns.boxplot(data = Data[Data.Year == 2009], x = ColumnaMainData, ax = ejes[9,1])
    sns.boxplot(data = Data[Data.Year == 2010], x = ColumnaMainData, ax = ejes[0,2])
    sns.boxplot(data = Data[Data.Year == 2011], x = ColumnaMainData, ax = ejes[1,2])
    sns.boxplot(data = Data[Data.Year == 2012], x = ColumnaMainData, ax = ejes[2,2])
    sns.boxplot(data = Data[Data.Year == 2013], x = ColumnaMainData, ax = ejes[3,2])
    sns.boxplot(data = Data[Data.Year == 2014], x = ColumnaMainData, ax = ejes[4,2])
    sns.boxplot(data = Data[Data.Year == 2015], x = ColumnaMainData, ax = ejes[5,2])
    sns.boxplot(data = Data[Data.Year == 2016], x = ColumnaMainData, ax = ejes[6,2])
    sns.boxplot(data = Data[Data.Year == 2017], x = ColumnaMainData, ax = ejes[7,2])
    sns.boxplot(data = Data[Data.Year == 2018], x = ColumnaMainData, ax = ejes[8,2])
    sns.boxplot(data = Data[Data.Year == 2019], x = ColumnaMainData, ax = ejes[9,2])
    return fig

def MayoresNMuertes(Data, Fecha, Causa, NRegistros = 1):
    return Data[Data["Year"] == Fecha][["Entity", Causa]].sort_values(by = [Causa]).tail()[-1:-(NRegistros+1):-1]

def Muertes(Data,Fecha, Causa, Territorio):
    return Data[Data["Entity"] == Territorio][Data["Year"] == Fecha][[Causa]]

def PorcentajeMuertePaisCausa(Data, Causa):
   return((Data[Causa]/Data["Poblacion"])*100)