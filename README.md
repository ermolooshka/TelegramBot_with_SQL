## TelegramBot с базой данных
### @CuRate_from_Ermoloohka_bot


### Задание: 

- подключить к боту https://github.com/ermolooshka/TelegramBot базу данных; 
- добавить команду для сохранения в базу данных:
     - значения курса
     - даты
     - валюты курсов


#### В Telegram-боте реализован следующий функционал:
- Бот возвращает цену на определённое количество валюты (евро, доллар или рубль)

- Человек отправляет сообщение боту в виде: 
   - <имя валюты цену которой он хочет узнать>  
   - <имя валюты в которой надо узнать цену первой валюты> 
   - <количество первой валюты>
 

- При вводе команды /start или /help пользователю выводятся инструкции по применению бота.
- При вводе команды /values выводится информация о всех доступных валютах в читаемом виде.
- При ошибке пользователя вызывать собственно написанное исключение APIException с текстом пояснения ошибки.
- Текст любой ошибки с указанием типа ошибки отправлятся пользователю в сообщения.


Данный бот не запущен, необходимо запустить бот со своего устройства (загрузить данный репозиторий на свой компьютер).
Для работы с данным телеграм-ботом необходимо установить библиотеки requests и PyTelegramBotAPI (версия 4.X).

