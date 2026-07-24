from skills.applications import Applications
from skills.browser import Browser

apps = Applications()
browser = Browser()


def execute(parsed):

    print(f"[DEBUG] Parsed: {parsed}")

    intent = parsed.get("intent")

    # -----------------------
    # OPEN
    # -----------------------

    if intent == "open":

        target = parsed.get("target")

        if target == "vscode":
            return apps.open_vscode()

        elif target == "notepad":
            return apps.open_notepad()

        elif target == "calculator":
            return apps.open_calculator()

        elif target == "cmd":
            return apps.open_cmd()

        elif target == "explorer":
            return apps.open_explorer()

        result = browser.open_website(target)

        if result:
            return result

    # -----------------------
    # GOOGLE
    # -----------------------

    elif intent == "google":

        return browser.google_search(
            parsed.get("query")
        )

    # -----------------------
    # YOUTUBE
    # -----------------------

    elif intent == "youtube":

        return browser.youtube_search(
            parsed.get("query")
        )

    return None