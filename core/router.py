from skills.applications import Applications
from skills.browser import Browser


class SkillRouter:

    def __init__(self):
        self.apps = Applications()
        self.browser = Browser()

        self.routes = {
            "open": self.open_skill,
            "google": self.google_skill,
            "youtube": self.youtube_skill,
        }

    def execute(self, parsed):

        intent = parsed.get("intent")

        skill = self.routes.get(intent)

        if skill:
            return skill(parsed)

        return None

    # -------------------------

    def open_skill(self, parsed):

        target = parsed.get("target")

        app_methods = {
            "vscode": self.apps.open_vscode,
            "notepad": self.apps.open_notepad,
            "calculator": self.apps.open_calculator,
            "cmd": self.apps.open_cmd,
            "explorer": self.apps.open_explorer,
        }

        if target in app_methods:
            return app_methods[target]()

        return self.browser.open_website(target)

    # -------------------------

    def google_skill(self, parsed):

        return self.browser.google_search(
            parsed.get("query")
        )

    # -------------------------

    def youtube_skill(self, parsed):

        return self.browser.youtube_search(
            parsed.get("query")
        )