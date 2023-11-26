from django.contrib import admin
from home.models import ContactFormMessage, Setting, UserProfile

# Register your models here.

admin.site.register(Setting)

class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name','subject','update_at','status'] #! görüntülenecek kısım.
    readonly_fields = ('name','subject','email','message','ip') #! düzenleme yapılamayacak olanlar.
    list_filter = ['status']
    #! fields = ['name','subject'] # sadece bu kısımlar görünür.
admin.site.register(ContactFormMessage, ContactFormMessageAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name','address', 'phone','city','country','image_tag']

admin.site.register(UserProfile, UserProfileAdmin)