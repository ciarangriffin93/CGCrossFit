from django.contrib import admin
from .models import ContactForm
from django_summernote.admin import SummernoteModelAdmin


@admin.register(ContactForm)
class ContactFormAdmin(SummernoteModelAdmin):
    list_display = ("name", "lastname", "phonenumber", "email", "message")
    search_fields = ["name", "email"]
