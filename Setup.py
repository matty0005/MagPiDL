#Downloads all the necesary librarys to run the script - Requires PIP
import pip
package = ["bs4","requests", "tqdm"]

#defining the installation process
def install(package):
    pip.main(['install', package])

	
for package in package:
	try:
		__import__(package)
		print '%s is installed.' % package
	except ImportError:
	   print 'Error, Module %s is required' % package
	   install('package')
	
