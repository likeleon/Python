formatter = "%s %s %s %s"

print(formatter % (1, 2, 3, 4))
print(formatter % ("하나", "둘", "셋", "넷"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % (
    "하하 1",
    "하하 '2'",
    "하하 3",
    "하하 4"
))

formatter2 = "%r %r %r %r"
print(formatter2 % (
    "하하 1",
    "하하 '2'",
    "하하 3",
    "하하 4"
))  