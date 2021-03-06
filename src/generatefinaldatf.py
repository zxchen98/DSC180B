def generate_final_dataframe(lastdataf_link, nonzeo_link,zero_link):
  last_dataf = pd.read_csv(lastdataf_link)
  M=pd.read_csv('en.txt', sep="\t", header=None,error_bad_lines=False,engine='python')
  M.columns=['M','title']
  M['title'] = M['title'].str.replace('_', ' ')
  
  zxc=last_dataf.merge(M,on='title',how='left')
  zxc.drop(columns = ['Unnamed: 0','Unnamed: 0.1'], inplace = True)
  
  nonzero0m = zxc[zxc['M']!=0]
  zerom = zxc[zxc['M']==0]
  
  nonzero0m.to_csv(nonzeo_link,index=False)
  zerom.to_csv(zero_link,index=False)
  
  return nonzero0m, zerom
  
