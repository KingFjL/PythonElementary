import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
hash = {}#新建一个空字典
n = int(raw_input())  # Number of elements which make up the association table.
q = int(raw_input())  # Number Q of file names to be analyzed.
for i in xrange(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = raw_input().split()
    hash[ext.lower()] = mt#将ext（不区分大小写）作为键，mt作为键值加入到hash字典中
    
for i in xrange(q):
    fname = raw_input()  # One file name per line.
    if '.' in fname:
        fname = fname.split('.')[-1]
        """
        分片操作：语法：str.split(str="",num=string.count(str))[n]
        参数说明：
           str：   表示为分隔符，默认为空格，但是不能为空('')。若字符串中没有分隔符，则把整个字符串作为列表的一个元素
           num：表示分割次数。如果存在参数num，则仅分隔成 num+1 个子字符串，并且每一个子字符串可以赋给新的变量
           [n]：   表示选取第n个分片
           注意：当使用空格作为分隔符时，对于中间为空的项会自动忽
        """
        print hash.get(fname.lower(), 'UNKNOWN')#get()函数得到键值，存在返回键值，不存在返回设定值‘UNKNOWN’（默认值为None）
    else:
        print 'UNKNOWN'
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."


# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.

