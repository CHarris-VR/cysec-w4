# Week 2 - Working with Variables
# Author: Curtis Harris

analyst_name = input("Enter your name: ")
system_name = input("Enter system hostname: ")
criticality = input("Enter system criticality (low, medium, high): ")

print("--- Asset Information ---")
print("Analyst:", analyst_name)
print("System:", system_name)
print("Criticality:", criticality)

# Input risk number

risk_score = input("Enter a risk score (1-10): ")

# Output risk logic and convernt from string to int

risk_score = int(risk_score)
print("Numeric risk score:", risk_score)
print("Data type now:", type(risk_score))

# Decision making logic addition based on risk score

if risk_score >= 8:
    print("[*] High-Risk Asset – prioritize review.")
elif risk_score >= 5:
    print("[!] Medium-Risk Asset – monitor closely.")
else:
    print("[+] Low-Risk Asset – standard monitoring.")