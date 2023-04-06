import os
# This is a Python script that checks if each tool in the tools list is installed on the system using the which command.
# If the tool is installed, the script prints a message indicating that the tool is installed.
# If the tool is not installed, the script prints a message indicating that the tool is not installed.

# Define the required tools
tools = [
    "subfinder",
    "dirsearch",
    "nmap",
    "getJS",
    "assetfinder",
    "sublist3r",
    "amass",
    "getallurls",
    "waybackurls",
    "massdns",
    "sublist3r",
    "ffuf",
    "httprobe",
    "xsstrike.py",
    "sqlmap",
    "XXEinjector.rb",
    "gopherus.py",
    "git_dumper.py",
    "corstest.py",
    "EyeWitness.py",
    "parameth.py"
]
# Check if each tool is installed
for tool_name in tools:
    if os.system(f"which {tool_name} > /dev/null") == 0:
        print(f"[+] {tool_name} is installed")
    else:
        print(f"[-] {tool_name} is not installed")
