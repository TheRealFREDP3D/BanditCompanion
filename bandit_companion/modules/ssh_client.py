# bandit_companion/modules/ssh_client.py
import paramiko
from dataclasses import dataclass
from typing import Optional

@dataclass
class SSHSession:
    """SSH session information"""
    level: int
    client: paramiko.SSHClient
    channel: Optional[paramiko.Channel] = None

class SSHClient:
    """SSH client for Bandit challenges"""
    def __init__(self):
        self.current_session: Optional[SSHSession] = None

    def connect(self, level: int, password: str) -> bool:
        """Connect to specified Bandit level"""
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(
                'bandit.labs.overthewire.org',
                port=2220,
                username=f'bandit{level}',
                password=password
            )
            self.current_session = SSHSession(level=level, client=client)
            return True
        except Exception as e:
            print(f"Connection failed: {str(e)}")
            return False

    def execute(self, command: str) -> str:
        """Execute command on current session"""
        if not self.current_session:
            return "Not connected to any level"
        
        try:
            stdin, stdout, stderr = self.current_session.client.exec_command(command)
            return stdout.read().decode()
        except Exception as e:
            return f"Command execution failed: {str(e)}"

# bandit_companion/modules/challenges.py
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Challenge:
    """Challenge information"""
    level: int
    title: str
    description: str
    hints: List[str]
    completed: bool = False

class ChallengeManager:
    """Manage Bandit challenges"""
    def __init__(self):
        self.challenges: List[Challenge] = self._init_challenges()
        self.current_level: Optional[int] = None

    def _init_challenges(self) -> List[Challenge]:
        """Initialize challenge data"""
        return [
            Challenge(
                level=0,
                title="Level 0",
                description="The goal of this level is to log into the game using SSH.",
                hints=["The host is 'bandit.labs.overthewire.org'", "The port is 2220"]
            ),
            Challenge(
                level=1,
                title="Level 0 → Level 1",
                description="The password for the next level is stored in a file called readme.",
                hints=["Use the 'ls' command to list files", "Use 'cat' to read file contents"]
            ),
            # Add more challenges here
        ]

    def get_challenge(self, level: int) -> Optional[Challenge]:
        """Get challenge information by level"""
        for challenge in self.challenges:
            if challenge.level == level:
                return challenge
        return None

    def mark_completed(self, level: int) -> None:
        """Mark challenge as completed"""
        challenge = self.get_challenge(level)
        if challenge:
            challenge.completed = True