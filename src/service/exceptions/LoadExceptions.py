
class LoadExceptions(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"Load Exception: {self.message}"
    
    def __repr__(self):
        return f"LoadExceptions(message={self.message})"
    
    def to_dict(self):
        return {"error": self.message}