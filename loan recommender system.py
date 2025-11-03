
print("===loan system RECOMMENDER ===")
# Input details
name = input("Enter applicant Name: ")
fuliza_limit= float(input("Enter fuliza limit: "))
monthly_salary = float(input("Enter Monthly salary: "))
CRB_status =input("enter crb satus(listed/not listed):")

# Validate monthly salary
if monthly_salary <0:
    print("Error: Salary cannot be negative.")
    exit()
#validate fuliza limit
if fuliza_limit <0:
  print("error:fuliza limit cannot be negative.")
  exit()
# Decision logic
if monthly_salary >50000 and fuliza_limit >10000:
        loan_category="platinum loan"
        maximum_loan_limit= 1000000
        remarks = "excellent borrower"
elif 30000 <= monthly_salary<= 50000 and 5000<=fuliza_limit<=10000:
        loan_category = "gold loan"
        maximum_loan_limit = 500000
        remarks = "reliable borrower"
elif monthly_salary<=30000 and fuliza_limit<=5000:
        loan_category = "silver loan"
        maximum_loan_limit = 100000
        remarks = "fair borrower"

else:
     loan_category = "not eligible"
maximum_loan_limit= 0
remarks = "crb issues detected"

# Display result
print("\n--- loan recommender system ---")
print("applicant Name:", name)
print("Monthly Salary: KES",monthly_salary)
print("fuliza limit:", fuliza_limit)
print("loan category:", loan_category)
print("maximum loan limit:",maximum_loan_limit )
print("crb status", CRB_status)
print("Remarks:", remarks)

print("\nThank you for using loan recommender system!")
