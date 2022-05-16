#22.05.13(금) 파이썬 심화 객체 과제 정재완
#2. 클래스 명 Student, 매개변수 생성
class Student:
    def __init__(self, name, grade, student_number, sex, address, phone_number, year):
        self.name = name
        self.grade = grade
        self.student_number = student_number
        self.sex = sex
        self.address = address
        self.phone_number = phone_number
        self.year = year
        
#3. 메소드 명 introduce      
    def introduce(self):
        print("이름은", name, "이다.")
        print("학년은", grade, "이다.")
        print("학번은", student_number, "이다.")
        print("성별은", sex, "이다.")
        print("주소는", address, "이다.")
        print("전화번호는 ", phone_number, "이다.")
        if(year == 1):
            print("멋사",year,"년차")
            print("우와 아기사자다!")
        else:
            print("멋사",year,"년차")
            print("우와 운영진이다 !")
#4. while True 반복문 사용, Class_name 변수, 나머지 매개변수 입력 받고 인스턴스 생성 후 메소드 사용해 출력
while True:
    Class_name = input("객체 명을 입력하시오. (단, 영문으로): ")
    if Class_name == "종료":
        break
    name = input("이름을 입력하시오. (단, 한글로): ")
    grade = int(input("학년을 입력하시오. (단, 숫자로): "))
    student_number = int(input("학번을 입력하시오. (단, 숫자로): "))
    sex = input("성별을 입력하시오. (모를 때는 모른다 라고 입력.): ")
    if sex == "모른다":
        sex = None
    address = input("주소를 입력하시오. (-시까지만): ")
    phone_number = input("전화번호를 입력하시오. (모를 때는 모른다 라고 입력.): ")
    if phone_number == "모른다":
        phone_number = None
    year = int(input("멋사 몇년차인가요? (단, 숫자로): "))
    Class_name = Student(name, grade, student_number, sex, address, phone_number, year)
    Class_name.introduce()    
    print()   