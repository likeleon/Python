ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("잠깐 아직 목록에 10개가 들어 있지 않으니 한 번 고쳐 봅시다.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("추가: ", next_one)
    stuff.append(next_one)
    print("이제 %d 항목이 있습니다." % len(stuff))

print("한 번 볼까요! ", stuff)

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
