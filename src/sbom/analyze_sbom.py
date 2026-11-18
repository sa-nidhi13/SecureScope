
import json
import csv
import os

# File paths
SBOM_FILE = "sbom/juice-shop-sbom.cdx.json"
OUTPUT_FILE = "reports/sbom_components.csv"

# Read the SBOM
with open(SBOM_FILE, "r", encoding="utf-8") as file:
    sbom = json.load(file)

# Extract components
components = sbom.get("components", [])

# Store extracted information
component_data = []

for component in components:
    component_data.append({
        "Name": component.get("name", "Unknown"),
        "Version": component.get("version", "Unknown"),
        "Type": component.get("type", "Unknown"),
        "Package URL": component.get("purl", "Not available")
    })

# Export to CSV
os.makedirs("reports", exist_ok=True)

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["Name", "Version", "Type", "Package URL"]
    )
    writer.writeheader()
    writer.writerows(component_data)

# Display summary
print("========== SBOM ANALYSIS ==========")
print("Total components:", len(component_data))
print("CSV report generated:", OUTPUT_FILE)
print("===================================")
