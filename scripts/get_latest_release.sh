get_latest_release() {
  curl --silent "https://api.github.com/repos/$1/releases/latest" | # Get latest release from GitHub api
    grep '"tag_name":' |                                            # Get tag line
    sed -E 's/.*"v([^"]+)".*/\1/'                                   # Pluck JSON value
}

# Usage
# get_latest_release "jsoconno/architectures"

# Example output:
# v0.31.4