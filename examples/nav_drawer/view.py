"""View for navigation drawer example."""

from nova.mvvm.trame_binding import TrameBinding
from nova.trame import ThemedApp
from nova.trame.view.components import InputField

from .view_model import ViewModel


class App(ThemedApp):
    """View for navigation drawer example."""

    def __init__(self) -> None:
        super().__init__()

        self.create_vm()
        # If you forget to call connect, then the application will crash when you attempt to update the view.
        self.view_model.view_state_bind.connect("view_state")

        self.create_ui()

    def create_ui(self) -> None:
        with super().create_ui() as layout:
            with super().add_drawer(open=True, width=400):
                InputField(v_model="view_state.input_text", no_resize=True, type="textarea")

            with layout.content:
                pass

    def create_vm(self) -> None:
        binding = TrameBinding(self.state)

        self.view_model = ViewModel(binding)
