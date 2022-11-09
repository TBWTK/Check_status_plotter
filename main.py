import urllib.request
import telebot
import threading

TOKEN = "YOUR_TOKEN"
# YOUR ID
user_id = 0
bot = telebot.TeleBot(TOKEN, parse_mode=None)


defect = '<img src="images/icon_status_major.gif'


url_plotter_one = "http://192.168.90.98/hp/device/webAccess/printer_status.htm?content=supplies"
url_plotter_two = ""


def check_status_one(url):
    with urllib.request.urlopen(url) as response:
        return response.read().decode('utf-8')


def check_status(url):
    if defect in check_status_one(url):
        return True
    return False


def infinite_loop():
    switch_status_plotter_one = True
    switch_status_plotter_two = True
    while True:
        if check_status(url_plotter_one):
            if switch_status_plotter_one:
                print("Дефект пришел")
                bot.send_message(user_id, "Плоттер 1 - ошибка, исправьте пожалуйста")
                switch_status_plotter_one = False
        else:
            switch_status_plotter_one = True

        if check_status(url_plotter_two):
            if switch_status_plotter_two:
                print("Дефект пришел")
                bot.send_message(user_id, "Плоттер 1 - ошибка, исправьте пожалуйста")
                switch_status_plotter_two = False
        else:
            switch_status_plotter_two = True


loop_thread = threading.Thread(target=infinite_loop)
loop_thread.start()


bot.set_my_commands([
    telebot.types.BotCommand("/done_plotter_one", "Ошибка плоттера 1 исправлена"),
    telebot.types.BotCommand("/done_plotter_two", "Ошибка плоттера 2 исправлена"),
])


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_all(message):
    print(message.text)
    if message.text == "/done_plotter_one":
        if not check_status(url_plotter_one):
            bot.reply_to(message, "Ошибка исправлена, плоттер 1 продолжает работу")

    if message.text == "/done_plotter_two":
        if not check_status(url_plotter_two):
            bot.reply_to(message, "Ошибка исправлена, плоттер 2 продолжает работу")


bot.infinity_polling()
