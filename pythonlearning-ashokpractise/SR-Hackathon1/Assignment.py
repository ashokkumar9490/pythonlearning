import csv
 
class InsurancePolicy:
    def __init__(self, policy_holder_name, policy_type, coverage_amount):
        self.policy_holder_name = policy_holder_name
        self.policy_type = policy_type
        self.coverage_amount = coverage_amount
 
    def calculate_premium(self):
        raise NotImplementedError("premium class is not implemented")
 
class CarInsurance(InsurancePolicy):
    def __init__(self, policy_holder_name, policy_type, coverage_amount, year_of_manufacture, driving_record):
        super().__init__(policy_holder_name, policy_type, coverage_amount)
        self.year_of_manufacture = int(year_of_manufacture)
        self.driving_record = driving_record
 
    def calculate_premium(self):
        base_premium = self.coverage_amount * 0.1
        age_factor = 0.1 if (self.year_of_manufacture) < 2010 else 0
        driving_record_factor = 0.2 if self.driving_record != "Clean" else 0
        final_premium = base_premium * (1 + age_factor + driving_record_factor)
        return final_premium
 
def calculate_and_write_premiums(policies, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Policy Holder', 'Policy Type', 'Premium'])
            for policy in policies:
                try:
                    premium = policy.calculate_premium()
                    writer.writerow([policy.policy_holder_name, policy.policy_type, premium])
                except Exception as e:
                    print(f"Error premium calculation for {policy.policy_holder_name}: {e}")
 
def main():
    policies = [
        CarInsurance("John Doe", "Car", 50000, "2020", "Clean"),
        CarInsurance("Mark Jones", "Car", 30000, "2015", "Accidents")
    ]
    calculate_and_write_premiums(policies, "output.csv")
 
if __name__ == "__main__":
    main()