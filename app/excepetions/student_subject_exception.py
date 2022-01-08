class InvalidKeySubjectRegisterError(Exception):
    def __init__(self) -> None:
        self.message = {
            'available_key': [
            'subject',
            'time_course'
            ]
        }

        super().__init__(self.message)


class InvalidTypeSubjectRegisterError(Exception):

    types = {
        str: 'string',
        int: 'integer',
        float: 'float',
        list: 'list',
        dict: 'dictionary',
        bool: 'boolean'
    }
    
    
    def __init__(self, subject: str, time_course: str) -> None:

        if type(subject) != str:
            self.message = {
                'available field': {
                    'subject': 'string'
                },
                'field sent': {
                    'subject': f'{self.types[type(subject)]}'
                }
            }
        elif type(time_course) != str:
            self.message = {
                'available field': {
                    'time_course': 'string'
                },
                'field sent': {
                    'time_course': f'{self.types[type(time_course)]}'
                }
            }

        super().__init__(self.message)