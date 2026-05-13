"""Runs the navigation drawer example."""

from examples.nav_drawer.view import App


def main() -> None:
    app = App()
    app.server.start(open_browser=False)


if __name__ == "__main__":
    main()
