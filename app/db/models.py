from sqlalchemy import Column  , String , UUID  , Enum , DateTime , Text
from .database_conn import Base
from sqlalchemy.dialects.postgresql import UUID , JSONB
from datetime import datetime , timezone
import uuid
import enum



class User(Base):
    __tablename__ = "users"

    class Status_type(str , enum.Enum):
        PENDING = "pending"
        ACTIVE ="active"
        DEACTIVATED = "deactivated"


    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    password = Column(Text, nullable=False)
    status =Column(Enum(Status_type) , nullable=False , default=Status_type.PENDING)
    created_at = Column(DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc))
