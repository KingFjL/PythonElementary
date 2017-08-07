#使用给定宽度打印格式化后的价格列表

width = float(raw_input('Please enter the width: '))

price_width = 10
item_width = width - price_width

header_format = '%-*s%*s'
format = '%-*s%*.2f'

print '=' * width
print header_format(item_width, 'Item', price_width, price)
print '-' * width

print format % (item_width, 'Apples', price_width, 0.4)
print format % (item_width, 'Pears', price_width, 0.5)
print format % (item_width, 'Cantaloupes', price_width, 1.92)
print format % (item_width, 'Prunes(4 lbs)', price_width, 12)

print '=' * width
