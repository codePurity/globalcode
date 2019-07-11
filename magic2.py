def age():
	old = int(input("Tell me the year you were born and i will tell if you were born on a leap year"))
	if old%4 == 0:
        	print("Hurray!!, you were born on a leap year")
	else:
		print("Sorry,you were not born on a leap year")
age()


