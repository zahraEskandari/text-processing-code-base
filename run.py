# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 22:14:18 2019

@author: eskandari
"""
import preprocessing as pp
import io_utils as iou
import configparser # read configurations 
import logging
import logging.config
from os import path


#load logger config
log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logger.conf')
logging.config.fileConfig(log_file_path)

#read Config Files 
config = configparser.ConfigParser()
config.read("config.ini")




#load data           
files_df = iou.get_apps_from_folder('path to folder')
#load data from db
#files_df = tm_io.get_apps_from_db(Server = Config.get('DB', 'Server') 
#                                    , Database = Config.get('DB', 'Database')
#                                    , UID = Config.get('DB', 'UID') 
#                                    , PWD = Config.get('DB', 'PWD') 
#                                    , Lang = 'fa' , appType = 'games')

docs = files_df["text"].values
logging.debug(str(len(docs)) + ' documents loaded.')
print(files_df[1:10])
print(files_df.columns)

#preprocess data
stopwords_path_key = 'stopwords_path'
stopwords_path = config.get('preprocessing', stopwords_path_key )
preprocessedDocs = pp.cleanText(docs , stopwords_path)

# ready to do further processing