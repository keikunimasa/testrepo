import datetime
import pandas as pd
import matplotlib
matplotlib.rc('font', family='BIZ UDGothic')

from pytrends.request import TrendReq
import requests
from lxml import etree


dt = datetime.datetime.today()
pytrends = TrendReq(hl='ja-jp', tz=540)


trend_list =pytrends.trending_searches(pn='japan')
top_word = trend_list[0][0]
kw_list = [top_word]
kw_list
pytrends.build_payload(kw_list=kw_list, timeframe=f'2022-01-01 {dt.year}-{dt.month}-{dt.day}', geo='JP')
df = pytrends.interest_over_time().drop('isPartial', axis = 1);df.plot(figsize=(15, 3), lw=.7);
pytrends.interest_by_region(resolution='COUNTRY', inc_geo_code = True).sort_values('geoCode')

#Pytrendの最上位の検索Sugest
for kw in kw_list:
    google_r = requests.get("http://www.google.com/complete/search",
    params={'q':kw,
                         'hl':'ja',
                         'ie':'utf_8',
                         'oe':'utf_8',
                         'output': 'toolbar'})
    google_root = etree.XML(google_r.text)
    google_sugs = google_root.xpath("//suggestion")
    google_sugstrs = [s.get("data") for s in google_sugs]
    google_suglist = []
    for ss in google_sugstrs:
       google_suglist.append(ss)
       print(ss)




queries = pytrends.related_queries();
queries[kw_list[0]]["rising"]
queries[kw_list[0]]['top']

topics = pytrends.related_topics()
topics[kw_list[0]]['rising']
topics[kw_list[0]]["top"]


