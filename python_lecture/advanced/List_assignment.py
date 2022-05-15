#22.05.13(금) 파이썬 심화 List 과제 정재완
#2. 빈 리스트 생성
List = []

#3. 첫 번째 반복문
for x in range(1, 16, 1):
    List.append(x)
    if(x==14):
        print(List)

#4. 두 번째 반복문 : 반복문과 조건문을 통해 2의 배수 리스트에서 제거
'''
for x in range(List[0], len(List)+1, 1):
    if(x % 2 == 0):
        List.remove(x)
'''
for x in List:
    if(x%2 == 0):
        List.remove(x)
        
#5. 리스트를 print()문 사용해 출력
print(List)

#6. 세 번째 반복문 사용
for x in List:
    if(x%3 == 0):
        List.remove(x)
        
#7. 리스트를 출력
print(List)

#8. 소수 리스트로 만들기
List.pop(0)
print(List)

List.insert(0, 2)
List.insert(1, 3)
print(List)