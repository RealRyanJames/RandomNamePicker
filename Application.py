class Application:

    def __init__(self, name: str):
        self.name = name

    def get(self) -> None:
        return self.name
