from pydantic import BaseModel
from datetime import date

class SalesPredictForm(BaseModel):
    store: int
    date: date
    promo: bool
    state_holiday: bool
    school_holiday: bool
    is_open: bool