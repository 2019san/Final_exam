def solution(letter):
      morse = {'.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f', '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l', '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r', '...':'s','-':'t','..-':'u','...-':'v', '.--':'w','-..-':'x', '-.--':'y','--..':'z'}
      if not (1 <= len(letter) <= 1000):	##length check
            return print("Please input 1000 characters or less.")
      elif "  " in letter:		#check 2 or more spaces
            return print("Delete two or more spaces in a row")
      a = letter.split()		#string splitting
      for i in range(0, len(a)):	#translation result output
           if(i==0):
                answer = "%s" % morse[a[0]]
           else:
                answer = answer + "%s" % morse[a[i]]
      return answer
