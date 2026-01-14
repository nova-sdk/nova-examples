"""Model implementation for form disabling example."""

from pydantic import BaseModel, Field


class FormData(BaseModel):
    """Pydantic model for the form data."""

    wavelength: float = Field(default=0.1, ge=0.1, le=1.0, title="Wavelength [0.1, 1.0]")


class Model:
    """Model implementation for form disabling example."""

    def __init__(self) -> None:
        self.form = FormData()
