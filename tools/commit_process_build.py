import subprocess
from conf_build import vVERSION

# command git add .
subprocess.run(['git', 'add', '.'])

# command git commit -m "Create new archive VERSION"
commit_message = f"Build version {vVERSION}"
subprocess.run(['git', 'commit', '-m', commit_message])

# command git push origin master
subprocess.run(['git', 'push', 'origin', 'master'])