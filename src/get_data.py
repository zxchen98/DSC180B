from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import os
import math
import csv 
from bs4 import BeautifulSoup
import bz2
import lxml
import requests


def find_count(name,name_dict):
    name_dict[name]+=1
    return name_dict[name]-1
    

def download_xml_file(url, to_csvfilename):
  URL = url
  filename = os.path.basename(URL)

  response = requests.get(URL, stream=True)


  zipfile = bz2.BZ2File(filename)# open the file
  data = zipfile.read() # get the decompressed data
  newfilepath = filename[:-4] # assuming the filepath ends with .bz2
  
  #parse the xml file 
  #convert the raw xml to pd.dataframe
  infile = open(newfilepath,"rb")
  contents = infile.read()
  soup = BeautifulSoup(contents,'html.parser')

  all_revision=soup.find_all('revision')

  revision_list=[]
  for i in all_revision:
      each_revision={}
      #find contributor of every revision
      contributor=i.find('contributor')
      try:
          username=contributor.find('username').get_text()
      except:
          username=np.nan
      each_revision['Contributor_Name']=username

      #find each revision time
      time=i.find('timestamp').get_text()
      each_revision['time']=time

      #find each revision comment
      try:
          comment=i.find('comment').get_text()
      except:
          comment=np.nan
      each_revision['comment']=comment 

      revision_list.append(each_revision)

  df=pd.DataFrame(revision_list)

  name_count={}
  all_contributor=df['Contributor_Name'].unique()
  for i in all_contributor:
      name_count[i]=0

  count_copy=name_count.copy()
  df['Revision Time']=df['Contributor_Name'].apply(find_count,args=(count_copy,))
  
  firstresult = df.to_csv(to_csvfilename,index=False)
  return firstresult
  
