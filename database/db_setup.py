from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import DB_PATH

Base = declarative_base()
engine = create_engine(f'sqlite:///{DB_PATH}')
SessionLocal = sessionmaker(bind=engine)


def init_db():
    import models.incident_report
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()