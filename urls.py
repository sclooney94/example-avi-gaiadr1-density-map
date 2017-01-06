"""
GAVIP Example AVIS: Simple AVI

These URLs are used by the AVI web-interface.
@req: REQ-0006
@comp: AVI Web System
"""
from django.conf.urls import include, patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from plugins.urls import job_list_urls
from avi import views, views_api

api_urls = [
    # API definitions
    url(r'^$',
        views_api.DemoModelList.as_view(),
        name='demomodel-list'),

    url(r'^(?P<pk>[0-9]+)/$',
        views_api.DemoModelDetail.as_view(),
        name='demomodel-detail'),

    url(r'^job_data/(?P<job_id>[0-9]+)/$',
        views_api.JobData.as_view(),
        name='api-job-data'),

    url(r'^view_jobs/$',
        views_api.ViewJobsList.as_view(),
        name='api-view-jobs'),

    url(r'^view_jobs/(?P<pk>[0-9]+)/$',
        views_api.ViewJobsListDetail.as_view(),
        name='api-view-jobs-detail'),

]

api_urls = format_suffix_patterns(api_urls)

urlpatterns = patterns(
    '',
    url(r'^$',
        views.index,
        name='index'),

    url(r'^api/',
        include(api_urls,
        namespace='api')),

    url(r'^job_list/',
        include(job_list_urls,
        namespace='job_list')),

    url(r'^run_query/$',
        views.run_query,
        name='run_query'),

    # Same as api-job-data above
    url(r'^job_data/(?P<job_id>[0-9]+)/$',
        views_api.JobData.as_view(),
        name='job_data'),

    url(r'^result/(?P<job_id>[0-9]+)/$',
        views.job_result,
        name='job_result')
)
