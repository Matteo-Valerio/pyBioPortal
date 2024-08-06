import os
import subprocess
from conf_build import vVERSION

output_folder = f"dist/{vVERSION}/pypi"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# commands to execute
commands = [
    f"python setup.py sdist --dist-dir {output_folder} bdist_wheel --dist-dir {output_folder}"
]

# command must be executed in root folder of repository
os.chdir("..")

print(f"Working Directory: {os.getcwd()}",)

for cmd in commands:
    print(f">>{cmd}: \n")
    subprocess.run(cmd, shell=True)

# Remove the build and pybioportal.egg-info directory after creating the packages
if os.path.exists("build"):
    if os.name == "nt":  # Check if running on Windows
        os.system(f"rmdir /s /q build")
    else:  # For Unix-like systems
        os.system(f"rm -rf build")

if os.path.exists("pybioportal.egg-info"):
    if os.name == "nt":  # Check if running on Windows
        os.system(f"rmdir /s /q pybioportal.egg-info")
    else:  # For Unix-like systems
        os.system(f"rm -rf pybioportal.egg-info")

# commit pypi build folder 
os.chdir(output_folder)

# command git add .
subprocess.run(["git", "add", "."])

# command git commit
commit_message = f"Build version {vVERSION}"
subprocess.run(["git", "commit", "-m", commit_message])

# command git push origin master
subprocess.run(["git", "push", "origin", "master"])