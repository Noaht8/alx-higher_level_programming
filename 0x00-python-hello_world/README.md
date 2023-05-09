# 0x00. Python - Hello, World

![Image link](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/231/48a9fdbd67c84a328a9df9ec8d93b9ac2458ac37721d7d53e51a27fb2bdc5263.jpg)

## Author:
* **Noah Tsegay** <[Noaht8](https://github.com/Noaht8)>  &#128511;

## Directory Contents
___

This directory contains the following files:

|File| Description|
|:-------|:-------|
|[0-run](0-run)| Shell script that runs a Python script<br>The Python file name will be saved in the environment variable ```$PYFILE```|
|[1-run_inline](1-run_inline)| Shell script that runs Python code<br>The Python code will be saved in the environment variable ```$PYCODE```|
|[2-print.py](2-print.py)| Python script that prints exactly ```"Programming is like building a multilingual puzzle```, followed by a new line|
|[3-print_number.py](3-print_number.py)|Print the integer stored in the variable number, followed by Battery street, followed by a new line|
|[4-print_float.py](4-print_float.py)|Print the float stored in the variable number with a precision of 2 digits.|
|[5-print_string.py](5-print_string.py)|Print 3 times a string stored in the variable str, followed by its first 9 characters.|
|[6-concat.py](6-concat.py)|Print ```Welcome to Holberton School!```|
|[7-edges.py](7-edges.py)|```word_first_3``` should contain the first 3 letters of the variable ```word```<br>```word_last_2``` should contain the last 2 letters of the variable ```word```<br>```middle_word``` should contain the value of the variable ```word``` without the first and last letters|
|[8-concat_edges.py](8-concat_edges.py)|Print ```object-oriented programming with Python```, followed by a new line|
|[9-easter_egg.py](9-easter_egg.py)|Python script that prints “The Zen of Python”, by TimPeters, followed by a new line|
|[10-check_cycle.c](10-check_cycle.c) [lists.h](lists.h)|Function in C that checks if a singly linked list has a cycle in it|
|[100-write.py](100-write.py)|Python script that prints exactly ```and that piece of art is useful - Dora Korpar, 2015-10-19```, followed by a new line|
|[101-compile](101-compile)|Script that compiles a Python script file<br>Python file name will be stored in the environment variable ```$PYFILE```<br>output filename has to be ```$PYFILEc``` (ex: ```export PYFILE=my_main.py``` => output filename: ```my_main.pyc```)|
|[102-magic_calculation.py](102-magic_calculation.py)|Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:|

### 102-magic_calculation.py The Byte code
```
 3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
```

