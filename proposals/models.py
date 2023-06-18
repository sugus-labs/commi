from django.db import models
import uuid

class Proposal(models.Model):
    id = models.UUIDField(
        help_text = "The unique identifier",
        verbose_name = "UUID",
        primary_key = True, default = uuid.uuid4, 
        editable = False)    
    title = models.CharField(
        help_text = "The main title identifier of the proposal",
        verbose_name = "title",        
        max_length = 500, 
        null = False, blank = False)
    content = models.TextField(
        help_text = "The explanation of the proposal",
        verbose_name = "content",        
        null = False, blank = False)  
    solution = models.TextField(
        help_text = "The solution of the proposal",
        verbose_name = "solution",        
        null = True, blank = True)  
    creation_date = models.DateTimeField(
        help_text = "The date of creation",
        verbose_name = "creation date",        
        auto_now_add = True)
    modification_date = models.DateTimeField(
        help_text = "The date of the last modification",
        verbose_name = "modification date",        
        auto_now = True)        
    deletion_date = models.DateTimeField(
        help_text = "The date of deletion",
        verbose_name = "deletion date",        
        null = True, blank = True)      

    class meta():
        verbose_name_plural = "proposals"
        ordering = ["modification_date"]

    def __str__(self):
        return self.title

#class Vote(models.Model):
#    question = models.ForeignKey(Question, on_delete=models.CASCADE)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)
