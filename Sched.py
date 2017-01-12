#Scheduler

class Coop_Sched():

    def __init__(self):
        #scheduler task queue
        self.task_queue = []

    #Add task to scheduler task queue
    def Add_Task(self,task):
        self.task_queue.append(task)

    #start scheduler
    def Start(self):
        self.__Scheduler__()

    #the hearth of scheduler
    def __Scheduler__(self):
        while True:
            for tasks in self.task_queue:
                tasks.Task()

