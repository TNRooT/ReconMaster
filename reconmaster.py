import os
import sys
# Print the title
print("*********************************************************************************************************************************************")
print(" _______  _______  _______  _______  _        _______  _______  _______ _________ _______  _______                                           ")
print("(  ____ )(  ____ \(  ____ \(  ___  )( (    /|(       )(  ___  )(  ____ \\__   __/(  ____ \(  ____ )                                          ")
print("| (    )|| (    \/| (    \/| (   ) ||  \  ( || () () || (   ) || (    \/   ) (   | (    \/| (    )|                                          ")
print("| (____)|| (__    | |      | |   | ||   \ | || || || || (___) || (_____    | |   | (__    | (____)|                                          ")
print("|     __)|  __)   | |      | |   | || (\ \) || |(_)| ||  ___  |(_____  )   | |   |  __)   |     __)                                          ")
print("| (\ (   | (      | |      | |   | || | \   || |   | || (   ) |      ) |   | |   | (      | (\ (                                             ")
print("| ) \ \__| (____/\| (____/\| (___) || )  \  || )   ( || )   ( |/\____) |   | |   | (____/\| ) \ \__                                          ")
print("|/   \__/(_______/(_______/(_______)|/    )_)|/     \||/     \|\_______)   )_(   (_______/|/   \__/                                          ")
print("")
print("")
print(" _______  _______  ______   _______  ______             __________________            _______  _______  _______ _________  _________ _       ")
print("(  ____ \(  ___  )(  __  \ (  ____ \(  __  \   |\     /|\__   __/\__   __/|\     /|  (  ____ )(  ___  )(  ___  )\__   __/  \__   __/( (    /|")
print("| (    \/| (   ) || (  \  )| (    \/| (  \  )  | )   ( |   ) (      ) (   | )   ( |  | (    )|| (   ) || (   ) |   ) (        ) (   |  \  ( |")
print("| |      | |   | || |   ) || (__    | |   ) |  | | _ | |   | |      | |   | (___) |  | (____)|| |   | || |   | |   | |        | |   |   \ | |")
print("| |      | |   | || |   | ||  __)   | |   | |  | |( )| |   | |      | |   |  ___  |  |     __)| |   | || |   | |   | |        | |   | (\ \) |")
print("| |      | |   | || |   ) || (      | |   ) |  | || || |   | |      | |   | (   ) |  | (\ (   | |   | || |   | |   | |        | |   | | \   |")
print("| (____/\| (___) || (__/  )| (____/\| (__/  )  | () () |___) (___   | |   | )   ( |  | ) \ \__| (___) || (___) |   | |        | |   | )  \  |")
print("(_______/(_______)(______/ (_______/(______/   (_______)\_______/   )_(   |/     \|  |/   \__/(_______)(_______)   )_(        )_(   |/    )_)")
print("")
print("*********************************************************************************************************************************************")


# Take user input for target URL and output directory
target_url = input("Enter target URL: ")
# Create output directory with target URL as name
output_dir = target_url.replace("http://", "").replace("https://", "").replace(".", "_")
os.makedirs(output_dir, exist_ok=True)

# Create directories for each reconnaissance type
subdomain_dir = os.path.join(output_dir, "subdomain_enumeration")
os.mkdir(subdomain_dir)

directory_dir = os.path.join(output_dir, "directory_enumeration")
os.mkdir(directory_dir)

port_dir = os.path.join(output_dir, "port_scanning")
os.mkdir(port_dir)

vuln_dir = os.path.join(output_dir, "vulnerability_scanning")
os.mkdir(vuln_dir)

web_dir = os.path.join(output_dir, "web_reconnaissance")
os.mkdir(web_dir)

network_dir = os.path.join(output_dir, "network_reconnaissance")
os.mkdir(network_dir)

# Display menu options to user
print("Please select a reconnaissance type:")
print("1. Subdomain Enumeration")
print("2. Directory Enumeration")
print("3. Port Scanning and Service Enumeration")
print("4. Vulnerability Scanning")
print("5. Web Technology Reconnaissance")
print("6. Network Reconnaissance")

# Take user input for selected reconnaissance type
selection = input("Enter your selection (1-6): ")

# Perform selected reconnaissance
if selection == "1":
    # Subdomain enumeration
    os.system(f"subfinder -d {target_url} -o {subdomain_dir}/subdomains.txt")
    os.system(f"amass enum -passive -d {target_url} -o {subdomain_dir}/amass.txt")
    os.system(f"assetfinder --subs-only {target_url} > {subdomain_dir}/assetfinder.txt")
    os.system(f"sublist3r -d {target_url} -o {subdomain_dir}/sublist3r.txt")

    # Check if subdomains are alive
    os.system(f"cat {subdomain_dir}/subdomains.txt | httprobe > {subdomain_dir}/alive.txt")
    os.system(f"cat {subdomain_dir}/amass.txt | httprobe >> {subdomain_dir}/alive.txt")
    os.system(f"cat {subdomain_dir}/assetfinder.txt | httprobe >> {subdomain_dir}/alive.txt")
    os.system(f"cat {subdomain_dir}/sublist3r.txt | httprobe >> {subdomain_dir}/alive.txt")

elif selection == "2":
    # Directory enumeration
    os.system(f"dirsearch -u {target_url} -e all -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -o {directory_dir}/dirs.txt")
    os.system(f"ffuf -c -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u {target_url}/FUZZ -o {directory_dir}/ffuf.txt")

elif selection == "3":
    # Port scanning and service enumeration
    os.system(f"nmap -p- -sS -sV -oN {port_dir}/nmap.txt {target_url}")

elif selection == "4":
    # Vulnerability scanning
    os.system(f"nmap --script vuln -oN -d {vuln_dir}/nmap_vuln.txt {target_url}")

elif selection == "5":
    # Web technology reconnaissance
    os.system(f"getJS -u {target_url} -o {web_dir}/js.txt")
    os.system(f"getallurls {target_url} > {web_dir}/urls.txt")
    os.system(f"waybackurls {target_url} > {web_dir}/wayback.txt")
    os.system(f"waybackrobots {target_url} > {web_dir}/robots.txt")
    os.system(f"racetheweb -u {target_url} -o {web_dir}/racetheweb.txt")
    os.system(f"EyeWitness.py -f {web_dir}/subdomains.txt -d {web_dir}/eyewitness -r http,https")

elif selection == "6":
    # Network reconnaissance
    os.system(f"massdns -r /path/to/resolvers.txt -t A -o S -w {network_dir}/massdns.txt {subdomain_dir}/alive.txt")
    os.system(f"xsstrike -u {target_url} -o {network_dir}/xss.txt")
    os.system(f"sqlmap -u {target_url} --batch --level=5 --risk=3 -o -f -o {network_dir}/sqlmap.txt")
    os.system(f"xxeinjector {target_url} -o {network_dir}/xxe.txt")
    os.system(f"gopherus.py -u {target_url} -o {network_dir}/ssrf.txt")
    os.system(f"git_dumper.py {target_url}/.git/ {network_dir}/git")
    os.system(f"gitallsecrets {network_dir}/git {network_dir}/gitallsecrets.txt")
    os.system(f"corstest.py -u {target_url}")
    os.system(f"parameth.py  -u {target_url} -o {network_dir}/parameth.txt")
else:
    print('Invalid choice.')
    sys.exit(1)
