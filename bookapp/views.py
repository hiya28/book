from django.http import HttpResponse
from .models import Book
from django.shortcuts import render, redirect
from .forms import AuthorForm,BookForm
from django.urls import reverse_lazy


# ////function based

# def CreateBook(request):
#
#
#     books = Book.objects.all()
#     if request.method=="POST":
#
#         title=request.POST.get("title")
#         author=request.POST.get("author")
#         price=request.POST.get("price")
#
#         book=Book(title=title,author=author,price=price)
#         book.save()
#
#     return render(request,"index.html",{"books":books})

def ListBook(request):

    books=Book.objects.all()
    return render(request,"list.html",{"books":books})


def DeatilView(request,book_id):
    book=Book.objects.get(id=book_id)
    return render(request,"detail.html",{"book":book})

#
# def UpdateView(request,book_id):
#     book=Book.objects.get(id=book_id)
#
#     if request.method == "POST":
#
#         title = request.POST.get("title")
#         author = request.POST.get("author")
#         price = request.POST.get("price")
#
#         book.title=title
#         book.author=author
#         book.price=price
#
#         book.save()
#     return render(request,"update.html",{"book":book})


def DeleteView(request,book_id):

    book=Book.objects.get(id=book_id)
    if request.method=="POST":
        book.delete()
        return redirect('/')

    return render(request,"delete.html",{"book":book})

# //classbased_views
# from django.urls import reverse_lazy
# from . models import Book
# from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
#
#
# class BookCreateView(CreateView):
#
#     model = Book
#     template_name = 'index.html'
#     fields = ['title','price']
#
#     success_url = reverse_lazy('booklist')
#
# class BookListView(ListView):
#
#     model = Book
#     template_name = 'list.html'
#
#     context_object_name = 'books'
#
#
# class BookDetailView(DetailView):
#     model = Book
#     template_name = 'details.html'
#
#
#     context_object_name = 'book'
#
#
# class BookUpdateView(UpdateView):
#     model = Book
#     template_name = 'update.html'
#
#     fields = ['title','price']
#
#     success_url = reverse_lazy('booklist')
#
# class BookDeleteView(DeleteView):
#
#     model = Book
#     template_name = 'delete.html'
#     context_object_name = 'book'
#
#     success_url = reverse_lazy('booklist')



# ///forms

def CreateBook(request):

   books=Book.objects.all()



   if request.method=='POST':
       form=BookForm(request.POST,request.FILES)

       if form.is_valid():
           form.save()

           return redirect('/')

   else:
       form =BookForm

   return render(request,'book.html',{'form':form,'books':books})


def Create_Author(request):
    if request.method=='POST':

        form = AuthorForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/')

    else:
        form=AuthorForm()
    return render(request,'author.html',{'form':form})


def UpdateView(request,book_id):
    book=Book.objects.get(id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST,instance=book)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BookForm(instance=book)
    return render(request,"update.html",{"form":form})


def demo(request):
    return render(request,'base.html')