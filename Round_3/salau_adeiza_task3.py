import random

def generate_password(length, include_special):
        if (type(length) == int) and ((include_special == "Y") or (include_special) == "N"):
            numbers = [1,2,3,4,5,6,7,8,9,0]
            letters = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
            special_char = ["!","@","#","$","%","^","&","*","(",")","_","-","=","+","[","]"]
            passList = []
            
            if include_special == "Y":
                for i in range(length):
                    num = numbers[random(0,len(numbers)-1)]
                    str = letters[random(0,len(letters)-1)]
                    char = special_char[random(0,len(special_char)-1)]
                    passList.append(num or str or char)
            else:
                for i in range(length):
                    num = numbers[random(0,len(numbers)-1)]
                    str = letters[random(0,len(letters)-1)]
                    char = special_char[random(0,len(special_char)-1)]
                    passList.append(num or str)
            return "".join(passList)
        else:
            return "error"
        
def run_app(func):
    print("Password Generator App")
    x = int(input("Enter Your Password Length: "))
    y = str(input("Do you want special character? (Y or N): "))
    password = func(x,y)
    if password == 'error':
        print("Please ensure you enter a number as your length and that you have answered 'Y' or 'N' to whether you want special character")
    else:
        print("Your Password is: ", password)

run_app(generate_password)

