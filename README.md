# DSC180B

This repository is mainly try to figure out our main purpose, which is "get a more accurate weighted sum formula to evluate the controversy for wikipedia articles". We made some python files to deal with the data and analysis which is related with this topic. But we have not finish this research yet. 

# Coding part

We are working on generating the final dataframe we will use and sentiment analysis for all the coding files we have. Specifically:
1. for get_data.py, it's main function is downloading and extract the comments part from the wikipedia XML files

2. for the deal_withcomment.py, the main function for this python file is to correct the format problem that exist in those XML files. After we getting a correct format, we will start to merge the dataframe we get from XML file to the English light dump data

3. for the english_lighdump.py, the main function for this python file is to download the English light dump data. And considering the efficiency, we use map reduce method to let our algorithm become faster. Also in this python file, we get the dataframe that merge English light dump data with the XML file data. 

4. for the page_view.py, we are getting the data from pageview API and we will use those data in the analysis part. 

4. for both senti_relate_analy.py and sentiment_analysis.py, their functions are related with sentiment analysis part. We are using vader to get a compound sentiment score for the comment content and label those sentiment score as "positive", "negative" or "neutral". We will use those labels to make future analysis.

# Notebook

For the content of the notebook, we put our main part of analysis into the notebook with charts to better show you our analysis result. 

# Resource

We get our English light dump data from WikiWarMonitor and XML file from the Wikipedia dump download website. Also, we get the M score of English Light dump data from the WikiWarMonitor

# Responsibility

Coding: Xingyu Jiang, Xiangchen Zhao and Hengyu Liu
Notebook: Xiangchen Zhao
Report: Xingyu Jiang, Xiangchen Zhao and Hengyu Liu
