from django.conf.urls import  url ,include
from . import  views
#from . import search
urlpatterns = [
    # path('admin/', admin.site.urls),
    url('^$',views.index),
    #url(r'^search-form$', search.search_form),
    #url(r'^angelo/login', search.login),
]

