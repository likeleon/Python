from sys import argv
from os.path import exists

script, from_file, to_file = argv

in_file = open(from_file)
indata = in_file.read()

print("입력 파일은 %d바이트입니다" % len(indata))

print("출력 파일이 존재하나요? %r" % exists(to_file))

out_file = open(to_file, 'w')
out_file.write(indata)

out_file.close()
in_file.close()