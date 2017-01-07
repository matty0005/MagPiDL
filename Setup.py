#Downloads all the necesary librarys to run the script - Requires PIP
import pip


#defining the installation process
def install(package):
    pip.main(['install', package])

#testing to see if bs4 is installed
try:
   import bs4
#if not, it will install the module
except ImportError:
   print 'Error, Module BeautifulSoup4 is required'
   install('bs4')
   
#testing to see if 'requests' is installed 
try:
   import requests
#if not, it will install the module
except ImportError:
   print 'Error, Module Requests is required'
   install('requests')

#testing to see if tqdm is installed
try:
   import tqdm
#if not, it will install the module
except ImportError:
   print 'Error, Module tqdm is required'
   install('tqdm')
