"""View for dialog example."""

from nova.mvvm.trame_binding import TrameBinding
from nova.trame import ThemedApp
from nova.trame.view.components import PersistentDialog
from nova.trame.view.layouts import VBoxLayout
from trame.widgets import client
from trame.widgets import vuetify3 as vuetify

from .view_model import ViewModel


class App(ThemedApp):
    """View for dialog example."""

    def __init__(self) -> None:
        super().__init__()

        self.create_vm()
        # If you forget to call connect, then the application will crash when you attempt to update the view.
        self.view_model.view_state_bind.connect("view_state")

        self.create_ui()

    def create_ui(self) -> None:
        with super().create_ui() as layout:
            with layout.content:
                with VBoxLayout(gap="0.5em", halign="center", valign="center", stretch=True):
                    vuetify.VBtn("Open the Dialog", click=self.view_model.open_dialog)
                    vuetify.VBtn("Open the Persistent Dialog", click=self.view_model.open_persistent_dialog)

                # An important note about working with Trame is that it doesn't automatically listen to changes in
                # Pydantic fields. While our InputField component handles this automatically, when you are using other
                # components to modify fields then you are responsible for ensuring that the field changes are synced to
                # the server properly. Fortunately, Trame provides a mechanism for managing this easily via the
                # DeepReactive component.
                with client.DeepReactive("view_state"):
                    # VDialog will automatically set view_state.dialog_open to False when the user clicks outside of the
                    # dialog. Try moving the VDialog outside of the DeepReactive context manager and see how it changes
                    # the behavior when attempting to close the dialog.
                    with vuetify.VDialog(v_model="view_state.dialog_open", width=400):
                        with vuetify.VCard(classes="pa-4"):
                            vuetify.VCardTitle("Dialog")
                            vuetify.VCardSubtitle("Click anywhere outside of the dialog to dismiss.")

                    # PersistentDialog will automatically set view_state.dialog_open to False when the user uses the
                    # escape key but not when they click outside of the dialog.
                    with PersistentDialog(
                        v_model="view_state.persistent_dialog_open",
                        # This is a default, but if you want to fully block closing the dialog you can set it to False.
                        close_on_escape=True,
                        width=400,
                    ):
                        with vuetify.VCard(classes="pa-4"):
                            vuetify.VCardTitle("Dialog")
                            vuetify.VCardSubtitle("Use the escape key to dismiss this dialog.")

    def create_vm(self) -> None:
        binding = TrameBinding(self.state)

        self.view_model = ViewModel(binding)
