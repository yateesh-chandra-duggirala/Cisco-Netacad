import time

class Student : 
    def take_nap(self, sec):
        print("I will take nap for some time.")
        time.sleep(sec)
        print("I rested peacefully. We shall resume")

student = Student()
student.take_nap(3)