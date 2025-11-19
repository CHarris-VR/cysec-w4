# Testing syntax for color

print("\033[31m" "Testing")

# Creating system for asset_report.py 

risk = input("Enter the Risk Score(1-10): ")
risk_int = int(risk)

if risk_int >= 8:
    print("\033[31m" "High-Risk Asset – prioritize review.")
elif risk_int >= 5:
    print("\033[33m" "Medium-Risk Asset – monitor closely.")
else:
    print("\033[37m" "Low-Risk Asset – standard monitoring.")