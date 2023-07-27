Для создания нового приложения с именем app_lesson_4, нужно выполнить следующие шаги:

Откройте командную строку или терминал в рабочей директории вашего проекта.
Введите следующую команду для создания нового Django приложения:

python manage.py startapp app_lesson_4
Перейдите в файл urls.py в основной директории проекта и добавьте следующий код:

from django.urls import path
from app_lesson_4.views import lesson_4_view

urlpatterns = [
    path('lesson_4/', lesson_4_view, name='lesson_4'),
    # Другие URL-адреса вашего проекта...
]
В созданной директории app_lesson_4 откройте файл views.py и добавьте следующий код:

from django.http import HttpResponse

def lesson_4_view(request):
    return HttpResponse("Домашка по 4 занятию")
Сохраните файлы и запустите сервер разработки Django, выполнив команду:

python manage.py runserver
Теперь представление будет доступно по адресу: http://127.0.0.1/lesson_4