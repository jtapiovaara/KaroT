from django.contrib import admin


from .models import TaiteilijaTaulu, TauluTaulu, KysyTaulusta


class TauluTauluAdmin(admin.ModelAdmin):
    list_display = ('nimi', 'tila')
    list_filter = ['tila']
    list_editable = ('tila',)


admin.site.register(TaiteilijaTaulu)
admin.site.register(TauluTaulu, TauluTauluAdmin)
admin.site.register(KysyTaulusta)
