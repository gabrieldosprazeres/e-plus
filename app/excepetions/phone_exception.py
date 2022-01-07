class InvalidKeyPhoneError(Exception):
    def __init__(self, **kwargs):
        avaliable_keys = ['name', 'phone_number']
        for key in kwargs.keys():
            for avaliable in avaliable_keys:
                if key != avaliable:
                    self.message = {
                        'available_keys': [
                        'name',
                        'phone_number'
                        ]
                    }
        super().__init__(self.message)


class InvalidTypePhoneError(Exception):

    types = {
        str: 'string',
        int: 'integer',
        float: 'float',
        list: 'list',
        dict: 'dictionary',
        bool: 'boolean'
    }
    
    
    def __init__(self, name: str, phone_number: str) -> None:

        keys = [name, phone_number]
        for key in keys:
            if type(key) != str:
                if key == name:
                    self.message = {
                        'available field': {
                            'name': 'string'
                        },
                        'field sent': {
                            'name': f'{self.types[type(name)]}'
                        }
                    }
                elif key == phone_number:
                    self.message = {
                        'available field': {
                            'phone_number': 'string'
                        },
                        'field sent': {
                            'phone_number': f'{self.types[type(phone_number)]}'
                        }
                    }

        super().__init__(self.message)


class InvalidAccessPhoneError(Exception):


    def __init__(self) -> None:
        self.message = {
            "message": "this phone is not yours"
        }

        super().__init__(self.message)


class PhoneIdNotFoundError(Exception):


    def __init__(self) -> None:
        self.message = {
            "message": "phone_id not found"
        }

        super().__init__(self.message)