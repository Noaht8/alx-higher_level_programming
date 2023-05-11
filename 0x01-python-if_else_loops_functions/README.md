# 0x01. Python - if/else, loops, functions

![Image link](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/233/code.png)

## Author:
* **Noah Tsegay** <[Noaht8](https://github.com/Noaht8)>  &#128511;

## Directory Contents
___

This directory contains the following files:

|File| Description|
|:-------|:-------|
|[0-positive_or_negative.py](0-positive_or_negative.py)| Positive anything is better than negative nothing|
|[1-last_digit.py](1-last_digit.py)| The last digit|
|[2-print_alphabet.py](2-print_alphabet.py)| Python program that prints the ASCII alphabet, in lowercase, not followed by a new line|
|[3-print_alphabt.py](3-print_alphabt.py)| Python program that prints the ASCII alphabet, in lowercase, not followed by a new line<br>Print all the letters except ```q``` and ```e```|
|[4-print_hexa.py](4-print_hexa.py)| Python program that prints all numbers from ```0``` to ```98``` in decimal and in hexadecimal|
|[5-print_comb2.py](5-print_comb2.py)| Python program that prints numbers from ```0``` to ```99```|
|[6-print_comb3.py](6-print_comb3.py)| Python program that prints all possible different combinations of two digits|
|[7-islower.py](7-islower.py)| Python function that checks for lowercase character|
|[8-uppercase.py](8-uppercase.py)| Python function that prints a string in uppercase followed by a new line|
|[9-print_last_digit.py](9-print_last_digit.py)| Python function that prints the last digit of a number|
|[10-add.py](10-add.py)| Python function that adds two integers and returns the result|
|[11-pow.py](11-pow.py)| Python function that computes ```a``` to the power of ```b``` and return the value|
|[12-fizzbuzz.py](12-fizzbuzz.py)| Python function that prints the numbers from 1 to 100 separated by a space<br>For multiples of three print ```Fizz``` instead of the number and for multiples of five print ```Buzz```<br>For numbers which are multiples of both three and five print ```FizzBuzz```|
|[13-insert_number.c](13-insert_number.c)  [lists.h](lists.h)| Insert in sorted linked list|
|[100-print_tebahpla.py](100-print_tebahpla.py)| Python program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (```z``` in lowercase and ```Y``` in uppercase) , not followed by a new line.|
|[101-remove_char_at.py](101-remove_char_at.py)| Python function that creates a copy of the string, removing the character at the position ```n``` (not the Python way, the “C array index”)|
|[102-magic_calculation.py](102-magic_calculation.py)| ByteCode -> Python #2|

The 102-magic_calculation.py bytecode<br>
```
 3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
```
