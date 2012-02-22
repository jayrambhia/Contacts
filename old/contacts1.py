#!/usr/bin/python2.7

# Uses a database
# Trying not to create an additional dict
# using pickle. Completely different code. Adding more memory.

import sys
import re
import gdbm
import string
import pickle

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
        print name[i], pickle.loads(f[name[i]])[0]
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
    if name in f.keys():
      print 'exists'
      contact_list_str = f[name]
      contact_list = pickle.loads(contact_list_str)
      num_list = contact_list[0]
      num_list.append(value)
      contact_list[0] = num_list
      contact_list_str = pickle.dumps(contact_list)
      f[name] = contact_list_str
    else:
      contact_list=[]
      num = []
      num.append(value)
      contact_list = [num,get_email(),get_DOB()]
      f[name] = pickle.dumps(contact_list) 
    print '\n' + name + ' added to contacts.\n'
  else:
    print 'Please enter only numbers.' + name + ' not added in contacts.'

  return f

def get_email():
  print 'Enter email id(Enter to exit)'
  str1 = raw_input()
  return str1
  
def get_DOB():
  print 'Enter Date of Birth(Enter to exit)'
  str1 = raw_input('(Month Date Year):\n')
  return str1

def show_list(f):
  name = sorted(f.keys())
  for i in range(len(name)):
    print name[i], pickle.loads(f[name[i]])[0]
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
  
def get_int(str1=''):
  while True:
    try:
      n=int(raw_input(str1))
      return n
      break
    except ValueError:
      print 'Enter int'
      
def main():
  n=42
  f=gdbm.open('contacts','c')
  
  while n!= 5:
    print '1. Add contact\n2. Search contact\n3. Show All contacts\n4. List according to char\n5. Quit'
    n = get_int('Choose an option')
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

