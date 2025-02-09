import pyttsx3

#Код для pyttsx3
engine = pyttsx3.init('sapi5') #Инициализация pyttsx3
voices = engine.getProperty('voices') #Берём список голосов
engine.setProperty('voice', voices[0].id) #Задаём свойства и выбираем голос

def speak(audio): #Создаём функцию для вызова в коде, которая будет запускать синтез речи
    engine.say(audio)
    engine.runAndWait()
