# РЕГУЛЯРНЫЕ ВЫРАЖЕНИЯ

## ЗАДАНИЯ:
1. Поместить Фамилию, Имя и Отчество человека в полях lastnameи firstnameсоответственно surname. В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О. Подсказка: работайте со срезом списка (три первых элемента) при помощи " ".join([:2])и split(" ")регулярки здесь НЕ НУЖНЫ .
2. Привести все телефоны в формате +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999. Подсказка: используйте регулярки для обработки телефонов .
3. Объединить все дублирующиеся записи о человеке в одной. Подсказка: группируйте записи по ФИО (если будет сложно, группировать только по ФИ) .