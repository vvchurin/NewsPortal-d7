from django_filters import FilterSet, DateTimeFromToRangeFilter
from django_filters.widgets import RangeWidget
from .models import Post

# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class PostFilter(FilterSet):
   time = DateTimeFromToRangeFilter(widget = RangeWidget(attrs={'type': 'datetime-local'}))

   class Meta:
       # В Meta классе мы должны указать Django модель,
       # в которой будем фильтровать записи.
       model = Post
       # В fields мы описываем по каким полям модели
       # будет производиться фильтрация.
       fields = {
           # поиск по названию
           'name': ['icontains'],
           # количество товаров должно быть больше или равно
           'author': ['exact'],

       }