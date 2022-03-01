from django import template
import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html

register = template.Library()


class HighlightRenderer(mistune.HTMLRenderer):
    def block_code(self, code, lang=None):
        if lang:
            lexer = get_lexer_by_name(lang, stripall=True)
            formatter = html.HtmlFormatter()
            return highlight(code, lexer, formatter)
        return f'<pre><code>{mistune.escape(code)}</pre></code>'


@register.filter
def markdown(value):
    renderer = HighlightRenderer()
    process = mistune.create_markdown(renderer=renderer, plugins=['strikethrough', 'task_lists'])
    return process(value)
