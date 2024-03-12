list1=eval(input("Enter the list of numbers: "))
list2=list(set(list1))
list2.sort(reverse=True)
print("The third largest number is ",list2[2])
