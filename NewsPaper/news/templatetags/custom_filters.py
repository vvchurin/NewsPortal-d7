from django import template


register = template.Library()

replacement_ = ['плохое', 'плохого']

# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter()
def censor(value):
   for word in replacement_:
      value = value.replace(word, '*****')
   # Возвращаемое функцией значение подставится в шаблон.
   return str(value)