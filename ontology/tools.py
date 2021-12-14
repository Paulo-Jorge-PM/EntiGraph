#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

__author__ = "Paulo PM"
__email__ = "paulo.jorge.pm@gmail.com"
__version__ = "0.1.0"
__license__ = "MIT"

def normalizeNonAlfanumerical(text):
    text=text.replace(" ", "_")
    #substitute for - non alfanumerical carachteres
    text=re.sub('[^0-9a-zA-Z_-]', '-', text)
    return text
