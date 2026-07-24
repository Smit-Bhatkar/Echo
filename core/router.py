from skills.applications import Applications
from skills.browser import Browser
from core.session import session


class SkillRouter:

    def __init__(self):
        self.apps = Applications()
        self.browser = Browser()

        self.routes = {
            "open": self.open_skill,
            "google": self.google_skill,
            "youtube": self.youtube_skill,
            "search": self.search_skill,
}

    def execute(self, parsed):

        intent = parsed.get("intent")

        skill = self.routes.get(intent)

        if skill:
            return skill(parsed)

        return None

    # -------------------------

    def update_session(self, service=None, skill=None, query=None):
            session.set_service(service)
            session.set_skill(skill)
            session.set_query(query)
            
            print("----- SESSION -----")
            print(session.get_service())
            print(session.get_skill())
            print(session.get_query())
            print("-------------------")

    def open_skill(self, parsed):

        target = parsed.get("target")

        app_methods = {
            "vscode": self.apps.open_vscode,
            "notepad": self.apps.open_notepad,
            "calculator": self.apps.open_calculator,
            "cmd": self.apps.open_cmd,
            "explorer": self.apps.open_explorer,
        }

        method = app_methods.get(target)

        if method:
            result = method()
        else:
            result = self.browser.open_website(target)

        if result:
            self.update_session(
                service=target,
                skill="open",
                query=None
            )

        return result

    # -------------------------

    def google_skill(self, parsed):

        query = parsed.get("query")

        result = self.browser.google_search(query)

        if result:
            self.update_session(
                service="google",
                skill="google",
                query=query
            )   

        return result
    # -------------------------

    def youtube_skill(self, parsed):

        query = parsed.get("query")

        result = self.browser.youtube_search(query)

        if result:
            self.update_session(
                service="youtube",
                skill="youtube",
                query=query
            )

        return result


    def search_skill(self, parsed):

        service = session.get_service()

        if service == "youtube":
            return self.youtube_skill(parsed)

        elif service == "google":
            return self.google_skill(parsed)

        # Default search engine
        return self.google_skill(parsed)