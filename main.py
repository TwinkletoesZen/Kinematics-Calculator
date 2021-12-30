import math
class Kinemetics:
  
  def QuantityFinder():
    Initial_Velocity = True
    Final_Velocity = True
    Acceleration = True
    Displacement = True
    Time = True
    
    print("Please Enter the Irrelveant Quantity in the questions, (V0, Vf, a, d, t)")
    Quantity_Given = input(": ").upper()
    

    Initial_Velocity = "V0" not in Quantity_Given
    Final_Velocity = "VF" not in Quantity_Given
    Acceleration = "A" not in Quantity_Given
    Displacement = "D" not in Quantity_Given
    Time = "T" not in Quantity_Given
    
    print(Initial_Velocity, Final_Velocity, Acceleration, Displacement, Time)

    if Time == False:
      print("Using Equation Vf^2=V0^2+2ad")
      
      list_of_Quantity_Needed = []
      n = int(input("Enter the Quantity in the Given Order (V0, Vf, a, d, t): "))
      
      for x in range(0, n):
        numbers= int(input())
        list_of_Quantity_Needed.append(numbers)
      
      print(list_of_Quantity_Needed)



  def TheDefinitionofAccleration():
    print("Vf=V0+at")
  
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
Kinemetics.QuantityFinder()



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

