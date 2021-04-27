import pandas as pd 
import numpy as np
import math
class Analysis:
    def get_ZT_data(self,data):
        Math=np.array(data['原始分']).tolist()
        feature=data['原始分'].describe()
        x=['0-15','15-30','30-45','45-60','60-75','75-90','90-105','105-120','120-135','135-150']
        s15=s30=s45=s60=s75=s90=s105=s120=s135=s150=0
        for i in Math:
            if i<=15:
                s15+=1
            elif i>15 and i<=30:
                s30+=1
            elif i>30 and i<=45:
                s45+=1
            elif i>45 and i<=60:
                s60+=1        
            elif i>60 and i<=75:
                s75+=1        
            elif i>75 and i<=90:
                s90+=1
            elif i>90 and i<=105:
                s105+=1
            elif i>105 and i<=120:
                s120+=1
            elif i>120 and i<=135:
                s135+=1
            else:
                s150+=1
        y=[s15,s30,s45,s60,s75,s90,s105,s120,s135,s150]
        return x,y,feature
    
    def get_FD_data(self,distance,data):
        l=[]
        x=[]
        y=[]
        Class=[]
        for i in range(0,151,int(distance)):
            l.append(i)
        data['评级']=pd.cut(data['原始分'],l,right=False)
        
        for i in list(data['评级'].unique()):
            x.append(str(i))
            y.append(data['评级'].value_counts()[i])
        n=len(set(data['评级']))
        for i in set(data['班级']):
            l=data[data['班级']==i]['评级']
            label=[]
            for j in set(l):
                label.append(l.value_counts()[j])
            if len(label)<n:
                label.extend([0]*(n-len(label)))
            label.insert(0,str(i))
            Class.append(label)
        return Class,x[::-1],y[::-1]
    
    def get_Fendang_data(self,one,two,three,data):
        Class=[]
        for i in list(data['班级'].unique()):
            f1=f2=f3=0
            s1=s2=s3=0
            t1=t2=t3=0
            l=data[data['班级']==i]['原始分']
            n=len(l)
            for j in l:
                if j>=one:
                    f1+=1
                elif j>=two and j<one:
                    s1+=1
                if j>=three and j<two:
                    t1+=1
            f2=f1
            s2=s1+f1
            t2=s1+f1+t1
            f3=round(f1/n*100,2)
            s3=round(s2/n*100,2)
            t3=round(t2/n*100,2)
            Class.append([str(i)+'班',f1,f2,f3,s1,s2,s3,t1,t2,t3])
        
        result=self.find_three(Class)
        f1=f2=f3=0
        s1=s2=s3=0
        t1=t2=t3=0
        for i in data['原始分']:
            if i>=one:
                f1+=1
            elif i>=two and i<one:
                s1+=1
            elif i>=three and i<two:
                t1+=1
        f2=f1
        s2=f1+s1
        t2=f1+s1+t1
        f3=round(f2/len(data)*100,2)
        s3=round(s2/len(data)*100,2)
        t3=round(t2/len(data)*100,2)
        Class.insert(0,['全体',f1,f2,f3,s1,s2,s3,t1,t2,t3])
        return Class,result
            
    def get_four(self,data):
        x=[]
        y=[]
        execllent=[]
        fine=[]
        Pass=[]
        low=[]
        for i in list(data['班级'].unique()):
            l=data[data['班级']==i]['原始分']
            l1=l.describe()
            x.append(str(i)+'班')
            y.append(round(l1['mean'],1))
            f1=f2=f3=0
            s1=s2=s3=0
            t1=t2=t3=0
            m1=m2=0
            n=len(l)
            for j in l:
                if j>=135:
                    f1+=1
                if j>=120:
                    s1+=1
                if j>=90:
                    t1+=1
                if j<45:
                    m1+=1
            f2=f1
            f3=round(f2/n*100,2)
            s3=round(s1/n*100,2)
            t3=round(t1/n*100,2)
            m2=round(m1/n*100,2)
            execllent.append(f3)
            fine.append(s3)
            Pass.append(t3)
            low.append(m2)
        
        p1=p2=p3=p4=0
        for i in data['原始分']:
            if i>=135:
                p1+=1
            if i>=120:
                p2+=1
            if i>=90:
                p3+=1
            elif i<45:
                p4+=1
        p1=round(p1/len(data)*100,1)
        p2=round(p2/len(data)*100,1)
        p3=round(p3/len(data)*100,1)
        p4=round(p4/len(data)*100,1)
        return x,y,execllent,fine,Pass,low,p1,p2,p3,p4
            
    
    def find_three(self,Class):
        one=[]
        two=[]
        c=[]
        for i in Class:
            c.append(i[0])
            one.append(i[3])
            two.append(i[6])
        result=[]
        best=0
        
        c1=c
        one1=one
        for i in range(3):
            best=c1[one1.index(max(one1))]
            c1.remove(best)
            one1.remove(max(one1))
            result.append(best)
            
        c1=c
        one1=one
        for i in range(3):
            best=c1[one1.index(min(one1))]
            c1.remove(best)
            one1.remove(min(one1))
            result.append(best)
        

        c2=c
        two1=two
        for i in range(3):
            best=c2[two1.index(max(two1))]
            c2.remove(best)
            two1.remove(max(two1))
            result.append(best)
            
        c2=c
        two1=two
        for i in range(3):
            best=c2[two1.index(min(two1))]
            c2.remove(best)
            two1.remove(min(two1))
            result.append(best)        
        
        return result
    
if __name__=='__main__':
    a=Analysis()
    data=pd.read_csv('综合成绩.csv')
    b=a.get_Fendang_data(120, 90, 60, data)
            
            
            
            
            
            
            
            
            
            
            
            
            
            