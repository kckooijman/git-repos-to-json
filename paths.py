import sys
import os

"""
Set all the relative paths, add the parentDir to sys.path so we can import
the necessary modules.
"""

fileDir = os.path.dirname(os.path.abspath("__file__"))
parentDir = os.path.dirname(fileDir)
sys.path.append(parentDir)


dataDir = os.path.join(fileDir, 'Data')
jsonDir = os.path.join(dataDir, 'json')
csvDir = os.path.join(dataDir, 'csv')
dumpsDir = os.path.join(dataDir, 'index-dumps')
repoDir = os.path.join(dataDir, 'repositories')
# moduleDir = os.path.join(parentDir, 'modules')
