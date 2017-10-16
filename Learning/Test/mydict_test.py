# -*- coding:utf-8 -*-
'''
为了对新建的Dict类进行单元测试
'''

__metaclass__ = type

import unittest
from mydict import Dict


class TestDict(unittest.TestCase):

	def test_init(self):
		d = Dict(a=1, b='test')
		self.assertEquals(d.a, 1)
		self.assertEquals(d.b, 'test')
		self.assertTrue(isinstance(d, dict))

	def test_key(self):
		d = Dict()
		d['key'] = 'value'
		self.assertEquals(d.key, 'value')

	def test_attr(self):
		d = Dict()
		d.key = 'value'
		self.assertTrue('key' in d)
		self.assertEquals(d['key'], 'value')

	def test_keyerror(self):
		d = Dict()
		with self.assertRaises(KeyError):
			value = d['empty']

	def test_attrerror(self):
		d = Dict()
		with self.assertRaises(AttributeError):
			value = d.empty


if __name__ == '__main__':
	unittest.main()



#还可以插入setUp与tearDown两种方法，在测试的前后分别被执行
