from pydantic import BaseModel, Field
from typing import Optional, Any



class ResourseResponse(BaseModel):
    id: int
    project_tasks_resource_id: int
    volume: str
    cost: str
    batch_number: Optional[str] = Field(default=None)
    batch_parent_request_id: Optional[int] = Field(default=None)
    is_over_budget: bool
    created_at: int  # Unix timestamp
    updated_at: int  # Unix timestamp
    user_id: int
    needed_at: int  # Unix timestamp
    created_by: int


class ResourseRequest(BaseModel):
    project_tasks_resource_id: int = Field(..., description="Ресурс")
    volume: Any = Field(..., description="Количество")  # Must be greater than 0
    cost: Any = Field(..., description="Цена, шт")  # Must be greater than 0
    needed_at: Any = Field(..., description="Понадобится  только для чтения")
    batch_number: Optional[int] = Field(default=None, description="Номер партии")
    batch_parent_request_id: Optional[int] = Field(default=None, description="Идентификатор изначального запроса")
    is_over_budget: Optional[int] = Field(default=0, description="Сверх бюджета")