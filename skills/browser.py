import webbrowser
import urllib.parse


class Browser:

    WEBSITES = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "github": "https://github.com",
        "linkedin": "https://www.linkedin.com",
        "chatgpt": "https://chat.openai.com",
        "gmail": "https://mail.google.com",
        "spotify": "https://open.spotify.com",
        "netflix": "https://www.netflix.com",
    }

    def open_website(self, name):

        if name in self.WEBSITES:

            webbrowser.open(self.WEBSITES[name])

            return f"Opening {name.title()}."

        return None

    def google_search(self, query):

        url = (
            "https://www.google.com/search?q="
            + urllib.parse.quote(query)
        )

        webbrowser.open(url)

        return f"Searching Google for {query}."

    def youtube_search(self, query):

        url = (
            "https://www.youtube.com/results?search_query="
            + urllib.parse.quote(query)
        )

        webbrowser.open(url)

        return f"Searching YouTube for {query}."