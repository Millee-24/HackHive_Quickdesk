from django.contrib import admin
from .models import Ticket, TicketComment, TicketAttachment, TicketVote, Category

class TicketAttachmentInline(admin.TabularInline):
    model = TicketAttachment
    extra = 0

class TicketCommentInline(admin.TabularInline):
    model = TicketComment
    extra = 0

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'status', 'priority', 'created_by', 'assigned_to', 'created_at', 'updated_at')
    list_filter = ('status', 'priority', 'category')
    search_fields = ('subject', 'description', 'id')
    date_hierarchy = 'created_at'
    inlines = [TicketAttachmentInline, TicketCommentInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(TicketComment)
class TicketCommentAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'author', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('content',)

@admin.register(TicketAttachment)
class TicketAttachmentAdmin(admin.ModelAdmin):
    list_display = ('filename', 'ticket', 'uploaded_by', 'uploaded_at')
    list_filter = ('uploaded_at',)
    search_fields = ('filename',)

@admin.register(TicketVote)
class TicketVoteAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'user', 'vote_type', 'created_at')
    list_filter = ('vote_type', 'created_at')
    search_fields = ('ticket__subject', 'user__username')
