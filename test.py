#https://www.youtube.com/watch?v=cuTUbPQk2R4&t=83s
from pytrends.request import TrendReq

#get top keyword in USA
pytrends = TrendReq(hl="en-US")
all_keywords = []
all_keywords =pytrends.trending_searches(pn = "united_states",)
top_key = all_keywords[0][0]

#all key word

##inputs 
cat = "12"
geo = '' #デフォルトは世界
kw_list = all_keywords[0][0:5]
group = "" #Youtube news images froogle default is 
keywords =[]
timeFrames =["today 5-y", "today 12-m", "today 3-m", "today 1-m"]


def check_trends(kw):
    pytrends.build_payload(kw_list, cat,timeframe= timeFrames[0], geo='', gprop="")
    data = pytrends.interest_over_time()
    mean = round(data.mean(),2)
    avg = round(data[kw][-52:].mean(),2)
    avg2 = round(data[kw][:52].mean(),2)
    trend = round((avg/mean[kw]-1)*100,2)
    trend2 = round(((avg/avg2)-1)*100,2)
    print(kw+"の平均は"+str(mean[kw]))
    print(kw+"の関心は過去5年にくらべると"+str(trend)+ "変化しました")
    # stable trends
    if mean[kw]>75 and abs(trend)<=5:
        print(kw + "のトレンドは安定的です")
    elif mean[kw]> 75 and abs(trend) > 5:
        print(kw + "のトレンドは徐々に増加している")
    elif mean[kw]> 75 and abs(trend) < -5:
        print(kw+"は徐々にトレンドが減少しています")
    #比較的安定
    elif mean[kw]>60 and abs(trend)<=15:
        print(kw+"への関心は比較的鞍点しています")
    elif mean[kw]>60 and abs(trend)>15:
        print(kw+"への関心は比較的安定して増加しています")
    elif mean[kw]>60 and trend <-15:
        print(kw+"への関心は比較的安定して減少しています")
    #季節的な変動
    elif mean[kw] >20 and abs(trend)<= 15:
        print(kw +"への関心は季節的です")
    elif mean[kw] >20 and abs(trend) > 15:
        print(kw+"への関心は急上昇です")
    elif mean[kw] >20 and abs(trend) < -15:
        print(kw+"への関心は急減少です")
    elif mean[kw] >5 and abs(trend) < 15:
        print(kw+"への関心は周期的です")
    #全く新しい場合
    elif mean[kw] >0 and trend >15:
        print(kw+"のトレンドは新しいトレンドです")
    elif mean[kw] >0 and trend < -15:
        print(kw+"のトレンドは減少中だが、ピークとは比べられない")
    else: print("例外")







for kw in all_keywords:
    keywords.append(kw)
    check_trends()
    keywords.pop()

