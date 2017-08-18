# -*- coding: UTF-8 -*-


#练习一
import fileinput


for line in fileinput.input(inplace = True):
    line = line.strip()
    num = fileinput.lineno()
    print '%-40s # %2i' % (line, num)




#练习二
from heapq import *
from random import shuffle


data = range(10)
shuffle(data)
heap = []

for n in data:
    heappush(heap, n)




#练习三
from collections import deque 


q = deque(range(5))
q.append(5)
q.appendleft(6)




#练习四
from random import *
from time import *


date1 = (2008, 1, 1, 0, 0, 0, -1, -1, -1)
time1 = mktime(date1)
date2 = (2009, 1, 1, 0, 0, 0, -1, -1, -1)
time2 = mktime(date2)
random_time = uniform(time1, time2)

print asctime(localtime(random_time))






#练习五
from random import randrange


num = input('How many dice? ')
sides = input('How many sides per die? ')
sum = 0

for i in range(num): sum += randrange(sides) + 1

print 'The result is', sum







#fortune.py
import fileinput, random


fortunes = list(fileinput.imput())

print random.choice(fortunes)





#练习
import shelve


s = shelve.open('test.bat')
s['x'] = ['a', 'b', 'c']
s['x'].append('d')








#database.py
import sys.shelve


def store_person(db):
    """

    Query user for data and store it in the shelf object
    """

    pid = raw_input('Enter unique ID number:　')
    person = {}
    person['name'] = raw_input('Enter name: ')
    person['age'] = raw_input('Enter age: ')
    person['phone'] = raw_input('Enter phone number: ')
    
    db[pid] = person


def lookup_person(db):
    """

    Query user for ID and desired field, and fetch the corresponding data 
    the shelf object
    """

    pid = raw_input('Enter ID number: ')
    field = raw_input('What would you like to know? (name, age, phone) ')
    field = field.strip().lower()

    print field.capitalize() + ':', \
          db[pid][field]

def print_help():
    print 'The available commands are: '
    print 'store  :Stores information about a person'
    print 'lookup :Looks up a person from ID number'
    print 'quit   :Save changes and exit'
    print '?      :Prints this message'

def enter_command():
    cmd = raw_input('Enter command (? for help): ')
    cmd = cmd.strip().lower()
    return cmd

def main():
    database = shelve.open('C:\\database.bat')#目录位置可更改
    try:
        while True:
        cmd = enter_command()
        if cmd == 'store':
            store_person(database)
        elif cmd == 'lookup':
            lookup_person(database)
        elif cmd == '?':
            print help()
        elif cmd == 'quit':
            return
    finally:
        pass
    database.close()


if __name__ == '__main__': main() 
    

































