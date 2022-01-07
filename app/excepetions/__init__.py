class EmailAlreadyExistsError(Exception):


    def __init__(self, email) -> None:

        self.message = {
            'message': f"email: '{email}' already exists"
        }

        super().__init__(self.message)