文件的目的：用一种逻辑方式存储数据，以便读取、更新
存储在一个文件的数据是特定的
### **3.2**python数据类型
解释性语言
数字-->字符串 str()
字符串-->数值变量int()/float()
print(a,b,c,d)一次可打印多个变量
添加空行  \n在字符串变量中
sys.copyright
sys.platform
sys.version

import datetime
from datetime import datetime,timezone
datetime.now()


input()获取用户的输入，返回字符串，读取键盘的输入

三引号括起长文本

用户输入不合法的输入值，，处理错误
try.....except  捕捉错误
有问题的代码行在try：块，有错误：except：中的代码会运行，任何情况下程序都会继续运行

每行一个显著的项的方式读取数据，读入一个变量中

操作文本
open（'文件名'，‘打开模式‘）
打开模式："r":打开文件读取数据,"w"：写入文件,"a"：添加数据,"r+":读取和写入,"w+：些如何读取","a+"：添加和读取数据
file=open("data.txt","r")
file.close()操作完成后要关闭文件

file.write()将文本数据写入到文件
writeline()单独一行写入文件
file=open("date2.txt","w")
file.write("sample file writing\n")为保存为单独一行加入\n
file.write("this is line 2\n")
file.close()

file=open("data.txt","r")
file.read(n)每次读取一个字符，n是读取的字符的数目
char=file.read(10)
print(char)从当前文件夹指针位置读取10个字符
all_data=file.read()
print(all_data)整个文件读入到一个字符变量中

file.readline(n)读取整行文本数据，n表示从当前行读入的字符的数目

file.readlines()读取数据文件中所有的行，会创建一个列表，每行是列表的一项
打印列表变量中的数据，
可以用for循环，像数组一样索引列表
string.strip()删去行末的换行字符

3.3.2 操作二进制文件
用二进制文件读取PNG位图文件
python读取数据并提供到缓存中以供使用
二进制文件模式
"rb":打开二进制文件读取数据
"wb"
"ab"
"rb+"
"wb+"
"ab+"

写二进制文件
struct库：将数据打包的到一个字符串中，并进行输出的功能

**代码要打开的文件必须和代码在同一个目录下，open（）会新建文件**

从二进制文件中读取
struct.calcsize()计算int类型大小
struct.unpack()针对每个数字读多少字节

##用pygame打印文本
##pygame将文本以图形化模式打印到屏幕上
pygame.font--->图形模式按字体打印文本
myfont=pygame.font.Font('字体'，’大小‘)
font.render()使用文本创建位图
screen.blit()将位图绘制屏幕上










