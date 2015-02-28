# -*- coding: UTF-8 -*-
'''
1.
backup for django-1.7.5 config,
when installed django-1.7.5, 
backup %PYTHON_HOME%\Lib\site-packages\django\conf to %PYTHON_HOME%\Lib\site-packages\django\conf_bak,
then copy this folder to %PYTHON_HOME%\Lib\site-packages\django\conf

can use ../updateDjangoConf.bat to make this change!

2.
update runserver.py to see console about hello page tip:
D:\app\Python27\Lib\site-packages\django\core\management\commands\runserver.py
change line 116 to:
"Starting development server at http://%(addr)s:%(port)s/\nAccess http://%(addr)s:%(port)s/hello to see the hello page\n"

3.
add admin-site favicon.ico
D:\app\Python27\Lib\site-packages\bootstrap_admin\templates\admin\base.html
line 6 insert:
<link rel="icon" href="{{STATIC_URL}}img/favicon.ico">

'''