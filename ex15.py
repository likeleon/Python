from sys import argv

script, filename = argv
txt = open(filename)

print("파일 %r의 내용" % filename)
print(txt.read())
txt.close()

print("파일 이름을 다시 입력해 주세요.")
file_again = input(">")

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()