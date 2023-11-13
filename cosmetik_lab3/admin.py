from django.contrib import admin
from .models import Cosmetiks
from .models import SubCosm
from .models import Substanses
from .models import Users

admin.site.register(Users)
admin.site.register(Substanses)
admin.site.register(SubCosm)
admin.site.register(Cosmetiks)
