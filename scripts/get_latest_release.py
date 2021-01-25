import os

def get_latest_release_version(user, repo):
    command = f"""
    curl --silent "https://api.github.com/repos/{user}/{repo}/releases/latest" | 
    grep '"tag_name":' | 
    sed -E 's/.*"v([^"]+)".*/\1/'   
    """

    return os.popen(command).read().strip()

version = get_latest_release_version('jsoconno', 'architectures')
print(version)