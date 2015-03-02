# -*- coding: UTF-8 -*-
#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings.common")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

#createsuperuser admin in cmd
#python manage.py createsuperuser --settings={{project_name}}.settings.dev


#python manage.py migrate {{app_name}} --settings={{project_name}}.settings.dev
#python manage.py makemigratioins {{app_name}} --settings={{project_name}}.settings.dev
#python manage.py sqlmigrate {{app_name}} (migration) --settings={{project_name}}.settings.dev
