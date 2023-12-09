import tarfile
import os
import subprocess
from conf_build import vVERSION

def create_tar_gz(output_file, folders, files):
    with tarfile.open(output_file, "w:gz") as tar:
        # Add folders to file tar.gz
        for folder in folders:
            tar.add(folder, arcname=os.path.basename(folder))

        # Add files to file tar.gz
        for file in files:
            arcname = file.replace("../", "").replace("/", os.sep)
            tar.add(file, arcname=arcname)
            #tar.add(file, arcname=os.path.basename(file))

if __name__ == "__main__":
    # Define folders and files to add to file tar.gz
    folders_to_add = ["../pybioportal"]
    files_to_add = ["../setup.py", "../LICENSE.txt", "../README.md", "../tools/conf_build.py"]

    # tar.gz file name
    output_folder = "../archive/"
    file_name = f"pybioportal-{vVERSION}.tar.gz"
    output_file = output_folder + file_name

    create_tar_gz(output_file, folders_to_add, files_to_add)

# commit archive folder
os.chdir(output_folder)

# command git add .
subprocess.run(["git", "add", file_name])

# command git commit -m "Create new archive VERSION"
commit_message = f"Create new archive {vVERSION}"
subprocess.run(["git", "commit", "-m", commit_message])

# command git push origin master
subprocess.run(["git", "push", "origin", "master"])
