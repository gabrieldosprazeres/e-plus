class InvalidKeyStudentError(Exception):
    def __init__(self, **kwargs) -> None:
        avaliable_keys = ['name', 'last_name', 'age', 'grade', 'email', 'password', 'state', 'city', 'district', 'street', 'house_number', 'complement']
        for key in kwargs.keys():
            for avaliable in avaliable_keys:
                if key != avaliable:
                    self.message = {
                        'available_keys': [
                        'name',
                        'last_name',
                        'age',
                        'grade',
                        'email',
                        'password',
                        'state',
                        'city',
                        'district',
                        'street',
                        'house_number',
                        'complement'
                        ]
                    }
        super().__init__(self.message)


class InvalidTypeStudentError(Exception):

    types = {
        str: 'string',
        int: 'integer',
        float: 'float',
        list: 'list',
        dict: 'dictionary',
        bool: 'boolean'
    }
    
    
    def __init__(self, name: str, last_name: str, age: int, grade: str, email: str, password: str, state: str, city: str, district: str, street: str, house_number: str, complement: str) -> None:

        keys = [name, last_name, grade, email, password, state, city, district, street, house_number, complement]
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
                elif key == last_name:
                    self.message = {
                        'available field': {
                            'last_name': 'string'
                        },
                        'field sent': {
                            'last_name': f'{self.types[type(last_name)]}'
                        }
                    }
                elif key == grade:
                    self.message = {
                        'available field': {
                            'grade': 'string'
                        },
                        'field sent': {
                            'grade': f'{self.types[type(grade)]}'
                        }
                    }
                elif key == email:
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
                elif key == state:
                    self.message = {
                        'available field': {
                            'state': 'string'
                        },
                        'field sent': {
                            'state': f'{self.types[type(state)]}'
                        }
                    }
                elif key == city:
                    self.message = {
                        'available field': {
                            'city': 'string'
                        },
                        'field sent': {
                            'city': f'{self.types[type(city)]}'
                        }
                    }
                elif key == district:
                    self.message = {
                        'available field': {
                            'district': 'string'
                        },
                        'field sent': {
                            'district': f'{self.types[type(district)]}'
                        }
                    }
                elif key == street:
                    self.message = {
                        'available field': {
                            'street': 'string'
                        },
                        'field sent': {
                            'street': f'{self.types[type(street)]}'
                        }
                    }
                elif key == house_number:
                    self.message = {
                        'available field': {
                            'house_number': 'string'
                        },
                        'field sent': {
                            'house_number': f'{self.types[type(house_number)]}'
                        }
                    }
                elif key == complement:
                    self.message = {
                        'available field': {
                            'complement': 'string'
                        },
                        'field sent': {
                            'complement': f'{self.types[type(complement)]}'
                        }
                    }

        if type(age) != int:
            self.message = {
                'available field': {
                    'age': 'integer'
                },
                'field sent': {
                    'age': f'{self.types[type(age)]}'
                }
            }

        super().__init__(self.message)


class InvalidKeyUpdatingError(Exception):
    def __init__(self, **kwargs) -> None:
        avaliable_keys = ['name', 'last_name', 'age', 'grade', 'email', 'password']
        for key in kwargs.keys():
            for avaliable in avaliable_keys:
                if key != avaliable:
                    self.message = {
                        'available_keys': [
                        'name',
                        'last_name',
                        'age',
                        'grade',
                        'email',
                        'password'
                        ]
                    }
        super().__init__(self.message)


class InvalidTypeUpdatingError(Exception):


    def __init__(self) -> None:

        self.message = {
            'available field': {
                'name': 'string',
                'last_name': 'string',
                'age': 'integer',
                'grade': 'string',
                'email': 'string',
                'password': 'string'
            }
        }

        super().__init__(self.message)


class InvalidKeyUpdatingAddressError(Exception):
    def __init__(self, **kwargs) -> None:
        avaliable_keys = ['state', 'city', 'district', 'street', 'house_number', 'complement']
        for key in kwargs.keys():
            for avaliable in avaliable_keys:
                if key != avaliable:
                    self.message = {
                        'available_keys': [
                        'state',
                        'city',
                        'district',
                        'street',
                        'house_number',
                        'complement'
                        ]
                    }
        super().__init__(self.message)


class InvalidTypeUpdatingAddressError(Exception):


    def __init__(self) -> None:

        self.message = {
            'available field': {
                'state': 'string',
                'city': 'string',
                'district': 'string',
                'street': 'string',
                'house_number': 'string',
                'complement': 'string'
            }
        }

        super().__init__(self.message)