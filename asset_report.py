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
    print("\033[31mHigh-Risk Asset – prioritize review.\033[0m")
elif risk_int >= 5:
    print("\033[33mMedium-Risk Asset – monitor closely.\033[0m")
else:
    print("\033[37mLow-Risk Asset – standard monitoring.\033[0m")

print ("=" * 40)
print (" ")

# Import time of report generation 
import datetime 

report_time = datetime.datetime.now()
print("Report Generated: ", report_time)
print ("=" * 40)