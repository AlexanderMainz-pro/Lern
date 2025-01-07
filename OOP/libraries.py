from accessify import private, protected #инсталлим для вызова методов доступов приватной или публичной доступности
from string import ascii_letters #библиотека всевозможных стрингов
from pprint import pprint #работа с файлами

import os #библиотека операционки
import tkinter #для создания приложений, front
from dataclasses import dataclass #декоратор по созданию классов

from functools import reduce
#filter() принимает два аргумента – функцию-предикат и итерируемый объект. Он возвращает новый итератор,
#содержащий только те элементы итерируемого объекта,
#которые удовлетворяют условиям, заданным функцией-предикатом.

#from memory_profiler import profile
#Установите Memory Profiler с помощью pip: pip install memory-profiler
#Используйте декоратор @profile перед функцией, которая может вызывать утечки памяти