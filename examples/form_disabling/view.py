"""View for form disabling example."""

from nova.mvvm.trame_binding import TrameBinding
from nova.trame import ThemedApp
from nova.trame.view.components import InputField
from nova.trame.view.layouts import GridLayout, VBoxLayout
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

        self.create_ui()

    def create_ui(self) -> None:
        self.set_theme("CompactTheme")

        with super().create_ui() as layout:
            with layout.pre_content:
                vuetify.VBanner(
                    "The form is in an error state.",
                    v_if="errors.data?.length > 0",
                    color="error",
                    icon="mdi-close",
                )

            with layout.content:
                with GridLayout(classes="mb-2", columns=2, gap="0.5em"):
                    InputField(v_model="data.num_banks")
                    InputField(v_model="data.wavelength")
                with VBoxLayout(halign="center"):
                    vuetify.VBtn(
                        "{{ errors.data?.length > 0 ? 'Errors Present' : 'No Errors' }}",
                        disabled=("errors.data?.length > 0",),
                    )

            with layout.post_content:
                vuetify.VAlert("{{ errors.data }}", v_if="errors.data?.length > 0", color="error")

    def create_vm(self) -> None:
        binding = TrameBinding(self.state)

        model = Model()
        self.view_model = ViewModel(model, binding)
