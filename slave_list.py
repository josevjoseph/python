list1=eval(input("Enter the list of numbers: "))
num=int(input("Enter the number: "))
new_list=[]
for i in list1:
    if(i<num):
        new_list.append(i)
print("The new list is: ",new_list)
