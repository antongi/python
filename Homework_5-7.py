import json
with open('Work-7.txt', 'r', encoding='Utf-8') as my_f, open('Work-7J.json', 'w') as my_f_w:
    my_list = [line.rstrip('.\n').split(' ') for line in my_f]
    sum_profit = 0
    for el in my_list:
        profit = int(el[2]) - int(el[3])
        del el[3]
        del el[1]
        el[1] = profit
        if profit > 0:
            sum_profit += profit
    sum_dict = {'average_profit': sum_profit}
    result_dict = dict(my_list)
    result_list = [result_dict, sum_dict]
    print(result_list)
    json.dump(result_list, my_f_w)


