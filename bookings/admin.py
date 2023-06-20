from django.contrib import admin
from .models import Resource, Schedule, Booking

class ResourceAdmin(admin.ModelAdmin):
    readonly_fields = [
        "creation_date", "modification_date", 
        "deletion_date"]
    fieldsets = [
        ("Information", {
            "fields": ["name", "timetable", "is_active"]}),
        ("Dates", {
            "fields": [
                "creation_date", "modification_date", 
                "deletion_date"]}),
    ]
    list_display = ["name", "timetable", "is_active", 
        "creation_date", "modification_date"]
    list_filter = ["is_active", "creation_date", "modification_date"]


class ScheduleAdmin(admin.ModelAdmin):
    readonly_fields = [
        "creation_date", "modification_date", 
        "deletion_date"]
    fieldsets = [
        ("Information", {
            "fields": ["resource", "slot", "comments"]}),
        ("Dates", {
            "fields": [
                "creation_date", "modification_date", 
                "deletion_date"]}),
    ]
    list_display = ["resource", "slot", "is_active", 
        "creation_date", "modification_date"]
    list_filter = ["resource", "is_active", "creation_date", "modification_date"]

class BookingAdmin(admin.ModelAdmin):

    def get_resource(self, obj):
        return obj.schedule.resource
    
    def get_slot(self, obj):
        return obj.schedule.slot    

    readonly_fields = [
        "creation_date", "modification_date", 
        "deletion_date"]
    fieldsets = [
        ("Information", {
            "fields": ["user", "schedule", "status", "date"]}),
        ("Dates", {
            "fields": [
                "creation_date", "modification_date", 
                "deletion_date"]}),
    ]    
    list_display = ["user", "get_resource", "get_slot", 
        "status", "date", "creation_date", "modification_date"]
    list_filter = ["user", "schedule__resource__name", 
        "schedule__slot", "status", "date", "creation_date", "modification_date"]

admin.site.register(Resource, ResourceAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Booking, BookingAdmin)