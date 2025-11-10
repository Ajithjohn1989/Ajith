tasklist=[]
def add():
    taskcount=int(input("How many task you want to enter: "))
    for i in range(taskcount):
        mytask=input("Enter the task: ")
        tasklist.append([mytask,False])
        print(tasklist)
        return tasklist

def show():

    print("Tasks")
    for i,n in enumerate(tasklist,1):
        status="done" if n[1] else "incomplete"
        print(f"{i} {n[0]}-{status}")
print()

while True:
 print("todotasks")
 print("1.add\n2.show")
 c=int(input("Enter your choice: "))
 match c:
    case 1:
      add()

    case 2:
      show()

    case 3:
       print("invalid input")

