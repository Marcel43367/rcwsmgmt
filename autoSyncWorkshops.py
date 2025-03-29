#!/usr/bin/env python
"""Auto sync workshops from pretix to database."""
import os
import sys
import datetime
import time

from django.core.management import execute_from_command_line

def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rcwsmgmt.settings")
    while True:
            now = datetime.datetime.now()
            if now.minute == 0 and now.second == 0:
                execute_from_command_line(['manage.py', 'sync_workshops'])
            time.sleep(1)


if __name__ == "__main__":
    main()
