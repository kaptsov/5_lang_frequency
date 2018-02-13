# Анализатор частоты слов

Скрипт получает на вход текстовый файл и определяет 10 наиболее часто встречающиехся слов. Чтобы задача была интересней, и чтобы отсечь все известные предлоги, за слово принята последовательность не менее чем из 4-х символов.

# Установка

Скрипт требует для своей работы установленный интерпретатор Python версии 3.5. 
~~~
$ install python
~~~

# Как запустить

Запуск на Linux:
~~~
$ python lang_frequency.py <text data filepath>
~~~

Пример:
~~~
$ python lang_frequency.py 1984.txt
Parsing text...
The most frequent words in file are:
уинстон - 471
было - 422
когда - 268
только - 258
даже - 248
если - 246
него - 185
была - 157
брайен - 156
может - 147
~~~


Запуск на Windows происходит аналогично.

# Цели проекта

Скрипт написан в образовательных целях. Исходный код взят на [DEVMAN.org](https://devman.org)
