     #
    ##
   ###
  ####
 #####
######



def staircase(n):
	for i in range(1,n+1):
		txt = "#" * i
		print(txt.rjust(n))

staircase(6)