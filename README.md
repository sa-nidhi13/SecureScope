🛡️ SecureScope

# Application Security Testing & SBOM Vulnerability Analysis Toolkit

SecureScope is a Python-based application security assessment toolkit developed to explore web application security testing, software supply-chain security, and vulnerability analysis.

The project combines established security tools with custom Python scripts to perform reconnaissance, inspect HTTP traffic, analyse security headers, generate Software Bills of Materials (SBOMs), and identify known vulnerabilities in software dependencies.

# Project Objectives

- Perform reconnaissance and identify exposed services.
- Intercept and analyse HTTP requests and responses.
- Examine HTTP security headers.
- Conduct automated web application security assessments.
- Generate CycloneDX Software Bills of Materials.
- Identify vulnerable software dependencies using OSV-Scanner.
- Automate SBOM and vulnerability data extraction using Python.
- Present assessment results through a Streamlit dashboard.

# Tools and Technologies

|          Category           |                 Tools                   |
|-----------------------------|-----------------------------------------|
| Programming                 | Python                                  |
| Web Application Testing     | Burp Suite Community Edition, OWASP ZAP |
| Network Reconnaissance      | Nmap                                    |
| Vulnerable Test Application | OWASP Juice Shop                        |
| SBOM Generation             | CycloneDX                               |
| Dependency Analysis         | OSV-Scanner                             |
| Data Processing             | Pandas                                  |
| Dashboard                   | Streamlit                               |
| Data Visualisation          | Matplotlib                              |
| Version Control             | Git and GitHub                          |

# Features

 1. Web Application Reconnaissance
- Port and service identification using Nmap.
- Identification of the target application's accessible services.

 2. HTTP Traffic Analysis
- Interception of HTTP requests and responses using Burp Suite.
- Examination of HTTP methods, headers, status codes, and response bodies.
- Observation of caching behaviour.

 3. Security Header Analysis
- Inspection of HTTP response security headers.
- Identification of existing and potentially missing security configurations.
- Preliminary assessment of header-related security concerns.

 4. Automated Security Scanning
- Baseline security scanning using OWASP ZAP.
- Review of security alerts and recommendations.

 5. SBOM Generation
- Generation of a CycloneDX SBOM for OWASP Juice Shop.
- Extraction of software component names, versions, types, and package URLs.

 6. Dependency Vulnerability Analysis
- Analysis of SBOM components using OSV-Scanner.
- Identification of known software dependency vulnerabilities.
- Extraction of vulnerability information into structured CSV reports.

 7. Python Automation
- Automated SBOM component extraction.
- Vulnerability data processing.
- CSV report generation.

 8. Security Dashboard
- Interactive Streamlit dashboard.
- Summary of software components and vulnerability findings.
- Tables and visualisations for assessment results.

# Project Structure
SecureScope/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── docs/
│   ├── target_scope.md
│   ├── exercise-01.md
│   ├── exercise-02.md
│   ├── exercise-03.md
│   ├── exercise-04.md
│   ├── exercise-05.md
│   └── exercise-06.md
│
├── src/
│   ├── sbom/
│   │   └── analyze_sbom.py
│   │
│   └── vulnerability/
│       └── analyze_vulnerabilities.py
│
├── sbom/
│   └── juice-shop-sbom.cdx.json
│
├── scans/
│   ├── nmap_initial.txt
│   ├── dependency_scan.txt
│   └── dependency_scan.json
│
├── reports/
│   ├── sbom_components.csv
|   ├── zap_baseline_report.html
│   └── vulnerability_report.csv
│
├── evidence/
│   ├── exercise-01/
│   ├── exercise-02/
│   ├── exercise-03/
│   ├── exercise-04.session
|   ├── exercise-04.session.data
|   ├── exercise-04.session
|   ├── exercise-04.session.script
│   ├── exercise-05/
│   ├── exercise-06/
│   └── exercise-09/
│
└── tests/

# Installation and Setup

# Prerequisites

- Python 3.10 or later
- Node.js and npm
- Git
- Nmap
- Burp Suite Community Edition
- OWASP ZAP
- OSV-Scanner

# 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/SecureScope.git
cd SecureScope
```

# 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

# 3. Install Python dependencies

```bash
python -m pip install -r requirements.txt
```

# 4. Prepare the test application

Clone and configure OWASP Juice Shop by following its official instructions:

https://github.com/juice-shop/juice-shop

Run it locally:

```bash
npm start
```

The application is generally accessible at:

```text
http://localhost:3000
```

# ▶️ Running SecureScope

# Generate SBOM component report

From the project root:

```bash
python src/sbom/analyze_sbom.py
```

# Generate vulnerability report

Ensure the OSV-Scanner JSON output exists in the `scans` directory, then run:

```bash
python src/vulnerability/analyze_vulnerabilities.py
```

# Launch the dashboard

```bash
streamlit run app.py
```

The dashboard will be available at:

```text
http://localhost:8501
```

# Project Outputs

|           Output           |                Description                 |
|----------------------------|--------------------------------------------|
| `juice-shop-sbom.cdx.json` | Generated CycloneDX SBOM                   |
| `nmap_initial.txt`         | Nmap reconnaissance results                |
| `dependency_scan.txt`      | OSV-Scanner output                         |
| `dependency_scan.json`     | Machine-readable vulnerability scan output |
| `sbom_components.csv`      | Extracted software component inventory     |
| `vulnerability_report.csv` | Structured vulnerability findings          |

# Test Environment

The project uses OWASP Juice Shop as an intentionally vulnerable local web application.

**Target:** `http://localhost:3000`

All testing activities are restricted to the local lab environment.

# Project Limitations

- The project currently uses a local test application.
- Python report generation depends on the structure of the scanner output.
- Automated security findings require manual validation.
- The dashboard displays available scan data and does not independently perform security scans.
- Mobile application testing is not currently implemented.

# Ethical and Legal Considerations

SecureScope is intended for educational and authorised security testing purposes.

Only test applications and systems for which explicit permission has been granted. Do not use the toolkit against unauthorised targets.

# Future Enhancements

- API security testing.
- Mobile application security testing using MobSF.
- Enhanced vulnerability severity analysis.
- CVE and CVSS enrichment.
- Automated report generation in HTML and PDF.
- Improved dashboard visualisation.
- Integration with additional vulnerability databases.

# Author

Developed as a cybersecurity portfolio project to explore application security testing, software supply-chain security, SBOM analysis, and Python automation.

