import enum
from sqlalchemy import String, Integer, ForeignKey, CheckConstraint, Enum
from sqlalchemy.orm import mapped_column, Mapped, relationship
from . import Base


class TaskStatus(enum.Enum):
    TODO = "TODO"
    IN_PROGRESS = "In progress"
    DONE = "Done"


class TaskModel(Base):
    __tablename__ = 'task'
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(127))
    description: Mapped[str] = mapped_column(String(2047), nullable=True)
    creator_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id'), nullable=False)
    status: Mapped[Enum] = mapped_column(Enum(TaskStatus), default=TaskStatus.TODO)
    priority: Mapped[int] = mapped_column(Integer, CheckConstraint('priority > 0 AND priority < 11'), default=1)

    executors = relationship('UserModel', secondary="task_executors", back_populates="task")
