f = open(r'E:\Project_Python\Lesson_5\my_file_1.txt', 'w')
str_list = ['stroka_1\n', 'stroka_2\n', 'stroka_stroka\n']
f.writelines(str_list)
f.close()