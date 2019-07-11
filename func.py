def evens():
    even_nums = []
    num2=int(input("enter first big number"))
    num1=int(input("enter a less number"))
    i = num1
    while(i<num2):
            if i%2 == 0:
                even_nums.append(i)
            i+=1
    return even_nums
def evens():
    even_nums = []
    num2=int(input("enter first big number"))
    num1=int(input("enter a less number"))
    i = num1
    while(i<num2):
            if i%2 == 0:
                even_nums.append(i)
            i+=1
    return even_num

def evens():
    even_nums = []
    num2=int(input("enter first big number"))
    num1=int(input("enter a less number"))
    i = num1
    while(i<num2):
            if i%2 == 0:
                even_nums.append(i)
            i+=1
    return even_nums
def reverse_evens():
    even_nums=evens()
    even_nums.reverse()
    return even_nums

print(evens())
print(reverse_evens())


