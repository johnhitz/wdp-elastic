schema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'email': {
        'type': 'string',
        'unique': True
    },
    '_id': {
        'type': 'objectid',
        'required': True,
        'unique': True,
    },
    'picture': {
        'type': 'string',
        'default': ''
    },
    'roles': {
        'type': 'list',
        'allowed': [
            'owner',
            'vet_aide',
            'vet',
            'catcher_aide',
            'catcher',
            'law_aide',
            'law',
            'super'
        ]
    }
}

model = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'account',

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST', 'DELETE'],

    'schema': schema
}
