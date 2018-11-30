#Getting input
boxWidth = int(input("Width? "))
boxCount = int(input("Number? "))
#Printing first line
print()
for ctr in range(boxCount-1):
    print('+' + ('-' * boxWidth) + '+ ', end="")
#Separate print for last box to avoid ending space
print('+' + ('-' * boxWidth) + '+')
#Printing second line
for ctr in range(boxCount - 1):
	print('|' + (' ' * boxWidth) + '| ', end="")
#Separate print for last box to avoid ending space
print('|' + (' ' * boxWidth) + '|')
#Printing last line
for ctr in range(boxCount-1):
    print('+' + ('-' * boxWidth) + '+ ', end="")
#Separate print for last box to avoid ending space
print('+' + ('-' * boxWidth) + '+')
