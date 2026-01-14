"""View for form disabling example."""

from nova.mvvm.trame_binding import TrameBinding
from nova.trame import ThemedApp
from nova.trame.view.components import InputField
from nova.trame.view.layouts import VBoxLayout
from trame.widgets import client
from trame.widgets import vuetify3 as vuetify

from .model import Model
from .view_model import ViewModel


class App(ThemedApp):
    """View for form disabling example."""

    def __init__(self) -> None:
        super().__init__()

        self.create_vm()
        # If you forget to call connect, then the application will crash when you attempt to update the view.
        self.view_model.form_data_bind.connect("data")
        self.view_model.view_state_bind.connect("state")

        self.create_ui()

    def create_ui(self) -> None:
        with super().create_ui() as layout:
            # This instructs the user interface to reset itself to the most recent valid state when a browser connects
            # to the tool or the browser is refreshed. This is not appropriate for all situations, so it is not a
            # default behavior at this time. You can disable this line and then refresh your browser while the user
            # interface is in an error state to see the difference between the two behaviors.
            client.ClientTriggers(mounted=self.view_model.init_view)

            with layout.pre_content:
                vuetify.VBanner(
                    "The form is in an error state.",
                    v_if="state.errors?.length > 0",
                    color="error",
                    icon="mdi-close",
                )

            with layout.content:
                with VBoxLayout(classes="mb-2"):
                    InputField(v_model="data.wavelength")
                with VBoxLayout(halign="center"):
                    vuetify.VBtn("{{ state.button_text }}", disabled=("state.errors?.length > 0",))

            with layout.post_content:
                vuetify.VAlert("{{ state.errors }}", v_if="state.errors?.length > 0", color="error")

    def create_vm(self) -> None:
        binding = TrameBinding(self.state)

        model = Model()
        self.view_model = ViewModel(model, binding)
