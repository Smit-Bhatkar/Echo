from playwright.sync_api import sync_playwright


class BrowserController:
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    def start(self):
        """Launch the browser if it isn't already running."""
        if self.browser:
            return

        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless=False
        )

        self.context = self.browser.new_context()

        self.page = self.context.new_page()

    def open(self, url: str):
        """Open a webpage."""
        self.start()
        self.page.goto(url)

    def current_page(self):
        return self.page

    def stop(self):
        """Close the browser cleanly."""
        if self.browser:
            self.browser.close()

        if self.playwright:
            self.playwright.stop()

        self.browser = None
        self.context = None
        self.page = None


browser = BrowserController()