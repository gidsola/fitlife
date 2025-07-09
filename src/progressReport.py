


import matplotlib.pyplot as plt

class ProgressReport:
    def __init__(self, report_id, report_date):
        self.report_id = report_id
        self.report_date = report_date

    def generate_visual_representation(self, data):
        plt.plot(data)
        plt.title("Fitness Progress")
        plt.xlabel("Time")
        plt.ylabel("Progress")
        plt.show()
        
        
    # def view_progress_report(self, report):
    #     print(f"Progress Report for {self.name} on {report.report_date}: Report ID {report.report_id}")