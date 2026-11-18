# Exercise 5: Software Bill of Materials (SBOM) Generation Using CycloneDX

# Objective
To generate a Software Bill of Materials (SBOM) for the OWASP Juice Shop application using CycloneDX and identify the software components and dependencies used by the application.

# Tools Used
- OWASP Juice Shop
- Node.js and npm
- CycloneDX npm

# Steps Performed
1. Opened the OWASP Juice Shop project directory in PowerShell.
2. Used the CycloneDX npm tool to generate an SBOM.
3. Generated the SBOM in JSON format.
4. Saved the generated file in the SecureScope project directory.
5. Opened the JSON file to inspect the listed components and dependency information.

# Command Used

```powershell
npx @cyclonedx/cyclonedx-npm --output-format JSON --output-file C:\MCA\Projects\SecureScope\sbom\juice-shop-sbom.json
```

# Results
- Successfully generated an SBOM for OWASP Juice Shop.
- The SBOM contains software component and dependency information.
- The generated file was saved in JSON format.
- The SBOM was subsequently used as input for dependency vulnerability analysis using OSV-Scanner.

# Output File
`sbom/juice-shop-sbom.cdx.json`

# Conclusion
Successfully generated a CycloneDX Software Bill of Materials for OWASP Juice Shop. The generated SBOM provides an inventory of software components and their dependencies, which can be used to identify known vulnerabilities and assess software supply-chain security.