import os

command = r"""
curl --silent "https://api.github.com/repos/jsoconno/architectures/releases/latest" | 
grep '"tag_name":' | 
sed -E 's/.*"v([^"]+)".*/\1/'   
"""

version = os.popen(command).read().strip()
print(version)