#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import subprocess                                       #importing necessary libraries


# p = subprocess.Popen([sys.executable, 'twitter_bot.py'], 
#                                     stdout=subprocess.PIPE, 
#                                     stderr=subprocess.STDOUT)

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'twitter_assist.settings')
    try:
        from django.core.management import execute_from_command_line                                       #django error handling
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':                                          #calling main
    main()
