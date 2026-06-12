# Certificate Verification System

certificates = {
    "CERT101": "Kavin Kumar",
    "CERT102": "Priya",
    "CERT103": "Arun"
}

print("===== Certificate Verification System =====")

certificate_id = input("Enter Certificate ID: ")

if certificate_id in certificates:
    print("\nCertificate Verified ✓")
    print("Certificate ID:", certificate_id)
    print("Holder Name:", certificates[certificate_id])
else:
    print("\nCertificate Not Found ✗")