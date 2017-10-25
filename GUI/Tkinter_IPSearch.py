# -*- coding:utf-8 -*-

'''
Python GUI 是实现根据IP地址定位地理位置
由于离线查询IP需要全球的分布数据，因此选择免费离线查询IP的数据包，
读取该数据包需要安装pygeoip模块
'''


import Tkinter
import pygeoip

class FindLocation(object):

	def __init__(self):
		self.gi = pygeoip.GeoIP("C:\\Users\\jlfan\\Desktop\\python\\GeoLiteCity.dat")
		#创建主窗口，用于容纳其他组件：
		self.root = Tkinter.Tk()
		#主窗口设置标题内容
		self.root.title(u"IP位置查询(离线版)")
		#创建一个输入框，设置尺寸
		self.ip_input = Tkinter.Entry(self.root, width=30)
		#创建一个回显的列表：
		self.display_info = Tkinter.Listbox(self.root, width=50)
		#创建一个查询的按钮：
		self.resylt_button = Tkinter.Button(self.root, command=self.find_position, \
			text=u"查询")

	#完成布局：
	def gui_arrang(self):
		self.ip_input.pack()
		self.display_info.pack()
		self.resylt_button.pack()

	#根据IP查找地理位置：
	def find_position(self):
		#获取输入信息
		self.ip_addr = self.ip_input.get()
		aim = self.gi.record_by_name(self.ip_addr)#最好采用正则表达式
		try:

			#获取目标城市：
			city = aim["city"]
			#获取目标国家：
			country = aim["country_name"]
			#获取目标地区：
			region_code = aim["region_code"]
			#获取目标经度：
			longitude = aim["longitude"]
			#获取目标纬度：
			latitude = aim["latitude"]

		except:
			pass

		#创建临时列表：
		the_ip_info = [u"所在纬度:"+str(latitude), u"所在经度:"+str(longitude), \
		u"地域代号:"+str(region_code), u"所在城市:"+str(city), \
		u"所在国家:"+str(country)]
		#清空回显列表可见部分，类似clear
		for item in range(10):
			self.display_info.insert(0, "")
		#为回显列表赋值：
		for item in the_ip_info:
			self.display_info.insert(0, item)
		return the_ip_info

def main():
	#初始化对象：
	FL = FindLocation()
	#进行布局：
	FL.gui_arrang()
	#主程序执行：
	Tkinter.mainloop()
	pass

if __name__ == "__main__":
	main()
