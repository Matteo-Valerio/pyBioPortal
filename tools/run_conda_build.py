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
