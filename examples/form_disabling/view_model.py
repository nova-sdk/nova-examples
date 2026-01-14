"""View model implementation for form disabling example."""

from typing import Any, Dict, List

from nova.mvvm.interface import BindingInterface
from pydantic import BaseModel, Field, computed_field

from .model import Model


class ViewState(BaseModel):
    """View state Pydantic model."""

    errors: List[str] = Field(default=[])

    @computed_field
    @property
    def button_text(self) -> str:
        return "Errors Present, Button Disabled" if self.errors else "No Errors, Button Enabled"


class ViewModel:
    """View model implementation for form disabling example."""

    def __init__(self, model: Model, binding: BindingInterface) -> None:
        self.model = model
        self.view_state = ViewState()

        # self.on_update is called any time the view updates the binding.
        self.form_data_bind = binding.new_bind(self.model.form, callback_after_update=self.on_update)
        self.view_state_bind = binding.new_bind(self.view_state)

    def on_update(self, results: Dict[str, Any]) -> None:
        self.view_state.errors = []
        errors = results.get("errored", [])
        for error in errors:
            self.view_state.errors.append(f"{error} is invalid")

        self.update_view_state()

    def update_form_data(self) -> None:
        # This will fail if you haven't called connect on the binding!
        self.form_data_bind.update_in_view(self.model.form)

    def update_view_state(self) -> None:
        # This will fail if you haven't called connect on the binding!
        self.view_state_bind.update_in_view(self.view_state)

    def init_view(self) -> None:
        self.view_state.has_errors = False

        self.update_form_data()
        self.update_view_state()
