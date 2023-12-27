# num1=3
# num2=2.7
# num3=2+3j
# print(num1, 'is of num',type(num1))
# print(num2, 'is of num',type(num2))
# print(num3, 'is of num',type(num3))


# -------------
# nation=('Viet Nam', 'China','Germany')
# print(nation[0])
# print(nation[2])

# ----------------

 
# product = ('Microsoft', 'Xbox', 499.99)
# print(product[0])   # Microsoft
# print(product[1])   # Xbox

#=-----------
# name = 'Python'
# print(name)  


# student_id = {112, 114, 116, 118, 115}
# print(student_id)
# print(type(student_id))


# numbers={1,3,4,8}
# print(numbers)
# numbers.add(6)
# print('updates',numbers)


# number={'lacoste','lv','gucci'}
# number_one=['apple', 'samsung', 'xiaomi']
# number.update(number_one)
# print(number)


# name={'Spider','Super','Goku'}
# print(name)
# removedValue=name.discard('Spider')
# print(name)


# x = 5
# y = 10
# print('The value of x is {} and y is {}'.format(x,y))

# num= float(input('Enter a number:'))
# print('Enter a number is:', num)
# print('data type of num:', type(num))


# a=4
# b=7
# print('a==b', a==b)
# print('a>b', a>b)


# global_var=20
# def outer_function():
#     outer_var=10
#     def inner_function():
#         inner_var=30
#         print(inner_var)
#     print(outer_var)
#     inner_function()
#     print(global_var)
# outer_function()
        
        
# number=["apple","app","banana","watermelon"]
# newnumber=[x for x in number if "a" in x ]
# print(newnumber)


# i=2
# while i <7:
#     print(i)
#     if i==3:
#         break
#     i+=1


# fruits=["banana", "apple", "watermelon"]
# for x in "banana":
#     print(x)
    
    
# for x in [0,1,2,3]:
#     pass    
    

# for x in range(6):
#   print(x)
# else:
#   print("Finally finished!")
    
    
    
# number=["chery","apple","banana"]
# print(number[1:2])

# def my_function(x):
#   return 5 + x

# print(my_function(3))
# print(my_function(5))
# print(my_function(9))

# def my_local(k):
#     if(k>0):
#         number= k+ my_local(k-1)
#         print(number)
#     else:
#         number=0
#     return number
# print("end")
# my_local(5)
# n = 10



# def get_product(number1, number2):
#     result=number1*number2
#     return result
 
# n1 = 5
# n2 = 6
# print(get_product(n1,n2))   



# def check_vowel(character):

#     if(character == 'a' or character == 'e' or character == 'i' or character == 'o' or character == 'u'):
#         print("ok")
#     else:
#         print("not ok")    
# character = input()
# result = check_vowel(character)
# print(result) 


# def compute_factorial(*number):
     
#      go=1
    
#      for i in range(1, number + 1):
#          go= go*i
#      return go
# result=compute_factorial(2)
# print(result) 



# def outer():
#     message='lmonkey'
#     def inner():
#         nonlocal message
#         message ='nonlocal'
#         print("inner:", message)

#     inner()
#     print("outer:", message)
# outer()

c=1
def add():
    global c
    c=c+2
    print("result:",c) 
add()    
        
       
    
    
    
      
    
 
    

  


        
     
    
    
        
    
    

    


