import os
import subprocess
from conf_build import VERSION, vVERSION

# Define tag name and description
tag_name = vVERSION
tag_message = f"Version {VERSION}"

os.chdir("..")

print(f"Working Directory: {os.getcwd()}",)

# Command to check if the tag exists locally
check_tag_command = f'git rev-parse --verify --quiet refs/tags/{tag_name}'

# Run the command to check if the tag exists
try:
    subprocess.run(check_tag_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    tag_exists = True
except subprocess.CalledProcessError as e:
    tag_exists = False

# Overwrite the existing tag with a new annotation if present, otherwise create a new tag
if tag_exists:
    overwrite_tag_command = f'git tag -a -f {tag_name} -m "{tag_message}"'

    try:
        subprocess.run(overwrite_tag_command, shell=True, check=True)
        print(f"Overwrote the existing '{tag_name}' tag with a new annotation successfully")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while overwriting the existing tag: {e}")
else:
    create_tag_command = f'git tag -a {tag_name} -m "{tag_message}"'

    try:
        subprocess.run(create_tag_command, shell=True, check=True)
        print(f"Created a new '{tag_name}' tag successfully")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while creating the tag: {e}")

# Push of all tags, including those edited or added
push_tags_command = 'git push --tags'

try:
    subprocess.run(push_tags_command, shell=True, check=True)
    print("Successfully pushed all tags to the remote repository.")
except subprocess.CalledProcessError as e:
    print(f"An error occurred while pushing tags to the remote repository: {e}")

