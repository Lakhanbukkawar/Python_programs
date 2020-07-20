#print odd numbers in list using lambda function
list1=[3,5,6,55,8]
list_odd_numbers=list(filter(lambda varx:varx%2==1,list1))
print("odd numbers in list are:",list_odd_numbers)
