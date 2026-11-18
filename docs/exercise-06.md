# Exercise 6: Software Dependency Vulnerability Analysis Using OSV-Scanner

# Objective
To identify known security vulnerabilities in the software dependencies of OWASP Juice Shop using OSV-Scanner and a generated Software Bill of Materials (SBOM).

# Tools Used
- OSV-Scanner 2.7.0
- CycloneDX
- OWASP Juice Shop

# Steps Performed
1. Generated a CycloneDX SBOM for OWASP Juice Shop.
2. Used OSV-Scanner to analyse the generated SBOM.
3. Compared the identified software components against known vulnerability databases.
4. Reviewed the scanner output and vulnerability information.
5. Saved the scan results for further analysis.

# Results
- SBOM file: juice-shop-sbom.cdx.json
- Scanner: OSV-Scanner 2.7.0
- Scan output: scans/dependency_scan.txt
- Vulnerability findings: Refer to the generated scan output.

# Conclusion
Successfully generated and analysed a Software Bill of Materials for OWASP Juice Shop using OSV-Scanner. The exercise provided practical experience in identifying potentially vulnerable software dependencies and understanding the importance of software supply-chain security.