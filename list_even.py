list1=eval(input("Enter the list of numbers: "))
even_list=[]
for i in list1:
    if(i%2==0):
        even_list.append(i)
even_list.sort()
print("The list of even numbers: ",even_list)
