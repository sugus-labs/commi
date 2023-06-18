from django.contrib import admin
from .models import Proposal

class ProposalAdmin(admin.ModelAdmin):
    readonly_fields = [
        "creation_date", "modification_date", 
        "deletion_date"]
    fieldsets = [
        ("Information", {
            "fields": ["title", "content",
                "solution"]}),
        ("Dates", {
            "fields": [
                "creation_date", "modification_date", 
                "deletion_date"]}),
    ]


admin.site.register(Proposal, ProposalAdmin)