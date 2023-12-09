def solution(numbers):
	 if not (1 <= len(numbers) <= 100000):	#length check
		  return print("The length is too short or too long. Please enter between 1 and 100,000.")
	 for num in numbers:	#length of element check
		  if not (0 <= num <= 1000):
			   return "There are too many elements. Please enter 1000 or less."
	 numbers.sort(reverse = True)	#reroder the list
	 a = list(map(str, numbers))	#convert to string
	 for i in range(0, len(a)):		#paste results
		  if(i==0):
			   answer = "%s" %a[0]
		  else:
			   answer = answer +"%s" % a[i]
	 return answer
