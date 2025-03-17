import os
import sys


def get_resource_path(relative_path):
        if hasattr(sys, '_MEIPASS'):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")
            
        return os.path.join(base_path, relative_path)