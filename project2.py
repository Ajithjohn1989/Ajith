class student:
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
           print(k.split("--"))
       file.close()
 def del_student(self):
     self.del_student=int("enter the student id to be removed: ")
     self.remove(del_student)
while True:
   print("1.Addstudent\n2.DisplayStudent\n3.Delete Student\n4.Exit")
   choice=int(input("enter your choice: "))
   if choice==1:
       student.addstudent()
   elif choice==2:
       student.readdata()
   elif choice==3:
       student.del_student()
   elif choice==4:
       break
   else:
       print("Invalid Input")