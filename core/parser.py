class CommandParser:

    FILLER_WORDS = {
          "please",
          "can",
          "could",
          "would",
          "you",
          "my",
          "the",
          "a",
          "an",
          "for",
          "me"
    }

    OPEN_WORDS = {
        "open",
        "launch",
        "start",
        "run",
    }

    GOOGLE_WORDS = {
        "search google for",
        "google",
        "look up",
        "find",
    }

    YOUTUBE_WORDS = {
        "search youtube for",
        "youtube",
    }

    def normalize(self, command):

        words = command.lower().split()

        cleaned = []

        for word in words:
            if word not in self.FILLER_WORDS:
               cleaned.append(word)

        return " ".join(cleaned)

    def parse(self, command):

        command = self.normalize(command)

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