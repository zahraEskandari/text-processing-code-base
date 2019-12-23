# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 22:45:32 2019

@author: eskandari
"""

import os
import pandas as pd 
import pickle


#helper function
def MergePerFolder(path):
    path1=os.listdir(path)
    for i in path1:       
        with open(path + "/" + i , encoding="utf8") as infile :            
            a = infile.read()            
            #yield a
            yield [i ,  a ]

                
#read app data from folder , each app as a file ,file name = packagename.txt
def get_docs_from_folder(app_file_path):#app_file_path
        files = list(MergePerFolder(app_file_path))
        files_df = pd.DataFrame.from_records(files)
        files_df.columns = ["DocName", "Text"]
        return files_df
    
    
    #read app data from folder , each app as a file ,file name = packagename.txt
def get_docs_from_db(Server , Database , UID , PWD , Lang ):
    import pyodbc
    conn = pyodbc.connect('Driver={SQL Server};'
                          +'Server='+Server+';'
                          +'Database='+Database+';'
                          +'UID='+UID+';'
                          +'PWD='+PWD+';'
                      #'Trusted_Connection=yes;'
    )
    
    
    SQL_Query = pd.read_sql_query( 'SELECT DocName , Text FROM Table ' , conn)
    df = pd.DataFrame(SQL_Query, columns=['DocName','Text'])               
    conn.close()
    return df

    
def save_results_to_db(Server , Database , UID , PWD , df):
    import pyodbc 
    conn = pyodbc.connect('Driver={SQL Server};'
                          +'Server='+Server+';'
                          +'Database='+Database+';'
                          +'UID='+UID+';'
                          +'PWD='+PWD+';'
                          #'Trusted_Connection=yes;'
                         )


    data = pd.DataFrame({
        'DocName':df['DocName'],
        'Text':df['Text']
    })
    # creating column list for insertion
    cols = ",".join([str(i) for i in data.columns.tolist()])
   
    cursor=conn.cursor()
    # Insert DataFrame recrds one by one.
    for i,row in data.iterrows():
        sql = "INSERT INTO Table (" +cols + ") VALUES (" + "?,"*(len(row)-1) + "?)"
        cursor.execute(sql, tuple(row))
        conn.commit()
    # the connection is not autocommitted by default, so we must commit to save our changes
    conn.close()




#save obj using pickle package
def save_obj(obj, name ):
    with open( name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


#load obj
def load_obj(name ):
    print ('loading ' + name + '.pkl')
    with open(name + '.pkl', 'rb') as f:
        return pickle.load(f)
    


