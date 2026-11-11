
from datetime import date
from decimal import Decimal
from pydantic import BaseModel, Field, model_validator


class TripRequest(BaseModel):
    origin: str | None = None

    destinations: list[str] = Field(min_length=1)

    start_date: date | None = None
    end_date: date | None = None

    budget: Decimal | None = Field(default=None, ge=0)
    currency: str = "MYR"

    travelers: int = Field(default=1, ge=1)

    interests: list[str] = Field(default_factory=list)

    travel_style: str = "balanced"

    @model_validator(mode="after")
    def validate_dates(self):
        if self.start_date and self.end_date:
            if self.end_date < self.start_date:
                raise ValueError(
                    "end_date cannot be earlier than start_date"
                )

        return self
