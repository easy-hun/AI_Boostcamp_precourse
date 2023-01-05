# 필수 수강강좌 인공지능 기초다지기 1.1 ~ 1.2
print("<< 필수 수강강좌 인공지능 기초다지기 1.1 ~ 1.2 >>")

### 1 자료구조 (보강 필요)
print('\n\n### 1 자료구조 ###')

# tuple
s = (1,)
print(str(s))

# dict
from collections import OrderedDict
d = dict()
d = {1, 'myName'}
print(str(d))

# deque
from collections import deque

deque_list = deque()
deque_list.append(1)
deque_list.append(2)
deque_list.append(3)
deque_list.appendleft(0)
print(str(deque_list))

# time
import time

### 2 OOP
print('\n\n### 2 OOP ###')

# class 객체
class SoccerPlayer(object):
    # __init__ : 객체 초기화 예약 함수 (C의 생성자 느낌)
    def __init__(self, name : str, position : str, back_number : int):
        # self 는 C++/Java의 this와 비슷함, 생성된 instance 자신
        self.name = name
        self.position = position
        self.back_number = back_number

    # __str__ : Java의 toString 메소드 느낌
    def __str__(self):
        return "Hello, My name is %s. I play in %s and my number is %d " % \
            (self.name, self.position, self.back_number)

    # __add__ : 객체의 합을 overriding
    def __add__(self, other):
        return str(self.back_number) + ", " + str(other.back_number)

    # class 내부 멤버 함수 정의하기
    def change_back_number(self, new_number):
        print(self.name + " 선수의 등번호를 " + str(self.back_number) + "에서 " + str(new_number) + "로 변경합니다.")
        self.back_number = new_number

# class 사용 예제
jihun = SoccerPlayer("easyhun", "LW", 17)
jihun.change_back_number(7)
print(jihun)

goat = SoccerPlayer("messi", "FW", 10)
print(jihun + goat)

# class 실습 : Note
class Note(object):
    def __init__(self, writer : str, content :str = None):
        self.writer = writer
        self.content = content

    def write_content(self, content):
        self.content = content

    def remove_all(self):
        self.content = None

    def __add__(self, other):
        return self.content + other.content

    def __str__(self):
        return '\n<' + self.writer + "'s Note>\n" + self.content

myNote = Note('Jihun', 'Im back on the microphone 지금만큼은 이 트랙으로 바꿔줘')
print(myNote)

yourNote = Note('Ronaldo', '알 나스르 LEGEND\n한 반 두 !')
print(yourNote)

yourNote2 = Note('콘텐츠없음', '')
print(yourNote2)

# class 실습 : Notebook
class NoteBook(object):
    def __init__(self, title : str = None):
        self.title = title
        self.page_number = 1
        self.notes = {}

    def add_note(self, note, page = 0):
        if self.page_number < 300:
            if page == 0:
                self.notes[self.page_number] = note
            else:
                self.notes = {page : note}
                self.page_number += 1

    def remove_note(self, page_number):
        if page_number in self.notes.keys():
            return self.notes.pop(page_number)
        else:
            print('There are no page number exist.')

    def get_number_of_pages(self):
        return len(self.notes.keys())

    def __str__(self):
        string =  "[" +self.title + " NoteBook]\n"
        for i in range(1, len(self.notes.keys()) + 1):
            string += str(self.notes[i])
        return string

myNoteBook = NoteBook('내 노트북')
myNoteBook.add_note(myNote)
myNoteBook.add_note(yourNote)
myNoteBook.add_note(yourNote2)
print(myNoteBook)

# 상속 class 예제, 부모 클래스
class Person:
    def __init__(self, name : str, age : int):
        self.name = name
        self.age = age

    def __str__(self):
        return "저의 이름은 {0} 입니다. 나이는 {1} 입니다.".format(self.name,self.age) 

# 자식 클래스, super() 는 Java 생각하면 될 듯
class Student(Person):
    def __init__(self, name, age, ID : str, major : str):
        super().__init__(name, age)
        self.ID = ID
        self.major = major

    def __str__(self):
        return super().__str__() + "\n 학번은 {0} 이고 전공은 {1} 입니다.".format(self.ID,self.major)

sJihun = Student("이지훈", "24", "201812767", "컴퓨터공학부")
print(sJihun)

# * 다형성 설명 (같은 이름의 다른 기능 메소드...)

# * 캡슐화 : 멤버 변수/함수 x의 private -> __x 등 접근 제어

# * decorate
# - 일등함수 또는 일급객체, 변수나 데이터 구조에 할당 가능, 파라메터 or 리턴
# - C++이나 Java에서는 상상도 못한 일이 가능하다...

def square(x):
    return x*x

f = square
print(str(f(10.5)))
print(str(2**(7**2)))