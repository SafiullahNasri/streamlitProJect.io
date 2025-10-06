# import time
# print('Hello world this is python with chaiwal...')
# name = "pro"
# print(name)



# for i in range(1,6):
#     for j in range(1, i+1):
#         print(j , end=" ")
#     print()



# n = 1

# while n<10:
#     if n==3:
#         print("add these tow favs")
#     else:
#         print(n)
#     n +=1




# for i in range(1,100):
#         if i==10:
#             continue
#         else:
#               print(i)
    # print(n)
# else:
#     print(n)




# sum = 0
# for i in range(1,100):
#     if i%2==0:
#         sum+=1
# print("the sum is: ", sum)



# for i in range(1,21):
#     print(i, i**2)


# sum = 0
# i = 0
# while i<=20:
#     if i%2==1:
#         sum+=i

#     i+=1    
# print(sum)




# def square(number):
#     print(number**2)
# square(4)



# def sum(a,b):
#     return a+b
# print(sum(1,2))




# import math
# def circle(radius):
#     print("Hi")
#     area = math.pi * radius **2
#     cr = 2*math.pi*radius
#     return area, cr
# # print(circle(2))
# a,c = circle(3)
# print(a,c)






# def greet(name):
#     return "Hello " + name + "! "
# print(greet("pro"))




# def greet(name = "user"):
#     return "Hello " + name + "! "
# print(greet())


# cub = lambda x: x**3
# print(cub(3))



# cub = lambda x: x**2
# print(cub(2))



# def sum(*args):
#     return sum(args)
# print(sum(1,2))
# print(sum(1,2,3,4,5))
# print(sum(1,2,3,5,6,7,8))



# print("Hello python i am your big fan sir for doing thsi course honsetly let's do it togetjer")
# print("hello python")




# for i in range(5):
#     price = int(input("Enter the price of the laptop here? "))



# number = 5
# factorial = 1

# while number>0:
#     factorial = factorial*number
#     number = number-1
# print(factorial)


# number = int(input("Enter the number here"))
# facotrial = 1
# if number ==0:
#     print("0")
# else:

#     for i in range(1, number+1):
#         facotrial = number*i

#     print("The factorial of number is", number, facotrial)




from time import process_time

list_python = [i for i in range(10000)]

start_time = process_time

list_python = [i+5 for i in list_python]

end_time = process_time
print(end_time - start_time)