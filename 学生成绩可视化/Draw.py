from pyecharts import options as opts
from pyecharts.charts import Bar, Grid, Line, Pie, Tab,Map,Geo,PictorialBar
from pyecharts.components import Table
from pyecharts.globals import ThemeType
from pyecharts.options import ComponentTitleOpts
from pyecharts.globals import SymbolType
import pandas as pd 
import numpy as np
from analysis import Analysis
import matplotlib
import matplotlib.pyplot as plt
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot
plt.rcParams['font.sans-serif']='simhei'
class Draw:
    def __init__(self):
        self.analysis=Analysis()
    
    def math_zongti(self):
        data=pd.read_csv('综合成绩.csv')
        x,y,feature=self.analysis.get_ZT_data(data)
        line= (
            Line()
            .add_xaxis(x)
            .add_yaxis('人数',y,is_smooth=True)
            .set_colors('blue')
            .set_series_opts(
                areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
                label_opts=opts.LabelOpts(is_show=True),
            )
            .set_global_opts(
                
                xaxis_opts=opts.AxisOpts(
                    name='分数段',
                    axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
                    is_scale=False,
                    boundary_gap=False,
                ),
                yaxis_opts=opts.AxisOpts(
                name='人数',
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
                ),
            )
        )
        line.render('成绩概括面积图.html')
        pie1 = (
        Pie()
        .add(
            "",
            [list(z) for z in zip(x, y)],
            radius=["40%", "55%"],
            center=["50%", "50%"],
            label_opts=opts.LabelOpts(
                position="outside",
                formatter="{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
                background_color="#eee",
                border_color="#aaa",
                border_width=1,
                border_radius=4,
                rich={
                    "abg": {
                        "backgroundColor": "#e3e3e3",
                        "width": "100%",
                        "align": "right",
                        "height": 22,
                        "borderRadius": [4, 4, 0, 0],
                    },
                    "hr": {
                        "borderColor": "#aaa",
                        "width": "100%",
                        "borderWidth": 0.5,
                        "height": 0,
                    },
                    "b": {"fontSize": 16, "lineHeight": 33},
                    "per": {
                        "color": "#eee",
                        "backgroundColor": "#334455",
                        "padding": [2, 4],
                        "borderRadius": 2,
                    },
                },
            ),
        )
        .set_global_opts(legend_opts=opts.LegendOpts(pos_right="60%"),)
        )
        pie1.render('成绩概括饼图.html')
        return feature,x,y,round(max(y)/len(data),2)
    
    def draw_bar(self,labels,y):
        plt.figure()
        plt.barh(labels, y,color='dodgerblue')
        for Y,X in enumerate(y):
            plt.text(X+10, Y-0.2, "%s" %X) 
        plt.xlabel('分段区间')
        plt.ylabel('人数')
        plt.title('分段成绩直方图')
        plt.savefig(fname="分段成绩直方图.png")
    def draw_pie(self,x,y):
        plt.figure()
        plt.pie(y,labels=x,autopct='%1.1f%%')
        plt.title("分段成绩饼图")
        plt.savefig(fname="分段成绩饼图.png")
    
    def draw_table(self,X,Class):
        table = Table()
        X.insert(0,'班级')
        headers =X
        rows = Class
        table.add(headers, rows)
        table.set_global_opts(
            title_opts=ComponentTitleOpts(title="分段成绩人数", subtitle="班级为单位")
        )
        table.render("表格图.html")
        
    def math_FD(self,distance):
        data=pd.read_csv('综合成绩.csv')
        Max,Min=max(data['原始分']),min(data['原始分'])
        Class,x,y=self.analysis.get_FD_data(distance,data)
        M,N=x[y.index(max(y))],x[y.index(min(y))]
        self.draw_bar(x,y)
        self.draw_pie(x,y)
        self.draw_table(x, Class)
        return Max,Min,M,N
    
    def math_fendang(self,one,two,three):
        data=pd.read_csv('综合成绩.csv')
        Class,result=self.analysis.get_Fendang_data(int(one), int(two), int(three), data)
        x=y1=y2=[]
        for i in Class[1:]:
            x.append(i[0])
            y1.append(i[3])
            y2.append(i[6])
        bar1= (
            Bar()
            .add_xaxis(x)
            .add_yaxis("一档率", y1)

            .set_global_opts(title_opts=opts.TitleOpts(title="一档直方图"),
                             datazoom_opts=[opts.DataZoomOpts()],)
        )
        bar1.render('一档直方图.html')  
        bar2= (
            Bar()
            .add_xaxis(x)
            .add_yaxis("二档率", y2)
            .set_global_opts(title_opts=opts.TitleOpts(title="二档直方图"),
                             datazoom_opts=[opts.DataZoomOpts()],)
        )
        bar2.render('二档直方图.html')   
        table = Table()
        headers =['班级','一档人数','一档累积人数','一档累计上线率(%)',
                  '二档人数','二档累积人数','二档累计上线率(%)',
                  '三档人数','三档累积人数','三档累计上线率(%)']
        rows = Class
        table.add(headers, rows)
        table.set_global_opts(
            title_opts=ComponentTitleOpts(title="分档成绩人数", subtitle="班级为单位")
        )
        table.render("分档表格图.html")
        result1=[]
        result1.append(Class[0][2])
        result1.append(Class[0][3])
        result1.append(Class[0][5])
        result1.append(Class[0][6])

        return result,result1
    
    
    def math_four(self):
        data=pd.read_csv('综合成绩.csv')
        x,y,execllent,fine,Pass,low,p1,p2,p3,p4=self.analysis.get_four(data)
        bar1= (
            Bar({"theme": ThemeType.MACARONS})
            .add_xaxis(x)
            .add_yaxis("人数", y)
            .set_global_opts(title_opts=opts.TitleOpts(title="平均分直方图"),
                             datazoom_opts=[opts.DataZoomOpts()],)
            
        )
        bar1.render('平均分图.html')
        
        bar2= (
            Bar({"theme": ThemeType.MACARONS})
            .add_xaxis(x)
            .add_yaxis("优秀率", execllent,color='red')
            .add_yaxis("良好率", fine,color='blue')
            .add_yaxis("及格率", Pass,color='yellow')
            .add_yaxis("低分率", low,color='green')
            .set_global_opts(title_opts=opts.TitleOpts(title="四率直方图"),
                             datazoom_opts=[opts.DataZoomOpts()],)
            
        )
        bar2.render('四率图.html')
        
        return p1,p2,p3,p4
    
    def print_png(self):
        make_snapshot(snapshot,'成绩概括面积图.html',"分段面积.png")
        make_snapshot(snapshot,'成绩概括饼图.html',"富文本饼.png")
        make_snapshot(snapshot,'一档直方图.html',"一档图.png")
        make_snapshot(snapshot,'二档直方图.html',"二档图.png")
        make_snapshot(snapshot,'四率图.html', "四率图.png")
        make_snapshot(snapshot,'平均分图.html',"平均分.png")
if __name__=="__main__":
    draw=Draw()
    draw.math_FD(30)