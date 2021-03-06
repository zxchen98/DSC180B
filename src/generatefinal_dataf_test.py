def generate_final_dataframe_test(lastdataf_link, nonzeo_link,zero_link):
  last_dataf = pd.read_csv(lastdataf_link)
  last_dataf['title'] = last_dataf['title'].str.replace('_', ' ')
  
  zxc = last_dataf.copy()
  zxc.drop(columns = ['Unnamed: 0'], inplace = True)
  nonzero0m = zxc[zxc['M']!=0]
  zerom = zxc[zxc['M']==0]
  
  nzerom['M']=np.log(nzerom['M'])
  zerom['M']=np.log(zerom['M']+1)
  
  nzerom['views']=np.log(nzerom['views'])
  zerom['views']=np.log(zerom['views'])
  
  nzerom['sentiment_score']=abs(nzerom['sentiment_score'])
  zerom['sentiment_score']=abs(zerom['sentiment_score'])
  
  
  nzero_title=nzerom.groupby('title').agg({'revert':'mean', 
                           'views':'mean', 
                           'sentiment_score':'mean', 
                           'M': 'mean'})

  zero_title=zerom.groupby('title').agg({'revert':'mean', 
                           'views':'mean', 
                           'sentiment_score':'mean', 
                           'M': 'mean'})

  
  nonzero0m.to_csv(nonzeo_link,index=False)
  zerom.to_csv(zero_link,index=False)
  
  return nonzero0m, zerom
