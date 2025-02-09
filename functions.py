import time
import webbrowser
import mouse
import tts
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
import config
import keyboard as keyb
import pyautogui
import winsound
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import os
import threading
import random




def picovoice_ready():
    winsound.Beep(400,200)

def picovoice_stop():
    winsound.Beep(200, 200)

def open_browser():
    webbrowser.open_new_tab('https://dzen.ru/?clid=2456109&yredirect=true')
    tts.speak('Открываю')

def open_youtube():
    webbrowser.open_new_tab('https://www.youtube.com')
    tts.speak('Открываю')

def scroll_wheel_down():
    mouse.wheel(-5)

def scroll_wheel_up():
    mouse.wheel(5)

'''def right_wheel():
    mouse.move(200, 0, absolute=False, duration=0.2)'''

'''def left_wheel():
    mouse.move(-200, 0, absolute=False, duration=0.2)'''

'''def down_wheel():
    mouse.move(0, 200, 0, duration=0.2)'''

'''def up_wheel():
    mouse.move(0, -200, 0, duration=0.2)'''

def click_wheel():
    mouse.click('left')
def click_wheel2():
    mouse.click('right')
def what_time():
    result = time.localtime(time.time())
    local_time = str(result.tm_hour) + ' часов ' + str(result.tm_min) + ' минут'
    tts.speak(local_time)

def what_data():
    result = time.localtime(time.time())
    local_time = str(result.tm_mday) + 'ое ' + str(result.tm_mon) + 'ое ' + str(result.tm_year) + 'ий'
    tts.speak(local_time)

def open_ria():
    webbrowser.open('https://ria.ru')
    tts.speak('Открываю риа новости')

def open_yandex():
    webbrowser.open('https://dzen.ru/news?issue_tld=ru')
    tts.speak('Открываю дзен')

def open_lenta():
    webbrowser.open('https://lenta.ru')
    tts.speak('Открываю Ленту')

def open_yandex_mail():
    webbrowser.open('https://mail.yandex.ru')
    tts.speak('Открываю яндекс почту')

def open_google():
    webbrowser.open('https://mail.google.com/mail')
    tts.speak('Открываю гугл почту')

def open_mailru():
    webbrowser.open('https://e.mail.ru/inbox')
    tts.speak('открываю мэил ру')


'''def get_weather(api):
    global owm
    owm = OWM(str(api))'''


'''def open_weather(name):
    try:
        global owm
        mgr = owm.weather_manager()

        observation = mgr.weather_at_place(name)
        w = observation.weather
        t = w.temperature('celsius')['temp']
        tts.speak('погода состовляет ' + str(t) + ' градусов')
    except:
        pass'''

def get_kino(kinopoisk):
    global k
    k = kinopoisk

def open_kino():
    global k
    webbrowser.open(k)

def text_write(text):
    keyb.write(str(text))

def text_enter():
    keyb.press("enter")

def browser_write_text(text):
    webbrowser.open_new_tab('https://yandex.ru/search/?lr=10735&text=' + str(text))

def screenshot():
    random_count = random.randint(1,10000)
    pyautogui.screenshot(f'screenshots/assistent_screen{random_count}.png')

def open_aptekaru():
    webbrowser.open('https://www.eapteka.ru')
    tts.speak('открываю аптека ру')

def open_stolichki():
    webbrowser.open('https://stolichki.ru')
    tts.speak('открываю столички')

def open_gorzdrav():
    webbrowser.open('https://gorzdrav.org')
    tts.speak('открываю горздрав')

def vol():
    global volume
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
def off_volume():
    global volume
    vol()
    volume.SetMute(1, None)

def on_volume():
    global volume
    volume.SetMute(0, None)

def up_volume():
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        current = volume.GetMasterVolumeLevel()
        volume.SetMasterVolumeLevel(current + 5.0, None)
    except:
        pass

def down_volume():
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        current = volume.GetMasterVolumeLevel()
        volume.SetMasterVolumeLevel(current + -5.0, None)
    except:
        pass

def open_whatsup():
    webbrowser.open('https://web.whatsapp.com')

def open_mosru():
    webbrowser.open('https://www.mos.ru')

def open_weather(text_weather):
    webbrowser.open_new_tab('https://yandex.ru/search/?lr=10735&text=' + str(text_weather))

def mouse_right(chiclo):
    if chiclo in config.dvadcat:
        mouse.move(20, 0, absolute=False, duration=0.2)
    elif chiclo in config.patdesat:
        mouse.move(50, 0, absolute=False, duration=0.2)
    elif chiclo in config.sto:
        mouse.move(100, 0, absolute=False, duration=0.2)
    elif chiclo in config.dvesti:
        mouse.move(200, 0, absolute=False, duration=0.2)
    elif chiclo in config.trista:
        mouse.move(300, 0, absolute=False, duration=0.2)
    elif chiclo in config.chetirista:
        mouse.move(400, 0, absolute=False, duration=0.2)
    elif chiclo in config.petsot:
        mouse.move(500, 0, absolute=False, duration=0.2)

