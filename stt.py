import vosk
import json, pyaudio

model = vosk.Model("small_model") #Создаём переменную для модели
rec = vosk.KaldiRecognizer(model, 16000) #Указываем частоту дискретизации
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000) #настраиваем pyaudio
stream.start_stream()

def listen(): #Создаём функцию, которая считывает наш голос и при помощи модели, преобразует его в текст в реально времени
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if (rec.AcceptWaveform(data)) and (len(data) > 0):
            answer = json.loads(rec.Result())
            if answer['text']:
                yield answer['text']
