from django.shortcuts import render, redirect
from firstApp.forms import BookForm
def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_book')
    else:
        form = BookForm()
    return render(request, 'firstApp/upload.html', {
        'form': form })



