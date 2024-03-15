from django.urls import path
from .import views

# ///function based views

#
urlpatterns = [

    path("create-book",views.CreateBook,name='createbook'),
    path("auther/",views.Create_Author,name="author"),
    path("",views.ListBook,name='booklist'),
    path("details/<int:book_id>/",views.DeatilView,name="details"),
    path("update/<int:book_id>/",views.UpdateView,name="update"),
    path("delete/<int:book_id>/",views.DeleteView,name="delete"),
    path('demo/',views.demo,name="demo"),


]


from django.urls import path
from . import views

# urlpatterns = [

    # path("",views.creatBook),
    # path("auther/",views.create_Author,name="author"),

    # path("",views.BookListView.as_view(),name='booklist'),
    # path('creatview/',views.BookCreateView.as_view(),name='createbook'),
    # path('detailsview/<int:pk>/',views.BookDetailView.as_view(),name='details'),
    # path('updateview/<int:pk>/',views.BookUpdateView.as_view(),name='update'),
    # path('deleteview/<int:pk>/', views.BookDeleteView.as_view(), name='delete')
# ]