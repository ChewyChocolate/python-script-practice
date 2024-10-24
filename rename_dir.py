import subprocess

command = subprocess.run(['ren firecafa newfolder'], capture_output=True, shell=True, text=True)

print(command.stdout)
