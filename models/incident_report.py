from sqlalchemy import Column, Integer, String, DateTime
import datetime
from database.db_setup import Base


class IncidentReport(Base):
    __tablename__ = 'incident_reports'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    date_time = Column(DateTime, default=datetime.datetime.utcnow)
    impact = Column(String)
    actions_taken = Column(String)
    severity_level = Column(String)
    reported_by = Column(String)
