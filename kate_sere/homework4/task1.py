my_dict = {}

my_dict['tuple'] = (1, 2, 5, 10, 'text')
my_dict['list'] = ['one', 2, 6, None, 5]
my_dict['dict'] = {'one': 'text1', 'two': 'text2', 'three': 'text3', 'four': True, 'five': False}
my_dict['set'] = {'set1', 5, 5, 6, 7, True, None}

# последний элемент кортежа
last_tuple_value = my_dict["tuple"][-1]
print(last_tuple_value)

# добавить элемент в список
my_dict['list'].append('last')
# удалить элемент 2-й элемент списка (индексом 1)
removed_list_value = my_dict['list'].pop(1)
1
# добавить элемент с ключом "i am a tuple" и любым значением
my_dict['dict'].update({'i am a tuple': 30})
# удалить любой элемент
my_dict['dict'].pop('one')

# добавить элемент в set
my_dict['set'].add('new')
# удалить элемент из set/ my_set.remove(3) my_set.discard() безопасное удаление
my_dict['set'].discard(True)

for key, value in my_dict.items():
    print(f'{key}: {value}')

