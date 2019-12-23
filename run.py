# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 22:14:18 2019

@author: eskandari
"""
import preprocessing.py as pp
import io_utils as iou
import configparser # read configurations 



#read Config Files 
Config = configparser.ConfigParser()
Config.read("config.ini")

stopwords_path_key = 'stopwords_path'
stopwords_path = Config.get('preprocessing', stopwords_path_key )


#load data           
files_df = iou.get_apps_from_folder('path to folder')
#load data from db
#files_df = tm_io.get_apps_from_db(Server = Config.get('DB', 'Server') 
#                                    , Database = Config.get('DB', 'Database')
#                                    , UID = Config.get('DB', 'UID') 
#                                    , PWD = Config.get('DB', 'PWD') 
#                                    , Lang = 'fa' , appType = 'games')

docs = files_df["text"].values
print(str(len(docs)) + ' documents loaded.')
print(files_df[1:10])
print(files_df.columns)

#preprocess data
preprocessedDocs = pp.cleanText(docs , stopwords_path)

# ready to do further processing