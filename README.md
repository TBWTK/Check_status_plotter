<h1>
  Проверка статуса плоттера HP Designjet T790 44in
</h1>
<div id="header" align="center">
  <img src="https://media.giphy.com/media/M9gbBd9nbDrOTu1Mqx/giphy.gif" width="100"/>
  <div id="badges">
  <a href="https://t.me/TBWTK">
    <img src="https://img.shields.io/badge/Telegram-33A8E3" alt="Telegram"/>
  </a>
</div>
</div>

<h3>
    Пет-проект: Программа для автоматической проверки статуса плоттера HP Designjet T790 44in
</h3>
<p>
   Веб-интерфейс плоттера HP Designjet T790 44in выглядит следующим образом:
</p>
   <img src="https://user-images.githubusercontent.com/66531375/200846744-755c67d0-7492-4da4-aef7-d57343a4afbf.png" />

<p>
   У него есть один статус ошибки который отображаетсся в представлении HTML через объект "img":
   img src="images/icon_status_major.gif.
</p>
<p>
   Данный объект img мы и бдуем проверять в нашей программе, и при возникновении ошибки отправлять сообщение пользователю через телеграм бот. 
   Вам больше не нужно постоянно заходить и проверять статус плоттера, за вас все сделает эта программа!) 
</p>


<h4>
    Создать и использовать бота
</h4
<p>
   Для начала вам нужно создать своего бота обратившись к @BotFather(https://telegram.me/BotFather)
   После создания своего бота, вам нужно будет всставить полученный токен вместо "YOUR_TOKEN" в:
</p>
<p>
      TOKEN = "YOUR_TOKEN"
</p>
<p>
   Далее вам нужно узнать свой user_id и вставить его вместо 0 в user_id = 0
   Узнать user_id вы меожете через сторонние сервисы телеграм ботов или распечатав отправленное на ваш бот сообщение
</p>
<h4>
    Настроить url адресса для плоттера
</h4
<p>
   Далее вам нужно перейти на веб-интерфейс плоттера и скопировать его url.
   url_plotter_one = "YOUR_URL/hp/device/webAccess/printer_status.htm?content=supplies"
   и обновить переменную url_plotter_one.
</p>


<h4>
    Убрать  плоттер(Оставить один) 
</h4
<p>
  Данный код расчитан на два плоттера, поэтому, чтобы убрать плоттер, вам нужно перестать использовать переменную url_plotter_two.
  А так же в функции def infinite_loop() Убрать часть кода, который начинается с if check_status(url_plotter_two).
  Таким образом, у вас останется только один плоттер
</p>
<p>
  Чтобы добавить еще один плоттер, вам нужно добавить переменную типа url_plotter_номер_плоттера(one,two и тд).
  В функции def infinite_loop() добавить переменную типа switch_status_plotter_номер_плоттера((one,two и тд).
  Добавить в цикле условные конструкции по типу тех, что уже действуют в коде:
</p>

  ```python
          if check_status(url_plotter_number):
            if switch_status_plotter_number:
                print("Дефект пришел")
                bot.send_message(user_id, "Плоттер number - ошибка, исправьте пожалуйста")
                switch_status_plotter_number = False
        else:
            switch_status_plotter_number = True
  ```
  
<p>
  Обновить переменную  bot.set_my_commands([]) добавив туда еще один плоттер
</p>

  ```python
          bot.set_my_commands([
    telebot.types.BotCommand("/done_plotter_one", "Ошибка плоттера 1 исправлена"),
    telebot.types.BotCommand("/done_plotter_number", "Ошибка плоттера number исправлена"),
])
  ```
  
<p>
  Обновить функцию def echo_all(messaage) добавив туда проверку для еще одного плоттера
</p>

  ```python
          @bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_all(message):
    print(message.text)
    if message.text == "/done_plotter_one":
        if not check_status(url_plotter_one):
            bot.reply_to(message, "Ошибка исправлена, плоттер 1 продолжает работу")

    if message.text == "/done_plotter_number":
        if not check_status(url_plotter_number):
            bot.reply_to(message, "Ошибка исправлена, плоттер number продолжает работу")
])
  ```

![](https://komarev.com/ghpvc/?username=your-TBWTK)
