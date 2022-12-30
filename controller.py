from model import read_csv, find_employee, find_employee_by_title, find_employee_by_salary, \
                  add_employee, csv_export, delete_employee, update_employee_data, json_export
from view import show_menu as ui

def controller():
    position = -1
    while position != 9:
        position = ui()
        data = read_csv()
        match position:
            case 1:
                find_employee(data)
            case 2:
                find_employee_by_title(data)
            case 3:
                find_employee_by_salary(data)
            case 4:
                add_employee(data)
            case 5:
                delete_employee(data)
            case 6:
                update_employee_data(data)
            case 7:
                json_export(data)
            case 8:
                csv_export(data)
    else:
        print("\t========== End ==========")