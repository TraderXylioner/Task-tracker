import enum
from sqlalchemy import String, Integer, Enum
from sqlalchemy.orm import mapped_column, Mapped, relationship
from . import Base


class UserRole(enum.Enum):
    ADMIN = "Admin"
    MANAGER = "Manager"
    EXECUTOR = "Executor"


class UserModel(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(127), unique=True)
    role: Mapped[Enum] = mapped_column(Enum(UserRole), default=UserRole.EXECUTOR)

    tasks = relationship('TaskModel', secondary="task_executors", back_populates="executor")
