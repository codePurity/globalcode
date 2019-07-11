def age():
	new_year = 2019
	old = int(input("Tell me the year you were born and i will tell your age"))
	if old < new_year:
		age=new_year- old
		print(age)
	return age
age()

