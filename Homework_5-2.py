lines = 0
with open('Work-2.txt', 'r') as f:
    for line in f:
        lines += 1
        line_list = line.split(' ')
        print(f'Кол-во слов в строке {lines} - {len(line_list)}')
    print(f'Кол-во строк - {lines}')
