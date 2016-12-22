import os


# 'cwd' 
cwd = os.getcwd()
print("pwd : " + cwd)


print("-"*80)


# 'cd /'
cwd = os.getcwd()
print("older pwd : " + cwd)

change = "\\"
os.chdir(change)

cwd = os.getcwd()
print("now pwd : " + cwd)
