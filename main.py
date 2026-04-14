from datetime import date
import sys

class Student:
    def __init__(self,name,age,num,birth):
        if not isinstance(age, int) or not isinstance(num, int):
            print("나이 또는 학번의 자료형이 잘못됨")
            sys.exit()
        else:
            self.name = name
            self.age = age
            self.num = num
            self.birth = birth
    def intro(self):
        print(f"제 이름은 {self.name} 이고 학번은 {self.num} 이고 나이는 {self.age} 살,생일은 {int(self.birth[:2])}월 {int(self.birth[2:])}일 입니다.")
    def isSchool(self):
        return date.today().weekday() < 5

class DdayStudent(Student):
    def __init__(self,name,age,num,birth):
        super().__init__(name,age,num,birth)
    def isBirthday(self):
        today = date.today()
        return (today.month, today.day) == (int(self.birth[:2]), int(self.birth[2:]))
            

seoxin = DdayStudent("양서진",18,20000,"0101")
seoxin.intro()
print(seoxin.isSchool())
print(seoxin.isBirthday())
