from Site_Validation.site import *


def getValidPassword(prompt):

    while len(value := input(prompt)) < 6:
        print("❌ Password must be at least 6 characters!")
    return value


def makePassword():
     while True:
          prompt1, prompt2 = "Your Password: ", "Confirm Password: "
          pwd1 = getValidPassword(prompt1)
          pwd2 = getValidPassword(prompt2)

          if pwd1 == pwd2:
               return pwd1 
          else:
               print("Passwords don't match")
