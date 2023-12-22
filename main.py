# string = '1 2 3 5 8 15 23 38'
# listVar = string.split()

   
# listOut = list()
# for i in listVar:
#     i = int(i)
#     if i % 2 == 0:
#         listOut.append((i, i**2))

# print(listOut)

# listInput = [1, 2, 3, 5, 8, 15, 23, 38]

# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# res = select(int, listInput)
# res = where(lambda x: x % 2 == 0, res)
# res = select(lambda x: (x, x*x), res)
# print(res)


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# listVar = list(filter(lambda x: x[0] != x[1], orbits))
# listVar = sorted(list(map(lambda x: (int(x[0]*x[1]), x), listVar)))
# print(listVar[-1][1])



# def print_operation_table(f, num_rows=9, num_columns=9):
#     if num_rows < 2:
#         print('ОШИБКА! Размерности таблицы должны быть больше 2!')
#         return
    
#     print(*[i for i in range(1, num_columns + 1)])
#     for j in range(2, num_rows + 1):
#         print(j, end='')
#         print(*[f(j, i) for i in range(2, num_columns + 1)])

# print_operation_table(lambda x, y: x + y, 4, 4)



# stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'.lower()
# phraseList = stroka.split()
# vowels = 'аеёиоуыэюя'
# sumSet = set()

# if len(phraseList) < 2:
#     print('Количество фраз должно быть больше одной!')
# else:
#     for item in phraseList:
#         sumSet.add(len([character for character in item if character in vowels]))
#     if len(sumSet) > 1:
#         print('Пам парам')
#     else:
#         print('Парам пам-пам')
    

# listInput = '8 11 0 -23 140 1'.split()
# print(*list(filter(lambda x: 10 <= abs(int(x)) < 100, listInput)))
# print(*list(filter(lambda x: len(str(abs(int(x)))) == 2, listInput)))

filePath = 'phonebook.txt'

def show_menu():
    print('1. Распечатать справочник\n'
          '2. Найти телефон по фамилии\n'
          '3. Изменить номер телефона\n'
          '4. Удалить запись\n'
          '5. Найти абонента по номеру телефона\n'
          '6. Добавить абонента в справочник\n'
          '7. Добавить абонента из другого справочника\n'
          '8. Закончить работу\n', sep = '\n')
    choice = int(input('Введите номер пункта меню: '))
    return choice

def read_txt(filePath):
      phone_book = []
      fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
      with open(filePath, 'r', encoding = 'utf-8') as phb:
            for line in phb:
                  record = dict(zip(fields, line.split(',')))
                  phone_book.append(record)

      return phone_book

def write_txt(filePath, phone_book):
      with open(filePath, 'w', encoding = 'utf-8') as pb_out:
            for index in range(0, len(phone_book)):
                  string = ''
                  for value in phone_book[index].values():
                        string += value + ','
                  pb_out.write(f'{string[:-1]}\n')

def find_by_lastname(phone_book, last_name):
      for item in phone_book:
            if last_name == item['Фамилия']:
                  return item['Телефон']
      return 'Абонент не найден'

def find_by_number(phone_book, number):
      for item in phone_book:
            if number == item['Телефон']:
                  return item.values()
      return 'Абонент не найден'

def add_user(phone_book, user_data):
      phone_book.append(user_data)
      write_txt(filePath, phone_book)
      return 'Абонент ' + user_data['Имя'] + ' ' + user_data['Фамилия'] + ' добавлен'

def change_number(phone_book, last_name, new_number):
      newItem = {}
      for item in phone_book:
            if last_name == item['Фамилия']:
                  newItem = item
                  newItem['Телефон'] = new_number
                  phone_book.remove(item).append(newItem)
                  write_txt(filePath, phone_book)
                  return 'Номер телефона абонента ' + newItem['Имя'] + ' ' + newItem['Фамилия'] + ' изменен'
      return 'Абонент не найден'

def delete_by_lastname(phone_book, last_name):
      for item in phone_book:
            if last_name == item['Фамилия']:
                  phone_book.remove(item)
                  write_txt(filePath, phone_book)
                  return 'Абонента ' + item['Имя'] + ' ' + item['Фамилия'] + ' удален'
      return 'Абонент не найден'

def work_with_phonebook():
      choice = show_menu()
      phone_book = read_txt(filePath)

      while (choice != 8):
            if choice == 1:
                  print(phone_book)
            elif choice == 2:
                  last_name = input('Введите фамилию: ')
                  print(find_by_lastname(phone_book, last_name))
            elif choice == 3:
                  last_name = input('Введите фамилию: ')
                  new_number = input('Введите номер телефона: ')
                  print(change_number(phone_book, last_name, new_number))
            elif choice == 4:
                  lastname = input('Введите фамилию: ')
                  print(delete_by_lastname(phone_book, lastname))
            elif choice == 5:
                  number = input('Введите номер телефона: ')
                  print(find_by_number(phone_book, number))
            elif choice == 6:
                  fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
                  user_data = {}
                  for item in fields:
                        inputStr = input('Введите ' + item + ': ')
                        if len(inputStr) == 0:
                              inputStr = input('Введите ' + item + ': ')
                        user_data[item] = inputStr
                  print(add_user(phone_book, user_data))
            elif choice == 7:
                  fileName = input('Введите наименование файла: ')
                  if len(fileName) > 0:
                        phoneList = read_txt(fileName)
                        for index in range(len(phoneList)):
                              print(f'{(index + 1)}. {phoneList[index]["Имя"]} {phoneList[index]["Фамилия"]} - {phoneList[index]["Телефон"]}')
                        numberItem = (int(input('Введите номер строки нужного абонента: ')) - 1)
                        phone_book.append(phoneList[numberItem])
                        write_txt(filePath, phone_book)
            choice = show_menu()

work_with_phonebook()