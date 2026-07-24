class SessionManager:
    def __init__(self):
        self.reset()

    def reset(self):
        self.active_service = None
        self.last_skill = None
        self.last_query = None

    def set_service(self, service):
        self.active_service = service

    def get_service(self):
        return self.active_service

    def set_skill(self, skill):
        self.last_skill = skill

    def get_skill(self):
        return self.last_skill

    def set_query(self, query):
        self.last_query = query

    def get_query(self):
        return self.last_query


session = SessionManager()