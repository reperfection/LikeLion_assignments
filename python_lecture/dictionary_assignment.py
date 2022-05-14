#딕셔너리 생성_정재완
Wanny = {'이름' : '정재완', '나이' : 27, '생일' : '1996년 2월 25일', 
         '성별' : '남자', '전화번호' : '010-2707-6813'}
Faker = {'이름' : '이상혁', '나이': 27, '생일' : '1996년 5월 7일',
         '성별' : '남자', '전화번호' : '010-0213-0507'}
Sua = {'이름' : '김보라', '나이' : 29, '생일' : '1994년 8월 10일',
       '성별' : '여자', '전화번호' : '010-2017-0113'}

#리스트 생성
list_name = [1, 2, 3]
list_age = [1, 2, 3]
list_birth = [1, 2, 3]
list_sex = [1, 2, 3]
list_phoneNum = [1, 2, 3]

#키값을 통해 밸류를 얻어 리스트 요소로 저장
#이름
list_name[0] = Wanny['이름']
list_name[1] = Faker['이름']
list_name[2] = Sua['이름']
#나이
list_age[0] = Wanny['나이']
list_age[1] = Faker['나이']
list_age[2] = Sua['나이']
#생일
list_birth[0] = Wanny['생일']
list_birth[1] = Faker['생일']
list_birth[2] = Sua['생일']
#성별
list_sex[0] = Wanny['성별']
list_sex[1] = Faker['성별']
list_sex[2] = Sua['성별']
#전화번호
list_phoneNum[0] = Wanny['전화번호']
list_phoneNum[1] = Faker['전화번호']
list_phoneNum[2] = Sua['전화번호']


#이름, 나이, 생일, 성별, 전화번호에 해당하는 리스트 출력
print("이름 리스트는 ",list_name)
print("나이 리스트는 ", list_age)
print("생일 리스트는 ", list_birth)
print("성별 리스트는 ", list_sex)
print("전화번호 리스트는 ", list_phoneNum)