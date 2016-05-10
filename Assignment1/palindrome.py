inp =  raw_input('Enter!: ')

i = len(inp)-1

inpreverse = "";
while i >= 0:
	inpreverse=inpreverse+inp[i]
	i=i-1

if inp.lower() == inpreverse.lower():
	print "String is palindrome"
else: 
	print "String is not palindrome"