months = [
         'January'
         'February'
         'March'
         'April'
         'May'
         'June'
         'July'
         'August'
         'September'
         'October'
         'November'
         'December'
]#日期列表

endings = ['st','nd','rd'] + 17*['th'] + ['st','nd','rd'] +7*['th'] + ['st']#1-31数字结尾的列表

year = raw_input('Year: ')
month = raw_input('Month(1-12): ')
day = raw_input('Day(1-31): ')

month_number = int(month)
day_number = int(day)

month_name = months[month_number - 1]
ordinal = day + endings[day_number - 1]#获取正确索引

print month_name + ' ' + ordinal + ',' + year #输出结果      
