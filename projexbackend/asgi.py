import os
from channels.layers import get_channel_layer
from channels.routing import get_default_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'projexbackend.config.development')
channel_layer = get_channel_layer()
application = get_default_application()