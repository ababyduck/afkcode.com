from django import template
import mistune

register = template.Library()


@register.filter
def markdown(value):
    md = mistune.create_markdown(plugins=['strikethrough', 'task_lists'])
    return md(value)
