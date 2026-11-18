# Exercise 1: Web Application Reconnaissance

Objective: To identify the availability of the target web application and determine the open port and service information using Nmap.

Tool Used: Nmap 7.993

Target: 127.0.0.1 (OWASP Juice Shop)

Command:
```bash
nmap -sV -p 3000 127.0.0.1
```

Results:
- The target host was found to be up.
- TCP port 3000 was found open.
- Nmap identified the service as `ppp?`, with uncertain service identification.
- The scan completed successfully in 12.82 seconds.

Conclusion: The scan confirmed that the target application is accessible through port 3000. Further application-level testing will be performed using Burp Suite and OWASP ZAP.