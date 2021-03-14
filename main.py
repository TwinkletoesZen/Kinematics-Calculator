# print("Welcome to Free Fall Calculator")

# Free_Fall_A = -9.81

# print("Enter V0")
# User_Entered_V0 = input(": ")

# print("Enter Time")
# User_Entered_Time = input(": ")

# print( float(User_Entered_V0) + Free_Fall_A * float(User_Entered_Time))

class Physic:

  def TheDefinitionofVelocity():
    print("Hi, Vf=V0+at")
  
    print("What Would you like to find?, Vf, V0, A or T")
    User_Desire_Var = input(": ").upper()
    
    if User_Desire_Var == "VF":
      print("Enter V0")
      User_Entered_V0 = input(": ")

      print("Enter Accleration")
      User_Entered_Accleration = input(": ")
      
      print("Enter Time")
      User_Entered_Time = input(": ")

      print(float(User_Entered_V0)+float(User_Entered_Accleration) * float(User_Entered_Time))

    elif User_Desire_Var == "V0":
      print("Enter VF")
      User_Entered_VF = input(": ")

      print("Enter Accleration")
      User_Entered_Accleration = input(": ")

      print("Enter Time")
      User_Entered_Time = input(": ")

      print(float(User_Entered_VF)/(float(User_Entered_Accleration)*float(User_Entered_Time)))

    elif User_Desire_Var == "A":
      print("Enter Vf")
      User_Entered_VF = input(": ")

      print("Enter V0")
      User_Entered_V0 = input(": ")

      print("Enter Time")
      User_Entered_Time = input(": ")

      print((float(User_Entered_VF)-float(User_Entered_V0))/float(User_Entered_Time))

    elif User_Desire_Var == "T":
      print("Enter Vf")
      User_Entered_VF = input(": ")

      print("Enter V0")
      User_Entered_V0 = input(": ")

      print("Enter Accleration")
      User_Entered_Accleration = input(": ")

      print((float(User_Entered_VF)-float(User_Entered_V0))/float(User_Entered_Accleration))


    elif User_Desire_Var == "BACK":
      return

    else:
      print("Try again later")


print("Welcome to a Physcis Calculator built by Twinkletoes")

while True:
  print("(1) Vf=V0+at), (2) d=V0t+1/2at^2")
  Command = input(": ").upper()
  if Command == "1":
    Physic.TheDefinitionofVelocity()
  elif Command == "2": 
    print("Coming Soon")
  elif Command == "EXIT":
    quit()
  else:
    print("Try Again, invaild command")