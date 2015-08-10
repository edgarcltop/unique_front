class User:
    def __init__(self, user_id: int, username: str, email: str, password: str):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
    def __repr__(self):
        return f"User(user_id={self.user_id}, username={self.username}, email={self.email}, password={self.password})"
    
    def to_dict(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email,
            "password": self.password
        }