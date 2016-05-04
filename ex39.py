states = {
    '충청북도': '충북',
    '경상북도': '경북',
    '전라남도': '전남',
    '경기도': '경기',
    '강원도': '강원'
}

cities = {
    '전남': '광주',
    '강원': '원주',
    '경북': '대구'
}

cities['경기'] = '수원'
cities['충북'] = '충주'

print('-' * 10)
print("경기도에는", cities['경기'])
print("충청북도에는", cities['충북'])

print('-' * 10)
print("강원도의 약자는", states['강원도'])
print("경상북도의 약자는", states['경상북도'])

print('-' * 10)
print("강원도에는", cities[states['강원도']])
print("경상북도에는", cities[states['경상북도']])

print('-' * 10)
for state, abbrev in states.items():
    print("%s의 줄임말은 %s입니다" % (state, abbrev))

print('-' * 10)
for abbrev, city in cities.items():
    print("%s에는 %s시가 있습니다" % (abbrev, city))

print('-' * 10)
for state, abbrev in states.items():
    print("%s의 줄임말은 %s이고 %s시가 있습니다" % (state, abbrev, cities[abbrev]))

print('-' * 10)
state = states.get('제주', None)

if not state:
    print("제주도는 없습니다.")

city = cities.get('제주', '없습니다')
print("'제주'의 시는 %s" % city)