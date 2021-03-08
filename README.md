# DSC180B

There are “wars” going on every day online, but instead of cities, they are defending their options, and perspects. This phenomenon is especially common on the Wikipedia platform where users are free to edit others' revisions. In fact, there are “about 12% of discussions are devoted to reverts and vandalism, suggesting that the WP development process is highly contentious.” As Wikipedia has become a trusted source of information and knowledge which is freely accessible, It is important to investigate how editors collaborate and controvert each other in such a platform. This repository will show our coding methods to discuss a new method of measuring controvisality in Wikipedia articles. We have found out that controversiality is highly related to the number of revert edits, the sentiment level among one article comments, and the view counts of that article. Thus we developed a weighted sum formula, which combines those three factors to accurately measure the controversy level within articles in Wikipedia. 


# Coding part
From the run.py file, you can notice that we have 2 targets, which is "All" and "Test". In the following part, We will discuss about the details of those two targets:
    
For the "ALL" target, it uses datasets from the Wikimedia Data Archives and English Light Dump. Then it used the functions that are listed in the process to generate our final analysis results. There are the purpose for different functions:

1. For the get_data.py and deal_withcomment.py, we use those coding files to download XML files from the Wikimedia Data Archives and then convert those raw XML file to dataframe, which is a better form to let us doing the analysis. 
    
2. For the english_lighdump.py, the function for the python file is to download the English Light dump file from the WikiWarMonitor and convert this dataset to a dataframe. It also merge the English Lightdump Dataframe with the comment dataframe that is generated by get_data.py and deal_withcomment.py. 
    
3. For the page_view.py, the function for this python file is to use the titles in the generated dataframe to find the raw description number of views on English Wikipedia of articles in the merged dataframe from those articles' start dates to 20210101. 
    
4. For the sentiment_analysis.py, the function for this python file is to use the comments content in the generated dataframe and the Vader model to generate the sentiment score for each comment. Finally, in this python file we will generate a final dataframe that contains M score, page view count, article title, date, comment and sentiment score to use for the future analysis. 
    
5. For the generatefinaldatf.py, the function for this python file is to generate two dataframes that we will use in our analysis part and generate some graphs from analysis. Those two dataframes are dataframe with M is zero and dataframe for all M. 
    
6. For the Analysis.py, the function for this python file is to make some analysis. We generate four graphs in this analysis part:
  
    a. first one is analysis for corr between M and sentiment score
    b. second one is analysis for example of Wooster Ohio
    c. third one is relationship between pageview and sentiment score
    d. fourth one is view counts with M
   For each graph, we save as one figures and use those figures in our report. 

7. For the Weighted_sum_formula.py, the function for this python file is to generate our final weighed sum formula. And we will use the new scores which are generated by weighted sum formula to make some comparisons with the scores that are generated by M-statistics, and make some analysis on this comparison.  


For the 'Test' target, it mainly runs our test dataset, which means that the result that is generated by our "test" target is not representative. And there are some special function for this target, such as generatefinal_dataf_test.py and page_view_test.py, we generate those files because we need to use our test dataset. However, by using this "test" target, the analysis result will not be representative. 

# Notebook

For the content of the notebook, we put our analysis graphs which are generated by 'ALL' target and we will use those graphs in our report. 

# Resource

English light dump data from WikiWarMonitor: http://wwm.phy.bme.hu/light.html

XML file from the Wikimedia Data Archives: https://dumps.wikimedia.org/enwiki/20210220/

And the pageview API from: https://github.com/Commonists/pageview-api

# Responsibility

Coding: Xingyu Jiang, Xiangchen Zhao
Notebook: Xingyu Jiang, Xiangchen Zhao
Report: Xingyu Jiang, Xiangchen Zhao and Hengyu Liu
