import os, sys

project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_dir)
os.chdir(project_dir)

# activate virtualenv
virtualenv = "env"
#site_packages = project_dir + "/" + virtualenv + "/lib/python2.6/site-packages"
#import site
#site.addsitedir(site_packages)
#print "Added site dir: " + site_packages

from api import app
application = app
