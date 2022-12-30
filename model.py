import csv
import json

def read_csv():
    employee = []
    with open('database.csv', 'r', encoding='UTF-8') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            employee.append(new_employee(row))
    return employee

def find_employee(data):
    print('\n===== Поиск сотрудника =====')
    name = input('-> Введите Имя или Фамилию сотрудника: ')
    [print(*i) for i in map(dict.values, filter(lambda x: x['first_name'] == name or x['last_name'] == name, data))]

def find_employee_by_title(data):
    print('\n===== Должность =====')
    employee_title = [i for i in enumerate(sorted(set(map(lambda x: x['position'], data))), 1)]
    [print("\t", *i) for i in employee_title]
    title = employee_title[int(input('-> Выберите ID должности: ')) - 1][1]
    print(f'\n===== {title} =====')
    [print(*i) for i in map(dict.values, filter(lambda x: x['position'] == title, data))]

def find_employee_by_salary(data):
    print('\n===== Зарплата =====')
    salary_min, salary_max = filter(str.isdigit, input('-> Задайте верхний и нижний порог зарплаты через пробел: ').split())
    [print(*i) for i in map(dict.values, filter(lambda x: float(salary_min) < x.get('salary') < float(salary_max), data))]

def new_employee(row):
    temp = dict()
    temp["id"] = int(row[0])
    temp["last_name"] = row[1].title()
    temp["first_name"] = row[2].title()
    temp["position"] = row[3]
    temp["phone_number"] = row[4]
    temp["salary"] = float(row[5])
    return temp

def add_employee(data):
    print('\n===== Добавить сотрудника =====')
    param = [data[-1]['id'] + 1, input('-> Фамилия: '), input('-> Имя: '),
             input('-> Должность: '), input('-> Телефон: '), input('-> Зарплата: ')]
    info = [s for s in param]
    data.append(new_employee(info))
    save_db(data)

def delete_employee(data):
    print('\n===== Удалить сотрудника =====')
    [print(*i) for i in map(dict.values, data)]
    employee_id = int(input('-> ID номер сотрудника на удаление: '))
    index = int(*map(data.index, filter(lambda x: x['id'] == employee_id, data)))
    print("* Запись -", data[index]['first_name'], data[index]['last_name'], "- успешно удалена из БД *")
    data.pop(index)
    save_db(data)

def update_employee_data(data):
    print('\n===== Обновление данных сотрудника =====')
    [print(*i) for i in map(dict.values, data)]
    employee_id = int(input('-> ID номер сотрудника для обновления: '))
    index = int(*map(data.index, filter(lambda x: x['id'] == employee_id, data)))
    print(*data[index].values())
    print('1 - Изменить фамилию\n2 - Изменить имя\n3 - Изменить должность\n4 - Изменить телефон\n5 - Изменить зарплату')
    match int(input('-> Номер параметра для обновления: ')):
        case 1:
            data[index]['last_name'] = input('-> Изменить фамилию: ')
        case 2:
            data[index]['first_name'] = input('-> Изменить имя: ')
        case 3:
            data[index]['position'] = input('-> Изменить должность: ')
        case 4:
            data[index]['phone_number'] = input('-> Изменить телефон: ')
        case 5:
            data[index]['salary'] = float(input('-> Изменить зарплату: '))
    save_db(data)

def json_export(data):
    with open('json-export.json', 'w', encoding='UTF-8') as file:
        json.dump(data, file)
        print(f'===== Данные экспортированы {file.name} =====')

def csv_export(data):
    with open('csv-export.csv', 'w', newline='', encoding='UTF-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writerows(data)
        print(f'===== Данные экспортированы {file.name} =====')

def save_db(data):
    with open('database.csv', 'w', newline='', encoding='UTF-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writerows(data)
        print(f'===== Изменения сохранены {file.name} =====')