class InvalidKeyStudentError(Exception):
    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key != 'full_name' or key != 'age' or key != 'phone':
                self.message = {
                    'available_keys': [
                    'full_name',
                    'age',
                    'phone'
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
    
    
    def __init__(self, full_name: str, age: int, phone: str) -> None:

        keys = [full_name, phone]
        for key in keys:
            if type(key) != str:
                if key == full_name:
                    self.message = {
                        'available field': {
                            'full_name': 'string'
                        },
                        'field sent': {
                            'full_name': f'{self.types[type(full_name)]}'
                        }
                    }
                elif key == phone:
                    self.message = {
                        'available field': {
                            'phone': 'string'
                        },
                        'field sent': {
                            'phone': f'{self.types[type(phone)]}'
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
