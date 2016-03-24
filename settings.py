# Get X_DOMAINS
# X_DOMAINS = os.getenv('X_DOMAINS', '').split(',')
# CONFIG = {
#    'DOMAIN': {
#        'people': {}
#    },
#    # 'MONGO_URI': os.getenv('MONGO_URI', 'mongodb://localhost:27017/apitest'),
# }
import os
DOMAIN = {
    'pets': {
        'RESOURCE_METHODS': ['GET', 'POST'],
        'MONGO_URI': os.getenv('MONGO_URI', 'mongodb://localhost:27017/apitest'),
        'TOKEN_SECRET': os.getenv('TOKEN_SECRET', '')
    }
}
