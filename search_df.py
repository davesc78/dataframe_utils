# -*- coding: utf-8 -*-
"""
Functions to simplify string search on dataframes

Created on Sat Jul  7 10:53:29 2018
Updated on Mon Jul 22 16:07    2024
@author: David Escobar
"""

import pandas as pd

def find_in_string_any(string, stringlist):
'''Returns true if the string contains at least one of the strings in stringlist'''     
     bol=False
     for s in list(stringlist):
             bol= (bol |  ((string.find(s)) != -1))
     return bol
    
def find_in_string_all(string, stringlist):
'''Returns true if the string contains all the strings in stringlist'''
     bol=True
     for s in list(stringlist):
             bol= (bol &  ((string.find(s)) != -1))
     return bol
    
    
def find_in_string(string, stringlist, find_type='any'):
'''Returns True if the string contains at least one (find_type='any')
or all (find_type='all') the strings in stringlist 
This is a convenience "wrapper" for find_in_string_any()
and find_in_string_all()'''  

     
    
    if find_type == 'any':
        return find_in_string_any(string, stringlist)
    elif find_type == 'all':
        return find_in_string_all(string, stringlist)

    
def find_in_data_frame(df, stringlist, find_type='any'):
    '''
    Returns a dataframe with rows that contain strings in stringlist, following the rule determined by "find_type" ("any" or "all")
    
    Input:
    df:DataFrame,
    stringlist:list of strings , 
    find_type: search type indicator. 'any' or 'all'
    
    Output:
    if (find_type='any'): 
    A DataFrame with the rows that contain at least one of the strings in stringlist in any column.
    
    if (find_type='all'): 
    A DataFrame with the rows that contain all the strings in stringlist in any column.'
    '''    
    
    dfm= df.applymap(lambda x: find_in_string(x, stringlist, find_type))
    return df.loc[dfm.any(axis='columns')]
   

my_df = pd.DataFrame({'a' : ['hello', 'yes', 'no'], 'b' : ['bubble', 'pet', 'unicorn'], 'c':['never', 'always', 'after']})   


"""
Usage example:

my_df
    a       b        c
0  hello  ubble    never
1   yes    pet    always
2   no   unicorn   after


find_in_dataFrame(my_df, ('p', 't'), 'any')

     a      b       c
1   yes    pet    always
2   no   unicorn   after


find_in_dataFrame(my_df, ('e', 'o'), 'all')

      a    b     c
0  hello  ubble    still

"""











