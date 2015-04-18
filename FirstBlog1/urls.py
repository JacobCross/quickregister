from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'FirstBlog1.blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^form/', 'FirstBlog1.blog.views.form', name = 'form'),
    url(r'^index/', 'FirstBlog1.blog.views.index', name = 'index'),
    url(r'^newform/', 'FirstBlog1.blog.views.newform', name = 'newform'),
    url(r'^finalform2/', 'FirstBlog1.blog.views.finalform2', name = 'finalform2'),
    url(r'^finalform3/', 'FirstBlog1.blog.views.finalform3', name = 'finalform3'),
    url(r'^finalform4/', 'FirstBlog1.blog.views.finalform4', name = 'finalform4'),
    url(r'^thanks/', 'FirstBlog1.blog.views.thanks', name = 'thanks'),
    url(r'^submitform/', 'FirstBlog1.blog.views.submit_form', name = 'submit_form'),
    url(r'^bootstraptest/', 'FirstBlog1.blog.views.bootstraptest', name = 'bootstraptest'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
