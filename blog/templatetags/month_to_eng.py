from django import template

register = template.Library()


@register.filter
def month_to_eng(value: str):
    month_dict = {
        '1월': 1, '2월': 2, '3월': 3, '4월': 4, '5월': 5, '6월': 6, '7월': 7, '8월': 8, '9월': 9, '10월': 10, '11월': 11, '12월': 12
    }
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return months[month_dict[value]-1]