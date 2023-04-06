### ReconMaster : gather information about a target website using various tools and techniques to perform subdomain enumeration,    directory enumeration, port scanning and service enumeration, vulnerability scanning, web technology reconnaissance, and network reconnaissance.

![/banner.png](https://github.com/TNRooT/ReconMaster/blob/main/banner.png)


#### Key Features :

   - Subdomain enumeration: discovers subdomains of a target domain, which can help identify potential attack surfaces and entry points.
   - HTTP probing: checks if discovered subdomains are live and responding to HTTP requests.
   - Directory enumeration: searches for directories and files on a web server that may be hidden or unprotected, which can be used to gain access or perform further attacks.
   - Port scanning and service enumeration: scans for open ports and services running on a target system, which can provide valuable information for vulnerability assessment and exploitation.
   - Vulnerability scanning: searches for known vulnerabilities in a target system, including network and web application vulnerabilities.
   - Web technology reconnaissance: discovers the web technologies and frameworks used by a target web application, which can help identify potential vulnerabilities and attack vectors.
   - Network reconnaissance: performs various network-based attacks such as DNS enumeration, SQL injection, cross-site scripting (XSS), and server-side request forgery (SSRF) attacks, which can help identify potential vulnerabilities and entry points.
   - Git repository enumeration: searches for Git repositories on a target system and extracts sensitive information such as passwords, private keys, and API keys that may have been accidentally committed to the repository.
   - CORS testing: tests for Cross-Origin Resource Sharing (CORS) misconfigurations, which can allow attackers to bypass same-origin policies and access sensitive data.
   - Parameter discovery: discovers parameters in a target URL, which can help identify potential vulnerabilities and attack vectors in web applications.

#### Introduction:
```
ReconMaster used in the script include subfinder, amass, assetfinder, sublist3r, httprobe, dirsearch, ffuf, nmap, getJS, getallurls, waybackurls, waybackrobots, racetheweb, EyeWitness.py, massdns, xsstrike, sqlmap, xxeinjector, gopherus.py, git_dumper.py, gitallsecrets, corstest.py, and parameth.py.

Subdomain enumeration is performed using subfinder, amass, assetfinder, and sublist3r. The results are saved to files in the output directory.

The script then checks if the subdomains are alive using httprobe and saves the results to the alive.txt file.

Directory enumeration is performed using dirsearch and ffuf, and the results are saved to files in the output directory.

Port scanning and service enumeration is performed using nmap and the results are saved to the nmap.txt file.

Vulnerability scanning is performed using nmap with the vuln script, and the results are saved to the nmap_vuln.txt file.

Web technology reconnaissance is performed using getJS, getallurls, waybackurls, waybackrobots, racetheweb, and EyeWitness.py. The results are saved to files in the output directory.

Network reconnaissance is performed using massdns, xsstrike, sqlmap, xxeinjector, gopherus.py, git_dumper.py, gitallsecrets, corstest.py, and parameth.py. The results are saved to files in the output directory.
```

#### Usage instructions :

```
Note : Use python 3.7+
       Install Missing Tools

    1-  Make sure you have Python 3 installed on your system.
    2-  Download the ReconMaster script and save it in a directory of your choice.
    3-  Checks if a list of tools are installed on the system with verify_tools.py
    4-  Install the missing tools.
    5-  Open a command prompt or terminal window and navigate to the directory where you saved the ReconMaster script.
    6-  Once the packages are installed, you can run the script using the following command: 'python reconmaster.py'
    7-  The script will prompt you for the target domain or IP address that you want to scan.
    8-  Enter the target domain or IP address and press Enter.
    9-  The script will run various reconnaissance techniques and gather information about the target.
    10- Once the scan is complete, the script will display the results in the terminal window.
    11- You can also find the results in the results directory, which will be created in the same directory where the script is located.
```
#### Note :
```
     # instructions on how to install the missing tools :

    [+]subfinder:
    Installation instructions can be found on the official website at
        [-] https://subfinder.github.io/
    [+]dirsearch:
    Installation instructions can be found on the official GitHub repository at
        [-] https://github.com/maurosoria/dirsearch
    [+]nmap:
    Installation instructions can be found on the official website at
        [-] https://nmap.org/
    [+]vulners:
    Installation instructions can be found on the official GitHub repository at
        [-] https://github.com/vulnersCom/nmap-vulners
    [+]getJS:
    Installation instructions can be found on the official GitHub repository at
        [-] https://github.com/003random/getJS
    [+]gofinder:
    Installation instructions can be found on the official GitHub repository at
        [-] https://github.com/1ndianl33t/gofinder
    [+]getallurls:
    Installation instructions can be found on the official GitHub repository at
        [-] https://github.com/lc/gau
    [+]waybackurls:
    Installation instructions can be found on the official GitHub repository at
        [-] https://github.com/tomnomnom/waybackurls
    [+]waybackrobots:
    Installation instructions can be found on the official GitHub repository at
        [-] https://github.com/tomnomnom/waybackrobots
    [+]massdns:
    Installation instructions can be found on the official GitHub repository at
        [-] https://github.com/blechschmidt/massdns
    [+]sublist3r:
    Installation instructions can be found on the official GitHub repository at
        [-] https://github.com/aboul3la/Sublist3r
    [+]ffuf:
    Installation instructions can be found on the official GitHub repository at
        [-] https://github.com/ffuf/ffuf
    [+]xsshunter:
    Installation instructions can be found on the official website at
        [-] https://xsshunter.com/
    [+]sqlmap:
    Installation instructions can be found on the official GitHub repository at
        [-] https://github.com/sqlmapproject/sqlmap
    [+]xxeinjector:
    Installation instructions can be found on the official GitHub repository at
        [-] https://github.com/enjoiz/XXEinjector
    [+]ssrfdetector:
    Installation instructions can be found on the official GitHub repository at
        [-] https://github.com/0xInfection/SSRFDetector
    [+]gitdumper:
    Installation instructions can be found on the official GitHub repository at
        [-] https://github.com/arthaud/git-dumper
    [+]gitallsecrets:
    Installation instructions can be found on the official GitHub repository at
        [-] https://github.com/awslabs/git-secrets
    [+]racetheweb:
    Installation instructions can be found on the official GitHub repository at
        [-] https://github.com/dwisiswant0/race-the-web
    [+]corstest:
    Installation instructions can be found on the official GitHub repository at
        [-] https://github.com/RUB-NDS/CORStest
    [+]eyewitness:
    Installation instructions can be found on the official GitHub repository at
        [-] https://github.com/FortyNorthSecurity/EyeWitness
    [+]parameth:
    Installation instructions can be found on the official GitHub repository at
        [-] https://github.com/maK-/parameth

```
  

#### Usage options :

```
1 - Open a terminal window.
2 - Navigate to the directory where the script is saved.
3 - Run the command chmod +x BFpuredns.sh to make the script executable. 
4 - Run the script using the command ./BFpuredns.sh 
5 - When prompted, enter the domain name to brute force.
6 - Enter the wordlist file path. Make sure the file exists in the specified location.
7 - Enter the output file name. The output file will be created in the same directory as the script.
8 - Wait for the script to complete the DNS brute forcing process.
9 - Open the output file to view the results. The output file will be in the same directory as the script.

```


#### Example :

```
# python3 verify_tool.py
# python3 reconmaster.py

```
#### Note :

```
Note: Use of this script should only be for legitimate and legal purposes. It is important to ensure that you have proper authorization before performing subdomain enumeration on any domain.
```

#### My Twitter :


**Say hello** : [TNRooT](https://github.com/TNRooT)
                
            
#### My Youtube Channel :
**Say hello** : [TNRooT](https://youtube.com/@The_Ethical_TN)

