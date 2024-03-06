
print(1)

for n in range (2,10):
    for x in range (2,n):
        if n % x ==0:
            print(n,"equals",x,"+",n//x)

            break
        else:
            #loop fell through without finding a factor
            print (n,'is a prime number')
for num in range(2,10):
    if num % 2 ==0:
        print("found an even",num)
        continue
    print("found a number",num)

#argument
def greet(name='world'):
    print(f"hello,{name}!")
    greet()
    greet ("alice")


    class MyClass:
        
        def __init__(self, name='World'):
         self.name = name

        def greet(self):
         print(f"Hello, {self.name}!")



print(greet)

def fib(n): #write fibonacci series up to n
    "print a Fibonacci series up to n"
    while a < n:
        print(a,end='')
        a,b=b,a+b
        print(fib)



    def ask_ok(prompt,retries=4,remimder='pleasetry again'):
        while True:
           ok=input(prompt)
           if ok in ('y','ye','yes'):
               return True
           if ok in ('n','no','nop','nope'):
               return False
           retries=retries-1
           if retries<0:
               raise ValueError('invalid user response')
               print(reminder)
def my_list():
        
 my_list=[1,2,3]
 my_list.append(4)
print(my_list) # output[1,2,3,4]


my_list=[1,2,3]
my-list.extend([4,5.6])
print(my_list) #output:[1,4,2,3]

my_list[1,2,3]
my_list.insert(1,4)
print(my_list)  # output:[1,4,2.3]

my_list=[1,2,3]
removed_item=my_list.pop(1)

print(my_list) #output:[1,3]
print(removed_item) #output:2

my_list=[1,2,3]
my_list.clear()
print(my_list) #output:[]

my_list=[1,2,3,2]
index=my_list.index(2)
print(index) #output:1

my_list=[1,2,3,2,2]
count=my_list.count(2)
print(count) #output:3

my_list=[3,1,2]
my_list.sort()
print(my_list) #output:[1,2,3]\

my_list=[1,2,3]
my_list.reverse()
print(my_list) #output :[3,2,1]

my_list=[1,2,3]
copied_list=my_list.copy
print(copied_list) #output :[1,2,3]



#list as stacks
stack=[3,4,5]
stack.append(6)
stack.apppend(7)

print(stack)

stack.pop()
stack.pop()


#Queues

from collections import deque
queue =deque(['eric','john','michael'])
queue.append("terry")
queue.append("Graham")
queue.popleft()


#list comprehensions

squares=[]
for x in range (10):
   squares.append(x**2)
   print()

   squares=[x**2 for x in range(10)]

   print()


   combs=[]
   for x in (1,2,3) :
      for y in (3,1,4):
         if x !=y:
            combs.append((x,y))

            print()


            #sets
            def basket (fruits):
               
             baskets={"apple",'orange',"apple",'pear','orange','banana'}

            for fruit in fruits :
               print ()
               if fruit== 'orange':
                  
                  print('found my orange')
               else:
                  print('this is not a orange')



                  basket= {'apple','orange','apple','pear','orange','banana'}
                  print(basket)
               


        #dictionaries
                  
def contacts ():
   contacts={
      "john":"john@gmail.com",
      "alice":"alice@gmail.com",
      "bob":"bob@gmail.com"

   }

   #acccessing values
   print(contacts["john"])

   #add a new contact
   contacts['eve'] ="eve@gmail.com"

   #modifying the existing contact
   contacts['bobs']="bob_new@gmail.com"

   #removing contact
   del contacts ['alice']

#printing all contacts

for name,email in contacts.items():
   print(f,"{name} : {email}")



def sentence (word_frequency):
 sentence=('this is a simple sentence with words.this is just an eXAMPLE')
word_frequency={}
word=sentence.split()
for word in word :
   word=word.lower()
   if word in word_frequency:
    word_frequency[word] +=1

   else:
      word_frequency[word]=1

      print(word_frequency)

    


#method attribute.
      
class myclass:
   def _init_(self,value):
      self.value=value

      def my_method(self):
         return f"value is {self.name}"
      
      obj=myclass(10)
      #accesing method attribute

      print(obj.my_method)

      #dynamic method.

      class myclass:
         def __init__(self) -> None:
            pass
         
      obj= myclass()

      obj.new.attribute=42
      print(obj.new.attribute)

         

class complex:
   def _init_(self,real,imag):
      self.real=real
      self.imag=imag

      def add(self,other):
         return complex(self.real+other.real,self.imag+other.real)
      
      def subtract(self,other):
         return complex(self.real-other.real,self.imag-other.real)
      def multiply(self,other):  
         real_part=(self.real*other.real+self.imag*other.real)
        
      


