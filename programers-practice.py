# # 이렇게 코딩하면 파이썬 스타일이 아니다! 명심!
# def solution(mylist):
#     answer = []
#     for i in range(len(mylist)):
#         answer.append(len(mylist[i]))


# # 몫과 나머지를 이쁘게 만들 수 있다
# a = 7
# b = 5
# print(*divmod(a, b))


# # 진법 변환, num은 str이어야 한다
# num, base = map(int, input().strip().split(' '))
# print(int(str(num), base))


# # ljust() : 문자열 왼쪽 정렬
# # center() : 가운데 정렬
# # rjust() : 오른쪽 정렬
# s, n = input().strip().split(' ')
# n = int(n)
# print(s.ljust(n))
# print(s.center(n))
# print(s.rjust(n))

# # 0 입력시 소문자 알파벳, 1 입력시 대문자 알파벳 표시
# # https://docs.python.org/3.4/library/string.html
# # 더 많은 상수 찾기
# # 파이썬에서는 상수를 정의하여 쓴다.
# import string
# num = int(input().strip())
# if num == 0:
#     print(string.ascii_lowercase)
# elif num == 1:
#     print(string.ascii_uppercase)

# # 원본을 유지한채, 정렬된 리스트 구하기 - sorted() 
# list1 = [3, 2, 1]
# list2 = sorted(list1)
# print(list2)


# # 2차원 리스트 뒤집기
# def solution(mylist):
#     new_list = list(map(list, zip(*mylist)))
#     return new_list

#  mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#  print(solution(mylist))
# for i in range(len(mylist)):
#    for j in range(len(mylist[i])):
#       print(mylist[j][i])

# mylist = [1, 2, 3]
# new_list = [40, 50, 60]
# for i in zip(mylist, new_list):
#     print (i)

# animals = ['cat', 'dog', 'lion']
# sounds = ['meow', 'woof', 'roar']
# answer = dict(zip(animals, sounds))
# print(answer)

