from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# pprint(contacts_list)


# Задание № 1: поместить Фамилию, Имя и Отчество человека в поля
# lastname, firstname и surname соответственно.

full_name = []
for item in contacts_list:
  sub_list = []
  for j in item[0:3]:
    sub_list.extend(j.split())
  sub_list.extend(item[3:])
  full_name.append(sub_list)
# pprint(full_name)

# Задание № 2: привести все телефоны в формат +7(999)999-99-99.
# Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999.

for item in full_name:
    pattern_phone = r"(\+7|8)(\s?\(?)(\d{3})(\-?\)?\s?)(\d{3})(\-?)(\d{2})(\-?)(\d{2})(\s?)(\(?)([д]?[о]?[б]?\.?)(\s?)(\d?\d?\d?\d?)(\)?)"
    result_phone = re.sub(pattern_phone, r"+7(\3)\5-\7-\9\10\12\14", item[5])
    item[5] = result_phone
pprint(full_name)

# Задание № 3: Объединить все дублирующиеся записи о человеке в одной.
# # Подсказка: группируйте записи по ФИО (если будет сложно, группировать только по ФИ).
dictionary = {}
for name, *specifications in full_name[1:]:
    if name not in dictionary:
        dictionary[name] = [""] * 6
    for i, (old, new) in enumerate(zip(dictionary[name], specifications)):
        dictionary[name][i] = old if old else new
contacts_result = [[k, *v] for k, v in dictionary.items()]

# # TODO 2: сохраните получившиеся данные в другой файл

with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(contacts_list)