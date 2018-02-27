from django.shortcuts import render, redirect
from firstApp.forms import DocumentForm
def upload_book(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'firstApp/upload.html', {
        'form': form })



