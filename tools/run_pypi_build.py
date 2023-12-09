import os
import subprocess
from conf_build import vVERSION

output_folder = f"dist/{vVERSION}/pypi"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# commands to execute
commands = [
    "python setup.py",
]

os.chdir("..")

print(f"Working Directory: {os.getcwd()}",)

for cmd in commands:
    print(f">>{cmd}: \n")
    subprocess.run(cmd, shell=True)

# commit pypi build folder 
os.chdir(output_folder)

# command git add .
subprocess.run(["git", "add", "."])

# command git commit
commit_message = f"Build version {vVERSION}"
subprocess.run(["git", "commit", "-m", commit_message])

# command git push origin master
subprocess.run(["git", "push", "origin", "master"])