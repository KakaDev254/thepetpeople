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
    
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        if db_field.name == 'content':
            kwargs['help_text'] = mark_safe('''
                <style>
                    .markdown-guide {
                        background: #f8fff8;
                        border: 2px solid #4CAF50;
                        border-radius: 8px;
                        padding: 20px;
                        margin: 15px 0;
                        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif;
                    }
                    .markdown-guide h3 {
                        color: #2c5e2e;
                        margin-top: 0;
                        border-bottom: 2px solid #4CAF50;
                        padding-bottom: 10px;
                    }
                    .markdown-grid {
                        display: grid;
                        grid-template-columns: repeat(2, 1fr);
                        gap: 15px;
                        margin: 15px 0;
                    }
                    .guide-box {
                        background: #ffffff;
                        padding: 12px;
                        border-radius: 6px;
                        border-left: 4px solid #2196F3;
                    }
                    .guide-box code {
                        background: #f5f5f5;
                        padding: 2px 6px;
                        border-radius: 3px;
                        font-family: 'Courier New', monospace;
                        font-size: 13px;
                    }
                    .guide-example {
                        background: #FFF3E0;
                        padding: 12px;
                        border-radius: 6px;
                        margin-top: 15px;
                        border-left: 4px solid #FF9800;
                        font-family: 'Courier New', monospace;
                        font-size: 13px;
                        white-space: pre-wrap;
                    }
                    .guide-tip {
                        background: #E8F5E9;
                        padding: 10px;
                        border-radius: 6px;
                        margin-top: 15px;
                    }
                </style>
                
                <div class="markdown-guide">
                    <h3>📝 Markdown Formatting Guide</h3>
                    
                    <div class="markdown-grid">
                        <div class="guide-box">
                            <strong style="color: #1976D2;">📌 Headers (Titles)</strong><br>
                            <code># Big Title</code><br>
                            <code>## Medium Title</code><br>
                            <code>### Small Title</code>
                        </div>
                        
                        <div class="guide-box">
                            <strong style="color: #7B1FA2;">✏️ Text Formatting</strong><br>
                            <code>**bold**</code> → <strong>bold</strong><br>
                            <code>*italic*</code> → <em>italic</em><br>
                            <code>***bold+italic***</code>
                        </div>
                        
                        <div class="guide-box">
                            <strong style="color: #E65100;">🔢 Numbered Lists</strong><br>
                            <code>1. First item</code><br>
                            <code>2. Second item</code><br>
                            <code>3. Third item</code>
                        </div>
                        
                        <div class="guide-box">
                            <strong style="color: #2E7D32;">• Bullet Lists</strong><br>
                            <code>- Item one</code><br>
                            <code>- Item two</code><br>
                            <code>- Item three</code>
                        </div>
                        
                        <div class="guide-box">
                            <strong style="color: #455A64;">💬 Quotes</strong><br>
                            <code>> This is a quote</code><br>
                            <code>> Multiple lines</code>
                        </div>
                        
                        <div class="guide-box">
                            <strong style="color: #006064;">🔗 Links</strong><br>
                            <code>[Click here](https://example.com)</code>
                        </div>
                    </div>
                    
                    <div class="guide-example">
                        <strong>📝 Quick Example:</strong><br><br>
# My Blog Title

This is a **normal paragraph** with *italic* text.

- First bullet point
- Second bullet point

> This is an important quote that stands out.

---

*Written by the author*
                    </div>
                    
                    <div class="guide-tip">
                        <strong>💡 Pro Tips:</strong><br>
                        • Press <strong>Enter twice</strong> to create a new paragraph<br>
                        • Press <strong>Shift + Enter</strong> for a single line break<br>
                        • No HTML needed - just use these simple symbols!
                    </div>
                </div>
            ''')
        return super().formfield_for_dbfield(db_field, request, **kwargs)