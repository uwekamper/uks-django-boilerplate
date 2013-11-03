Installation
=============

* virtualenv --distribute --no-site-packages .
* pip install -r requirements.txt
* copy local_settings.py.sample to local_settings.py
* bower install
* cd myproject
  * ./manage.py syncdb
  * ./manage.py migrate