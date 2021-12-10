n = 0
list_k = ['Один ', 'Два ', 'Три ', 'Четыре ']
with open('Work-4.txt', mode='r') as my_f_r, open('Work-4_rt.txt', encoding='Utf-8', mode='w') as my_f_w:
    for line in my_f_r:
        list_r = line.split('-')
        list_r[0] = list_k[n]
        n += 1
        my_f_w.write('-'.join(list_r))
        print(list_r)
