import subprocess

code = subprocess.call(["ping", "www.google.com"])
if code == 0:
    print("Success!")
else:
    print("Error!")
    
