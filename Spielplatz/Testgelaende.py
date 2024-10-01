'''#Aufgabe1
def extract_area_code(phone_number):
    if "(" in phone_number:
        position_one = phone_number.find("(")
        position_one=position_one+1

        position_two =phone_number.find(")")

        area=phone_number[position_one:position_two]

        return (area)


phone_number=("(120) 291 - 6932")
print(extract_area_code(phone_number))'''
import area_and_volume_calculator

#------------------------------------------------------

#Aufgab2
'''def duplicate_last_item(random_list):
    double=random_list[-1] #last element
    random_list.append(double) #list+last element
    return random_list

random_list=["3", 3, 3.0, 20]
print(duplicate_last_item(random_list))'''

'''

def duplicate_last_item(random_list):
    double = random_list[-1]  # Letztes Element der Liste abrufen
    print(double)  # Letztes Element ausgeben
    random_list.append(double)  # Letztes Element der Liste nochmal anhängen
    return random_list  # Die Liste zurückgeben

# Verwende eine Liste anstelle eines Tupels
random_list = [3, 3, 3.0, 20]

# Die Funktion aufrufen und das Ergebnis ausgeben
print(duplicate_last_item(random_list))'''

#------------------------------------------------

#Aufgabe 3
'''
def add_tax (price):
    if price>100:
        price=price*1.15
        return (price)
    else:
        return (price)
add_tax(120)
'''

#-----------------------------------------------


#Aufgabe4
'''
def count_first_letter(text):
    letter=text[0]
    print(letter)
    number=int(text.count(letter))
    return (number)


print (count_first_letter("alaska"))
print (type(count_first_letter("alaska")))
'''
#----------------------------------------------

#Aufgabe5

'''
def reformat_date (date):
    days=date[3:5] #Tag
    month=date[0:2] #Monat
    year=date[6:] #Jahr

    new_date=(days+"/"+month+"/"+year) #Neu geordneter String
    #print(new_date)
    return (new_date)

reformat_date("12-25-2021") #Aufruf der Funktion
'''

#----------------------------------------------

#Aufgabe6

"""
def generate_case_variants(text):
    headlineup=text.upper()
    #print (headlineup)
    headlinelow = text.lower()
    #print (headlinelow)
    headlist=[headlinelow,headlineup]
    #print (headlist)
    return (headlist)

generate_case_variants("Hallo")
"""

#----------------------------------------------

#Aufgabe7

'''
def validate_discount(products):
    numbers=len (products)
    if numbers>= 5 and "Ice Cream" in products: #Beide Faktoren in einer UND-Abrfage
        validation="YES"
        return (validation)
    else:
        validation="NO"
        return (validation)


shopping=["Ice Cream", "Eggs", "Bacon", "Dog", "Gun"]
validate_discount(shopping)

'''

#-----------------------------------------------------

#Aufgabe8
'''
def has_passed(grade1, grade2):
    if grade1<=55 or grade2<=55 or ((grade1+grade2)/2)<75:
        passing="FAIL"
        #print(passing)
        #print(type(passing))
        return(passing)
    else:
        passing="PASS"
        #print(passing)
        #print(type(passing))
        return(passing)
has_passed(60,80)'''

#-------------------------------------------------------

#Aufgabe9

'''
def period_adder(sentence):
    period=sentence[-1]
    if period=="." or period=="!" :
        #print (sentence)
        return(sentence)

    else:
        sentence=sentence+"."
        #print(sentence)
        return (sentence)

period_adder("New Park Opens to Rave Reviews")

'''
#--------------------------------------------------

#Aufgabe10

'''
def convert(value):
    if "€" in value:
        value=int(value[1:])
        value=value*1.1
        value=round(value,2)
        value = str(value)
        value = ("$" + value)
        #print(value)
        return (value)
    else:
        value = int(value[1:])
        value = value / 1.1
        value = round(value, 2)
        value=str(value)
        value=("€"+value)
        #print(value)
        return (value)
convert("$110")

'''
#Aufgabe11

'''
def is_leap(year):
    century1=str(year)[-2:]
    cebtury2=year%400
    #print (century1)
    #print (cebtury2)
    quarter=year%4
    #print(quarter)
    if quarter==0 and century1!= "00":
        result="Leap year"
        return (result)
    elif century1=="00" and cebtury2==0:
        result2 = "Leap year"
        return(result2)
    else:
        result3 = "Not a leap year"
        return(result3)

is_leap(1900)
'''

import area_and_volume_calculator


print((area_and_volume_calculator))