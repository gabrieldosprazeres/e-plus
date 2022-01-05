class PhoneAlreadyExistsError(Exception):


    def __init__(self, phone) -> None:

        self.message = {
            'message': f"phone: '{phone}' already exists"
        }

        super().__init__(self.message)