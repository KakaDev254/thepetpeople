from django import template
import markdown

register = template.Library()

@register.filter
def render_markdown(value):
    """Convert Markdown to HTML"""
    if not value:
        return ''
    return markdown.markdown(value, extensions=[
        'extra',  # Tables, footnotes, etc.
        'nl2br',  # New line to break
        'sane_lists',  # Better list handling
        'codehilite',  # Code highlighting
    ])