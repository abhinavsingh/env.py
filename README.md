env.py
======

Easily manage your python application settings for different environments

Usage:
------

Consider following file structure somewhere in your python application:

```
- app
  - settings.py
  - local_env.py            # required by env.py
  - local_settings.py
  - dev_settings.py
  - prod_settings.py
  - prodstage_settings.py
  - test_settings.py
```

What `env.py` does is, it allows you to define different environment custom settings 
inside files named `$env_settings.py`. Then, inside `local_env.py` define 
current environment like `ENV='prod'`.

At the top or at the bottom of `settings.py` based upon how you use `env.py`, use as:

`from env import *`

This will configure your application for your current `ENV` custom settings along with common `settings.py`
