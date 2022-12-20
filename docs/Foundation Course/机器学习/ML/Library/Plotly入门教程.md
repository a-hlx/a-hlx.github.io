（Github 源代码地址：https://github.com/WillKoehrsen/Data-Analysis/blob/master/plotly/Plotly%20Whirlwind%20Introduction.ipynb）

Plotly是一个非常著名且强大的开源数据可视化框架，它通过构建基于浏览器显示的web形式的可交互图表来展示信息，可创建多达数十种精美的图表和地图，本文以ModelWhale为开发工具，详细介绍Plotly的基础内容。

// 本文所使用的数据集为 [世界大学排行榜](https://link.zhihu.com/?target=https%3A//www.heywhale.com/mw/dataset/5bfe4c5e954d6e0010682700)

```
# 加载numpy和pandas包
import numpy as np 
import pandas as pd 

# 加载plotly包
import plotly.plotly as py
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode(connected=True)
import plotly.graph_objs as go

# 云词库
from wordcloud import WordCloud

# 加载matplotlib包
import matplotlib.pyplot as plt
```

## 数据加载与特征说明

-   timesData数据包含以下14个特征:

-   world\_rank
-   university\_name
-   country
-   teaching
-   international
-   research
-   citations
-   income
-   total\_score
-   num\_students
-   student\_staff\_ratio
-   international\_students
-   female\_male\_ratio
-   year

```
# 加载数据
timesData = pd.read_csv("/home/mw/input/dataset8837/timesData.csv")
```

```
# timesData相关信息
timesData.info()
```

