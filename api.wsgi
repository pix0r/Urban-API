import os, sys

project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_dir)
os.chdir(project_dir)

# activate virtualenv
virtualenv = "env"

import glob, site
for dir in glob.glob(virtualenv + "/lib/python*"):
	site_packages = dir + "/site-packages"
	print "adding", site_packages
	site.addsitedir(site_packages)

from api import app
application = app
