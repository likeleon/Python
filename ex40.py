class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["생일 축하합니다", "하하", "이만!"])

bulls_on_parade = Song(["조개를 가득 찬 주머니 차고", "가족 주위에 모여든 그들"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()