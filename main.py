from Sched import Coop_Sched

class Task1():


    def __init__(self, arg):
        self.arg=arg

    def Task(self):
        print(self.arg)
        print(self.add(1 , 1))

    def add(self, x, y):
        return x + y

class Task2():

    def __init__(self,arg):
        self.arg=arg

    def Task(self):
        print(self.arg)


#Create object tasks
t1 = Task1("Task 1")
t2 = Task2("Task 2")
#Create scheduler object
scheduler = Coop_Sched()
#Add Tasks to scheduler
scheduler.Add_Task(t1)
scheduler.Add_Task(t2)
#Start scheduler
scheduler.Start()