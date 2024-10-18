"""Entry point for Bandit Companion"""
from textual.app import App
from textual.binding import Binding
from textual.widgets import Header, Footer, Static
from textual.containers import Container
from textual.screen import Screen

class WelcomeScreen(Screen):
    """Welcome screen with ASCII art and loading animation"""
    
    def compose(self):
        yield Header()
        yield Container(
            Static(self.get_banner(), id="banner"),
            Static("Loading...", id="loading"),
            id="welcome"
        )
        yield Footer()

    def get_banner(self) -> str:
        return """
╔══════════════════════════════════════════╗
║             Bandit Companion             ║
║        Master the Command Line!          ║
╚══════════════════════════════════════════╝
        """

class BanditCompanion(App):
    """Main application class"""
    
    CSS = """
    Screen {
        align: center middle;
    }

    #welcome {
        width: 80%;
        height: auto;
        border: solid green;
        align: center middle;
        padding: 1;
    }

    #banner {
        content-align: center middle;
        width: 100%;
        height: auto;
    }

    #loading {
        text-align: center;
    }
    """

    BINDINGS = [
        Binding("q", "quit", "Quit", show=True),
    ]

    def on_mount(self):
        """Called when app starts"""
        self.push_screen(WelcomeScreen())

def main():
    """Run the application"""
    app = BanditCompanion()
    app.run()

if __name__ == "__main__":
    main()