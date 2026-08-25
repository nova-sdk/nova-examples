"""View model implementation for navigation drawer example."""

from nova.mvvm.interface import BindingInterface
from pydantic import BaseModel, Field


class ViewState(BaseModel):
    """Pydantic model for holding view state."""

    input_text: str = Field(default="", title="Text Area")


class ViewModel:
    """View model implementation for navigation drawer example."""

    def __init__(self, binding: BindingInterface) -> None:
        self.view_state = ViewState()
        self.view_state_bind = binding.new_bind(self.view_state)
