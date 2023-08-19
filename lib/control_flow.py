#!/usr/bin/env python3

def admin_login(username, password):
    if username == "admin":
       password == 12345 
       print("access granted")
    elif username == "ADMIN":
         password == 12345
         print("access granted")   
    else :
        print("access denied")   
    
#admin_login("ADMIN", 12345)    

def hows_the_weather(temperature):
    if temperature < 40 :
        print("It's brisk out there!")
    elif temperature <= 65 :
        print("It's a little chilly out there!")
    elif temperature > 85 :
        print("It's too dang out there! ")    
    else:
        print("It's perfect out there!")

#hows_the_weather(90)        

def fizzbuzz(num):
    # your code here
    pass

def calculator(operation, num1, num2):
    # your code here
    pass
