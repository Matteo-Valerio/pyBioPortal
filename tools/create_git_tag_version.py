import os
import subprocess
from conf_build import VERSION, vVERSION

#---- Define tag name and description
tag_name = vVERSION
tag_message = f"Version {VERSION}"
release_message = f"Version {VERSION}"

os.chdir("..")

print(f"Working Directory: {os.getcwd()}",)

#---- Command to check if the tag exists locally
check_tag_command = f'git rev-parse --verify --quiet refs/tags/{tag_name}'

# Run the command to check if the tag exists locally
try:
    subprocess.run(check_tag_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    tag_exists = True
except subprocess.CalledProcessError as e:
    tag_exists = False

#---- Command to check if the tag exists remotely
check_remote_tag_command = f'git ls-remote --tags origin {tag_name}'

# Run the command to check if the tag exists remotely
result = subprocess.run(check_remote_tag_command, shell=True, capture_output=True, text=True)
remote_tag_exists = tag_name in result.stdout

# If the remote tag exists, delete it; otherwise, display a message indicating the tag is new
if remote_tag_exists:
    delete_remote_tag_command = f'git push origin --delete {tag_name}'

    try:
        subprocess.run(delete_remote_tag_command, shell=True, check=True)
        print(f"Deleted existing '{tag_name}' tag from the remote repository")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while deleting the existing tag: {e}")
else:
    print(f"The remote tag '{tag_name}' is new")


#---- Overwrite the existing tag with a new annotation if present, otherwise create a new tag
if tag_exists:
    overwrite_tag_command = f'git tag -a -f {tag_name} -m "{tag_message}"'

    try:
        subprocess.run(overwrite_tag_command, shell=True, check=True)
        print(f"Overwrote the existing '{tag_name}' tag locally with a new annotation successfully")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while overwriting the existing tag locally: {e}")
else:
    create_tag_command = f'git tag -a {tag_name} -m "{tag_message}"'

    try:
        subprocess.run(create_tag_command, shell=True, check=True)
        print(f"Created a new local '{tag_name}' tag successfully")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while creating the local tag: {e}")


#---- Push of all tags, including those edited or added
push_tags_command = 'git push --tags'

try:
    subprocess.run(push_tags_command, shell=True, check=True)
    print("Successfully pushed all tags to the remote repository.")
except subprocess.CalledProcessError as e:
    print(f"An error occurred while pushing tags to the remote repository: {e}")


#---- Create a release associated with the tag
create_release_command = f'git push origin master && git tag -a {tag_name} -m "{release_message}" && git push origin {tag_name}'
try:
    subprocess.run(create_release_command, shell=True, check=True)
    print(f"Release '{tag_name}' created successfully.")
except subprocess.CalledProcessError as e:
    print(f"An error occurred while creating the release: {e}")