# Week 2 Challenge
# Author - Curtis Harris


# Collect inputs from user

analyst_name = input("Enter your name: ")
Department = input("Enter your Department: ")
system_name = input("Enter system hostname: ")
criticality = input("Enter system criticality (low, medium, high): ")
risk = input("Enter the Risk Score(1-10): ")
risk_int = int(risk)

print ("=" * 40)
print ("Cyber Defense - Asset Report")
print ("=" * 40)
print (" ")

# Print information from input data

print("Analyst: ", analyst_name)
print("Department: ", Department)
print("System Name: ", system_name)
print("Criticality: ", criticality)
print("Risk Factor: ", risk)
print (" ")

# Decision making logic addition based on risk score
# Risk Factor number determins color of print out:
# Red - high, Yellow - medium, white - low

print ("=" * 40)

if risk_int >= 8:
    print("\033[31m" "High-Risk Asset – prioritize review.")
elif risk_int >= 5:
    print("\033[33m" "Medium-Risk Asset – monitor closely.")
else:
    print("\033[37m" "Low-Risk Asset – standard monitoring.")

print ("=" * 40)