# Cinemas

This script searches for movies shown in the movie theater and displays the list of films with the highest rating.

#How to use

The script requires the installed Python interpreter version 3.5 To call the help, run the script with the -h or --help option.
```Bash
>python cinemas.py -h
usage: cinemas.py [-h] [-count COUNT]

Number of output films

optional arguments:
  -h, --help    show this help message and exit
  -count COUNT  enter number of output films
```
To search for a movie, you can specify the number of movies to be displayed (the default is 10 movies)
```Bash
>cinemas.py -count 8
Get a list of movies shown in the cinema from Afisha.ru...
Get movies rating from Kinopoisk.ru...
Collecting data:: 100%|██████████| 12/12 [00:16<00:00,  1.40s/it]
+------------------------------------------+----------+----------------+---------+
| Movie title                              |   Rating |   Rating count |   Votes |
|------------------------------------------+----------+----------------+---------|
| Три билборда на границе Эббинга, Миссури |    8.304 |          46517 |      65 |
| Движение вверх                           |    8.271 |          58562 |      79 |
| Приключения Паддингтона-2                |    8.268 |           8132 |      65 |
| Лед                                      |    7.136 |           6556 |     140 |
| Все деньги мира                          |    6.833 |            321 |      96 |
| Секретное досье                          |    6.597 |           1467 |      82 |
| Дикий                                    |    5.566 |            908 |      58 |
| Пятьдесят оттенков свободы               |    5.548 |           9296 |     112 |
+------------------------------------------+----------+----------------+---------+
```
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
