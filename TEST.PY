def bisiesto(year):
    if type(year) == int:
        year = int(year)
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            print(f"El año {year} es bisiesto")
        else:
            print(f"El año {year} no es bisiesto")
    else:
        print("El valor ingresado no es numerico")


bisiesto(12)
