def solution(age):
      u = "%d" %age		#Receives an int type as a string.
      p = {'0':'a', '1':'b', '2':'c', '3':'d', '4':'e', '5':'f', '6':'g', '7':'h', '8':'i', '9':'j'}
      if(age > 1000):		#check range
           return print("Please input a number less than 1000")	#warming message
      elif(len(u)==4):		#for 4-digit age
           answer = '%s' % p[u[0]] + p[u[1]] + p[u[2]] + p[u[3]]
      elif(len(u) == 3):	#for 3-digit age
           answer = '%s' % p[u[0]] + p[u[1]] + p[u[2]]
      elif(len(u) == 2):	#for 2-digit age
           answer = '%s' % p[u[0]] + p[u[1]]
      else:					#for 1-digit age
           answer = '%s' % p[u[0]]
      return answer
