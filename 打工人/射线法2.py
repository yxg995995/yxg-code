from fractions import Fraction 
def isPointinPolygon(pointlist, rangelist):#射线法先判断点是否在大多边形里面
    # 判断是否在外包矩形内，如果不在，直接返回false
    xlist = []#装大多边形的点的横坐标
    ylist = []#装大多边形的点的纵坐标
    for i in range(len(rangelist)-1):
        xlist.append(rangelist[i][0])
        ylist.append(rangelist[i][1])
    maxx = max(xlist)
    minx = min(xlist)
    maxy = max(ylist)
    miny = min(ylist)
    #判断点是否大于外包矩阵的x,y或者小于外包矩阵的x,y
    for point in pointlist:
        if (point[0] > maxx or point[0] < minx or
            point[1] > maxy or point[1] < miny):
            print('小图形不在大图形里面')
            return False
    count = 0
    point1 = rangelist[0]
    for point in pointlist:
        for i in range(1, len(rangelist)):
            point2 = rangelist[i]
            # 点与多边形顶点重合
            if ((point[0] == point1[0] and point[1] == point1[1]) or
                (point[0] == point2[0] and point[1] == point2[1])):
                print('小图形不在大图形里面')
                return False
            # 判断线段两端点是否在射线两侧 不在肯定不相交 射线（-∞，lat）（lng,lat）
            if (point1[1] < point[1] and point2[1] >= point[1]) or (point1[1] >= point[1] and point2[1] < point[1]):
                # 求线段与射线交点 再和lat比较
                point12lng = point2[0] - (point2[1] - point[1]) * (point2[0] - point1[0])/(point2[1] - point1[1])
                # 点在多边形边上
                if (point12lng == point[0]):
                    print("小图形不在大图形里面")
                    return False
                if (point12lng < point[0]):
                    count +=1
            point1 = point2
        if count%2 == 0:
            print('小图形不在大图形里面')
            return False
        else:
            print('点在大图形里面')
            return True

def line(line):#生成多边型每条边的函数形式并且输入x,y的范围
    result=[]
    for i in range(len(line)):
        if i==len(line)-1:
            break
        if line[i][1]==line[i+1][1]:#形如x=b
            a=0
            b=line[i][1]
            result.append([a,b,line[i][0],line[i+1][0],line[i][1],line[i+1][1]])
        elif line[i][0]==line[i+1][0]:#形如y=b
            a='不存在系数'
            b=0
            result.append([a,b,line[i][0],line[i+1][0],line[i][1],line[i+1][1]])
        else:#形如y=ax+b
            a=(line[i+1][1]-line[i][1])/(line[i+1][0]-line[i][0])
            b=line[i][1]-a*line[i][0]
            result.append([a,b,line[i][0],line[i+1][0],line[i][1],line[i+1][1]])
    return result


def islineinPolygon(pointlist,rangelist):#判断两个多边形的边是否相交
    pointline=line(pointlist)
    rangeline=line(rangelist)
    x=0
    y=0
    for i in pointline:
        for j in rangeline:
            if i[0]=='不存在系数' and j[0]=='不存在系数':#两条边都为x=b的形式一定是平行或者重合
                x=0
            if i[0]=='不存在系数':#小多边形的边为x=b形式
                y=j[0]*i[2]+j[1]
                if y>min(j[4:]) and y<max(j[4:]) and y>min(i[4:]) and y<max(i[4:]):
                    return print('小图形不在大图形里面')
            if j[0]=='不存在系数':#大多边形的边为x=b形式
                y=i[0]*j[2]+i[1]
                if y>min(j[4:]) and y<max(j[4:]) and y>min(i[4:]) and y<max(i[4:]):
                    return print('小图形不在大图形里面')
            if i[0]!=j[0] and i[0]!='不存在系数' and j[0]!='不存在系数':
                x=(j[1]-i[1])/(i[0]-j[0])
                if x>min(j[2:4]) and x<max(j[2:4]) and x>min(i[2:4]) and x<max(i[2:4]):
                    return print('小图形不在大图形里面')
    print('小图形在大图形里面')


if __name__ == '__main__':
    #大多边形构成的坐标点，开始点和最后的点要一样
    l=[[0,4],[3,2],[1,0],[3,-2],[0,-4],[-3,-2],[-1,0],[-3,2],[0,4]]
    #小多边形构成的坐标点，开始点和最后的点要一样
    pointlist=[[-2,2],[2,-2],[-2,-2],[-2,2]]
    if isPointinPolygon(pointlist, l):
        islineinPolygon(pointlist,l)
        
        
