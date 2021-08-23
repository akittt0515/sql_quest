from django.contrib import admin
from .models import QA_data, SQL_syntax, std_data,QA,QC

admin.site.register(std_data)
admin.site.register(QA_data)
admin.site.register(SQL_syntax)
admin.site.register(QA)
admin.site.register(QC)



# Register your models here.
