# -*- coding: utf-8 -*-
"""
Functions to simplify string search on dataframes

Created on Sat Jul  7 10:53:29 2018
Updated on Mon Jul 22 16:07    2024
@author: David Escobar
"""

import pandas as pd

def find_in_string_any(my_str, string_list):
'''Returns true if my_str contains at least one of the strings in string_list
Inputs
my_str: the string to be searched in.
string_list: list of strings whose elements will be searched in my_str

Returns: bolean
'''     
     bol=False
     for s in list(string_list):
             bol= (bol |  ((my_str.find(s)) != -1))
     return bol


def find_in_string_all(my_str, string_list):
'''Returns true if the my_str contains all the strings in string_list.
Inputs
my_str: the string to be searched in.
string_list: list of strings whose elements will be searched in my_str.

Returns: bolean
'''
     bol=True
     for s in list(string_list):
             bol= (bol &  ((my_str.find(s)) != -1))
     return bol
    
    
def find_in_string(my_str, string_list, find_type='any'):
'''Returns True if the my_str contains at least one (find_type='any')
or all (find_type='all') the strings in string_list 
This is a convenience "wrapper" for find_in_string_any()
and find_in_string_all()'''   
    
    if find_type == 'any':
        return find_in_string_any(my_str, string_list)
    elif find_type == 'all':
        return find_in_string_all(my_str, string_list)



def find_in_data_frame(df, string_list, find_type='any'):
    '''
    Returns a dataframe with rows that contain strings in string_list, following the rule determined by "find_type" ("any" or "all")
    
    Input:
    df:DataFrame,
    string_list:list of strings , 
    find_type: search type indicator. 'any' or 'all'.
    
    Output:
    if (find_type='any'): 
    A DataFrame with the rows that contain AT LEAST ONE of the strings in string_list in any column.
    
    if (find_type='all'): 
    A DataFrame with the rows that contain ALL the strings in string_list in any column.
    '''    
    
    dfm= df.applymap(lambda x: find_in_string(x, string_list, find_type))
    return df.loc[dfm.any(axis='columns')]




my_df = pd.DataFrame({'a' : ['hello', 'yes', 'no'], 'b' : ['bubble', 'pet', 'unicorn'], 'c':['never', 'always', 'after']})   


"""
Usage example:

my_df
    a       b         c
0  hello  bubble    never
1   yes    pet     always
2   no   unicorn    after


find_in_data_frame(my_df, ('p', 't'), 'any')

     a      b       c
1   yes    pet    always
2   no   unicorn   after


find_in_data_frame(my_df, ('e', 'o'), 'all')

      a    b     c
0  hello  ubble    still

"""











