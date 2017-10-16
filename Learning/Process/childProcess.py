# -*- coding:utf-8 -*-


'''
启动一个子进程并等待其结束
'''

from multiprocessing import Process
import os


def run_proc(name):
	print 'Run child process %s (%s)...' % (name, os.getpid())

if __name__ == '__main__':
	print "Parent process %s." % os.getpid()
	p = Process(target=run_proc, args=('test',))
	print 'Process will start.'
	p.start()
	p.join()
	print 'Process end'





'''
运行结果：
Parent process 5080.
Process will start.
Run child process test <6016>...
Process end
'''
