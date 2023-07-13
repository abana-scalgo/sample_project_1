from django.shortcuts import render,redirect,get_object_or_404
from .models import CMS
from .forms import CMSForm

# Create your views here.
def add_content(request):
    if request.method == 'POST':
        form = CMSForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_content')
    else:
        form = CMSForm()
    return render(request, 'add_content.html', {'form': form})

def edit_content(request, pk):
    content = get_object_or_404(CMS, pk=pk)
    if request.method == 'POST':
        form = CMSForm(request.POST,instance=content)
        if form.is_valid():
            form.save()
            return redirect('list_content')
    else:
        form = CMSForm(instance=content)
    return render(request, 'edit_content.html',{'form': form})

def delete_content(request, pk):
    content = get_object_or_404(CMS, pk=pk)
    if request.method == 'POST':
        content.delete()    
        return redirect('list_content')
    return render(request, 'delete_content.html', {'content': content})

def list_content(request):
    contents = CMS.objects.all()
    return render(request,'list_content.html', {'contents': contents})