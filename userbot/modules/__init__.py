# Copyright (C) 2020 Poyraz Usta.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

# Endles UserBot - Poyraz Usta

""" Tüm modülleri yükleyen init dosyası """
from userbot import LOGS


def __list_all_modules():
    from os.path import dirname, basename, isfile
    import glob

    mod_paths = glob.glob(dirname(__file__) + "/*.py")
    return [
        basename(f)[:-3] for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]


ALL_MODULES = sorted(__list_all_modules())
LOGS.info("Yüklenecek modüller: %s", str(ALL_MODULES))
__all__ = ALL_MODULES + ["ALL_MODULES"]
