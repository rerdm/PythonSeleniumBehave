from setuptools import setup,find_packages

setup(name='PythonSeleniumBehaveBDD',
      version='1.0',
      description='Python behave BDD examples',
      author='Rene Erdmann',
      author_email='reneerdmann87@web.de',
      url='test.com',
      # List all Modules with Common functions and steps
      packages=find_packages(),
    )

#  1. create a setup.py file - See template ( here located in  examples/test/ )
#  2. List all Packages (Folder) where your packages ar stored inside the setup.py
#  2. If you create new folders in your Projekt with new Functions you have to add them in the List
#  and run the command again
#  3. run the setup.py `python setup.py install` or `python setup.py develop`
#  4 . this will Create several folders:
# - PythonSeleniumBehaveBDD.egg-info
# - build ( Containing the Imported Folders with the classes)
# - dist
#  Reinstall :
#  python "C:\Users\rerdmann\Rerd_Programme\PythonSeleniumBehave\examples\setup.py" install

