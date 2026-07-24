class SessionState:
    def __init__(self):
        self.last_service = None
        self.last_intent = None

    def update(self, parsed):
        """
        Store the last successful command.
        """

        if parsed.get("intent") == "open":
            self.last_service = parsed.get("target")

        elif parsed.get("intent") in ("youtube", "google"):
            self.last_service = parsed.get("intent")

        self.last_intent = parsed.get("intent")

    def clear(self):
        self.last_service = None
        self.last_intent = None