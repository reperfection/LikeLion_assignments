#22.05.10(화)list과제_정재완

#2. 모든 알파벳과 공백''이 요소로 들어있는 리스트

alphabet = ['a', ' ', 'b', ' ', 'c', ' ', 'd', ' ', 'e', ' ', 'f', 
            ' ', 'g', ' ', 'h', ' ', 'i', ' ', 'j', ' ', 'k', 
            ' ', 'l', ' ', 'm', ' ', 'n', ' ', 'o', ' ', 'p', 
            ' ', 'q', ' ', 'r', ' ', 's', ' ', 't', ' ', 'u', 
            ' ', 'v', ' ', 'w', ' ', 'x', ' ', 'y', ' ', 'z']

#3. 0부터 9까지 숫자와 문자'-'가 들어있는 리스트
number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '-']

#4. alphabet 리스트에서 인덱싱을 이용한 문장 만들기
likelion = alphabet[44], alphabet[8], alphabet[1], alphabet[0], alphabet[34], alphabet[8], alphabet[21], alphabet[36], alphabet[20], alphabet[14], alphabet[40], alphabet[41], alphabet[22], alphabet[16], alphabet[20], alphabet[8], alphabet[22], alphabet[16], alphabet[28], alphabet[26]
likelion = ''.join(likelion)
print(likelion)

hack_your_life = alphabet[14], alphabet[0], alphabet[4], alphabet[20], alphabet[21], alphabet[48], alphabet[28], alphabet[40], alphabet[34], alphabet[45], alphabet[22], alphabet[16], alphabet[10], alphabet[8]
hack_your_life = ''.join(hack_your_life)
print(hack_your_life)

my_name_is = alphabet[24], alphabet[48], alphabet[49], alphabet[26], alphabet[0], alphabet[24], alphabet[8], alphabet[9], alphabet[16], alphabet[36], alphabet[37], alphabet[18], alphabet[0], alphabet[8], alphabet[44], alphabet[0], alphabet[26]
my_name_is = ''.join(my_name_is)
print(my_name_is)

#5. number 리스트에서 인덱싱을 이용해 생일, 전화번호, 학번 만들고 출력
birth = number[1], number[9], number[9], number[6], number[0], number[2], number[2], number[5]
phoneNum = number[0], number[1], number[0], number[10], number[2], number[7], number[0], number[7], number[10], number[6], number[8], number[1], number[3]
classOf = number[2], number[0], number[1], number[7], number[1], number[1], number[0], number[2], number[2]

#리스트의 요소를 지정된 함수로 처리하는 map함수를 이용
birth = ''.join(map(str, birth))
print("제 생일은", birth,"입니다.")

phoneNum = ''.join(map(str, phoneNum))
print("제 전화번호는", phoneNum, "입니다.")

classOf = ''.join(map(str, classOf))
print("제 학번은", classOf, "입니다.")