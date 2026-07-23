class CommandParser:

    OPEN_WORDS = [
        "open",
        "launch",
        "start",
        "run",
    ]

    GOOGLE_WORDS = [
        "search google for",
        "google",
        "look up",
        "find",
    ]

    YOUTUBE_WORDS = [
        "search youtube for",
        "youtube",
    ]

    def parse(self, command):

        command = command.lower().strip()

        # ---------- OPEN ----------
        for word in self.OPEN_WORDS:

            if command.startswith(word):

                target = command.replace(word, "", 1).strip()

                return {
                    "intent": "open",
                    "target": target
                }

        # ---------- GOOGLE ----------
        for word in self.GOOGLE_WORDS:

            if command.startswith(word):

                query = command.replace(word, "", 1).strip()

                return {
                    "intent": "google",
                    "query": query
                }

        # ---------- YOUTUBE ----------
        for word in self.YOUTUBE_WORDS:

            if command.startswith(word):

                query = command.replace(word, "", 1).strip()

                return {
                    "intent": "youtube",
                    "query": query
                }

        return {
            "intent": "chat",
            "text": command
        }