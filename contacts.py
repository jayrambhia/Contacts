#!/usr/bin/python2.7

# Uses a database
# Trying not to create an additional dict

import sys
import re
import gdbm
import string

def search_contact(f):
  count=0
  str1 = raw_input('Enter the name:\t')
  print ''
  temp_str1=str1.lower()
  name=sorted(f.keys())
  for i in range(len(f)):
    result = None
    search_name = name[i].lower()
    result = re.search('.*'+temp_str1+'.*',search_name)
    if result:
      try:
        print name[i] + '  ' + f[name[i]]
        count+=1
      except KeyError:
        print 'KeyError'
  if count==0:
    print '\n' + str1 + ' not found\n' 
  print ''
  
  return
  
def add_contact(f):

  name = str(raw_input('\nName: '))
  value = str(raw_input('Number: '))
  
  if value.isdigit():
    f[name]=value
    print '\n' + name + ' added to contacts.\n'
  else:
    print 'Please enter only numbers.' + name + ' not added in contacts.'

  return f
  
def show_list(f):
  name = sorted(f.keys())
  for i in range(len(name)):
    print name[i] + ' ' + f[name[i]]
  return
  
def show_alpha_list(f,c):
  new_dic={}
  name = (f.keys())
  print 'First Name:'
  for i in range(len(f)):
    result = None
    if c == name[i][0].lower():
      new_dic[name[i]] = f[name[i]]
  show_list(new_dic)
  print ''
  del new_dic
  new_dic={}
  print 'Last Name:'
  for i in range(len(f)):
    result = None
    search_name = name[i].lower()
    result = re.search('\s' + c +'\S*',search_name)
    if result:
      new_dic[name[i]] = f[name[i]]
  show_list(new_dic)
  print ''
  return
  
def main():
  n=42
  f=gdbm.open('contacts','c')
  
  while n!= 5:
    print '1. Add contact\n2. Search contact\n3. Show All contacts\n4. List according to char\n5. Quit'
    while True:
      try:
        n=int(raw_input('Enter: '))
        break
      except ValueError:
        print 'Please choose a valid option'
    if n==1:
      f = add_contact(f)
    elif n==2:
      search_contact(f)
    elif n==5:
      print 'Quit.\n'
      return
    elif n==3:
      show_list(f)
    elif n==4:
      c=raw_input('Enter the character.')
      show_alpha_list(f,c)
    else:
      print 'Please enter a valid option'
      
  return
if __name__ == '__main__':
  main()

