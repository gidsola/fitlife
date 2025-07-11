
import matplotlib.pyplot as plt
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.user import User
    
from src.report import Report

class ReportManager:
    def __init__(self, user: 'User'):
        self.user = user
        # self.report_id = report_id
        # self.report_date = report_date
        
    def generate_progress_report(self, report_id, report_date):
        report = Report(report_id, report_date)
        data = [activity.calories_burned for activity in self.activities]
        report.generate_visual_representation(data)
        return report

    def generate_visual_representation(self, data):
        plt.plot(data)
        plt.title("Fitness Progress")
        plt.xlabel("Activity Index")
        plt.ylabel("Calories Burned")
        plt.show()
        
        
    def share_progress_report(self, report):
        self.share_progress_report(report)

        
    # def view_progress_report(self, report):
    #     print(f"Progress Report for {self.name} on {report.report_date}: Report ID {report.report_id}")
    
def showProgressReportMenu(user):
        report_id = 1
        report_date = input("Report date (YYYY-MM-DD): ")
        report = Report(report_id=report_id, report_date=report_date)
        # user.view_progress_report(report)
        report.generate_visual_representation([1, 2, 3, 4, 5])
        input("Press Enter to continue...")