import os
import subprocess


class Applications:

    def open_vscode(self):
        subprocess.Popen("code.cmd", shell=True)
        return "Opening VS Code."

    def open_notepad(self):
        subprocess.Popen("notepad")
        return "Opening Notepad."

    def open_calculator(self):
        subprocess.Popen("calc")
        return "Opening Calculator."

    def open_cmd(self):
        subprocess.Popen(
            ["cmd.exe"],
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )
        return "Opening Command Prompt."

    def open_explorer(self):
        subprocess.Popen("explorer")
        return "Opening File Explorer."