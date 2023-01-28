from data_create import name_data, surname_data, adress_data, phone_data


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()
    var = int(input(f"В каком варианте записать данные?\n\n"
                    f"1 вариант:\n"
                    f"{name}\n"
                    f"{surname}\n"
                    f"{phone}\n"
                    f"{adress}\n\n"
                    f"2 вариант:\n"
                    f"{name};{surname};{phone};{adress}\n\n"
                    f"Выберите номер варианта: "))

    while var != 1 and var != 2:
        var = int(input("Ещё один шанс! Ваш выбор: "))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding = 'utf-8') as file:
            file.write(f'{name}\n{surname}\n{phone}\n{adress}\n\n')
    else:
        with open('data_second_variant.csv', 'a', encoding = 'utf-8') as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')

    print('Успешно !!')

def print_data():
    print('1 файл: ')
    with open('data_first_variant.csv', 'r', encoding = 'utf-8') as file:
        data_first = file.readlines()
        data_first_second = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_second.append(''.join(data_first[j:i]))
                j = i
        data_first = data_first_second
        print(''.join(data_first))



    print('2 файл: ')
    with open('data_second_variant.csv', 'r', encoding = 'utf-8') as file:
        data_second = list(file.readlines())

        print(*data_second)
    
    return data_first, data_second

def put_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()
    var = int(input(f"В каком варианте изменить данные?\n\n"
                    f"1 вариант:\n"
                    f"{name}\n"
                    f"{surname}\n"
                    f"{phone}\n"
                    f"{adress}\n\n"
                    f"2 вариант:\n"
                    f"{name};{surname};{phone};{adress}\n\n"
                    f"Выберите номер варианта: "))

    while var != 1 and var != 2:
        var = int(input("Ещё один шанс! Ваш выбор: "))

    if var == 1:
        print_data(1)
        with open('data_first_variant.csv', 'r', encoding = 'utf-8') as file:
            dir_num = int(input('\nУкажите номер записи, которую Вы хотите изменить: '))
            book = file.readlines()
            new_book = []
            counter = 1
            i = 0
            while i < len(book):
                if counter != dir_num:
                    if book[i] != '\n':
                        new_book.append(f'{book[i]}')
                        i += 1
                    else:
                        new_book.append('\n')
                        counter += 1
                        i += 1
                else:
                    new_book.extend([name_data() + '\n', surname_data() + '\n', phone_data() + '\n', adress_data() + '\n', '\n'])
                    counter += 1
                    i += 5

        with open('data_first_variant.csv', 'w', encoding = 'utf-8') as file:
            for i in new_book:
                file.write(i)
                
    else:
        with open('data_second_variant.csv', 'r', encoding = 'utf-8') as file:
            print_data(2)
            dir_num = int(input('\nУкажите номер записи, которую Вы хотите изменить: '))
            book = file.readlines()
            new_book = []
            counter = 1
            i = 0
            while i < len(book):
                if counter != dir_num:
                    if book[i] != '\n':
                        new_book.append(f'{book[i]}')
                        i += 1
                    else:
                        new_book.append('\n')
                        counter += 1
                        i += 1
                else:
                    new_book.append(f'{name_data()};{surname_data()};{phone_data()};{adress_data()}\n')
                    counter += 1
                    i += 1

        with open('data_second_variant.csv', 'w', encoding = 'utf-8') as file:
            for i in new_book:
                file.write(i)



def delete_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()
    var = int(input(f"В каком варианте удалить данные?\n\n"
                    f"1 вариант:\n"
                    f"{name}\n"
                    f"{surname}\n"
                    f"{phone}\n"
                    f"{adress}\n\n"
                    f"2 вариант:\n"
                    f"{name};{surname};{phone};{adress}\n\n"
                    f"Выберите номер варианта: "))

    while var != 1 and var != 2:
        var = int(input("Ещё один шанс! Ваш выбор: "))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding = 'utf-8') as file:
            print_data(1)
            dir_num = int(input('\nУкажите номер записи, которую Вы хотите удалить: '))
            book = file.readlines()
            new_book = []
            counter = 1
            i = 0
            while i < len(book):
                if counter != dir_num:
                    if book[i] != '\n':
                        new_book.append(f'{book[i]}')
                        i += 1
                    else:
                        new_book.append('\n')
                        counter += 1
                        i += 1
                else:
                    counter += 1
                    i += 5
                
        with open('data_first_variant.csv', 'w', encoding = 'utf-8') as file:
            for i in new_book:
                file.write(i)

    else:
        with open('data_second_variant.csv', 'a', encoding = 'utf-8') as file:
            print_data(2)
            dir_num = int(input('\nУкажите номер записи, которую Вы хотите удалить: '))
            book = file.readlines()
            new_book = []
            counter = 1
            i = 0
            while i < len(book):
                if counter != dir_num:
                    if book[i] != '\n':
                        new_book.append(f'{book[i]}')
                        i += 1
                    else:
                        new_book.append('\n')
                        counter += 1
                        i += 1
                else:
                    counter += 1
                    i += 2
            
        with open('data_second_variant.csv', 'w', encoding = 'utf-8') as file:
            for i in new_book:
                file.write(i)
