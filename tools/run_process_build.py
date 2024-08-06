import subprocess

# script list to run
scripts_to_run = ["update_pyprj_toml.py",
                  "update_meta_yaml.py", 
                  "create_archive.py", 
                  "run_pypi_build.py", 
                  "run_conda_build.py",
                  "create_git_tag_version.py"]

for script in scripts_to_run:
    subprocess.run(["python", script])