from django import template

register = template.Library()

@register.filter
def translate_number(value):
    value = str(value)
    en_to_pe_table= value.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')
    return value.translate(en_to_pe_table)