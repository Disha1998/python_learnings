# name = input("Enter name : ")
# age = input("Enter your Age : ")

# print("Name is : ", name, "and Age is : ", age)


# Arithmetic operators 

# num1 = 3
# num2 = 4.5
# num3 = -55
# num4 = 43

# sum_num1_num2 = num1 + num2
# print("sum of number 1 and number 2 is  : ", sum_num1_num2)

# sum = num3+num4
# print("sum is :", sum)


# number = input( "Enter the number : ")

# print(int(number) + 1)

# num2 = input()
# print (int(num2) + 5)

# string methods

# hello = True

# print(type(hello))

# name = "HeLlO how are you Llll"

# print(name.count('L'))


# a = 'hello'
# b = "hi "

# print(a + b)



# if - else

# x = 5
# y = 10

# if x < y :
#     print(True, '-- in if statement')
# else :
#     print(False, '-- in else statment')

# name = input('Enter the name : ')

# if name == "Disha" :
#     print('uhh you are correct...!!!')

# else :
#     print("Wrong wrong wrong...!!!!!")




# name = input('Enter the name : ')

# if name == "Disha" :
#     print('uhh you are correct...!!!')
# elif name == "DD" :
#     print('inside of else if')
# else :
#     print("Wrong wrong wrong...!!!!!")



    # List is same like array in js


# a = [True, "Disha", 7]
# b = "Disha"
# print(a[1])

# print(len(a))
# print(len(b))

# a.extend(["dsd", "dsds", "5343"])

# print(a)


# x = [1, 2, 4]

# x[0] = "tete"

# print('x  :', x)


# tuples - immutable

# a = (9, 4, "didd", 5)
# print(a)


# for loop in python - START, STOP, STEP
# while  - we don't know till when the condition will going to false (Repeats a block of code as long as a condition is true. )

# for i in range(5):
#     print('i',i)


# for i in range(10, -1 , -1): #- start, stop, step
#     print(i)



# for i in [1,2,34,4]:
#     print(i)


#  --- while


# i = 0

# while True:
#     print(i + 1, '-----')
#     i += 1

#     if i == 4:
#         break

# slice in python

# index -    0 1 2 3 4 5
# x = [2,3,4,5,6,7]

# result = x[0:5:3]
# print(result)

# sets in python

# x = set()

# s1 = {32,'ff','gt4tr',23423,65}
# s2 = {32, 'fdd', 5454, 'sjssj'}

# print(32 in s1)
# print('fdd' in s2)


# Disctinory 

# user = {
#     'name' : "Disha",
#     'phon' : 32323232,
#     'address' : "Bandelgath",
#     'email' : 'dbca@gmail.com'
# }

# user['a'] = 5

# print(user['name'])
# print(user['phon'])

# del user['a']
# print(user)



# functions --- 

# def abc(a,b):
#     print('basic function defination', a + b)
#     return a, b

# print(abc(3,5))


# *args and **kwargs -- unpack the data like dictionary, list, set, tupple
# assum that you don't know how many key values or position then we use this - for dictonry - **
#  -- *args - use for tupple,list
#  -- **kwargs (keyword arguments) - use for disctionary
# x = [32, 434, "Disha", 55, "ririri"]

# print(x)
# print(*x)



# raise means the throw in js
# try and except in python & finally

# try:
#     x = 6 / 0
#     print(x)
# except Exception as e:
#     print(e)  

# finally:
#     print('even though there is err finally block will run')


# lambda - one line an anoynamus function [not recomend to use]
# x = lambda x : x * 6
# print(x(2))

# map

# x = [2,3,4,5,6,7,43,2,3,5,6,7,4,3,4,5,67,7,4,3,7]

# def test(n):
#     return(n * 2)

# print(list(map(test, x)))


