from shop_service import *
import pyodbc
import datetime
import random as r

def generate_dates_birth_employees():
    range_dates_birth_employees = []
    date_start = datetime.date(1990, 9, 13)  
    date_end = datetime.date(1995, 9, 13)
    delta_dates = date_end - date_start
    for date in range(delta_dates.days + 1):
        range_dates_birth_employees.append(date_start + datetime.timedelta(date))
    return range_dates_birth_employees

def genarate_employees_info():
    employees_info=[]
    employees_status = ['женат', 'не женат']
    employees_children = ['да', 'нет']

    for i in range(10):
        employee_status = r.choice(employees_status)
        birth_employee = str (r.choice(generate_dates_birth_employees()))
        employee_children = r.choice(employees_children)
        employees_info.append((employee_status, birth_employee, employee_children))
    
    return employees_info
         



def genarate_products():
    products=['колбаса','хлеб','молоко','сметана','макороны','сыр','капуста','соль','сахар','картошка','лук',
            'арбуз','сгушенка','шоколад','пиво','водка','кола','мясо курицы','мясо говядины','мясо свинины']
    return products  

def product_storage():
    storage=['колбаса','хлеб','молоко','сметана','макороны','сыр','капуста','соль','сахар','картошка','лук',
            'арбуз','сгушенка','шоколад','пиво','водка','кола','мясо курицы','мясо говядины','мясо свинины']
    return storage

def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            list_info_client = file.read().split("\n")
            if not list_info_client or list_info_client == ['']:
                raise EmptyFileError("Файл пустой")
            return list_info_client
    except FileNotFoundError:
        raise FileNotFoundError("Файла или директории не существует")
    except IOError:
        raise IOError("Ошибка файловой системы")
    
    
def generate_full_name(list_fisrtnames, list_lastnames, list_patronymics):
    firstname = r.choice(list_fisrtnames)
    lastname = r.choice(list_lastnames)
    patronymic = r.choice(list_patronymics)
    if list_fisrtnames.index(firstname) >= 32:
        if patronymic[-2:] == "ич":
            patronymic = patronymic[:-2] + "на"
        else:
            patronymic = patronymic[:-2] + "овна"
        if lastname[-1] == "в" or lastname[-1] == "н":
            lastname = lastname + "а"
        elif lastname[-1] == "и" or lastname[-1] == "й":
            lastname = lastname[:-2] + "ая"
    full_name = [lastname, firstname, patronymic]
    return " ".join(full_name)


def main ():

    list_fisrtnames = read_file("firstnames.txt")
    list_lastnames = read_file("lastnames.txt")
    list_patronymics = read_file("patronymics.txt")

 
    print(generate_full_name(list_fisrtnames, list_lastnames, list_patronymics))
    write_database("employees", generate_full_name(list_fisrtnames, list_lastnames, list_patronymics))
    #products = genarate_products()
    #write_database ("product", products)
    #storage = product_storage()
    #write_database ("storage", storage)
    #print (genarate_employees_info())
    #write_database('suppliersinfo',genarate_employees_info())
    

    







if "__main__" == __name__:
    
    try:
        main()
    except Exception as error:
      
        print(error)
