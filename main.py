import math

class Kinemetics:
  
  def QuantityFinder():
    Initial_Velocity = False
    Final_Velocity = False
    Acceleration = False
    Displacement = False
    Time = False
    
    print("Please Enter the Quantity Given in the questions, (V0, Vf, a, d, t)")
    Quantity_Given = input(": ").upper()
    
    Initial_Velocity = "V0" in Quantity_Given
    Final_Velocity = "VF" in Quantity_Given
    Acceleration = "A" in Quantity_Given
    Displacement = "D" in Quantity_Given
    Time = "T" in Quantity_Given
    
    


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


  def TheDisplacementCurve():
    print("Hi, d=V0t+1/2at^2")
    print("What Would you like to find?")
    User_Desire_Var = input(": ").upper()

    if User_Desire_Var == "D":
      User_Entered_V0 = input("V0: ")
    
      User_Entered_Time = input("Time: ")

      User_Entered_Accleration = input("A: ") 

      print( (float(User_Entered_V0)*float(User_Entered_Time)) + (1/2 * float(User_Entered_Accleration) * float(User_Entered_Time)**2))

    elif User_Desire_Var == "V0":
      User_Entered_D = input("D: ") 

      User_Entered_Time = input("T: ")

      User_Entered_Accleration = input("A: ")

      print("Coming Soon")
      # print( float(User_Entered_D)/float(User_Entered_Time) - (1/2*float(User_Entered_Accleration)    

    elif User_Desire_Var == "A":
      User_Entered_D = input("D: ")
    
      User_Entered_V0 = input("V0: ")

      User_Entered_Time = input("A: ")

      print("Coming Soon")
      # print("")

    elif User_Desire_Var == "T":
      User_Entered_D = input("D: ")

      User_Entered_V0 = input("V0: ")

      User_Entered_Accleration = input("A: ")

      print("Coming Soon")
      # print("")

    elif User_Desire_Var == "BACK":
      return

    else:
      print("Wrong Command")
      



print("Welcome to a Physcis Calculator built by Twinkletoes")



# while True:
#   print("(1) Vf=V0+at), (2) d=V0t+1/2at^2")
#   Command = input(": ").upper()
#   if Command == "1":
#     Kinemetics.TheDefinitionofVelocity()
#   elif Command == "2": 
#     Kinemetics.TheDisplacementCurve()
#   elif Command == "EXIT":
#     quit()
#   else:
#     print("Try Again, invaild command")

