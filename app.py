
import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="SecureScope",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ SecureScope")
st.subheader("Application Security & SBOM Analysis Dashboard")

st.markdown("---")

# Load SBOM components
sbom_file = "reports/sbom_components.csv"
vuln_file = "reports/vulnerability_report.csv"

if os.path.exists(sbom_file):
    sbom = pd.read_csv(sbom_file)
else:
    sbom = pd.DataFrame()

if os.path.exists(vuln_file):
    vulnerabilities = pd.read_csv(vuln_file)
else:
    vulnerabilities = pd.DataFrame()

# Summary metrics
total_components = len(sbom)
total_vulnerabilities = len(vulnerabilities)

col1, col2, col3 = st.columns(3)

col1.metric("Total Components", total_components)
col2.metric("Vulnerabilities Found", total_vulnerabilities)
col3.metric(
    "Assessment Status",
    "Completed" if total_components else "Pending"
)

st.markdown("---")

# SBOM section
st.header("📦 Software Components")

if not sbom.empty:
    st.dataframe(sbom, use_container_width=True)
else:
    st.info("No SBOM component data available.")

# Vulnerability section
st.header("🔍 Vulnerability Analysis")

if not vulnerabilities.empty:
    st.dataframe(vulnerabilities, use_container_width=True)

    st.subheader("Vulnerability Distribution by Package")

    package_counts = (
        vulnerabilities["Package"]
        .value_counts()
        .reset_index()
    )
    package_counts.columns = ["Package", "Count"]

    st.bar_chart(
        package_counts.set_index("Package")
    )
else:
    st.success("No vulnerability records found in the report.")

st.markdown("---")

st.caption("SecureScope | Application Security Assessment Toolkit")
