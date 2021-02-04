  import pandas as pd
  from datetime import datetime

def dealwith_comment(inputfilelink, col1, col2, output_link):


  comments = pd.read_csv(inputfilelink)

  otherinfo = comments.rename(columns={"time": col1})
  otherinfo = otherinfo.rename(columns={"Contributor_Name": col2})

  otherinfo[col1] = otherinfo[col1].apply(lambda x: x.replace('^^^_',''))
  otherinfo[col1] = otherinfo[col1].apply(lambda x: x.replace('T',' '))
  otherinfo[col1] = otherinfo[col1].apply(lambda x: x.replace('Z',''))
  
  secondresult = pd.to_csv(output_link,index=False)

  return secondresult
