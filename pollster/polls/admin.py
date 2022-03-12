from django.contrib import admin

from .models import Question, Choice

class ChoiceInLine(admin.TabularInline):
  model = Choice
  extra = 3
  
class QuestionAdmin(admin.ModelAdmin):
  fieldsets = [(None, {'fields': ['question_text']}), 
               ('Date Information', {'fields': ['pub_date'], 
              'classes':['collapse']}),]
  inlines = [ChoiceInLine]


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Question)
# admin.site.register(Choice)

#change django administration
admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"
admin.site.index_title = "welcome to Pollster Admin"