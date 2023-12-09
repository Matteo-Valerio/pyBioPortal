import subprocess

# script list to run
scripts_to_run = ["update_meta_yaml.py", "create_archive.py", "run_pypi_build.py", "run_conda_build.py"]

for script in scripts_to_run:
    subprocess.run(["python", script])