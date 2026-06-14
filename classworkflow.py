class Workflow:
    def __init__(self, name):
        self.name = name
        self.steps = []

    def add_step(self, step_name, action):
        self.steps.append((step_name, action))

    def run(self):
        print(f"\nRunning Workflow: {self.name}")
        print("-" * 30)

        for step_name, action in self.steps:
            print(f"Executing: {step_name}")
            action()

        print("-" * 30)
        print("Workflow Completed!")


# Sample Actions
def send_email():
    print("📧 Email sent successfully.")

def generate_report():
    print("📊 Report generated.")

def backup_data():
    print("💾 Data backed up.")

# Create Workflow
workflow = Workflow("Daily Automation")

workflow.add_step("Generate Report", generate_report)
workflow.add_step("Send Email", send_email)
workflow.add_step("Backup Data", backup_data)

# Run Workflow
workflow.run()