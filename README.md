# es.wallapop-auto-account-create

как запустить? 
ну хз качни питон https://www.python.org/
добавиь питон в path  
`pip install socks requests` или `pip install -r requirements.txt` - `.\build.bat` - собрает все зависимости \
`py main.py` - `python main.py` - `.\run.bat` - запускает проект \
команда сборки:
```
pip install -r requirements.txt
```
эту фигню один раз запускать
закидываешь список прокси в `proxy.txt` (файл создан сейчас но он пуст)
```
192.168.42.70:30000
192.168.42.70:30001
192.168.42.70:30002
192.168.42.70:30003
192.168.42.70:30004
```
закидываешь почты и пароли в `credentials.txt` (файл тоже есть)
в таком формате:
почта пароль
между почтой и паролем один пробел
```
dbjSo10gBoUp@hotmail.com Tn3BiYDFBvs2
6wXMkeMKJgHl@hotmail.com M4jSZnZWClNI
NPJF7Ainv9bP@hotmail.com 3TbnSqOOfp6V
TmDFA8R2PG5R@hotmail.com oN6vCUz2S7Q1
```
и запускаешь шарманку 
```
py main.py
```