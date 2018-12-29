from django import template

register = template.Library()
@register.filter(name='customCut')
def custom_cut(value,arg):
    """
    This cut out all values of 'arg' from the string!
    """
    return value.replace(arg,'')

# register.filter('customCut',custom_cut)
