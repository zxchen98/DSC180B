import requests as req
import pandas as pd
import numpy as np

def sentiment_related(sco_linkl, githublink, lexicon_link, tocsvname):
  score_dataf = pd.read_csv(sco_link)
  url = githublink
  res = req.get(url)

  file = open(lexicon_link, 'w')
  file.seek(0)
  file.write(res.text)
  file.seek(0)
  file.close()

  #start check the stange words in lexicon
  f = open("vader_lexicon.txt", "r")
  x = f.readlines()
  find_list = []
  for i in x:
      insert_line = i.replace('\n','').split("\t")
      find_list.append(insert_line[0])
      
  
  list_aonothercol = []
  for i in np.arange(score_dataf.shape[0]):
      putin = 0
      comment = score_dataf.iloc[i]['comment']
      if comment is not np.nan:   
          for i in comment:
              if i not in find_list:
                  putin+=1
              else:
                  putin+=0
          if putin == len(comment):
              list_aonothercol.append(1)
          else:
              list_aonothercol.append(0)
      else:
          list_aonothercol.append(0)
          
  score_dataf = score_dataf.assign(negative_also=list_aonothercol)
  score_dataf['sentiment_score']=score_dataf['sentiment_score'].apply(lambda x: 'positive' if x>0 else ('neutral' if x==0 else 'negative'))
  
  result = score_dataf.to_csv(tocsvname, index = False)
  return result 
  


  
  
  
  
