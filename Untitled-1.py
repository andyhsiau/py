b = 'test'
a = """

123
123%s123
123

"""%b


p = b'123123\xff\xfeW['.decode('utf-8')


print(p)