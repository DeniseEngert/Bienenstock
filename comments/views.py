from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

@login_required
def new_commentary(request, pk):
    project = get_object_or_404(Project, pk=pk)
    # so den eingeloggten user verwenden oder direkt über request.user:
    user = request.user

    # usw.

    return render(request, 'new_commentary.html')