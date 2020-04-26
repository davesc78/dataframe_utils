# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 10:53:29 2018

@author: david
"""

import pandas as pd

def find_in_string_any(string, stringlist):
# retorna verdadero si string contiene al menos una de las cadenas en stringlist
     bol=False
     for s in stringlist:
             bol= (bol |  ((string.find(s)) != -1))
     return bol
    
def find_in_string_all(string, stringlist):
# retorna verdadero si string contiene al todas las cadenas en stringlist
     bol=True
     for s in stringlist:
             bol= (bol &  ((string.find(s)) != -1))
     return bol
    
    
def find_in_string(string, stringlist, find_type='any'):
# retorna verdadero si string contiene al menos una (find_type='any')
# o todas (find_type='all')las cadenas en stringlist 
# Esto se un "wrapper" de conveniencia de las funciones find_in_string_any()
# y find_in_string_all()  
    
    if find_type == 'any':
        return find_in_string_any(string, stringlist)
    elif find_type == 'all':
        return find_in_string_all(string, stringlist)

    
def find_in_dataFrame(df, stringlist, find_type='any'):
    '''input= DataFrame,  lista de cadenas de texto, find_type: indicador de tipo de busqueda
    
    si (find_type='any'): 
    output= DataFrame con las filas que contienen al menos una de las cadenas
    en cualquiera de sus columnas
    
    si (find_type='all'): 
    output= DataFrame con las filas que contienen todas las cadenas
    en cualquiera de sus columnas'
    
    '''    
    
    dfm= df.applymap(lambda x: find_in_string(x, stringlist, find_type))
    return df.loc[dfm.any(axis='columns')]
   

midf = pd.DataFrame({'uno' : ['hola', 's', 'no'], 'dos' : ['chao', 'pero', 'hasta'], 'tres':['nunca', 'simepre', 'cuando']})   


'''Ejemplo uso
df
    uno    dos     tres
0  hola   chao    nunca
1     s   pero  simepre
2    no  hasta   cuando


find_in_dataFrame(midf,['p', 't'], 'any')

  uno    dos     tres
1   s   pero  simepre
2  no  hasta   cuando


find_in_dataFrame(midf,['a', 'o'], 'all')

    uno    dos    tres
0  hola   chao   nunca
2    no  hasta  cuando'''











