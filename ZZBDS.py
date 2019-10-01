import re

ingredient = "kumquat: 2 cups"
#使用?P<name>标识每个分组
pattern_text = r'(?P<ingredient>\w+):\s+(?P<amount>\d+)\s+(?P<unit>\w+)'
#编译模式
pattern = re.compile(pattern_text)
#使用模式匹配输入文本
match = pattern.match(ingredient)
#print (match is None)
#提取到包含不同字段的元组
print (match.groups())
#print (match.group('ingredient'))
