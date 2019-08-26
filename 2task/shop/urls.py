from shop import views
from django.urls import path

urlpatterns = [
    path('', views.imports),
    path('/<int:import_id>/citizens/<int:citizen_id>', views.change),
    path('/<int:import_id>/citizens', views.get_citizens),
    #path('/<int:imports_id>/citizens/birthdays', views.birthdays),
    #path('/<int:imports_id>/towns/stat/percentile/age', age_percentile),
    #path('/test', response_test_view)
]