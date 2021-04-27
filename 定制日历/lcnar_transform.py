import  sxtwl
import requests
import json
from chinese_calendar import is_workday, is_holiday
import chinese_calendar as calendar
import datetime
def trans(date):
    url='http://v.juhe.cn/calendar/day?date='+date+'&key=9666832e09159f99a1f4dd7fbef27d50'
    r=requests.get(url)
    data=json.loads(r.text)
    if data['result']==None:
        new_url='http://api.djapi.cn/wannianli/get?date='+date+'&\
                token=9666832e09159f99a1f4dd7fbef27d50&cn_to_unicode=0'
        r=requests.get(new_url)
        new_data=json.loads(r.text)
        year=new_data['Result']['nianci'][0:2]+' '+new_data['Result']['shengxiao']+'年'
        day=new_data['Result']['nongli']
        holiday1=new_data['Result']['festivals_nl']
        holiday2=new_data['Result']['festivals_gl']
        if holiday1!='':
            return year,day,holiday1,''
        elif holiday2!='':
            return year,day,holiday2,''
        else:
            return year,day,'',''
    else:
        year=data['result']['data']['lunarYear'][:-1]+' '+data['result']['data']['animalsYear']+'年'
        day=data['result']['data']['lunar']
        try:
            
            holiday=data['result']['data']['holiday']
            desc=data['result']['data']['desc']
            return year,day,holiday,desc
        except KeyError:
            return year,day,'',''
        
    

def WeaApi(cityname):
    url='https://restapi.amap.com/v3/geocode/geo?address='+cityname+\
            '&output=JSON&key=cf7e42980fb04cb489bdeeae075249db'
    r=requests.get(url)
    data=json.loads(r.text)
    adcode=data['geocodes'][0]['adcode']
    new_url='https://restapi.amap.com/v3/weather/weatherInfo?city='+adcode+\
        '&key=cf7e42980fb04cb489bdeeae075249db'
    new_r=requests.get(new_url)
    new_data=json.loads(new_r.text)
    result=new_data['lives'][0]
    new_r=requests.get(new_url+'&extensions=all')
    data1=json.loads(new_r.text)
    lim=data1['forecasts'][0]['casts'][0]['nighttemp']+'~'+data1['forecasts'][0]['casts'][0]['daytemp']+'℃'
    result['lim']=lim
    return result
    
def insertPic(weather):
    return './img/'+weather+'.png'
    
def judge(year,month,day):
    april_last = datetime.date(year, month, day)
    on_holiday, holiday_name = calendar.get_holiday_detail(april_last)
    if on_holiday:
        if holiday_name!=None:
            return holiday_name
        else:
            return '周末'
    elif is_workday(april_last):
        return '工作日'

    
    