from django.contrib import admin
from .models import CustomUser


class UserAdmin(admin.ModelAdmin):
    search_fields = ['apellidoPaterno', 'email']
    ordering = ['apellidoPaterno']
    list_display = ('primerNombre', 'segundoNombre',
                    'apellidoPaterno', 'apellidoMaterno', 'email')
    
    def save_model(self, request, obj, form, change):
        # encripta el password antes de guardarlo
        obj.set_password(form.cleaned_data['password'])
        super().save_model(request, obj, form, change)

admin.site.register(CustomUser, UserAdmin)