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
print("Risk score entered:", risk_score)
print("Data type of risk_score:", type(risk_score))



# Output risk

risk_score = int(risk_score)
print("Numeric risk score:", risk_score)
print("Data type now:", type(risk_score))