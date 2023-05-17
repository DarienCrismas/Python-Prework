#Question 1
#Write a function to print “hello_USERNAME!” USERNAME is the input of the function.
def hello_name():
    username=input("Please input your username: ")
    print("hello_" + username)
hello_name()


print()


#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds():
    for x in range(101):
        if x%2==1:
            print(x)
first_odds()


print()


#Question 3 
#Please write a Python function, max_num_in_list to return the max number of a given list. 
def max_num_in_list(a_list):
    sorted(a_list)
    return a_list[-1]
    
test_list=[3,5,6,2,10]
test_list2=[2,54,-6,5,95,103]
print(max_num_in_list(test_list))
print(max_num_in_list(test_list2))


print()


#Question 4 
#Write a function to return if the given year is a leap year. 
#A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
#The return should be boolean Type (true/false).
def is_leap_year(a_year):
    if a_year%4 != 0:
        return False
    if a_year%100==0:
        if a_year%400==0:
            return True
        else: 
            return False
not_leap_test= 2023
leap_test= 2000

print(is_leap_year(not_leap_test))
print(is_leap_year(leap_test))


print()


#Question 5 
#Write a function to check to see if all numbers in list are consecutive numbers. 
#For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
#The return should be boolean Type.
def is_consecutive(a_list):
    sorted_list=sorted(a_list)
    full_list=list(range(min(a_list), max(a_list)+1))
    return sorted_list == full_list

test_not_consecutive=[6,3,10,2,7,12,59]
test_consecutive=[1,2,3,4,5,6,7]

print(is_consecutive(test_not_consecutive))
print(is_consecutive(test_consecutive))