# (Почти)Криптоанализ/расшифровка шифра Виженера
Расшифровка сообщения, зашифрованного шифром Виженера.  
Нет, это **не взлом**, а простая расшифровка, основанная на знании ключа.

Криптоанализ производится на основании знания о длине ключа

# Что, как и почему [Криптоанализ]
Файл _analysis.py_
Python3 eeeeaaahhh 

В теле скрипта прописываете путь к файлу с шифртекстом, правите согласно комментам участки кода в зависимости от длины ключа  
Запускаете: ```python3 analisys.py```  
Посчитает частоты по столбцам, вычислит сдвиги и выведет все возможные ключи  
Найдя ключ можно приступит к расшифровке  

# Что, как и почему [Расшифровка]
Файлы _analysis.py_ и _vd_light.py_
Все действо происходит на Python3  

Расшифровка сообщений со следующим алфавитом:
```АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ_```

Есть 2 версии - обычная и легкая.  
Обычная пускается с консоли как-то так:  
Входные параметры: ```-f имя_файла_с_шифртекстом -k ключ_расшифрования```  
Использование: ```python3 vd.py -f vigenere.txt -k НОС```

Легкая версия ```vd_light.py``` может быть просто скопирована в любой онлайн интерпретатор Python3  (например [Ideone](https://ideone.com/)), подставлены шифр текст и ключ и выполнена без установки Python на компьютер.  

# Невероятные факты
Оказывается, этот скрипт может расшифровать шифртекст из какой-то лабы по криптографии... ~~По секрету это 4 лаба~~
