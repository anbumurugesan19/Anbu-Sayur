from datetime import date,datetime

#This function is used for cal the price based on the age
def calPrice(dob):
    Amount = 0
    # this curdate is stored the current datetime values
    curdate = datetime.now() 
    #get the current day
    curday = curdate.strftime("%A")
    #cal the age with current year - user birth year
    age = curdate.year - dob.year


    # give ticket amount based on the age..
    if age < 18:
        Amount += 20
    elif age >= 18 and age <= 60:
        Amount += 75
    elif age > 60:
        Amount += 50

    # if the current day is Thursday or Tuesday give 20% discount
    if (curday == "Thursday" or curday == "Tuesday"):
        Amount -= Amount*0.2


    #return the calculation amount
    return Amount


user = input("Enter your name: ")
year = int(input("Enter the birth year: "))
#check if the user birth year is greater than the present year
while year > date.today().year:
    print("Your year is greater than the present year")
    year = int(input("Enter a valid year "))
    
month = int(input("Enter the birth month: "))
day = int(input("Enter the birth day: "))

dob = date(year, month, day)
amount = calPrice(dob)
print(f"{user} your amount to entering the park is {amount}")