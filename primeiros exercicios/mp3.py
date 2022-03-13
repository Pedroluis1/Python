from pygame import mixer

mixer.init()
mixer.music.load('alok.mp3'), ('bela c.mp3')
mixer.music.play()
print('agora tu escuchas?muchacha')
mixer.music.stop(input('aperte enter para parar >>>>'))

