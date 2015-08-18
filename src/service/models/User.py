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
    
    def from_dict(data: dict):
        return User(
            user_id=data.get("user_id"),
            username=data.get("username"),
            email=data.get("email"),
            password=data.get("password")
        )
    def update_email(self, new_email: str):
        self.email = new_email

    def update_password(self, new_password: str):
        self.password = new_password

    def greet(self):        
        return f"Hello, {self.username}!"
    
    def is_valid_email(self):
        return "@" in self.email and "." in self.email.split("@")[-1]
    
    def check_password(self, password: str):
        return self.password == password