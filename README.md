# Cooperative-Scheduler-Python-NodeMCU-
Implementation of Cooperative Scheduler for NodeMCU in python

Cada tarea es creada en un objecto diferente y la funcionalidad está escrita en él.
Para el correcto funcionamiento del Scheduler es necesario que el método que queramos que se ejecute periódicamente se llame
Task.

Ejemplo:

    from Sched import Coop_Sched

    class Task1():


      def __init__(self, arg):
          self.arg=arg

      def Task(self):
          print(self.arg)
          print(self.add(1 , 1))

      def add(self, x, y):
        return x + y

    #Create object tasks
    t1 = Task1("Task 1")
    #Create scheduler object
    scheduler = Coop_Sched()
    #Add Tasks to scheduler
    scheduler.Add_Task(t1)
    scheduler.Add_Task(t2)
    #Start scheduler
    scheduler.Start()
    
   
Y la salida en consola será:
Task 1
2
Task 1
2
...
