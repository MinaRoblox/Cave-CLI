import os
import sys
import time
import random
import termios
import tty
from sprites import *
from colorama import Fore, Back, Style


debugMode = False
productionMode = False


mandatory_message = "Made using the libraries of gameEngineLibraries.py"