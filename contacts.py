"""
Author : Jay Rambhia
email : jayrambhia777@gmail.com
Git : https://github.com/jayrambhia
gist : https://gist.github.com/jayrambhia
=============================================
Name : contacts
Repo : Contacts
Git : https://github.com/jayrambhia/Contacts
version 0.3
"""
#            Copyright (c) 2012 Jay Rambhia

# Permission is hereby granted, free of charge, to any person obtaining 
# a copy of this software and associated documentation files (the "Software"), 
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the 
# Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included 
# in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY 
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import re
import gdbm
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
      contact_list = [num,get_email(),get_DOB(),get_tags()]
      f[name] = pickle.dumps(contact_list) 
    print '\n' + name + ' added to contacts.\n'
  else:
    print 'Please enter only numbers.' + name + ' not added in contacts.'

  return f
  
def get_tags():
  tags = str(raw_input('Enter tags(separated by comma): '))
  if tags:
    tags = tags.split(',')
    for i in range(len(tags)):
      if tags[i].startswith(' '):
        tags[i] = tags[i][1:]
  
  return tags
  
def show_all_tags(f):
  name = f.keys()
  tags=[]
  for i in range(len(name)):
    contact_data_string = f[name[i]]
    contact_data = pickle.loads(contact_data_string)
    for j in range(len(contact_data[3])):
      tags.append(contact_data[3][j])
  tags = list(set(tags))
  for i in range(len(tags)):
    print tags[i]
  return

def search_with_tag(f):
  tag = raw_input('Enter Tag: ')
  name = sorted(f.keys())
  for i in range(len(name)):
    contact_data_string = f[name[i]]
    contact_data = pickle.loads(contact_data_string)
    for j in range(len(contact_data[3])):
      if tag in contact_data[3][j]:
        print name[i], contact_data[0]
        break
  return
    
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
  f=gdbm.open('contacts_new_1','c')
  
  while n!= 7:
    print '1. Add contact\n2. Search contact\n3. Show All contacts\n4. List according to char\n5. Search according to tag\n6. Show All Tags\n7. Quit'
    n = get_int('Choose an option: ')
    if n==1:
      f = add_contact(f)
    elif n==2:
      search_contact(f)
    elif n==7:
      print 'Quit.\n'
      return
    elif n==3:
      show_list(f)
    elif n==6:
      show_all_tags(f)
    elif n==5:
      search_with_tag(f)
    elif n==4:
      c=raw_input('Enter the character.')
      show_alpha_list(f,c)
    
    else:
      print 'Please enter a valid option'
      
  return
if __name__ == '__main__':
  main()

