from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'published', 'has_image')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('published', 'created_at', 'author')
    search_fields = ('title', 'content')
    
    def has_image(self, obj):
        return bool(obj.featured_image)
    has_image.boolean = True
    has_image.short_description = 'Has Image'
    
    # Add helpful formatting guide for the client
    fieldsets = (
        ('Blog Post Information', {
            'fields': ('title', 'slug', 'author', 'featured_image')
        }),
        ('Content (Use Markdown for formatting)', {
            'fields': ('content',),
            'description': '''
                <div style="background: #f0f7f0; padding: 20px; margin: 10px 0; border: 2px solid #4CAF50; border-radius: 8px; font-family: Arial, sans-serif;">
                    <h3 style="color: #2c5e2e; margin-top: 0;">📝 Markdown Formatting Guide - Easy to Use!</h3>
                    <p style="margin-bottom: 10px;">No HTML needed! Just use these simple symbols:</p>
                    
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin: 15px 0;">
                        <div style="background: white; padding: 10px; border-radius: 5px;">
                            <strong>📌 Headers (Titles)</strong><br>
                            # Big Title<br>
                            ## Medium Title<br>
                            ### Small Title
                        </div>
                        <div style="background: white; padding: 10px; border-radius: 5px;">
                            <strong>✏️ Text Formatting</strong><br>
                            **bold text**<br>
                            *italic text*<br>
                            ***bold & italic***
                        </div>
                        <div style="background: white; padding: 10px; border-radius: 5px;">
                            <strong>🔢 Numbered Lists</strong><br>
                            1. First item<br>
                            2. Second item<br>
                            3. Third item
                        </div>
                        <div style="background: white; padding: 10px; border-radius: 5px;">
                            <strong>• Bullet Lists</strong><br>
                            - Item one<br>
                            - Item two<br>
                            - Item three
                        </div>
                        <div style="background: white; padding: 10px; border-radius: 5px;">
                            <strong>💬 Quotes</strong><br>
                            > This is a quote<br>
                            > It stands out
                        </div>
                        <div style="background: white; padding: 10px; border-radius: 5px;">
                            <strong>🔗 Links</strong><br>
                            [Click here](https://example.com)
                        </div>
                        <div style="background: white; padding: 10px; border-radius: 5px;">
                            <strong>➖ Horizontal Line</strong><br>
                            ---
                        </div>
                        <div style="background: white; padding: 10px; border-radius: 5px;">
                            <strong>📏 Line Break</strong><br>
                            Two spaces at end of line<br>
                            then enter for new line
                        </div>
                    </div>
                    
                    <div style="background: #fff3cd; padding: 10px; border-radius: 5px; margin-top: 10px;">
                        <strong>💡 Pro Tip:</strong> Press Enter twice to start a new paragraph. 
                        Use the preview button to see how your post will look!
                    </div>
                </div>
            ''',
        }),
        ('Publication Settings', {
            'fields': ('published',),
            'classes': ('collapse',),
            'description': 'Uncheck this to hide the post from the website'
        }),
    )
    
    # Add custom CSS to make the content field larger
    class Media:
        css = {
            'all': ('blog/css/admin_blog.css',)
        }