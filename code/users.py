class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role  # 'admin' or 'user'

    def has_permission(self, action):
        permissions = {
            "admin": ["view_logs", "manage_modules"],
            "user": ["view_modules", "complete_modules"]
        }
        return action in permissions.get(self.role, [])