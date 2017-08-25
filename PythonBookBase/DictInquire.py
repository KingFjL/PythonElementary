#一个利用字典构造简单的数据库，其中人名作为键，每个人用另外一个字典表示

people = {
    'Alice' : {
        'phone' : '2341',
        'addr' : 'Foo drive 23'
        },
    'Beth' : {
        'phone' : '3578',
        'addr' : 'Bar Street 31'
        },
    'Ceil' : {
        'phone':'6789',
        'addr':'Road 15'
        }
    }
    
labels = {
    'phone' : 'phone number',
    'addr' : 'address'
    }#针对电话号码和地址使用的描述性标签
    
name = raw_input('Name: ')  
request = raw_input('Phone Number (p) or address (a)?')#查找电话或地址？

key = request #输入的键p/a均不是
if request == 'p':
    key = 'phone'
if request == 'a':
    key = 'addr'  #使用正确的键
    
person = people.get(name, {})
label = labels.get(key, key)
result = person.get(key, 'not available')

if name in people:
    print "%s's %s is %s." % (name, label, result)
    

    
