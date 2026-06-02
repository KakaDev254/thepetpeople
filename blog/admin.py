from django.contrib import admin
from django.utils.safestring import mark_safe
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
    
    # Add fieldsets with better visible formatting guide
    fieldsets = (
        ('Blog Post Information', {
            'fields': ('title', 'slug', 'author', 'featured_image')
        }),
        ('Content (Write using simple Markdown - see guide below)', {
            'fields': ('content',),
            'description': mark_safe('''
                <div style="background: #f8fff8; padding: 20px; margin: 15px 0; border: 2px solid #4CAF50; border-radius: 8px; font-family: Arial, sans-serif;">
                    <h3 style="color: #2c5e2e; margin-top: 0; border-bottom: 2px solid #4CAF50; padding-bottom: 10px;">
                        📝 Markdown Formatting Guide
                    </h3>
                    
                    <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px; margin: 15px 0;">
                        <!-- Headers -->
                        <div style="background: #ffffff; padding: 12px; border-radius: 6px; border-left: 4px solid #2196F3;">
                            <strong style="color: #1976D2; font-size: 16px;">📌 Headers (Titles)</strong><br>
                            <code style="background: #f0f0f0; padding: 2px 6px;"># Big Title</code><br>
                            <code style="background: #f0f0f0; padding: 2px 6px;">## Medium Title</code><br>
                            <code style="background: #f0f0f0; padding: 2px 6px;">### Small Title</code>
                        </div>
                        
                        <!-- Text Formatting -->
                        <div style="background: #ffffff; padding: 12px; border-radius: 6px; border-left: 4px solid #9C27B0;">
                            <strong style="color: #7B1FA2; font-size: 16px;">✏️ Text Formatting</strong><br>
                            <code style="background: #f0f0f0; padding: 2px 6px;">**bold**</code> → <strong>bold</strong><br>
                            <code style="background: #f0f0f0; padding: 2px 6px;">*italic*</code> → <em>italic</em><br>
                            <code style="background: #f0f0f0; padding: 2px 6px;">***bold+italic***</code>
                        </div>
                        
                        <!-- Numbered Lists -->
                        <div style="background: #ffffff; padding: 12px; border-radius: 6px; border-left: 4px solid #FF9800;">
                            <strong style="color: #E65100; font-size: 16px;">🔢 Numbered Lists</strong><br>
                            <code style="background: #f0f0f0; padding: 2px 6px;">1. First item</code><br>
                            <code style="background: #f0f0f0; padding: 2px 6px;">2. Second item</code><br>
                            <code style="background: #f0f0f0; padding: 2px 6px;">3. Third item</code>
                        </div>
                        
                        <!-- Bullet Lists -->
                        <div style="background: #ffffff; padding: 12px; border-radius: 6px; border-left: 4px solid #4CAF50;">
                            <strong style="color: #2E7D32; font-size: 16px;">• Bullet Lists</strong><br>
                            <code style="background: #f0f0f0; padding: 2px 6px;">- Item one</code><br>
                            <code style="background: #f0f0f0; padding: 2px 6px;">- Item two</code><br>
                            <code style="background: #f0f0f0; padding: 2px 6px;">- Item three</code>
                        </div>
                        
                        <!-- Quotes -->
                        <div style="background: #ffffff; padding: 12px; border-radius: 6px; border-left: 4px solid #607D8B;">
                            <strong style="color: #455A64; font-size: 16px;">💬 Quotes</strong><br>
                            <code style="background: #f0f0f0; padding: 2px 6px;">> This is a quote</code><br>
                            <code style="background: #f0f0f0; padding: 2px 6px;">> Multiple lines</code>
                        </div>
                        
                        <!-- Links -->
                        <div style="background: #ffffff; padding: 12px; border-radius: 6px; border-left: 4px solid #00BCD4;">
                            <strong style="color: #006064; font-size: 16px;">🔗 Links</strong><br>
                            <code style="background: #f0f0f0; padding: 2px 6px;">[Click here](https://example.com)</code>
                        </div>
                    </div>
                    
                    <div style="background: #FFF3E0; padding: 12px; border-radius: 6px; margin-top: 10px; border-left: 4px solid #FF9800;">
                        <strong style="color: #E65100;">💡 Quick Examples:</strong><br><br>
                        <code style="background: #f0f0f0; padding: 8px; display: block; margin: 5px 0;">
                            # My Blog Title<br><br>
                            This is a **normal paragraph** with *italic* text.<br><br>
                            - First bullet point<br>
                            - Second bullet point<br><br>
                            > This is an important quote that stands out.<br><br>
                            ---<br><br>
                            *Written by the author*
                        </code>
                    </div>
                    
                    <div style="background: #E8F5E9; padding: 10px; border-radius: 6px; margin-top: 10px;">
                        <strong style="color: #2E7D32;">✅ Pro Tips:</strong><br>
                        • Press <strong>Enter twice</strong> to create a new paragraph<br>
                        • Press <strong>Shift + Enter</strong> for a single line break<br>
                        • Use the preview button to see how your post looks
                    </div>
                </div>
            ''')
        }),
        ('Publication Settings', {
            'fields': ('published',),
            'classes': ('collapse',),
            'description': 'Check this box to publish the post on your website'
        }),
    )