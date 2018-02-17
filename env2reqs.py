"""
	Date: 14 February 2018
	Purpose: Creates a requirements.txt file from the directory of a python project.
"""
import sys
import os
from virtualenvapi.manage import VirtualEnvironment

venvFiles=['include','bin','local','lib','pip-selfcheck.json']

def envPath(directory_path):
	"""
		Parameters:
			directory_path : Directory of the python project. 
		Returns the absolute path of the virtual environment folder.
	"""
	for dir in os.listdir(directory_path):
		#Checks for every folder if it contains the virtual env files.
		if os.path.isdir(os.path.join(directory_path,dir)) and set(venvFiles).issubset(set(os.listdir(os.path.join(directory_path,dir)))):
			return os.path.join(directory_path,dir)

if __name__ == '__main__':
	try:
		#Checks if the virtual environment is present in the specified path and creates one if not.
		env = VirtualEnvironment(envPath(sys.argv[1])) 
		#Lists the python packages installed in the virtual env.
		pkgs=env.installed_packages
		with open("requirements.txt","w") as f:
			for pkg,pkg_version in pkgs:
				f.write(pkg+"==="+pkg_version+"\n")
	except:
		print "No virtual env folder"