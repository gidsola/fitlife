

class Report:
    def __init__(self, report_id, report_date, content=None):
        self.report_id = report_id
        self.report_date = report_date
        self.content = content if content is not None else ""
        
    