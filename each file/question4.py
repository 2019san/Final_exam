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