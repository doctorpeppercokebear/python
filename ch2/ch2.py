## 숫자 자료형
print(5)
print(-10)
print(3.14)
print(1000)

# 수식
print( 5+ 3)
print(2 * 8)
print(6 /3)
print(3 * (3 + 1))

# 문자열 자료형
# 작은따옴표 와 큰 따옴표 어떤 걸 사용해도 상관은 없으나 반드시 한 쌍을 맞춰야함
print("풍선")  # 정상 출력
# print("풍선') # 오류
print('나비')
print("파이썬" * 3) # 큰따옴표로 감쌌기 때문에 숫자가 아니라 문자로 인식

# 볼 자료형
# True, False로 출력
print(5 > 10)
print(5 < 10)
#  not 연산자 : 부정하는 연산자 값이 True -> False False -> True 로 출력
print(not True)  # False 로 출력
print(not False) # True 로 출력
# 5는 10보다 크지 않다.
not(5 > 10)

# 변수
print("반려동물을 소개해 주세요")
print("우리 집 반려동물은 개인데, 이름이 연탄이예요")
print("연탄이는 4살이고, 산책을 아주 좋아해요")
print("연탄이는 수컷인가요?")
print("네.")
# 이 문장에서 연탄이 이름을 바꾸려면 연탄을 모두 찾아서 변경해야한다. --> 변수를 사용해서 간단하게 해결
# 변수명 = 값
name = "연탄이"
animal = "개"
age = 4
hobby = "산책"
is_mal = True
# "문자열" + 변수 + "문자열"
print("우리 집 반려동물은" + animal + "인데, 이름이" + name + "예요")
# print(name + "는 " + age + "살이고, " + hobby + "을 아주 좋아해요") # age 변수는 숫자 이기에 자료형으로 변경해줘야함
print(name + "는 " + str(age) + "살이고, " + hobby + "을 아주 좋아해요") # str으로 감싸서 형변환
# 정리

print("반려동물을 소개해 주세요")
print("우리 집 반려동물은" + animal + '인데, 이름이' + name + "예요" )
print(name + "는 " + str(age) + "살이고," + hobby + "을 아주 좋아해요.") 
