def addstudent ():
      name=input("enter your name: ")
      age=input("enter your age: ")
      course=input("enter your course: ")
      std_id=input("enter student ID: ")
      file=open("std_details.txt","a")
      file.write(f"\n {name}--{age}--{course}--{std_id}")
      file.close()
def readdata():
       file=open("std_details.txt","r")
       data=file.readlines()
       for k in data:
           print((k))
       file.close()
def del_student():
     filename = "std_details.txt"
     num=int(input("enter the Id to be deleted: "))
     delete = num

     # Read all lines
     with open(filename, "r") as file:
         lines = file.readlines()

     # Filter out the value
     with open(filename, "w") as file:
         for line in lines:
             if line.pop() == num:
                 file.write(line)



while True:
   print("1.Add student\n2.Display Student\n3.Delete Student\n4.Exit")
   choice=int(input("enter your choice: "))
   if choice==1:
       addstudent()
   elif choice==2:
       readdata()
   elif choice==3:
       del_student()
   elif choice==4:
       break
   else:
       print("Invalid Input")