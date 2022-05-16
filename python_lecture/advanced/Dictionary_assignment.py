#22.05.13(금) 파이썬 심화 Dictionary 과제 정재완
#2. 빈 딕셔너리 생성
Dic = {}

#3. 반복문 이용해 정수 key값과 문자열 value값 입력받아 딕셔너리에 저장
while True:  
    key = int(input("Key 값 입력 : "))
    value = input("value 값 입력 : ")
#4. 반복문 안 조건문을 통해 반복문 실행 종료 및 입력한 딕셔너리 출력    
    if(key == 0) or (value == "종료"):
        print("그만")
        print(Dic)
        break
    else:
        Dic[key] = value


#5. dict_keys 객체와 dict_values 객체, dict_items 객체 리스트 변환, 출력
dict_keys = list(Dic.keys())
dict_values = list(Dic.values())
dict_items = list(Dic.items())
print(dict_keys)
print(dict_values)
print(dict_items)