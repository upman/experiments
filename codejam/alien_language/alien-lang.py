#!/usr/bin/python
#Solution to problem at http://code.google.com/codejam/contest/90101/dashboard#s=p0
import re #Regular Expressions

infile=open('alien-lang-large.in','r') 
outfile=open('alien-lang-large.out','w')

params_list= infile.readline().split(' ')
token_count,word_count,test_cases=[int(x) for x in params_list]#Parallel assignment

words_list=''
for x in range (word_count):
  words_list+=infile.readline()#All words (in the language) in a single string separated by \n from infile
  
  
for case_number in range(1,test_cases+1):
  word_approximate=infile.readline().rstrip('\n')
  word_approximate=word_approximate.replace('(','[').replace(')',']')#Making a regular expression string
 #Every character inside [] is perceived a possible character by the Regex Parser
  matches=re.findall(word_approximate,words_list)#All matching words returned as a list
  outfile.write('Case #%d: %d\n' %(case_number,len(matches)))
infile.close()
outfile.close()

