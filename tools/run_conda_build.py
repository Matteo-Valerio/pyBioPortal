import subprocess
import os
from conf_build import vVERSION

output_folder = f"..\\dist\\{vVERSION}\\anaconda"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# commands to execute
commands = [
    'cd..',
    f'conda build ..\ --output-folder {output_folder}',
    'conda build purge'
]

print(f'Current Directory: {os.getcwd()}',)

for cmd in commands:
    print(f'>>{cmd}: \n')
    subprocess.run(cmd, shell=True)

# command git add .
subprocess.run(['git', 'add', '.'])

# command git commit
commit_message = f"Build version {vVERSION}"
subprocess.run(['git', 'commit', '-m', commit_message])

# command git push origin master
subprocess.run(['git', 'push', 'origin', 'master'])
