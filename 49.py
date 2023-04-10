# Задача №49. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, 
# номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные.
# 2. Программа должна сохранять данные в текстовом файле.
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи (например: имя или фамилию человека).
# 4. Использование функций. Ваша программа не должна быть линейной.
# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.

def read_file():
    with open('dog.txt', 'r', encoding='UTF-8') as file:
        data = file.readlines()
    return data

def show_all():
    print('КЛИЧКА СОБАКИ'.ljust(15) + 'ПОРОДА СОБАКИ'.ljust(15) + 'ИМЯ ХОЗЯИНА'.ljust(15) + 'ТЕЛЕФОН ХОЗЯИНА'.ljust(15))
    for dog in read_file():        
        print(*[_.ljust(14) for _ in dog.strip().split(';')])

def new_contact():
    a = input('Введите кличку собаки: ')
    b = input('Введите породу собаки: ')
    c = input('Введите имя хозяина: ')
    d = input('Введите телефон хозяина: ')
    with open('dog.txt', 'a', encoding='UTF-8') as file:
        file.write('\n' + a + ';' + b + ';' + c + ';' + d)

def search_contakt():
    print('Введите цифру критерия поиска или "0" для выхода в главное меню:', '1. По кличке собаки.', '2. По породе собаки.', '3. По имени хозяина.', '4. По телефону хозяина.', sep='\n')
    n = input('>')
    if n == '1':
        s = input('Введите кличку собаки: ')
    if n == '2':
        s = input('Введите породу собаки: ')
    if n == '3':
        s = input('Введите имя хозяина: ')
    if n == '4':
        s = input('Введите телефон хозяина: ')
    if n == '0':
        return
    print('КЛИЧКА СОБАКИ'.ljust(15) + 'ПОРОДА СОБАКИ'.ljust(15) + 'ИМЯ ХОЗЯИНА'.ljust(15) + 'ТЕЛЕФОН ХОЗЯИНА'.ljust(15))    
    for dog in [_.strip().split(';') for _ in read_file()]:
        if dog[int(n) - 1] == s:
            for i in range(len(dog)):
                print(dog[i].ljust(15), end='')
            print()

def del_contact():    
    data = [_.strip().split(';') for _ in read_file()]
    for i in range(len(data)):
        data[i].insert(0, i + 1)
    print('№'.ljust(15) + 'КЛИЧКА СОБАКИ'.ljust(15) + 'ПОРОДА СОБАКИ'.ljust(15) + 'ИМЯ ХОЗЯИНА'.ljust(15) + 'ТЕЛЕФОН ХОЗЯИНА'.ljust(15))
    for dog in data:
        for i in range(len(dog)):
            print(str(dog[i]).ljust(15), end='')
        print()    
    n = int(input('Введите № строки для удаления или "0" для выхода в главное меню: '))
    if n == 0:
        return
    else:
        del data[n - 1]
    for i in range(len(data)):
        data[i].pop(0)        
    new_data = []
    for i in range(len(data)):
        new_data.append(';'.join(data[i]))
    new_data = '\n'.join(new_data)    
    with open('dog.txt', 'w', encoding='UTF-8') as file:
        file.write(new_data)

def changing_contact():
    data = [_.strip().split(';') for _ in read_file()]
    for i in range(len(data)):
        data[i].insert(0, i + 1)
    print('№'.ljust(15) + 'КЛИЧКА СОБАКИ'.ljust(15) + 'ПОРОДА СОБАКИ'.ljust(15) + 'ИМЯ ХОЗЯИНА'.ljust(15) + 'ТЕЛЕФОН ХОЗЯИНА'.ljust(15))
    for dog in data:
        for i in range(len(dog)):
            print(str(dog[i]).ljust(15), end='')
        print()    
    n = int(input('Введите № строки для изменения или "0" для выхода в главное меню: '))
    if n == 0:
        return
    else:
        print('Введите цифру критерия изменения или "0" для выхода в главное меню:', '1. Кличка собаки.', '2. Порода собаки.', '3. Имя хозяина.', '4. Телефон хозяина.', sep='\n')
        n_s = input('>')
        if n_s == '1':
            s = input('Введите кличку собаки: ')
        if n_s == '2':
            s = input('Введите породу собаки: ')
        if n_s == '3':
            s = input('Введите имя хозяина: ')
        if n_s == '4':
            s = input('Введите телефон хозяина: ')
        if n_s == '0':
            return    
    del data[n - 1][int(n_s)]
    data[n - 1].insert(int(n_s), s)    
    for i in range(len(data)):
        data[i].pop(0)        
    new_data = []
    for i in range(len(data)):
        new_data.append(';'.join(data[i]))
    new_data = '\n'.join(new_data)    
    with open('dog.txt', 'w', encoding='UTF-8') as file:
        file.write(new_data)

n = -1
while n != '0':
    print('СОБАКО-ТЕЛЕФОННЫЙ СПРАВОЧНИК')
    print('       Главное меню')
    print('1. Просмотр всех контактов.', '2. Создание нового контакта.', '3. Поиск контакта.', '4. Изменение контакта.', '5. Удаление контакта.', '0. Выход (окончание работы).', sep='\n')
    n = input('Введите цифру критерия выбора: ')
    if n == '1':
        show_all()
    if n == '2':
        new_contact()
    if n == '3':
        search_contakt()
    if n == '4':
        changing_contact()
    if n == '5':
        del_contact()
    




#changing_contact()

#del_contact()

# phone_book = []

# file = open('sample.txt', 'r', encoding='UTF-8')
# data = file.readlines() 
# file.close()
# for contact in data:
#     new_contact = contact.strip().split(';')
#     new_contact = {'name':new_contact[0],
#                    'phone':new_contact[1],
#                    'comment':new_contact[2]}
#     phone_book.append(new_contact)

# phone_book.append({'name': 'Антон Пальчиков',
#                    'phone': '999-999',
#                    'comment': 'Друг Ноггано'})
# print(phone_book)

# new_phone_book = []
# for contact in phone_book:
#     new_contact = ';'.join([values for values in contact.values()])
#     new_phone_book.append(new_contact)

# new_phone_book = '\n'.join(new_phone_book)

# file = open('sample.txt', 'w', encoding='UTF-8')
# file.write(new_phone_book)
# file.close()

# cont = '\nАнгелина Воробьева;4564654;Куртизанка'

# file = open('sample.txt', 'a', encoding='UTF-8')
# file.write(cont)
# file.close()

# with open('sample.txt', 'a', encoding='UTF-8') as file:
#     file.write(cont)
