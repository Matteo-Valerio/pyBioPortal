import subprocess
import os
from conf_build import vVERSION

output_folder = f"../dist/{vVERSION}/anaconda"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# commands to execute
commands = [
    f"conda build . --output-folder {output_folder}",
    "conda build purge"
]

# command must be executed in recipe folder of repository
os.chdir("../recipe")

print(f"Working Directory: {os.getcwd()}",)

for cmd in commands:
    print(f">>{cmd}: \n")
    subprocess.run(cmd, shell=True)

# commit anaconda build folder 
os.chdir(output_folder)

# command git add .
subprocess.run(["git", "add", "."])

# command git commit
commit_message = f"Build version {vVERSION}"
subprocess.run(["git", "commit", "-m", commit_message])

# command git push origin master
subprocess.run(["git", "push", "origin", "master"])
