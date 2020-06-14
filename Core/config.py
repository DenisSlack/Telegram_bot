import importlib
import os
import sys


def load_config():
    conf_name = os.environ.get("TG_CONF")
    if conf_name is None:
        conf_name = "development"
    try:
        r = importlib.import_module("settings.{}".format(conf_name))
        print("Loaded config \"{}\" - OK".format((conf_name)))
        return r
    except (TypeError, ValueError, ImportError):
        print("Invalid config \"{}\"".format(conf_name))
        sys.exit(1)