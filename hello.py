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

if __name__ == '__main__':
   print(convert(11))





