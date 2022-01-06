class InvalidKeyStudentError(Exception):
    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key != 'name' or key != 'last_name' or key != 'age' or key != 'grade' or key != 'email' or key != 'password':
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


class InvalidTypeStudentError(Exception):

    types = {
        str: 'string',
        int: 'integer',
        float: 'float',
        list: 'list',
        dict: 'dictionary',
        bool: 'boolean'
    }
    
    
    def __init__(self, name: str, last_name: str, age: int, grade: str, email: str, password: str) -> None:

        keys = [name, last_name, grade, email, password]
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
