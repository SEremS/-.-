import pyaudio
import stt
import functions as func
import config
import threading
import pvporcupine
import struct
import time
import tts

is_running = False
def run():
    global is_running
    while True:
        for text in stt.listen():
            v = text.split()
            print('Вы сказали: ', text)
            if text in config.browser_open:
                func.open_browser()
            if text in config.youtube_open:
                func.open_youtube()
            if text in config.wheel_scroll_down:
                func.scroll_wheel_down()
            if text in config.wheel_scroll_up:
                func.scroll_wheel_up()
            if text in config.wheel_click:
                func.click_wheel()
            if text in config.time_what:
                func.what_time()
            if text in config.data_what:
                func.what_data()
            if text in config.ria_open:
                func.open_ria()
            if text in config.yandex_open:
                func.open_yandex()
            if text in config.lenta_open:
                func.open_lenta()
            if text in config.yandex_mail_open:
                func.open_yandex_mail()
            if text in config.google_open:
                func.open_google()
            if text in config.mailru_open:
                func.open_mailru()
            '''if v[0] in config.weather_open:
                try:
                    city_name = v[1]
                    func.open_weather(city_name)
                except:
                    pass
            if text in config.kino_open:
                try:
                    func.open_kino()
                except:
                    pass'''
            if v[0] in config.write_text:
                func.text_write(text[6:])
            if text in config.enter_text:
                func.text_enter()
            if v[0] in config.write_browser_text:
                func.browser_write_text(text[6:])
            if text in config.screnshoot_word:
                func.screenshot()
            if text in config.aptekaru_open:
                func.open_aptekaru()
            if text in config.stolichki_open:
                func.open_stolichki()
            if text in config.gorzdrav_open:
                func.open_gorzdrav()
            if text in config.stop_word:
                func.picovoice_stop()
                main()
            if text in config.volume_off:
                func.off_volume()
            if text in config.volume_on:
                func.on_volume()
            if text in config.volume_up:
                func.up_volume()
            if text in config.volume_down:
                func.down_volume()
            if text in config.whatsup_open:
                func.open_whatsup()
            if text in config.mosru_open:
                func.open_mosru()
            if text.count('погода') == 1:
                func.open_weather(text)
            try:
                if v[0] in config.wheel_right:
                    func.mouse_right(v[1])
            except:
                pass
            try:
                if v[0] in config.wheel_left:
                    func.mouse_left(v[1])
            except:
                pass
            try:
                if v[0] in config.wheel_up:
                    func.mouse_up(v[1])
            except:
                pass
            try:
                if v[0] in config.wheel_down:
                    func.mouse_down(v[1])
            except:
                pass
            try:
                if text in config.libreoffice_open:
                    func.open_libreoffice()
            except:
                pass
            if text in config.notepad_open:
                func.open_notepad()
            if text in config.notepad_save:
                func.save_notepad()
            if text in config.delete_all:
                func.all_delete()
            if text in config.program_exit:
                func.exit_program()
            if text in config.copy_text:
                func.text_copy()
            if text in config.paste_text:
                func.text_paste()
            if text in config.camera_open:
                func.open_camera()
            if text in config.make_video:
                func.video_make()
            if text in config.calc_open:
                func.open_calc()
            if text in config.how_many:
                func.many_how()
            if text in config.ymnojenie_baza:
                func.ymnojenie()
            if text in config.plus_baza:
                func.plus()
            if text in config.minus_baza:
                func.minus()
            if text in config.recorder_voice:
                func.voice_recorder()
            if text in config.record_sound:
                func.video_make()
            if text in config.stop_sound:
                func.video_make()
            if text in config.thx:
                tts.speak('всегда пожалуйста!')
            if text in config.yandex_disk_open:
                func.open_yandex_disk()
            if text in config.google_disk_open:
                func.open_google_disk()
            if text in config.gosyslygi_open:
                func.open_gosyslygi()
            if text in config.open_kinopoisk:
                func.kinopoisk_open()
            if text in config.open_ivi:
                func.ivi_open()
            if text in config.open_okko:
                func.okko_open()
            if text in config.okru:
                func.okru_open()
            if text in config.vk:
                func.vk_open()
            if text in config.wheel_click2:
                func.click_wheel2()
            if text in config.commands:
                func.open_commands()
            if text in config.space_command:
                func.space()
            if text:
                pass
            func.picovoice_ready()

def main():
    porcupine = None
    pa = None
    audio_stream = None
    print('Жду пока меня позовут: ')
    try:
        porcupine = pvporcupine.create(keywords=['computer'])
        pa = pyaudio.PyAudio()
        audio_stream = pa.open(
            rate=porcupine.sample_rate,
            channels=1,
            format= stt.pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length)

        while True:
            pcm = audio_stream.read(porcupine.frame_length)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            keyword_index = porcupine.process(pcm)
            if keyword_index >= 0:
                tts.speak('слушаю')
                func.picovoice_ready()
                print('wake word detected.. \n', end='')
                run()
                time.sleep(1)
    finally:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if pa is not None:
            pa.terminate()

def button_clicked():
    global is_running
    if not is_running:
        is_running = True
        threading.Thread(target=main).start()
    else:
        is_running = False
