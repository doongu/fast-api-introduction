from sqlalchemy.orm import declarative_base
from sqlalchemy import Boolean, Column, Integer, String

Base = declarative_base()

class ToDo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, index=True)
    contents = Column(String(256), nullable=False)
    is_done = Column(Boolean, nullable=False)

    def __repr__(self):
        return f"Todo(id={self.id}, contents={self.contents}, is_done={self.is_done})"