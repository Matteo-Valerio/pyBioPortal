import ruamel.yaml
import os
import subprocess
import hashlib
from conf_build import VERSION, vVERSION, URL_ARCHIVE

file_path = "../recipe/meta.yaml"

#--- calculate sha256 of the source tar.gz

# tar.gz file name
output_file = f"../archive/pybioportal-{vVERSION}.tar.gz"

# hash_sha256 = hashlib.sha256()

# with open(output_file, 'rb') as f:
#     for chunk in iter(lambda: f.read(4096), b''):
#         hash_sha256.update(chunk)

def update_version_in_yaml(new_version, file_path):
    file_path = file_path

    yaml = ruamel.yaml.YAML()
    yaml.preserve_quotes = True  # maintain double quotes around values

    with open(file_path, "r") as file:
        data = yaml.load(file) 

    # update version value
    data["package"]["version"] = new_version
    data["source"]["url"] = f"{URL_ARCHIVE}/pybioportal-v{new_version}.tar.gz"
    #data["source"]["sha256"] = hash_sha256.hexdigest()

    with open(file_path, "w") as file:
        yaml.dump(data, file)

update_version_in_yaml(VERSION, file_path)

# commit repository
os.chdir("../recipe")

# command git add .
subprocess.run(["git", "add", "meta.yaml"])

# command git commit
commit_message = f"Update version: {VERSION}"
subprocess.run(["git", "commit", "-m", commit_message])

# command git push origin master
subprocess.run(["git", "push", "origin", "master"])
