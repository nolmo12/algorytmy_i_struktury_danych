#Zadanie 1.
def concate_character_and_name(first_name_character, last_name):
    return first_name_character+"."+last_name
polaczenie=concate_character_and_name('J', "Kowalski")
print(polaczenie)
#Zadanie 2.
def concate_to_upper(first_name, last_name):
    return first_name[0].capitalize()+"."+last_name.capitalize()
print(concate_to_upper("jan", "kowalski"))
#Zadanie 3.
def birthdate(first_two_numbers_of_year, last_two_numbers_of_year, age):
    rok=str(first_two_numbers_of_year)+str(last_two_numbers_of_year)
    rok=int(rok)
    return rok-age
print(birthdate(20, 22, 32))
#Zadanie 4.
def foo(a, b, function):
    return function(a, b)
print(foo("jan","kowalski",concate_to_upper))
#Zadanie 5.
def divide(a, b):
    if(a>0 and b>0 and b!=0):
        return a/b
    return "Blad"
print(divide(10,2))
#Zadanie 6.
suma=0
for x in range(100):
    print(suma)
    if(suma<100):
        suma+=x
    else:
        break
#Zadanie 7.
