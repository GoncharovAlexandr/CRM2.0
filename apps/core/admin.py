from django.contrib import admin

from apps.core.models import Ivan_Mazur, Задания, Dima_Vinokurov, Katya_Sidorina

#@admin.register(Задание)
#class ЗаданиеAdmin(admin.ModelAdmin):
#    ...

@admin.register(Ivan_Mazur)
class Ivan_MazurAdmin(admin.ModelAdmin):
    ...

@admin.register(Dima_Vinokurov)
class Dima_VinokurovAdmin(admin.ModelAdmin):
    ...

@admin.register(Katya_Sidorina)
class Katya_SidorinaAdmin(admin.ModelAdmin):
    ...

@admin.register(Задания)
class ЗаданияAdmin(admin.ModelAdmin):
    ...
