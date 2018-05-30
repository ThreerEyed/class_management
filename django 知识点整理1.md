## django 知识点整理1



### 常见的过滤器


一、形式：小写

{{ name | lower }}

 

二、过滤器是可以嵌套的，字符串经过三个过滤器，第一个过滤器转换为小写，第二个过滤器输出首字母，第三个过滤器将首字母转换成大写

标签

{{ str|lower|first|upper }}

 

三、过滤器的参数

显示前30个字

{{ bio | truncatewords:"30" }}

格式化

{{ pub_date | date:"F j, Y" }}

过滤器列表

{{ 123|add:"5" }} 给value加上一个数值

{{ "AB'CD"|addslashes }} 单引号加上转义号，一般用于输出到javascript中

{{ "abcd"|capfirst }} 第一个字母大写

{{ "abcd"|center:"50" }} 输出指定长度的字符串，并把值对中

{{ "123spam456spam789"|cut:"spam" }} 查找删除指定字符串

{{ value|date:"F j, Y" }} 格式化日期

{{ value|default:"(N/A)" }} 值不存在，使用指定值

{{ value|default_if_none:"(N/A)" }} 值是None，使用指定值

{{ 列表变量|dictsort:"数字" }} 排序从小到大

{{ 列表变量|dictsortreversed:"数字" }} 排序从大到小

{% if 92|pisibleby:"2" %} 判断是否整除指定数字

{{ string|escape }} 转换为html实体

{{ 21984124|filesizeformat }} 以1024为基数，计算最大值，保留1位小数，增加可读性

{{ list|first }} 返回列表第一个元素

{{ "ik23hr&jqwh"|fix_ampersands }} &转为&

{{ 13.414121241|floatformat }} 保留1位小数，可为负数，几种形式

{{ 13.414121241|floatformat:"2" }} 保留2位小数

{{ 23456 |get_digit:"1" }} 从个位数开始截取指定位置的1个数字

{{ list|join:", " }} 用指定分隔符连接列表

{{ list|length }} 返回列表个数

{% if 列表|length_is:"3" %} 列表个数是否指定数值

{{ "ABCD"|linebreaks }} 用新行用

、
标记包裹

{{ "ABCD"|linebreaksbr }} 用新行用
标记包裹

{{ 变量|linenumbers }} 为变量中每一行加上行号

{{ "abcd"|ljust:"50" }} 把字符串在指定宽度中对左，其它用空格填充

{{ "ABCD"|lower }} 小写

{% for i in "1abc1"|make_list %}ABCDE,{% endfor %} 把字符串或数字的字符个数作为一个列表

{{ "abcdefghijklmnopqrstuvwxyz"|phone2numeric }} 把字符转为可以对应的数字？？

{{ 列表或数字|pluralize }} 单词的复数形式，如列表字符串个数大于1，返回s，否则返回空串

{{ 列表或数字|pluralize:"es" }} 指定es

{{ 列表或数字|pluralize:"y,ies" }} 指定ies替换为y

{{ object|pprint }} 显示一个对象的值

{{ 列表|random }} 返回列表的随机一项

{{ string|removetags:"br p p" }} 删除字符串中指定html标记

{{ string|rjust:"50" }} 把字符串在指定宽度中对右，其它用空格填充

{{ 列表|slice:":2" }} 切片

{{ string|slugify }} 字符串中留下减号和下划线，其它符号删除，空格用减号替换

{{ 3|stringformat:"02i" }} 字符串格式，使用Python的字符串格式语法

{{ "EABCD"|striptags }} 剥去[X]HTML语法标记

{{ 时间变量|time:"P" }} 日期的时间部分格式

{{ datetime|timesince }} 给定日期到现在过去了多少时间

{{ datetime|timesince:"other_datetime" }} 两日期间过去了多少时间

{{ datetime|timeuntil }} 给定日期到现在过去了多少时间，与上面的区别在于2日期的前后位置。

{{ datetime|timeuntil:"other_datetime" }} 两日期间过去了多少时间

{{ "abdsadf"|title }} 首字母大写

{{ "A B C D E F"|truncatewords:"3" }} 截取指定个数的单词