![](https://pic2.zhimg.com/v2-3c050071e11346e885bf8b7375d00781_b.jpg)

![](https://pic4.zhimg.com/v2-c667ae2ed3a1c281cad503b17a469bfb_b.jpg)

## Line Charts（折线图）

plotly中的graph\_objs是plotly下的子模块，用于导入plotly中所有图形对象。在根据绘图需求从graph\_objs中导入相应的obj之后，接下来需要做的事情是基于待展示的数据，为指定的obj配置相关参数，这在plotly中称为构造traces(create traces)。

1、Import graph\_objs as go

2、构造traces：

-   x ： x轴
-   y ： y轴
-   mode ： plot的类型（如marker, line ， line + markers）
-   name ： plot的名称
-   marker ： 定义点的性质，字典型

-   color ： 线的颜色，包括RGB(红，绿，蓝)和不透明度(alpha)

-   text ： 悬停文本

3、data ： 保存trace的list

4、定义layout ： 布局，字典型

-   title ： 图像的主标题
-   x axis ： 字典型

-   title ： x轴标题
-   ticklen ： x轴刻度线的长度
-   zeroline ： 是否显示零线

5、fig ： 将graph部分和layout部分组合成figure对象

6、iplot() ： 绘制由data和layout创建的图

示例图像：'Citation and Teaching**vs**World Rank of Top 100 Universities'

```
# 创建 data frame
df = timesData.iloc[:100,:]

# import graph objects as "go"
import plotly.graph_objs as go

# 设置第一条折线trace1
# go.Scatter可以创建一个散点图或者折线图的对象，我们将其命名为trace1
trace1 = go.Scatter(
                    x = df.world_rank,   # 定义坐标轴的映射关系，将world_rank这一列作为x轴
                    y = df.citations,    # 同理，将citations这一列作为y轴
                    mode = "lines",      # 我们要绘制折线图，所以将mode设置为“lines”
                    name = "citations",  # 将这条折线命名为citations
                    marker = dict(color = 'rgba(16, 112, 2, 0.8)'), 
                    # maker用来定义点的性质，如颜色、大小等
                    text= df.university_name)
                    # 将university_name一列设置为悬停文本（鼠标悬停在图片上方显示的内容）

# 设置第二条折线trace2
trace2 = go.Scatter(
                    x = df.world_rank,
                    y = df.teaching,
                    mode = "lines+markers", #绘制的折线图由散点连接而成，即lines+markers
                    name = "teaching",
                    marker = dict(color = 'rgba(80, 26, 80, 0.8)'),
                    text= df.university_name)

data = [trace1, trace2]

# 添加图层layout
layout = dict(title = 'Citation and Teaching vs World Rank of Top 100 Universities',
              # 设置图像的标题
              xaxis= dict(title= 'World Rank',ticklen= 5,zeroline= False)
              # 设置x轴名称，x轴刻度线的长度，不显示零线
             ) 

# 将data与layout组合为一个图像
fig = dict(data = data, layout = layout)
# 绘制图像
iplot(fig)
```

![](https://pic3.zhimg.com/v2-f9a6cb3dfca0fa898ba087b87d10ba1e_b.jpg)

## Scatter Charts（散点图）

示例图像: Citation**vs**world rank of top 100 universities with 2014, 2015 and 2016 years

```
# 创建 data frames
df2014 = timesData[timesData.year == 2014].iloc[:100,:]
df2015 = timesData[timesData.year == 2015].iloc[:100,:]
df2016 = timesData[timesData.year == 2016].iloc[:100,:]
# import graph objects as "go"
import plotly.graph_objs as go
# 创建 trace1
trace1 =go.Scatter(
                    x = df2014.world_rank,
                    y = df2014.citations,
                    mode = "markers",
                    name = "2014",
                    marker = dict(color = 'rgba(255, 128, 255, 0.8)'),
                    text= df2014.university_name)
# 创建 trace2
trace2 =go.Scatter(
                    x = df2015.world_rank,
                    y = df2015.citations,
                    mode = "markers",
                    name = "2015",
                    marker = dict(color = 'rgba(255, 128, 2, 0.8)'),
                    text= df2015.university_name)
# 创建 trace3
trace3 =go.Scatter(
                    x = df2016.world_rank,
                    y = df2016.citations,
                    mode = "markers",
                    name = "2016",
                    marker = dict(color = 'rgba(0, 255, 200, 0.8)'),
                    text= df2016.university_name)
data = [trace1, trace2, trace3]
layout = dict(title = 'Citation vs world rank of top 100 universities with 2014, 2015 and 2016 years',
              xaxis= dict(title= 'World Rank',ticklen= 5,zeroline= False),
              yaxis= dict(title= 'Citation',ticklen= 5,zeroline= False)
             )
fig = dict(data = data, layout = layout)
iplot(fig)
```

![](https://pic1.zhimg.com/v2-4d7f3a2115e18d980268979be7a03ad4_b.jpg)

## Bar Charts（柱状图）

示例图像一: 2014年全国大学排名前三名的引文与教学情况(style1)

```
# 准备 data frames
df2014 = timesData[timesData.year == 2014].iloc[:3,:]
df2014
```

![](https://pic3.zhimg.com/v2-0d6544dfd552adc7c3f72a4032376216_b.jpg)

```
# 准备 data frames
df2014 = timesData[timesData.year == 2014].iloc[:3,:]
# import graph objects as "go"
import plotly.graph_objs as go

# go.Bar可以创建一个柱状图对象，我们将其命名为trace1
# 构造 trace1 
trace1 = go.Bar(
                x = df2014.university_name,
                y = df2014.citations,
                name = "citations",
                marker = dict(color = 'rgba(255, 174, 255, 0.5)',
                             line=dict(color='rgb(0,0,0)',width=1.5)),
                text = df2014.country)
# 构造 trace2 
trace2 = go.Bar(
                x = df2014.university_name,
                y = df2014.teaching,
                name = "teaching",
                marker = dict(color = 'rgba(255, 255, 128, 0.5)',
                              line=dict(color='rgb(0,0,0)',width=1.5)),
                text = df2014.country)
data = [trace1, trace2]
# barmode：设置条形图的形式，“group”为分组条形图
layout = go.Layout(barmode = "group")   
fig = go.Figure(data = data, layout = layout)
iplot(fig)
```

![](https://pic1.zhimg.com/v2-28aa17e13255c09f073d5f176293e228_b.jpg)

示例图像二: 2014年全国大学排名前三名的引文与教学情况(style2)

PS:实际上，在前面的示例中只将`barmode`从`group`更改为`stack`，就可以实现在这里所做的操作。本例使用了不同的语法。

```
# 准备 data frames
df2014 = timesData[timesData.year == 2014].iloc[:3,:]
# import graph objects as "go"
import plotly.graph_objs as go

x = df2014.university_name

trace1 = {
  'x': x,
  'y': df2014.citations,
  'name': 'citation',
  'type': 'bar'
};
trace2 = {
  'x': x,
  'y': df2014.teaching,
  'name': 'teaching',
  'type': 'bar'
};
data = [trace1, trace2];
layout = {
  'xaxis': {'title': 'Top 3 universities'},
  'barmode': 'stack',   # 条形图形式设置为堆积条形图
  'title': 'citations and teaching of top 3 universities in 2014'
};
fig = go.Figure(data = data, layout = layout)
iplot(fig)
```

![](https://pic1.zhimg.com/v2-56385f4650dc359eb00fee2a3e7b31f4_b.jpg)

示例三: 水平条形图(style3)， Citation **vs** income for universities

-   Import graph\_objs as go 并且 import tools

-   Tools: 用于创建子图

-   构造 trace1

-   bar: 柱状图

-   x = x 轴
-   y = y 轴
-   marker

-   color: 每个bar的颜色
-   line: bar的边框颜色和宽度

-   name: bar的名称
-   orientation: bar的方向：例如水平（horizontal）

-   构造 trace2
-   scatter: 散点图

-   x = x 轴
-   y = y 轴
-   mode: 设置散点图类型为 `'line + markers'`
-   line: 线的属性
-   color: 线的颜色
-   name: 散点图的名称

-   layout: 添加 axis, legend(图例), margin（旁注）, paper 和 plot properties

```
# import graph objects as "go" and import tools
import plotly.graph_objs as go
from plotly import tools
import matplotlib.pyplot as plt
# 准备 data frames
df2016 = timesData[timesData.year == 2016].iloc[:7,:]

y_saving = [each for each in df2016.research]
y_net_worth  = [float(each) for each in df2016.income]
x_saving = [each for each in df2016.university_name]
x_net_worth  = [each for each in df2016.university_name]
trace0 = go.Bar(
                x=y_saving,
                y=x_saving,
                marker=dict(color='rgba(171, 50, 96, 0.6)',line=dict(color='rgba(171, 50, 96, 1.0)',width=1)),
                name='research',
                orientation='h',    # Bar的方向设置为水平（horizontal）
)
trace1 = go.Scatter(
                x=y_net_worth,
                y=x_net_worth,
                mode='lines+markers',
                line=dict(color='rgb(63, 72, 204)'),
                name='income',
)
layout = dict(
                title='Citations and income',
                yaxis=dict(showticklabels=True,domain=[0, 0.85]),  # showticklables用来决定是否显示每个bar的旁注，domain用来设置y轴长度
                yaxis2=dict(showline=True,showticklabels=False,linecolor='rgba(102, 102, 102, 0.8)',linewidth=2,domain=[0, 0.85]),
                xaxis=dict(zeroline=False,showline=False,showticklabels=True,showgrid=True,domain=[0, 0.42]),
                xaxis2=dict(zeroline=False,showline=False,showticklabels=True,showgrid=True,domain=[0.47, 1],side='top',dtick=25),
                legend=dict(x=0.029,y=1.038,font=dict(size=10) ),  #设置图例标志的大小和位置
                margin=dict(l=200, r=20,t=70,b=70), # 设置bar旁注的长度、大小等
                paper_bgcolor='rgb(248, 248, 255)', # 设置整个面板的背景色
                plot_bgcolor='rgb(248, 248, 255)',  # 设置图像部份的背景色
)
annotations = []
y_s = np.round(y_saving, decimals=2)
y_nw = np.rint(y_net_worth)
# 添加 labels
for ydn, yd, xd in zip(y_nw, y_s, x_saving):
    # 标注散点图
    annotations.append(dict(xref='x2', yref='y2', y=xd, x=ydn - 4,text='{:,}'.format(ydn),font=dict(family='Arial', size=12,color='rgb(63, 72, 204)'),showarrow=False))
    # 标注条形图
    annotations.append(dict(xref='x1', yref='y1', y=xd, x=yd + 3,text=str(yd),font=dict(family='Arial', size=12,color='rgb(171, 50, 96)'),showarrow=False))

layout['annotations'] = annotations

# 创建两个子图
fig = tools.make_subplots(rows=1, cols=2, specs=[[{}, {}]], shared_xaxes=True,
                          shared_yaxes=False, vertical_spacing=0.001)

fig.append_trace(trace0, 1, 1)
fig.append_trace(trace1, 1, 2)

fig['layout'].update(layout)
iplot(fig)
```

This is the format of your plot grid:  
\[ (1,1) x1,y1 \] \[ (1,2) x2,y2 \]  

![](https://pic4.zhimg.com/v2-6bf92365fa6a0288aab4feb8d6148bbb_b.jpg)

Pie Charts（饼图）

示例: Students rate of top 7 universities in 2016

-   fig: 创建图形

-   data:

-   values: 值
-   labels: 标签
-   name: 名称
-   hoverinfo: 悬停文本
-   hole: 孔宽
-   type: 图像类型，如pie

-   layout: 布局

-   title: 标题
-   annotations: font, showarrow, text, x, y

```
# 准备数据
df2016 = timesData[timesData.year == 2016].iloc[:7,:]
pie1 = df2016.num_students
pie1_list = [float(each.replace(',', '.')) for each in df2016.num_students]  # str(2,4) => str(2.4) = > float(2.4) = 2.4
labels = df2016.university_name
# figure
fig = {
  "data": [
    {
      "values": pie1_list,
      "labels": labels,
      "domain": {"x": [0, .5]},
      "name": "Number Of Students Rates",
      "hoverinfo":"label+percent+name",
      "hole": .3,
      "type": "pie"
    },],
  "layout": {
        "title":"Universities Number of Students rates",
        "annotations": [
            { "font": { "size": 20},
              "showarrow": False,
              "text": "Number of Students",
                "x": 0.20,
                "y": 1
            },
        ]
    }
}
iplot(fig)
```

![](https://pic3.zhimg.com/v2-8d3d9cf33bcd65e2635451356cadd60e_b.jpg)

## Bubble Charts（冒泡图）

冒泡图示例: University world rank (first 20) **vs** teaching score with number of students(size) and international score (color) in 2016

-   x ：x 轴
-   y ：y 轴
-   mode ：markers(scatter)
-   marker ：marker的属性

-   color
-   size

-   text: university names

<class 'pandas.core.frame.DataFrame'>  
Int64Index: 7 entries, 1803 to 1809  
Data columns (total 14 columns):  
world\_rank 7 non-null object  
university\_name 7 non-null object  
country 7 non-null object  
teaching 7 non-null float64  
international 7 non-null object  
research 7 non-null float64  
citations 7 non-null float64  
income 7 non-null object  
total\_score 7 non-null object  
num\_students 7 non-null object  
student\_staff\_ratio 7 non-null float64  
international\_students 7 non-null object  
female\_male\_ratio 6 non-null object  
year 7 non-null int64  
dtypes: float64(4), int64(1), object(9)  
memory usage: 840.0+ bytes

```
# 准备数据
df2016 = timesData[timesData.year == 2016].iloc[:20,:]
num_students_size  = [float(each.replace(',', '.')) for each in df2016.num_students]
international_color = [float(each) for each in df2016.international]
data = [
    {
        'y': df2016.teaching,
        'x': df2016.world_rank,
        'mode': 'markers',
        'marker': {
            'color': international_color,
            'size': num_students_size,
            'showscale': True
        },
        "text" :  df2016.university_name    
    }
]
iplot(data)
```

![](https://pic1.zhimg.com/v2-660d3666cad36f73f5716b89294f2724_b.jpg)

## Histogram（直方图）

让我们看一下2011年和2012年学生与员工比例的直方图：'students-staff ratio in 2011 and 2012 years'

-   trace1 ： 第一个直方图

-   x ： x 轴
-   y ： y 轴
-   opacity ： histogram的不透明度
-   name ： 图例名称
-   marker ： histogram的颜色

-   trace2 ： 第二个直方图
-   layout ： 布局

-   barmode ： 直方图模式，如`overlay`，`stack`

```
# 准备数据
x2011 = timesData.student_staff_ratio[timesData.year == 2011]
x2012 = timesData.student_staff_ratio[timesData.year == 2012]

trace1 = go.Histogram(
    x=x2011,
    opacity=0.75,
    name = "2011",
    marker=dict(color='rgba(171, 50, 96, 0.6)'))
trace2 = go.Histogram(
    x=x2012,
    opacity=0.75,
    name = "2012",
    marker=dict(color='rgba(12, 50, 196, 0.6)'))

data = [trace1, trace2]
layout = go.Layout(barmode='overlay',
                   title=' students-staff ratio in 2011 and 2012',
                   xaxis=dict(title='students-staff ratio'),
                   yaxis=dict( title='Count'),
)
fig = go.Figure(data=data, layout=layout)
iplot(fig)
```

![](https://pic4.zhimg.com/v2-dbef01e584b26da34138dbd2468335f3_b.jpg)

## Word Cloud（词云）

不是pyplot，但学习词云对于可视化很有帮助。让我们看看2011年哪个国家被提及最多。

-   WordCloud ： 导入的词云库

-   background\_color ：背景颜色
-   generate ： 生成国家/地区名称列表（x2011）词云

```
# 准备数据
x2011 = timesData.country[timesData.year == 2011]
plt.subplots(figsize=(8,8))
wordcloud = WordCloud(
                          background_color='white',
                          width=512,
                          height=384
                         ).generate(" ".join(x2011))
plt.imshow(wordcloud)
plt.axis('off')
plt.savefig('graph.png')

plt.show()
```

![](https://pic1.zhimg.com/v2-49701112fb1d544e117173055bc3afc8_b.jpg)

## Box Plots（箱型图）

盒图(boxplot)对于显示数据的离散的分布情况效果不错

![](https://pic2.zhimg.com/v2-7fa1f6c6910175c34482a0d86f1b9691_b.jpg)

盒图是在1977年由美国的统计学家约翰·图基(John Tukey)发明的。它由五个数值点组成：最小值(min)，下四分位数(Q1)，中位数(median)，上四分位数(Q3)，最大值(max)。也可以往盒图里面加入平均值(mean)。如上图。下四分位数、中位数、上四分位数组成一个“带有隔间的盒子”。上四分位数到最大值之间建立一条延伸线，这个延伸线成为“胡须(whisker)”。

由于现实数据中总是存在各式各样地“脏数据”，也成为“离群点”，于是为了不因这些少数的离群数据导致整体特征的偏移，将这些离群点单独汇出，而盒图中的胡须的两级修改成最小观测值与最大观测值。这里有个经验，就是最大(最小)观测值设置为与四分位数值间距离为1.5个IQR(中间四分位数极差)。即：

![](https://pic1.zhimg.com/v2-4b7aff49a173e0e6b529a7afdc0cdc7c_b.jpg)

-   IQR = Q3-Q1，即上四分位数与下四分位数之间的差，也就是盒子的长度。
-   最小观测值为min = Q1 - 1.5\* IQR，如果存在离群点小于最小观测值，则胡须下限为最小观测值，离群点单独以点汇出。如果没有比最小观测值小的数，则胡须下限为最小值。
-   最大观测值为max = Q3 -1.5\* IQR，如果存在离群点大于最大观测值，则胡须上限为最大观测值，离群点单独以点汇出。如果没有比最大观测值大的数，则胡须上限为最大值。

通过盒图，在分析数据的时候，盒图能够有效地帮助我们识别数据的特征：

-   直观地识别数据集中的异常值(查看离群点)。
-   判断数据集的数据离散程度和偏向(观察盒子的长度，上下隔间的形状，以及胡须的长度)

_以上内容引自该博客：[https://www.cnblogs.com/tsingke/p/6565605.html](https://link.zhihu.com/?target=https%3A//www.cnblogs.com/tsingke/p/6565605.html)_

```
# 准备数据
x2015 = timesData[timesData.year == 2015]

trace0 = go.Box(
    y=x2015.total_score,
    name = 'total score of universities in 2015',
    marker = dict(
        color = 'rgb(12, 12, 140)',
    )
)
trace1 = go.Box(
    y=x2015.research,
    name = 'research of universities in 2015',
    marker = dict(
        color = 'rgb(12, 128, 128)',
    )
)
data = [trace0, trace1]
iplot(data)
```

![](https://pic1.zhimg.com/v2-529eee18978c7c80020430388b596374_b.jpg)

## ScatterPlot Matrix（散点图矩阵）

Scatter Matrix ： 散点图矩阵允许同时看到多个单独变量的分布和它们两两之间的关系

-   import figure factory as ff
-   create\_scatterplotmatrix ：创建散点图

-   data2015 ：用到的数据，即索引1-401之间的 `research`, `international` 和 `total scores` 三个变量
-   colormap ：色盘
-   colormap\_type ：色盘类型
-   height

-   weight

```
# import figure factory
import plotly.figure_factory as ff
# 准备数据
dataframe = timesData[timesData.year == 2015]
data2015 = dataframe.loc[:,["research","international", "total_score"]]
data2015["index"] = np.arange(1,len(data2015)+1)
# 绘制散点图矩阵
fig = ff.create_scatterplotmatrix(data2015, diag='box', index='index',colormap='Portland',
                                  colormap_type='cat',
                                  height=700, width=700)
iplot(fig)
```

![](https://pic2.zhimg.com/v2-a06fe3d928c046d6d3bf8ea5cd27e595_b.jpg)

## Inset Plots（内置图）

-   Inset Matrix ： 2个图在一个窗口中

内置图示例：'Income and Teaching **vs** World Rank of Universities'

```
# 第一个线型图
trace1 = go.Scatter(
    x=dataframe.world_rank,
    y=dataframe.teaching,
    name = "teaching",
    marker = dict(color = 'rgba(16, 112, 2, 0.8)'),
)
# 第二个线型图
trace2 = go.Scatter(
    x=dataframe.world_rank,
    y=dataframe.income,
    xaxis='x2',
    yaxis='y2',
    name = "income",
    marker = dict(color = 'rgba(160, 112, 20, 0.8)'),
)
data = [trace1, trace2]
layout = go.Layout(
    xaxis2=dict(
        domain=[0.6, 0.95],
        anchor='y2',        
    ),
    yaxis2=dict(
        domain=[0.6, 0.95],
        anchor='x2',
    ),
    title = 'Income and Teaching vs World Rank of Universities'

)

fig = go.Figure(data=data, layout=layout)
iplot(fig)
```

![](https://pic4.zhimg.com/v2-1580d3ace99c9171337f5028329d8c6b_b.jpg)

## 3D Scatter Plot (3D散点图)

3D Scatter: 有时2D不足以理解数据。因此，添加一个维度会增加数据的可懂度。

-   go.Scatter3d: 创建三维散点图
-   x,y,z: 图像的3个轴
-   mode: 设置为scatter
-   size: marker的大小
-   color: 色卡

```
# 构造3D散点图trace1
trace1 = go.Scatter3d(
    x=dataframe.world_rank,
    y=dataframe.research,
    z=dataframe.citations,
    mode='markers',
    marker=dict(
        size=10,
        color='rgb(72,61,139)',     # RGB颜色对照表可参考：https://tool.oschina.net/commons?type=3    
    )
)

data = [trace1]
layout = go.Layout(
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0  
    )
    
)
fig = go.Figure(data=data, layout=layout)
iplot(fig)
```

![](https://pic1.zhimg.com/v2-2f67d26dff5964df9452262351aba2b0_b.jpg)

## Multiple Subplots（多子图）

Multiple Subplots: 在比较多个特征时，多个子图很有效。

```
trace1 = go.Scatter(
    x=dataframe.world_rank,
    y=dataframe.research,
    name = "research"
)
trace2 = go.Scatter(
    x=dataframe.world_rank,
    y=dataframe.citations,
    xaxis='x2',
    yaxis='y2',
    name = "citations"
)
trace3 = go.Scatter(
    x=dataframe.world_rank,
    y=dataframe.income,
    xaxis='x3',
    yaxis='y3',
    name = "income"
)
trace4 = go.Scatter(
    x=dataframe.world_rank,
    y=dataframe.total_score,
    xaxis='x4',
    yaxis='y4',
    name = "total_score"
)
data = [trace1, trace2, trace3, trace4]
layout = go.Layout(
    xaxis=dict(
        domain=[0, 0.45]
    ),
    yaxis=dict(
        domain=[0, 0.45]
    ),
    xaxis2=dict(
        domain=[0.55, 1]
    ),
    xaxis3=dict(
        domain=[0, 0.45],
        anchor='y3'
    ),
    xaxis4=dict(
        domain=[0.55, 1],
        anchor='y4'
    ),
    yaxis2=dict(
        domain=[0, 0.45],
        anchor='x2'
    ),
    yaxis3=dict(
        domain=[0.55, 1]
    ),
    yaxis4=dict(
        domain=[0.55, 1],
        anchor='x4'
    ),
    title = 'Research, citation, income and total score VS World Rank of Universities'
)
fig = go.Figure(data=data, layout=layout)
iplot(fig)
```

![](https://pic1.zhimg.com/v2-07fcd952e4b5049552a48ee1dc466fdc_b.jpg)

本项目根据[Plotly Tutorial for Beginners](https://link.zhihu.com/?target=https%3A//www.kaggle.com/artemseleznev/plotly-tutorial-for-beginners)进行编译，若有错误，欢迎大家在评论区指出。

欢迎进入[和鲸社区](https://link.zhihu.com/?target=https%3A//www.kesci.com/)使用K-Lab进行调试学习。

转载本文请联系**[和鲸](https://link.zhihu.com/?target=https%3A//www.heywhale.com/)**取得授权，**[和鲸社区](https://link.zhihu.com/?target=https%3A//www.heywhale.com/about)**是聚合数据人才和行业问题的在线社区，率先打造国内首款K-Lab 在线数据分析协作平台，为数据工作者的学习与工作带来全新的体验。