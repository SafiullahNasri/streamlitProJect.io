# print("HELLO WROLD")
lst = ["kamla", "jamal", 'kaham', "wow", 1,2,3,4]   # list 
print(lst)
print(type(lst))

# list slicing 
print(lst[0])
print(lst[1])
print(lst[2])
print(lst[3])
print(lst[4])
print(lst[-3])
print(lst[2:])
print(lst[2:3])
print(lst[:2])
print(lst[1:])
print(lst[::2])
print(lst[-3:-1])
print(lst[::-1])
print(lst[-1:-4:-1])


# list iterations
for i in lst:
    print(i)

for i in range(len(lst)):
    print(lst[i])



i  = 0
while i<(len(lst)):
    print(lst[i])
    i+=1

# short hand for loop
[print (i) for i in lst]



# lsit functions in the python

# funcito number on of the function
print(len(lst))
# function number two in teh pyton of the fucntion
print(lst.count("wow"))
# function number three in the python fo r the fucntion
lst.append("ramzia")
print(lst)
# function nmber four in the python fo r the fucntion
lst.insert(1,"Vision")
print(lst)
# remvoe the function in the python let's go fo rhtis 
lst.remove("wow")
print(lst)
# nwo rmvoe the location fromthe particular location of the values

lst.pop(2)
print(lst)


# lsit fucntion two part

# crete the copy of a list 
b = lst.copy()
print(b)

# print(lst.index("kamal"))
c = ["aram", "safiullah"]
lst.extend(c)
print(lst)

# reverese the values
lst.reverse()
print(lst)

# sort the lsit now
# lst.sort()
# print(lst)
# clear the list now
lst.clear()
print(lst)

# list comprehension

L1 = [20,30,40,50]
l2 = []
for i in L1:
    print(i)





lst1 = [1,2,3,4,5]
lst2  = []
for i in lst1:
    print(i)





lst1 = [1,2,3,4,5]
lst2  = []
for i in lst1:
    # print(i)
    lst2.append(lst1)
print(lst2)







pro = ['Ross', 'Rachel', 'Monica', 'Joe']
pro[0], pro[3] = pro[3], pro[0]
print(pro)

# this one swapped the elelment with eache other



# no = [1,2,3,4]
# no[0], no[3] = no[3],no[0]
# print(no)

pro1 = ['Ross', 'Rachel', 'Monica', 'Joe']
pro1.insert(2, "Kamal")
# pro1[2] = 'Kamal'
print(pro1)


pro2 = ['Ross', 'Rachel', 'Monica', 'Joe']
pro2.pop(3)
print(pro2)


# multiplication the numbe rin the list
pro3 = [13,16,7,8]
mul = 1
for i in pro3:
    mul*=i
print(mul)



pro4 = [45,23,577,45]
pro4.sort()
print(pro4)
print("The largest value is : ", pro4[-1])



# new topic is tuple in the python amazing topic it is let's get enjoy guys!

tpl = "kamal", "jamal","khan", 1,2,5
print(tpl)
print(type(tpl))

tpl2 = "kamal",
print(type(tpl2))




# conversion tuples in tuples function in the python