{{ "111221"|truncatewords_html:"2" }} 截取指定个数的html标记，并补完整

 

{{ list|unordered_list }}
多重嵌套列表展现为html的无序列表

{{ string|upper }} 全部大写

linkage url编码

{{ string|urlize }} 将URLs由纯文本变为可点击的链接。 

{{ string|urlizetrunc:"30" }} 同上，多个截取字符数。 

{{ "B C D E F"|wordcount }} 单词数

{{ "a b c d e f g h i j k"|wordwrap:"5" }} 每指定数量的字符就插入回车符

{{ boolean|yesno:"Yes,No,Perhaps" }} 对三种值的返回字符串，对应是 非空,空,None





### 静态文件加载

1. load的方式

- 使用这种方式需要注意,  在<!DOCTYPE html> 下需要加载 {% load staticfiles %}

```django
<img src='{% static 'img/xxx.ipg' %}'/>
```

2. 写路径的方式

```django
<img src='/static/img/xxx.jpg'/>
```





### 虚拟环境的创建

虽然使用 pycharm 我们可以很方便的创建出一个虚拟环境,  但是我们每次都需要创建一个新的虚拟环境这样太花费时间,  也显得很业余,  并且我们并不是总是能使用pycharm 创建虚拟环境,  所以单独创建一个django 适用的虚拟环境是一个不错的办法。



在一个指定的空文件夹下使用如下命令。

```django
pip install virtualenv
virtualenv --no-site-packages 虚拟环境名
```

注意上面第二个命令中的参数 --no-site-packages  这个参数可以保证我们创建的虚拟环境是干净的， 没有其他的东西。

```
pip freeze   # 查看我们通过install安装过的包  
pip list     # 查看我们所有安装过的包(包括系统自带的)
```

安装django  :

```
pip install django==1.11
```

安装pymsql  :

```
pip install pymysql
```





### 通过虚拟环境创建项目

首先我们得先激活虚拟环境windows  下和mac  以及Linux 下略有不同 . 

激活之后创建项目以及APP应用

```
django-admin startproject 项目名

python manage.py startapp app名
```

创建完成之后更改 __init__ 文件和修改配置即可

```
import pymysql
pymysql.install_as_MySQLdb()
```



运行

```
python manage.py runserver
```

可以查看项目是否创建成功





### 分页功能(paginator)

```python
class Paginator(object)  
	def __init__(self, object_list, per_page, orphans=0,                  					allow_empty_first_page=True)
```

```python
def grade(request):

    if request.method == 'GET':
        page_num = request.GET.get('page_num', 1)
        grades = Grade.objects.all()
        paginator = Paginator(grades, 3)
        pages = paginator.page(int(page_num))
        return render(request, 'grade.html', {'grades': grades, 'pages': pages})
```

以上代码实现一个分页的功能显示,

paginator  是一个实例化对象 

has_next  是否有下一页

has_previous  是否有上一页

next_page_number   上一页的代码

previous_page_number   下一个的页码





### get and filter



- ##### get

django的get方法是从数据库的取得一个匹配的结果，返回一个对象，如果记录不存在的话，它会报错。 

比如我数据库里有一条记录，记录的name的值是老王python的话，我用student = Student.objects.get(name=’老王python’)， 

返回的是一个记录对象，你可以通过student . _ _ dict _ _来查看，它返回的是一个字典的形式，｛’key’:valeus｝,key是字段的名称，而values是值的内容。 

而如果我用get方法来查询一个数据库里不存在的记录，程序会报错。 

比如:`student = Student.objects.get(name='老王')`,你自己可以运行看下。 



如果你用django的get去取得关联表的数据的话，而关键表的数据如果多于2条的话也会报错。 



- ##### filter

django的filter方法是从数据库的取得匹配的结果，返回一个对象列表，如果记录不存在的话，它会返回[]。 

比如我数据库里有一条记录，记录的name的值是老王python的话，我用 

`student = Student.objects.filter(name='老王python').first()` 

它返回的student是一个对象的列表，可以看的出来student[0]和上面的get方式返回的student的结果是一样的。 