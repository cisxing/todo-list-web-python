from selenium import webdriver
#this is comments
#write test first before writing the program
browser = webdriver.Firefox()
#start a portal 8000
browser.get('http://localhost:8000')

assert 'Django' in browser.title

#the last line is similar to the following:
#if ! 'django' in browser.title:
#   throw new AssertionError
