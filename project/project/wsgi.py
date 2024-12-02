import os
from django.core.wsgi import get_wsgi_application


# Ställ in rätt miljövariabel för inställningarna
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.project.settings')

application = get_wsgi_application()


