import subprocess
import os

subprocess = subprocess.call(["pip", "freeze"])
subprocess.call("pip freeze > requirements.txt", shell=True)
print(subprocess)

with open('requirements.txt', 'w') as file_:
    subprocess.Popen(['pip', 'freeze'], stdout=file_).communicate()

with open('requirements.txt', 'w') as file_:
    subprocess.call(['pip', 'freeze'], stdout=file_)

os = os.system('pip freeze')
print(os)