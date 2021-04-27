from DataBase import DataBase

def Print_ticket():
    db=DataBase()
    result=db.get_order()
    Sum=0
    msg=''
    msg+='{:<20}{:<8}{:<7}{:<7}\n'.format('名称','价格','数量','合计')
    for i in result:
        Sum+=i[3]
        n1=len(i[0])
        n=n1-2
        q='{:<'+str(20-n)+'}{:<10}{:<10}{:<10}\n'
        msg+=q.format(i[0],str(i[1])+'元',str(i[2]),str(i[3])+'元')
    msg+='{:<20}{:<10}{:<10}{:<10}'.format('总计','','',str(Sum)+'元')
    return msg

if __name__=='__main__':
    a=Print_ticket()
    print(a)
