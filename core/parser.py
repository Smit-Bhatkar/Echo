import re

SERVICES = {
    # ---------- Websites ----------
    "youtube": {
        "intent": "youtube",
        "aliases": ["youtube", "yt", "you tube"]
    },

    "google": {
        "intent": "google",
        "aliases": ["google"]
    },

    "github": {
        "intent": "open",
        "aliases": ["github", "git hub", "gh"]
    },

    "linkedin": {
        "intent": "open",
        "aliases": ["linkedin", "linked in"]
    },

    "gmail": {
        "intent": "open",
        "aliases": ["gmail", "google mail"]
    },

    # ---------- Applications ----------
    "vscode": {
        "intent": "open",
        "aliases": [
            "vscode",
            "vs code",
            "visual studio code",
            "visual studio",
            "code"
        ]
    },

    "calculator": {
        "intent": "open",
        "aliases": [
            "calculator",
            "calc"
        ]
    },

    "notepad": {
        "intent": "open",
        "aliases": [
            "notepad"
        ]
    },

    "cmd": {
        "intent": "open",
        "aliases": [
            "cmd",
            "command prompt",
            "terminal"
        ]
    },

    "explorer": {
        "intent": "open",
        "aliases": [
            "explorer",
            "file explorer"
        ]
    }
}

class CommandParser:

    STOP_WORDS = {
        "please",
        "could",
        "would",
        "can",
        "you",
        "me",
        "my",
        "the",
        "a",
        "an",
        "to",
        "for",
        "of",
        "on",
        "at",
        "in",
        "is",
        "it",
        "i",
        "want"
}

    OPEN_WORDS = {
        "open",
        "launch",
        "start",
        "run",
        "execute",
        "load",
    }

    SEARCH_WORDS = {
        "search",
        "find",
        "look",
        "google",
        "lookup",
    }

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
        "me",
    }

    WAKE_WORDS = {
        "echo",
        "hey",
        "hello",
        "hi",
    }

    CONNECTOR_WORDS = {
        "for",
        "on",
        "in",
        "at",
        "to",
    }

    CORRECTIONS = {
        "vs code": "vscode",
        "visual studio code": "vscode",
        "git hub": "github",
        "linked in": "linkedin",
        "you tube": "youtube",
        "command prompt": "cmd",
        "file explorer": "explorer",
    }

    def find_service(self, command):
        """
        Returns:
            canonical_name, service_info
        """

        command_words = command.split()

        for name, info in SERVICES.items():

            for alias in info["aliases"]:

                alias_words = alias.split()

                # Slide through the command and compare whole words
                for i in range(len(command_words) - len(alias_words) + 1):

                    if command_words[i:i + len(alias_words)] == alias_words:
                        print(f"[SERVICE] Matched '{alias}' -> {name}")
                        return name, info

        return None, None

    def tokenize(self, command):
        return command.split()

    def detect_intent(self, command, words):

        service, info = self.find_service(command)

        if service:
            return info["intent"]

        if any(word in self.OPEN_WORDS for word in words):
            return "open"

        if any(word in self.SEARCH_WORDS for word in words):
            return "search"

        return "chat"

    def extract_argument(self, intent, words):

    # -----------------------------
    # OPEN commands
    # -----------------------------
        if intent == "open":

            for name, info in SERVICES.items():

                for alias in info["aliases"]:

                    alias_words = alias.split()

                    # Exact alias match
                    if words == alias_words:
                        return name

                    # Alias appears inside sentence
                    for i in range(len(words) - len(alias_words) + 1):

                        if words[i:i + len(alias_words)] == alias_words:
                            return name

            return ""

    # -----------------------------
    # GOOGLE / YOUTUBE searches
    # -----------------------------
        query = []

        skip_words = (
            self.SEARCH_WORDS
            | self.OPEN_WORDS
            | self.CONNECTOR_WORDS
        )

        # Remove every alias from the sentence
        service_aliases = set()

        for info in SERVICES.values():
            service_aliases.update(info["aliases"])

        for word in words:

            if word in skip_words:
                continue

            if word in service_aliases:
                continue

            query.append(word)

        return " ".join(query)

    def normalize(self, command):

        command = command.lower().strip()

        # Remove punctuation
        command = re.sub(r"[^\w\s]", "", command)

        words = command.split()
        words = [word for word in words if word not in self.STOP_WORDS]
        cleaned = [
            word
            for word in words
            if word not in self.FILLER_WORDS
            and word not in self.WAKE_WORDS
        ]

        return " ".join(cleaned)
    
    def apply_corrections(self, command):

        for wrong, correct in self.CORRECTIONS.items():
            command = command.replace(wrong, correct)

        return command

    def parse(self, command):

        command = self.normalize(command)
        command = self.apply_corrections(command)

        words = self.tokenize(command)

        intent = self.detect_intent(command, words)

        if intent == "chat":
             return {
                "intent": "chat",
                "text": command
            }

        argument = self.extract_argument(intent, words)

        key = "target" if intent == "open" else "query"

        return {
            "intent": intent,
            key: argument
        }

    