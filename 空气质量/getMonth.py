import time
import datetime

def get_month_range(start,end):
    start=datetime.date(int(start[0:4]),int(start[5:7]), int(start[8:]))
    end=datetime.date(int(end[0:4]),int(end[5:7]), int(end[8:]))
    months = (end.year-start.year)*12 + end.month-start.month
    month_range = ['%s-%s'%(start.year + mon//12,mon%12+1) 
                        for mon in range(start.month-1,start.month + months)]
      
    month=[]
    for i in month_range:
        if len(i)!=7:
            a=list(i)
            a.insert(5, '0')
            b=''.join(a)
            month.append(b)
        else:
            month.append(i)
    return month