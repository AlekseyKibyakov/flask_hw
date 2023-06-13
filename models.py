from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, DateTime, Integer, func, Text

engine = create_engine('postgresql://postgres:1@127.0.0.1:5432/flask_hw')
Session = sessionmaker(bind=engine)
Base = declarative_base()

Base.metadata.create_all(bind=engine)

class Announcement(Base):
    __tablename__ = 'announcement'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    creation_datetime = Column(DateTime, server_default=func.now())
    owner = Column(String, nullable=False)
    

