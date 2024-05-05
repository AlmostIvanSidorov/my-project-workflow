#!/usr/bin/python3


def main():
   your_name = input("Please enter your name:")
   return f"Hello {your_name}, glad to see you!"

def extend_list(value, lst=None):
   if lst is None:
      lst = []
   lst.append(value)
   return lst

def convert(n: int) -> str:
   return ''.join(map(str,range(n+1)))

def task_1():
   a = ([],1)
   a[0].append(1)

   return a

def task_2():
   a = []
   for i in range(5):
      a.append(i)

   a = {i+1:i**2 for i in range(5) if i%2 == 0}

   return a 

def task_3():
   a = [1,2,3]
   b = a
   return a is b 

import copy

def task_4():
   a = [1,[3]]

   b,c = copy.copy(a),copy.deepcopy(a)

   # b.append(3)

   # b[1].append(4)

   c.append(3)

   c[1].append(4)

   return a

def task_5():
   a = [i for i in range(5)]

   # map

   m = map(lambda x: x**2, a)

   m1 = list(m)

   m = map(lambda x: x**2, a)
   

   # filter

   f = filter(lambda x: x%2 == 0, m)


   # zip

   z = zip(list(m1),list(f))

   return list(z)



if __name__ == '__main__':
   print(task_5())





