from django.contrib import admin
from .models import Party, User, Vote

admin.site.register(User)
admin.site.register(Party)
admin.site.register(Vote)


# Register your models here.
