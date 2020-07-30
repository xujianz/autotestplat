"""AutoZOne URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#路由mi
from django.contrib import admin
from django.urls import include, path,re_path
from request import views
from  robotframework import webviews
# from  mytestplat import settings
# from django.conf.urls.static import static
# from django.views.static import serve
# from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.Login),
    path('home/', views.Home),
    path('logout/', views.Logout),
    path('create_product/', views.create_product),
    path('product_add_data/', views.product_add_data),
    path('create_product/delete_id/', views.product_delete_data),
    path('create_product/product_change_data/', views.product_change_data),
    path('project_search_name/',views.product_search_data),
    path('product_test_speed/', views.product_test_speed),
    path('left/', views.left),
    path('welcome/', views.welcome),
    path('api_search_name/',views.search_api_name),
    path('singel_api_test/', views.singel_api_test),
    path('singel_api_test/add_singel_data/', views.add_singel_api),
    path('singel_api_test/delete_id/', views.del_singel_api),
    path('singel_api_test/change_singel_data/', views.change_singel_api),
    path('with_data_depend_api/', views.process_api_test),
    path('with_data_depend_api/add_depend_data_apis/', views.add_process_api_test),
    path('with_data_depend_api/delete_depend_api/', views.del_process_api_test),
    path('with_data_depend_api/change_depend_api/', views.change_process_api_test),
    path('singel_periodic_task/addtask_data/', views.add_task_singel_api_test),
    path('singel_periodic_task/', views.periodic_task),
    path('singel_periodic_task/delete_id/', views.del_task_singel_api_test),
    path('process_periodic_task/', views.process_periodic_task),
    path('process_periodic_task/addtask_data/', views.add_process_api_test_task),
    path('process_periodic_task/delete_id/', views.del_task_process_api_test),
    path('singel_periodic_task/start_immediapage/',views.start_singel_apis_task),
    path('singel_periodic_task/start_time_taske/', views.get_singel_api_task_time),
    path('Web_test_robotframework/add_web_casename/', webviews.add_web_casename),
    path('search_webcasename/',webviews.searche_web_casename),
    path('Web_test_robotframework/', webviews.web_testcase_page),
    path('Web_test_robotframework/delete_id/', webviews.del_web_casename),
    path('webcasestep_manage/', webviews.display_web_casesteps,name='webcasestep_manage'),
    path('testReport/', views.write_singel_apis_result),
    # path('webcasestep_manage/save_step/',webviews.manage_web_casesteps),
    path('webcasestep_manage/delete_id/',webviews.delete_web_casesteps),
    # path('webcasestep_manage/save_edit/',webviews.edit_web_casestep),
    path('add_image/',webviews.upload_file),
    path('keywordslibrary/',webviews.display_keywords),
    path('keywordslibrary/save/', webviews.add_keywords),
    path('keywordslibrary/delete_id/',webviews.del_keywords),
    path('keywordslibrary/save_edit/',webviews.change_keywords),
    path('webcasestep_manage/fast_test/',webviews.maoyan_test),
    path('webcasestep_manage/save_test/',webviews.remove_test_txt),
    path('webcase_periodic_task/',webviews.webUI_periodic_task),
    path('webcase_periodic_task/addwebtask_data/',webviews.add_task_webcase_test),
    path('webcase_periodic_task/start_immediately_task/',webviews.run_webcase_immediately),
    path('webcase_periodic_task/start_time_task/',webviews.get_webcase_task_time),
    path('robotframework/results/report/',webviews.web_report),
    path('email_add_page/delete_email/', webviews.delete_recevier_message),
    path('email_add_page/edit_email_data/', webviews.edit_recevier_message),
    path('add_email_recevier/',webviews.add_email_recevier),
    path('add_email_sendermessage/',webviews.add_email_sender),
    path('email_add_page/',webviews.display_email),

]
# +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# re_path(r'^media/(.*)$', serve, {'document_root': settings.MEDIA_ROOT})

