from django.contrib import admin
from community.models import Dashboard, Question, AddReply

# Register your models here.

from django.contrib.admin.options import ModelAdmin

admin.site.site_header = 'WitQuake Administration'                 # default: "Django Administration"
admin.site.index_title = 'WitQuake Database Structure'                 # default: "Site administration"
admin.site.site_title = 'WitQuake Site Admin'                      # default: "Django site admin"


class DashboardAdmin(ModelAdmin):
    list_display = ["name", "profession"]
    search_fields = ["name", "profession"]
    list_filter = ["name", "profession"]


admin.site.register(Dashboard, DashboardAdmin)


class QuestionAdmin(ModelAdmin):
    list_display = ["uploaded_by", "title", "tag1", "tag2", "tag3"]
    search_fields = ["uploaded_by", "title", "tag1", "tag2", "tag3"]
    list_filter = ["uploaded_by", "title", "tag1", "tag2", "tag3"]


admin.site.register(Question, QuestionAdmin)


class AddReplyAdmin(ModelAdmin):
    list_display = ["to", "by", "reply"]
    search_fields = ["to", "by", "reply"]
    list_filter = ["to", "by", "reply"]


admin.site.register(AddReply, AddReplyAdmin)


