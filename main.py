from genericpath import isfile
import os
import shutil
import git
from git import Repo

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

try:
    repo = Repo(os.path.join(os.getcwd(), "dirs", ".git"))
except:
    repo = Repo.init(os.path.join(os.getcwd(), "dirs"))

for item in shw:
    print("processing " + item)
    if not (os.path.exists(os.path.join(os.getcwd(), "dirs", item[0:len(item)-4]))):
        os.mkdir(os.path.join(os.getcwd(), "dirs", item[0:len(item)-4]))
        shutil.copy2(os.path.join(MAGICQ_DIR, item), os.path.join(os.getcwd(), "dirs", item[0:len(item)-4]))
        repo.git.add(os.path.join(os.getcwd(), "dirs", item[0:len(item)-4], item), update=True)
    else:
        shutil.copy2(os.path.join(MAGICQ_DIR, item), os.path.join(os.getcwd(), "dirs", item[0:len(item)-4], item))
for item in xhw:
    print("processing " + item)
    if not (os.path.exists(os.path.join(os.getcwd(), "dirs", item[0:len(item)-4]))):
        os.mkdir(os.path.join(os.getcwd(), "dirs", item[0:len(item)-4]))
        shutil.copy2(os.path.join(MAGICQ_DIR, item), os.path.join(os.getcwd(), "dirs", item[0:len(item)-4]))
        repo.git.add(os.path.join(os.getcwd(), "dirs", item[0:len(item)-4], item), update=True)
    else:
        shutil.copy2(os.path.join(MAGICQ_DIR, item), os.path.join(os.getcwd(), "dirs", item[0:len(item)-4], item))
for item in sbk:
    print("processing " + item)
    if not (os.path.exists(os.path.join(os.getcwd(), "dirs", item[0:len(item)-4]))):
        os.mkdir(os.path.join(os.getcwd(), "dirs", item[0:len(item)-4]))
        shutil.copy2(os.path.join(MAGICQ_DIR, item), os.path.join(os.getcwd(), "dirs", item[0:len(item)-4]))
        repo.git.add(os.path.join(os.getcwd(), "dirs", item[0:len(item)-4], item), update=True)
    else:
        shutil.copy2(os.path.join(MAGICQ_DIR, item), os.path.join(os.getcwd(), "dirs", item[0:len(item)-4], item))

repo.git.commit(m="Committing all files")
my_new_branch = repo.create_head('my_new_branch')
my_new_branch.checkout()
origin = repo.create_remote('origin', "https://parkero2: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@github.com/OTC-PAC/Backup.git")
repo.git.push("--set-upstream", origin, repo.head.ref)