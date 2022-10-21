from genericpath import isfile
import os
import shutil
import git

shw, xhw, sbk = [], [], []

MAGICQ_DIR = "C:\\Users\\oliver\\Documents\\MagicQ\\show"

print("Looking for shows in " + MAGICQ_DIR)

for filename in os.listdir(MAGICQ_DIR):
    if os.path.isfile(os.path.join(MAGICQ_DIR, filename)) and filename.endswith(".shw"):
        shw.append(filename)
    elif os.path.isfile(os.path.join(MAGICQ_DIR, filename)) and filename.endswith(".xhw"):
        xhw.append(filename)
    elif os.path.isfile(os.path.join(MAGICQ_DIR, filename)) and filename.endswith(".sbk"):
        sbk.append(filename)

print("Found " + str(len(shw)) + " .shw files, " + str(len(xhw)) + " .xhw files, and " + str(len(sbk)) + " .sbk files")

for item in shw:
    if not (os.path.exists(os.path.join(os.getcwd(), "dirs", item[0:len(item)-4]))):
        os.mkdir(os.path.join(os.getcwd(), "dirs", item[0:len(item)-4]))
        shutil.copy2(os.path.join(MAGICQ_DIR, item), os.path.join(os.getcwd(), "dirs", item[0:len(item)-4]))
    else:
        shutil.copy2(os.path.join(MAGICQ_DIR, item), os.path.join(os.getcwd(), "dirs", item[0:len(item)-4], item))
for item in xhw:
    if not (os.path.exists(os.path.join(os.getcwd(), "dirs", item[0:len(item)-4]))):
        os.mkdir(os.path.join(os.getcwd(), "dirs", item[0:len(item)-4]))
        shutil.copy2(os.path.join(MAGICQ_DIR, item), os.path.join(os.getcwd(), "dirs", item[0:len(item)-4]))
    else:
        shutil.copy2(os.path.join(MAGICQ_DIR, item), os.path.join(os.getcwd(), "dirs", item[0:len(item)-4], item))
for item in sbk:
    if not (os.path.exists(os.path.join(os.getcwd(), "dirs", item[0:len(item)-4]))):
        os.mkdir(os.path.join(os.getcwd(), "dirs", item[0:len(item)-4]))
        shutil.copy2(os.path.join(MAGICQ_DIR, item), os.path.join(os.getcwd(), "dirs", item[0:len(item)-4]))
    else:
        shutil.copy2(os.path.join(MAGICQ_DIR, item), os.path.join(os.getcwd(), "dirs", item[0:len(item)-4], item))

