# Pacman Project

Взаимодействие с пользователем:\
Первый ход делает игрок (он управляет пакманом(обозначение @)):
для этого нужно написать направление хода (right/left/up/down)\
Второй ход делают призраки (в простой версии они в рандомном направлении двигаются на один шаг)\
И так далее процесс повторяется\
В конце игры вы увидите сообщение "Game is over. You are won:)!" или "Game is over. You are lost:(!"
в зависимости от исхода\
Запуск проекта\
main.py\
Обновление (2 итерация)\
Теперь есть графический интерфейс и 3 уровня сложности(они различаюся по размеру поля и количеству привидений). В начале игры в консоль нужно ввести 
желаемую сложность(easy/medium/hard) и тип интерфейса(console/graphic).Так же теперь отображается количество жизней у пакмана и количество очков.\
Классы и паттерны:\
Порождающие паттерны:\
Фабричный метод:\
ConsoleInterface, GraphicInterface,TelegramInterface наследуются от Interface;\
Pacman, Ghost,Dot, Wall, Empty наследуются от GameObject;\
EasyLevel, MediumLevel, HardLevel наследуются от Level;\
Структурные паттерны:\
Мост:\
Game содержит в себе Move, Interface\
Move содержит в себе Level, Field\
Легковес:\
Использование класса Info, где содержатся данные, которые одинаковы для всех объектов какого-то типа\
Поле для простого уровня\
![Alt text](https://github.com/KhristoforovaDasha/MIPT_TP_PROJECT/blob/dev/readme_images/pacman_field.png)
![Alt text](https://github.com/KhristoforovaDasha/MIPT_TP_PROJECT/blob/dev/readme_images/pacman_game.png)
![Alt text](https://github.com/KhristoforovaDasha/MIPT_TP_PROJECT/blob/dev/readme_images/lives_decrease.png)
![Alt text](https://github.com/KhristoforovaDasha/MIPT_TP_PROJECT/blob/dev/readme_images/won.png)
![Alt text](https://github.com/KhristoforovaDasha/MIPT_TP_PROJECT/blob/dev/readme_images/game_over.png)

Поле для среднего уровня
![Alt text](https://github.com/KhristoforovaDasha/MIPT_TP_PROJECT/blob/dev/readme_images/medium.png)

Поле для тяжёлого уровня
![Alt text](https://github.com/KhristoforovaDasha/MIPT_TP_PROJECT/blob/dev/readme_images/hard.png)
