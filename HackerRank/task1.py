# 1. ------ If n is odd, print Weird

# n = int(input("enter number:"))

# if n % 2 != 0:
#     print("weired")
# else:
#     print("not weired")


# 2.-------- If n is even and in the inclusive range of 2 to 5, print Not Weird
 

# if n % 2 == 0 and (n >= 2 or n <= 5):
#     print('not weired')
# else:
#     print('nopt match')


# 3. ------ If n is even and in the inclusive range of 6 to 20, print Weird
 

# if n % 2 != 0 and (n >= 6 or n <= 20):
#     print('weired!')

# 4.----- If n is even and greater than 20, print Not Weird

 

# if n % 2 == 0 and n >= 20:
#     print('not weired!!')



# final code which i submited in hackerrank
# if n % 2 != 0:
#     print("Weird")   
# elif n % 2 == 0:
#     if 2 <= n <= 5:
#         print("Not Weird")   
#     elif 6 <= n <= 20:
#         print("Weird")   
#     elif n > 20:
#         print("Not Weird") 


# edabit - python challenges

price_input = int(input())
discount_input = int(input())

print("price_input : ", price_input)
print("discount_input : ", discount_input)


def dis(price_input, discount_input):
    a = price_input * discount_input / 100
    return price_input - a

print(dis(price_input,discount_input))
	
