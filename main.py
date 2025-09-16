"""
windows_installer_bot.py

A simple Python structure simulating a Windows installer bot for DigitalOcean VPS Droplets.
When run, it prints a message directing users to the actual Telegram bot @WinDeployBot.

Usage:
    python windows_installer_bot.py
"""

class WindowsInstallerBot:
    def __init__(self):
        self.bot_name = "@WinDeployBot"

    def run(self):
        print(f"Go to the bot {self.bot_name}")

if __name__ == "__main__":
    bot = WindowsInstallerBot()
    bot.run()
