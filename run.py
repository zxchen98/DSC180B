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
import pandas as pd
from datetime import datetime
import urllib.request
import zipfile
from functools import reduce
from attrdict import AttrDict 
import pageviewapi
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import requests as req
import sys
import json


sys.path.insert(0, 'src') # add library code to path
from src.deal_withcomment import dealwith_comment
from src.english_lighdump import first_step, create_title_col, merge_with_en, concat_together, english_ligh_dump
from src.get_data import find_count,download_xml_file
from src.page_view import page_view
from src.senti_relate_analy import sentiment_related
from src.sentiment_analysis import sentiment_analysis




DEALWITHCOMMENT_PARAMS = 'config/deal_withcomment_parans.json'
ENGLISH_LIGHDUMP_DATA_PARAMS = 'config/english_lightdump_params.json'
FIRSET_STEP_PARAMS = 'config/first_step_params.json'
GET_DATA_PARAMS = 'config/get_data_params.json'
PAGE_VIEW_PARAMS = 'config/page_view_params.json'
SENTIRELATED_PARAMS = 'config/senti_relate_analy_params.json'
SENTIMENT_ANALYSIS_PARAMS = 'config/sentiment_anakysis_params.json'



def load_params(fp):
    with open(fp) as fh:
        param = json.load(fh)

    return param


def main(targets):

    if "all" in targets: 
        cfg = load_params(GET_DATA_PARAMS)
        result_M = download_xml_file(**cfg)
        
                
        cfg = load_params(DEALWITHCOMMENT_PARAMS)
        result_M = dealwith_comment(**cfg)

        cfg = load_params(FIRSET_STEP_PARAMS)
        revision_analysis_df = first_step(**cfg)

        cfg = load_params(ENGLISH_LIGHDUMP_DATA_PARAMS)
        revision_analysis_df = english_ligh_dump(**cfg)

        cfg = load_params(PAGE_VIEW_PARAMS)
        age_range_df = page_view(**cfg)
        
        cfg = load_params(SENTIMENT_ANALYSIS_PARAMS)
        non_botand_bot = sentiment_analysis(**cfg)
        

        cfg = load_params(SENTIRELATED_PARAMS)
        bot_csv = sentiment_related(**cfg)


    if "test" in targets:

        cfg = load_params(PAGE_VIEW_PARAMS)
        age_range_df = page_view(**cfg)
        
        cfg = load_params(SENTIMENT_ANALYSIS_PARAMS)
        non_botand_bot = sentiment_analysis(**cfg)

        cfg = load_params(SENTIRELATED_PARAMS)
        bot_csv = sentiment_related(**cfg)

        
        
        
    return


if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)
