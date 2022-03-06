from django_minify_html.middleware import MinifyHtmlMiddleware


class CompliantMinifyHtmlMiddleware(MinifyHtmlMiddleware):
    minify_args = MinifyHtmlMiddleware.minify_args | {
        'do_not_minify_doctype': True,
        'keep_spaces_between_attributes': True,
    }
