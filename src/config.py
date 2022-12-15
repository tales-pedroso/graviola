# -*- coding: utf-8 -*-
from os.path import dirname, basename
from os import sep

SRC_PATH = __file__
ROOT_PATH = dirname(dirname(SRC_PATH))
DEPENDENCIES_PATH = ROOT_PATH + sep + 'dependencies'
GECKODRIVER_PATH = DEPENDENCIES_PATH + sep + 'geckodriver' 



