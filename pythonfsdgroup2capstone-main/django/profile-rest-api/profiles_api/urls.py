from django.urls import include, path
from profiles_api import views
from rest_framework.routers import DefaultRouter
from profiles_api import views
from .views import MovieViewSet, MoviereleaseViewSet, TicketsViewSet

router = DefaultRouter()
router.register('bookvs', views.BookViewSet, basename='bookvs')
router.register('empvs', views.EmpViewSet, basename='empvs')
router.register('profile', views.UserProfileViewSet)
router.register('feedvs', views.UserProfileFeedViewSet)
router.register('movies', MovieViewSet)
router.register('moviesrelease', MoviereleaseViewSet)
router.register('tickets', TicketsViewSet)

urlpatterns = [
	path('hello-view/', views.HelloApiView.as_view()),
	path('books/', views.BookApiView.as_view()),
	path('emp/', views.EmpApiView.as_view()),
	path('login/', views.UserLoginApiView.as_view()),
 	path('', include(router.urls)),

]