def mouse_left(chiclo):
    if chiclo in config.dvadcat:
        mouse.move(-20, 0, absolute=False, duration=0.2)
    elif chiclo in config.patdesat:
        mouse.move(-50, 0, absolute=False, duration=0.2)
    elif chiclo in config.sto:
        mouse.move(-100, 0, absolute=False, duration=0.2)
    elif chiclo in config.dvesti:
        mouse.move(-200, 0, absolute=False, duration=0.2)
    elif chiclo in config.trista:
        mouse.move(-300, 0, absolute=False, duration=0.2)
    elif chiclo in config.chetirista:
        mouse.move(-400, 0, absolute=False, duration=0.2)
    elif chiclo in config.petsot:
        mouse.move(-500, 0, absolute=False, duration=0.2)

def mouse_up(chiclo):
    if chiclo in config.dvadcat:
        mouse.move(0, -20, 0, duration=0.2)
    elif chiclo in config.patdesat:
        mouse.move(0, -50, 0, duration=0.2)
    elif chiclo in config.sto:
        mouse.move(0, -100, 0, duration=0.2)
    elif chiclo in config.dvesti:
        mouse.move(0, -200, 0, duration=0.2)
    elif chiclo in config.trista:
        mouse.move(0, -300, 0, duration=0.2)
    elif chiclo in config.chetirista:
        mouse.move(0, -400, 0, duration=0.2)
    elif chiclo in config.petsot:
        mouse.move(0, -500, 0, duration=0.2)

def mouse_down(chiclo):
    if chiclo in config.dvadcat:
        mouse.move(0, 20, 0, duration=0.2)
    elif chiclo in config.patdesat:
        mouse.move(0, 50, 0, duration=0.2)
    elif chiclo in config.sto:
        mouse.move(0, 100, 0, duration=0.2)
    elif chiclo in config.dvesti:
        mouse.move(0, 200, 0, duration=0.2)
    elif chiclo in config.trista:
        mouse.move(0, 300, 0, duration=0.2)
    elif chiclo in config.chetirista:
        mouse.move(0, 400, 0, duration=0.2)
    elif chiclo in config.petsot:
        mouse.move(0, 500, 0, duration=0.2)


def open_libreoffice2():
    os.system('"C:/Program Files/LibreOffice/program/soffice.exe"')
def open_libreoffice():
    threading.Thread(target=open_libreoffice2).start()
    tts.speak('открываю')
def open_notepad2():
    os.system("notepad")

def open_notepad():
    threading.Thread(target=open_notepad2).start()
    tts.speak('открываю')

def save_notepad():
    keyb.press('ctrl + s')
    keyb.release('ctrl + s')

def all_delete():
    keyb.press('ctrl + a')
    keyb.release('ctrl + a')
    keyb.press('delete')
    keyb.release('delete')

def exit_program():
    keyb.press('alt + f4')
    keyb.release('alt + f4')

def text_copy():
    keyb.press('ctrl + a')
    keyb.release('ctrl + a')
    keyb.press('ctrl + c')
    keyb.release('ctrl + c')
    mouse.click('left')

def text_paste():
    keyb.press('ctrl + v')
    keyb.release('ctrl + v')

def open_camera2():
    os.system('start microsoft.windows.camera:')
def open_camera():
    threading.Thread(target=open_camera2).start()
    tts.speak('открываю камеру')

def video_make():
    keyb.press('space')
    keyb.release('space')

def open_calc2():
    os.system('calc')
def open_calc():
    threading.Thread(target=open_calc2).start()
    tts.speak('открываю калькулятор')

def many_how():
    keyb.press('enter')
    keyb.release('enter')

def ymnojenie():
    keyb.press('shift + *')
    keyb.release('shift + *')

def plus():
    keyb.press('shift + =')
    keyb.release('shift + =')

def minus():
    keyb.press('shift + -')
    keyb.release('shift + -')

def voice_recorder():
    os.system('explorer.exe shell:appsFolder\Microsoft.WindowsSoundRecorder_8wekyb3d8bbwe!App')

def open_yandex_disk():
    webbrowser.open('https://360.yandex.ru/disk/')

def open_google_disk():
    webbrowser.open('https://www.google.ru/drive/')

def open_gosyslygi():
    webbrowser.open('https://www.gosuslugi.ru')

def kinopoisk_open():
    webbrowser.open('https://www.kinopoisk.ru')

def ivi_open():
    webbrowser.open('https://www.ivi.ru')

def okko_open():
    webbrowser.open('https://okko.tv')

def okru_open():
    webbrowser.open('https://ok.ru')

def vk_open():
    webbrowser.open('https://vk.com')

def open_commands():
    webbrowser.open('https://telegra.ph/Komandy-Golosovogo-assistenta-Computer-02-14')

def space():
    keyb.press('space')
    keyb.release('space')
