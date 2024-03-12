list1=eval(input("Enter the first list of numbers: "))
list2=eval(input("Enter the second list of numbers: "))
list3=[]
for i in list1:
    if(i in list2):
        list3.append(i)
print("The list of common elements are: ",list3)
