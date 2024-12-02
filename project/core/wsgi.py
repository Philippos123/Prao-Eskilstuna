import os
from django.core.wsgi import get_wsgi_application

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

# Ställ in rätt miljövariabel för inställningarna
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.core.settings')

application = get_wsgi_application()


