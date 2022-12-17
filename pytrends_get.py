from pytrends.request import TrendReq
pytrends = TrendReq(hl='ja-jp', tz=-540)
kw_list = ['ソフトバンク'];
queries = pytrends.related_queries()


pytrends.build_payload(kw_list=kw_list, timeframe='2019-01-01 2021-06-30', geo='JP')
pytrends.interest_over_time().drop('isPartial', axis = 1);
pytrends.interest_by_region(resolution='COUNTRY', inc_geo_code = True).sort_values('geoCode')


queries[kw_list[0]]["rising"]
queries[kw_list[0]]['top']

topics = pytrends.related_topics()

topics[kw_list[0]]['rising']
topics[kw_list[0]]["top"]

# 急上昇キーワードの取得
pytrends.trending_searches(pn='japan')