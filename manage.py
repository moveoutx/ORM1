#!/usr/bin/env python
import os
import sys
import psycopg2

conn = psycopg2.connect(dbname='orm1_phones', user='postgres',
                        password='Gthtw!50', host='localhost')
cursor = conn.cursor()

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', "main.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
