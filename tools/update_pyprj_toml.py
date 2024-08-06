import tomlkit
import os
import subprocess
from conf_build import VERSION

file_path = "../pyproject.toml"

# read pyproject.toml
with open(file_path, 'r') as file:
    toml_content = file.read()

# parse toml content
parsed_toml = tomlkit.parse(toml_content)

# update value
parsed_toml['project']['version'] = VERSION

# write pyproject.toml
with open(file_path, 'w') as file:
    file.write(parsed_toml.as_string()) 

# commit file toml in root repository
os.chdir("..")

# command git add .
subprocess.run(["git", "add", "pyproject.toml"])

# command git commit
commit_message = f"Update version: {VERSION}"
subprocess.run(["git", "commit", "-m", commit_message])

# command git push origin master
subprocess.run(["git", "push", "origin", "master"])