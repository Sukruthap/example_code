from django.conf.urls import url, include
from rest_framework import routers
from .api import AnswerquestionViewSet
from app_answer import views

router = routers.DefaultRouter()
router.register(r'questionanswer', views.add_qaans)

urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'addanswer/',views.add_questionanswer, name='add-answer'),
]