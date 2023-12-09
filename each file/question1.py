def solution(my_string, target):
     if my_string.islower() and target.islower():	#lowercase check
          if 1<=len(my_string) <= 100 and 1<= len(target) <=100:	#length check
                  if target in my_string:			#substring 1 or not 0
                          answer = 1						
                  else:
                          answer = 0
                  return answer
          else:
                  return print("Please write in 100 words or less")	 #out of range, a warning message
     return print("Please write in lowercase")	#not lowercase print warning message
