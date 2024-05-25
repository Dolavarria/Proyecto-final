import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","Inmobiliaria.settings")
django.setup()

from Arriendos.models import User,Propiedad,SolicitudArriendo

select = """select * from public.my_python_post where title
like ‘%post 2%’"""