from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('', views.index, name='index'),
    path('login', views.login_view, name="login"),
    path('signup', views.signup, name="signup"),
    path('home', views.home, name="home"),
    path('log', views.log, name="log"),
    path('weather', views.weather, name="weather"),
    path('logout', views.logout_view, name="logout"),
    path('sign', views.sign, name="sign"),
    path('blogpost-like/<int:pk>', views.BlogPostLike, name="blogpost_like"),
    path('blogpost-comment/<int:pk>', views.comment, name="blogpost_comment"),
    path('upload', views.upload, name='upload'),
    path('add/<slug:username>/<slug:eotp>/<slug:potp>/', views.add, name='add'),
    path('profile/<slug:user>', views.profile, name='profile'),




    # crops Sections
    path('jute', views.jute, name='jute' ),
    path('wheat', views.wheat,  name='wheat'),
    path('rice', views.rice, name='rice' ),
    path('sugarcane', views.sugarcane, name='sugarcane'),
    path('maize', views.maize, name='maize'),
    path('pulses', views.pulses, name='pulses' ),

    #notice board
    path('pms', views.pms, name="pms"),
    path('pmb', views.pmb, name="pmb"),
    path('pmk', views.pmk,name="pmk" ),
    path('pmm', views.pmm, name="pmm"),



]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)