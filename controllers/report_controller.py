from models.incident_report import IncidentReport
from database.db_setup import SessionLocal


class ReportController:
    def __init__(self):
        self.db = SessionLocal()

    def create_report(self, title, description, impact, actions_taken, severity_level, reported_by):
        new_report = IncidentReport(
            title=title,
            description=description,
            impact=impact,
            actions_taken=actions_taken,
            severity_level=severity_level,
            reported_by=reported_by
        )
        self.db.add(new_report)
        self.db.commit()

    def get_reports(self):
        return self.db.query(IncidentReport).all()

    def get_report_by_id(self, report_id):
        return self.db.query(IncidentReport).filter(IncidentReport.id == report_id).first()

    def delete_report(self, report_id):
        report = self.get_report_by_id(report_id)
        if report:
            self.db.delete(report)
            self.db.commit()

    def update_report(self, report_id, **kwargs):
        report = self.get_report_by_id(report_id)
        if report:
            for key, value in kwargs.items():
                setattr(report, key, value)
            self.db.commit()
