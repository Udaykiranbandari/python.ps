# EASY QUESTIONS
# question-1
num1 = int(input("enter a number:"))

if num1 == 0:
    print("zero")

elif num1 >= 0:
    print("positive")
else:
   print("negitive")

# question-2
num3= int(input("Enter a Number:"))

if num3 % 2 == 0:
  print("Even")
else :
  print("odd")

# question-3
num4 =int(input("Enter a number:"))

if num4 >= 18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")
# question-4
num5 = int(input("Enter a number:"))
num6 = int(input("Enter a number:"))
if num5 > num6:
  print("the greatest of two numbers is num5:",num5)
else:
  print("the greatest of two numbers is num6:",num6)

# question-5
num1=50
res = "pass" if num1 >= 40 else "fail"
print(res)
#  question-6

num1 = int(input("Enter a Day:"))
if num1 == 1:
  print("monday")
elif num1 == 2:
  print("tuesday")
elif num1 == 3:
  print("wednesday")
elif num1 == 4:
  print("thursday")
elif num1 == 5:
  print("friday")
elif num1 == 6:
  print("saturday")
elif num1 == 7:
  print("sunday")
else:
  print("invalid")

# question-8
def get_month_name(month_number):
    if month_number == 1:
        return "January"
    elif month_number == 2:
        return "February"
    elif month_number == 3:
        return "March"
    elif month_number == 4:
        return "April"
    elif month_number == 5:
        return "May"
    elif month_number == 6:
        return "June"
    elif month_number == 7:
        return "July"
    elif month_number == 8:
        return "August"
    elif month_number == 9:
        return "September"
    elif month_number == 10:
        return "October"
    elif month_number == 11:
        return "November"
    elif month_number == 12:
        return "December"
    else:
        return "Invalid month number!"

month_number = int(input("Enter a month number (1-12): "))
print("Month:", get_month_name(month_number))

# MEDIUM QUESTIONS
# question-1
while True:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    c = int(input("Enter the third number: "))
    
    if a >= b and a >= c:
        print("The greatest number is {a}")
    elif b >= a and b >= c:
        print("The greatest number is {b}")
    else:
        print("The greatest number is {c}")
    
    # question-2
    year = int(input())
if year % 4 ==0:
  print(year, "is a leap year")
elif year %400 ==0:
  print(year,"is a leap year")
else:
  print("not a leap year")

  # question-3
  while True:
    char = input("Enter a  single character: ").lower()
    if len(char) != 1:
        print("invalid input")
    elif char in ["a","e","i","o","u"]:
        print("it is a vowel")
    elif char.isalpha():
        print("it is a consonant.")
    else:
        print("special characters and symbols are not accepted")

        # question-4
  marks = int(input("Enter marks:"))
if marks > 100:
    print("invalid input")
elif marks >= 90 and marks <=100 :
    print("grade-A")
elif marks >= 80 and marks <=89:
    print("grade-B")
elif marks >=70 and  marks <=79:
    print("grade-C")
else:
    print("FAIL")


# questions-5

a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
c = int(input("Enter c number: "))

if a + b > c and a + c > b and b + c > a:
    print("Yes, it forms a triangle")
else:
    print("It does not form a triangle")

    