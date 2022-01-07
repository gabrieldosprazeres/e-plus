class SubjectAlreadyExistsError(Exception):


    def __init__(self, subject: str) -> None:

        self.message = {
            'message': f"subject: '{subject}' already exists"
        }

        super().__init__(self.message)


class InvalidKeySubjectError(Exception):
    def __init__(self, subject: str) -> None:
        if subject != 'subject':
            self.message = {
                'available_key': [
                'subject'
                ]
            }
        super().__init__(self.message)


class InvalidTypeSubjectError(Exception):

    types = {
        str: 'string',
        int: 'integer',
        float: 'float',
        list: 'list',
        dict: 'dictionary',
        bool: 'boolean'
    }
    
    
    def __init__(self, subject: str) -> None:

        if type(subject) != str:
            self.message = {
                'available field': {
                    'subject': 'string'
                },
                'field sent': {
                    'subject': f'{self.types[type(subject)]}'
                }
            }

        super().__init__(self.message)
