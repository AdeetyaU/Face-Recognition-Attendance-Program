import sys
import subprocess
print("Installing Packages...")
# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'opencv-contrib-python'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'numpy'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'pandas'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'Pillow'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'pytest-shutil'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'python-csv'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'yagmail'])



# process output with an API in the subprocess module:
reqs = subprocess.check_output([sys.executable, '-m', 'pip',
'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

print(installed_packages)
