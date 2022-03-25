class ArquivoAudio:
    def __init__(self, arquivo):
        self.ext = ''
        if not arquivo.endswith(self.ext):
            raise Exception('Formato inválido!')
        self.arquivo = arquivo


class ArquivoMP3(ArquivoAudio):
    ext = 'mp3'

    def tocar(self):
        return f'Tocando {self.arquivo} como MP3'


class ArquivoWav(ArquivoAudio):
    ext = 'wav'

    def tocar(self):
        return f'Tocando {self.arquivo} como WAV'


class ArquivoOgg(ArquivoAudio):
    ext = 'ogg'

    def tocar(self):
        return f'Tocando {self.arquivo} como ogg'


class ArquivoAAC:
    def __init__(self, arquivo):
        if not arquivo.endswith('.aac'):
            raise Exception('Formato inválido!')
        self.arquivo = arquivo

    def tocar(self):
        return f'Tocando {self.arquivo} como acc'


ogg = ArquivoOgg('musica.ogg')
mp3 = ArquivoMP3('musica.mp3')
wav = ArquivoWav('musica.wav')

print(ogg.tocar())
print(mp3.tocar())
print(wav.tocar())

teste_ogg = ArquivoMP3('outramusica.ogg')
print(teste_ogg.tocar())

aac = ArquivoAAC('musica.aac')
print(aac.tocar())
