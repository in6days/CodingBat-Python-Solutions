# print("Hello Islamic World")
#
# note = 10
#
# if note >= 10:
#     print('Congratulation')
# else:
#     print('Sorry')
# print('-----------------')
# var = 5
# print(type(var))
#print('-----------------')
# message = '''This string that will span across multiple lines. No need to use newline characters for the next lines.
# The end of lines within this string is counted as a newline when printed.'''
# print('Message: ', message)
#print('-----------------')
# dictionary = {
#     1: 'One',
#     2: 'Tow',
#     3: 'Three',
#     4: 'Four',
#     5: 'Five'
# }
# # هنا قمنا بعرض قيمة العنصر الذي يحمل المفتاح رقم 3
# print(dictionary[5])
# # print('-----------------')
# for n in range(1, 6, 1):
#     print(n)
# print('-----------------')
# for n in range(5, 0, -1):
#     print(n)
# print('-----------------')
# for n in range(1, 6, 2):
#     print(n)
# print('-----------------')
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
# print('-----------------')
# i = 1
# while i <= 5:
#     print(i)
#     i += 1
# else:
#     print('This block is executed when the condition return False!')
# print('-----------------')
# counter = 1
# while counter <= 10:
#     print(counter)
#     if counter == 5:
#         break
#     counter += 1
# print('The loop was stopped when counter =', counter)
# print('-----------------')
# for n in range(1, 11):
#     print(n)
#     if n == 5:
#         break
# print('The loop was stopped when n =', n)
# print('-----------------')
# for n in range(1, 6):
#     if n == 3:
#         continue
#     print(n)
# print('-----------------')
# for n in range(1, 11):
#     if n % 2 == 0:
#         continue
#     print(n)
# print('-----------------')
# # بعدها سيتم عرضه .n هنا قمنا بإنشاء سلسلة من الأرقام الموجودة بين 1 إلى 5. في كل دورة في الحلقة سيتم جلب رقم من هذه السلسلة و تخزينه في المتغير
# for n in range(1, 6):
#     print(n)
# # بعد أن توقفت الحلقة n هنا عرضنا القيمة الموجودة في المتغير
# print('n contains:', n )
# print('-----------------')
# import MyModule
# MyModule.greeting()
#
# import platform
# # هنا قمنا بعرض إسم نظام التشغيل
# print('Operating System:', platform.system())
# # هنا قمنا بعرض كل المعلومات المتوفرة عن المعالج
# print('Processor:', platform.processor())
# # هنا قمنا بعرض إصدار بايثون المنصب على الجهاز
# print('Python Version:', platform.python_version())

# math هنا قمنا بتضمين كل محتوى الموديول
# import math
# # dir() و التي سترجعها الدالة math هنا قمنا بعرض أسماء جميع الأشياء الموجودة في الموديول
# print(dir(math))

import datetime
# dt في الكائن datetime ككائن من الكلاس now() هنا قمنا بتخزين التاريخ و الوقت الحالي الذي سترجعه الدالة
dt = datetime.datetime.now()
# dt هنا قمنا بعرض قيمة الكائن
print(dt)

import calendar
# لعرض تقويم سنة 2018 calendar من الكلاس prcal() هنا قمنا باستدعاء الدالة
calendar.prcal(2020)