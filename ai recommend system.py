
# house_recommender.py
# AI-Based Living House Recommender
# This program recommends a type of house based on the user's monthly salary and marital status.
print("=== AI-BASED LIVING HOUSE RECOMMENDER ===")
# Input details
name = input("Enter Full Name: ")
salary = float(input("Enter Monthly Salary (KES): "))
marital_status = input("Enter Marital Status (Single/Married): ")

# Validate salary
if salary < 0:
    print("Error: Salary cannot be negative.")
    exit()

# Decision logic
if marital_status == "Single":
    if salary < 25000:
        house_type = "Single Room"
        rent = 5000
        remarks = "Affordable option for low income"
    elif 25000 <= salary <= 50000:
        house_type = "Bedsitter"
        rent = 10000
        remarks = "Ideal for moderate earners"
    else:
        house_type = "One Bedroom"
        rent = 20000
        remarks = "Comfortable living for high income"

elif marital_status == "Married":
    if salary < 40000:
        house_type = "Bedsitter"
        rent = 10000
        remarks = "Modest starter home"
    elif 40000 <= salary <= 80000:
        house_type = "One Bedroom"
        rent = 20000
        remarks = "Standard family setup"
    else:
        house_type = "Two Bedroom"
        rent = 35000
        remarks = "Spacious for family comfort"
else:
    print("Error: Invalid marital status. Please enter 'Single' or 'Married'.")
    exit()

# Display result
print("\n--- Housing Recommendation Result ---")
print("Client Name:", name)
print("Monthly Salary: KES", salary)
print("Marital Status:", marital_status)
print("Recommended House Type:", house_type)
print("Estimated Monthly Rent: KES", rent)
print("Remarks:", remarks)
#alternative dispay method using f string

#f string roles as it allows embedding expressions inside string literals, using curly braces {}.
print("\n---Second method Housing Recommendation Result ---")
print(f"Client Name: {name}")
print(f"Monthly Salary: KES {salary}")
print(f"Marital Status: {marital_status}")
print(f"Recommended House Type: {house_type}")
print(f"Estimated Monthly Rent: KES {rent}")
print(f"Remarks: {remarks}")

print("\nThank you for using the AI-Based Living House Recommender!")
