def Analysis(nonzero_link, zero_link):
  #first analysis for corr between M and sentiment score
  nzerom = pd.read_csv(nonzero_link)
  zerom = pd.read_csv(zero_link)
  zero_title=nzerom.groupby('title').mean()
  zero_title.plot.scatter(x='M',
                        y='sentiment_score',
                        c='DarkBlue',
                         title='M VS Sentiment')
  zero_title.savefig('test/output/figure/M_VS_Sentiment.png')
  
  #second analysis for example of Wooster Ohio
  zerom_withsen=zerom.loc[zerom['title']=='Wooster, Ohio']['sentiment_score']
  plt.hist(zerom_withsen)
  plt.title('Sentiment Score Distribution in One Article')
  plt.xlabel('Sentiment Score') 
  plt.ylabel('Comment Counts')
  
  plt.savefig('test/output/figure/Wooster_example.png')
  
  #third analysis for relationship between pageview and sentiment score
  all_views=nzerom.groupby('title').mean()
  all_views['views']=np.log(all_views['views'])
  y=all_views['views']
  x=all_views['sentiment_score']
  plt.scatter(y=abs(y),x=abs(x))

  z = np.polyfit(x, y, 1)
  p = np.poly1d(z)
  plt.plot(x,p(x),"r--")

  plt.xlabel('Sum Sentiment Score')
  plt.ylabel('View Counts')
  plt.title('Sentiment VS View')
  plt.savefig('Sentiment vs View.png')
  
  #fourth analysis for view counts with M
  logm = all_views.copy()
  logm['M'] = np.log(logm['M']+1)
  y=logm['views']
  x=logm['M']
  plt.scatter(y=abs(y),x=abs(x))

  z = np.polyfit(x, y, 1)
  p = np.poly1d(z)
  plt.plot(x,p(x),"r--")

  plt.xlabel('M')
  plt.ylabel('View Counts')
  plt.title('View counts v.s. M')
  plt.savefig('Viewcounts v.s. M.png')
  
  


