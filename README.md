env.py
======

Easily manage your python application settings for different environments

Usage:
------

Consider following file structure somewhere in your python application:

- app
  - settings.py
  - local_env.py            # required by env.py
  - local_settings.py
  - dev_settings.py
  - prod_settings.py
  - prodstage_settings.py
  - test_settings.py

What `env.py` does is, it allows you to define your different environment settings 
inside a file named `$env_settings.py`. Then, inside `local_env.py` you define 
something like `ENV='prod'`.

Then at the top (or at the bottom) of your `settings.py` use as:

`from env import *`

This will configure your application for your current `ENV` settings along with common `settings.py`
