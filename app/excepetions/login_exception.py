class EmailNotFoundError(Exception):

    def __init__(self, email) -> None:

        self.message = {
            "email": f'{email}',
            "message": "Not registered"
        }

        super().__init__(self.message)


class IncorrectPasswordError(Exception):

    def __init__(self) -> None:

        self.message = {
            "message": "Invalid password"
        }

        super().__init__(self.message)


class InvalidKeyLoginError(Exception):

    def __init__(self, **kwargs) -> None:

        avaliable_keys = ['email', 'password']

        for key in kwargs.keys():
            for avaliable in avaliable_keys:
                if key != avaliable:
                    self.message = {
                        'available_keys': [
                        'email',
                        'password'
                        ]
                    }

        super().__init__(self.message)


class InvalidTypeLoginError(Exception):

    types = {
        str: 'string',
        int: 'integer',
        float: 'float',
        list: 'list',
        dict: 'dictionary',
        bool: 'boolean'
    }
    
    
    def __init__(self, email: str, password: str) -> None:

        keys = [email, password]
        for key in keys:
            if type(key) != str:
                if key == email:
                    self.message = {
                        'available field': {
                            'email': 'string'
                        },
                        'field sent': {
                            'email': f'{self.types[type(email)]}'
                        }
                    }
                elif key == password:
                    self.message = {
                        'available field': {
                            'password': 'string'
                        },
                        'field sent': {
                            'password': f'{self.types[type(password)]}'
                        }
                    }

        super().__init__(self.message)