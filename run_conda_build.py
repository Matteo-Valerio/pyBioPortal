import subprocess
import os

version = "v1.0.0"
output_folder = f"dist\\{version}\\anaconda"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# commands to execute
commands = [
    f'conda build . --output-folder {output_folder}',
    'conda build purge'
]

print(f'Current Directory: {os.getcwd()}',)

for cmd in commands:
    print(f'>>{cmd}: \n')
    subprocess.run(cmd, shell=True)
