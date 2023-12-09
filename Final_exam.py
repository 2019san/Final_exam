#<오픈소스프로그래밍 기말 프로젝트>
#
# ● 아래의 코드를 수정 혹은 프로그래밍하여 문제를 해결하시오.
# ● 문제의 점수는 각각 표시되며, 부분점수가 존재합니다.
#
# 학번 : 20201834 이름 : 류재훈

import os
import time

# Q.1 10점
#
# 문자열 my_string과 target이 매개변수로 주어질 때,
# target이 문자열 my_string의 부분 문자열이라면 1을,
# 아니라면 0을 return 하는 solution 함수를 작성하시오.
#
# 제한사항
# 1 ≤ my_string 의 길이 ≤ 100
# my_string 은 영소문자로만 이루어져 있습니다.
# 1 ≤ target 의 길이 ≤ 100
# target 은 영소문자로만 이루어져 있습니다.

def solution(my_string, target):
     if my_string.islower() and target.islower():	#lowercase check
          if 1<=len(my_string) <= 100 and 1<= len(target) <=100:	#length check
                  if target in my_string:	#substring 1 or not 0
                          answer = 1
                  else:
                          answer = 0
                  return answer
          else:
                  return print("Please write in 100 words or less")	#out of range, a warning message
     return print("Please write in lowercase")	#not lowercase print warning message

# Q.2 10점
#
# 모스부호 해독 프로그램 만들기
# 문자열 letter 가 매개변수로 주어질 때,
# letter 영어 소문자로 바꾼 문자열을 return 하는
# solution 함수를 완성하시오.
#
# 제한사항
# 1 ≤ letter 의 길이 ≤ 1,000
# letter 의 모스부호는 공백으로 나누어져 있습니다.
# letter 에 공백은 연속으로 두 개 이상 존재하지 않습니다.
#
# letter = "- .... .. -. -.- .... .- .-. -.."

def solution(letter):
      morse = {'.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f', '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l', '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r', '...':'s','-':'t','..-':'u','...-':'v', '.--':'w','-..-':'x', '-.--':'y','--..':'z'}
      if not (1 <= len(letter) <= 1000):		#length check
            return print("Please input 1000 characters or less.")
      elif "  " in letter:		#check 2 or more spaces
            return print("Delete two or more spaces in a row")
      a = letter.split()		#string splitting
      for i in range(0, len(a)):		#translation result output
           if(i==0):
                answer = "%s" % morse[a[0]]
           else:
                answer = answer + "%s" % morse[a[i]]
      return answer

# Q.3 10점
#
# 행성의 나이를 알파벳으로 표현할 때,
# a는 0, b는 1, ..., j는 9
# 예를 들어 cd는 23살, fb는 51살입니다.
# age가 매개변수로 주어질 때
# PROGEAMMER-857식 나이를 return 하도록
# solution 함수를 완성하시오.
#
# 제한사항
# age는 자연수입니다.
# age ≤ 1,000
# PROGRAMMERS-857 행성은 알파벳 소문자만 사용합니다.

def solution(age):
      u = "%d" %age	#Receives an int type as a string.
      p = {'0':'a', '1':'b', '2':'c', '3':'d', '4':'e', '5':'f', '6':'g', '7':'h', '8':'i', '9':'j'}	#Use dictionary
      if(age > 1000):	#check range
           return print("Please input a number less than 1000")
      elif(len(u)==4):	#for 4-digit age
           answer = '%s' % p[u[0]] + p[u[1]] + p[u[2]] + p[u[3]]
      elif(len(u) == 3):	#for 3-digit age
           answer = '%s' % p[u[0]] + p[u[1]] + p[u[2]]
      elif(len(u) == 2):	#for 2-digit age
           answer = '%s' % p[u[0]] + p[u[1]]
      else:			#for 1-digit age
           answer = '%s' % p[u[0]]
      return answer

# Q.4 10점
#
# x축과 y축으로 이루어진 2차원 직교 좌표계에 중심이 원점인
# 서로 다른 크기의 원이 두 개 주어집니다.
# 반지름을 나타내는 두 정수 r1, r2가 매개변수로 주어질 때,
# 두 원 사이의 공간에 x좌표와 y좌표가 모두 정수인 점의 개수를
# return하도록 solution 함수를 완성해주세요.
# ※ 각 원 위의 점도 포함하여 셉니다.
#
# 제한사항
# 1 ≤ r1 < r2 ≤ 1,000,000

def solution(r1, r2):
      #variable declaration
      answer = 0 
      dot1 = 0
      dot2 = 0
      dot3 = 0
      dot４ = 0
      c = 0
      d = 0
      if(r1>=r2):    #r1>r2
          return print("input a value smaller than r2 in r1")
      elif(r1 < 1 or r1 > 1000000 or r2 < 1 or r2 > 1000000):    #check range
          return print("Please input a value between 1 and 1000000")
      else:
          for x in range(1, r1 + 1): 	#dot inside r1 circle in first quadrant
              y = int((r1**2 - x**2) **0.5)
              dot1 = dot1 + y
          for x in range(1, r2 + 1): 	#dot inside r2 circle in first quadrant
              y = int((r2**2 - x**2) **0.5)
              dot2 = dot2 + y
          for x in range(-r1, r1 + 1):	#dot on r1 circle
                    for y in range(-r1, r1 + 1):
                              if x**2 + y**2 == r1**2:
                                        c=c+1
          dot3 = c
          for x in range(-r2, r2 + 1):	#dot on r2 circle
                    for y in range(-r2, r2 + 1):
                              if x**2 + y**2 == r2**2:
                                        d=d+1
          dot4 = d   
          answer = (dot2 - dot1)*4 + dot3 + dot4
          return answer


# Q.5 10점
#
# 0 또는 양의 정수가 주어졌을 때,
# 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.
#
# 예를 들어, 주어진 정수가 [6, 10, 2]라면
# [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
# 이중 가장 큰 수는 6210입니다.
#
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어
# return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
#
# numbers = [8, 30, 17, 2, 23]

def solution(numbers):
      if not (1 <= len(numbers) <= 100000):	#length check
            return print("The length is too short or too long. Please enter between 1 and 100,000.")
      for num in numbers:		#length of element check
            if not (0 <= num <= 1000):
                  return "There are too many elements. Please enter 1000 or less."
      numbers.sort(reverse = True)	#reorder the list
      a = list(map(str, numbers))	#convert to string
      for i in range(0, len(a)):		#paste results
           if(i==0):
                answer = "%s" %a[0]
           else:
                answer = answer +"%s" % a[i]
      return answer