from django.urls import path
# Импортируем созданное нами представление
from news.views import ArticleCreate, NewsUpdate, NewsDelete


urlpatterns = [

   path('create/', ArticleCreate.as_view()),
   path('<int:pk>/edit', NewsUpdate.as_view()),
   path('<int:pk>/delete', NewsDelete.as_view(), name='delete'),
]