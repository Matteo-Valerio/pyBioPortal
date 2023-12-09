import tarfile
import os
import subprocess
from conf_build import VERSION, vVERSION

def create_tar_gz(output_file, folders, files):
    with tarfile.open(output_file, "w:gz") as tar:
        # Add folders to file tar.gz
        for folder in folders:
            tar.add(folder, arcname=os.path.basename(folder))

        # Add files to file tar.gz
        for file in files:
            arcname = file.replace("..", "root").replace("/", os.sep)
            tar.add(file, arcname=arcname)
            #tar.add(file, arcname=os.path.basename(file))

if __name__ == "__main__":
    # Define folders and files to add to file tar.gz
    folders_to_add = ["../pybioportal", "../tools/conf_build.py"]
    files_to_add = ["../setup.py", "../LICENSE.txt", "../README.md"]

    # tar.gz file name
    output_file = f"../archive/pybioportal-{vVERSION}.tar.gz"

    create_tar_gz(output_file, folders_to_add, files_to_add)

os.chdir('..')

# command git add .
subprocess.run(['git', 'add', '.'])

# command git commit -m "Create new archive VERSION"
commit_message = f"Create new archive {VERSION}"
subprocess.run(['git', 'commit', '-m', commit_message])

# command git push origin master
subprocess.run(['git', 'push', 'origin', 'master'])
