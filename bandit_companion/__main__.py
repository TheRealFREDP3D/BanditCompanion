# bandit_companion/__main__.py
from bandit_companion.app import BanditCompanion

def main():
    """Entry point for Bandit Companion"""
    app = BanditCompanion()
    app.run()

if __name__ == "__main__":
    main()

# bandit_companion/app.py
from textual.app import App
from textual.binding import Binding
from bandit_companion.screens.welcome import WelcomeScreen
from bandit_companion.screens.main_menu import MainMenuScreen

class BanditCompanion(App):
    """Main application class"""
    CSS = """
    Screen {
        align: center middle;
    }
    """

    BINDINGS = [
        Binding("q", "quit", "Quit", show=True),
        Binding("escape", "pop_screen", "Back", show=True),
    ]

    def on_mount(self) -> None:
        """Handle application start"""
        self.push_screen(WelcomeScreen())

    def on_welcome_screen_complete(self) -> None:
        """Switch to main menu after welcome screen"""
        self.push_screen(MainMenuScreen())

# bandit_companion/screens/welcome.py
from textual.screen import Screen
from textual.containers import Container
from textual.widgets import Header, Footer, Static
from textual.app import ComposeResult
import time

class WelcomeScreen(Screen):
    """Welcome screen with ASCII art and loading animation"""

    BINDINGS = []  # No bindings needed for welcome screen

    def compose(self) -> ComposeResult:
        """Create child widgets for the welcome screen"""
        yield Header()
        yield Container(
            Static(self.get_banner(), id="banner"),
            Static("Loading...", id="loading"),
            id="welcome"
        )
        yield Footer()

    def get_banner(self) -> str:
        """Return ASCII art banner"""
        return """
        ╔══════════════════════════════════════════╗
        ║             Bandit Companion             ║
        ║        Master the Command Line!          ║
        ╚══════════════════════════════════════════╝
        """

    def on_mount(self) -> None:
        """Handle screen mount"""
        self.call_later(self.animate_loading)

    async def animate_loading(self) -> None:
        """Animate loading text and transition to main menu"""
        loading = self.query_one("#loading")
        for _ in range(3):
            for dots in [".", "..", "..."]:
                loading.update(f"Loading{dots}")
                await self.sleep(0.3)
        self.app.post_message(self.WelcomeComplete())

    class WelcomeComplete(Message):
        """Message sent when welcome screen is complete"""

# bandit_companion/screens/main_menu.py
from textual.screen import Screen
from textual.containers import Container
from textual.widgets import Header, Footer, Button
from textual.app import ComposeResult

class MainMenuScreen(Screen):
    """Main menu screen with module selection"""

    def compose(self) -> ComposeResult:
        """Create child widgets for the main menu"""
        yield Header()
        yield Container(
            Button("Start Challenge", id="start", variant="primary"),
            Button("Challenge List", id="list"),
            Button("Command History", id="history"),
            Button("Settings", id="settings"),
            Button("Help", id="help"),
            classes="menu-container"
        )
        yield Footer()

    CSS = """
    .menu-container {
        width: 80%;
        height: auto;
        align: center middle;
        background: $panel;
        padding: 2;
    }

    Button {
        width: 100%;
        margin: 1;
    }
    """

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button clicks"""
        button_id = event.button.id
        if button_id == "start":
            # TODO: Implement challenge start
            pass
        elif button_id == "list":
            # TODO: Show challenge list
            pass
        elif button_id == "history":
            # TODO: Show command history
            pass
        elif button_id == "settings":
            # TODO: Show settings
            pass
        elif button_id == "help":
            # TODO: Show help
            pass