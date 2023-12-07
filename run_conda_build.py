import subprocess
import os

version = "v1.0.0"
output_folder = f"dist\\{version}\\anaconda\\"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# commands to execute
commands = [
    'cls',
    'conda activate conda_build_package',
    f'conda build . --output-folder {output_folder}',
    'conda build purge'
]

for cmd in commands:
    subprocess.run(cmd, shell=True)
