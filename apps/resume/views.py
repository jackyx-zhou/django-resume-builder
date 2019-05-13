from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect

from .forms import ResumeItemForm, ResumeForm
from .models import ResumeItem, Resume

@login_required
def resume_index_view(request):
    """
    Handle a request to view a user's resume index.
    """
    resumes = Resume.objects\
        .filter(user=request.user)\
        .order_by('-title')

    return render(request, 'resume/resume_index.html', {
        'resumes': resumes
    })

@login_required
def resume_create_view(request):
    """
    Handle a request to create a new resume.
    """
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            new_resume = form.save(commit=False)
            new_resume.user = request.user
            new_resume.save()

            return redirect(resume_detail_view, new_resume.id)
    else:
        form = ResumeItemForm()

    return render(request, 'resume/resume_create.html', {'form': form})

@login_required
def resume_detail_view(request, resume_id):
    """
    Handle a request to see the detail of a resume.
    :param resume_id: The database ID of the Resume to edit.
    """
    try:
        resume = Resume.objects\
            .filter(user=request.user)\
            .get(id=resume_id)
    except ResumeItem.DoesNotExist:
        raise Http404

    resume_items = ResumeItem.objects\
        .filter(user=request.user)\
        .order_by('-start_date')

    return render(request, 'resume/resume_detail.html', {
        'resume_items': resume_items
    })


@login_required
def resume_item_create_view(request):
    """
    Handle a request to create a new resume item.
    """
    if request.method == 'POST':
        form = ResumeItemForm(request.POST)
        if form.is_valid():
            new_resume_item = form.save(commit=False)
            new_resume_item.user = request.user
            new_resume_item.save()

            return redirect(resume_item_edit_view, new_resume_item.id)
    else:
        form = ResumeItemForm()

    return render(request, 'resume/resume_item_create.html', {'form': form})


@login_required
def resume_item_edit_view(request, resume_item_id):
    """
    Handle a request to edit a resume item.

    :param resume_item_id: The database ID of the ResumeItem to edit.
    """
    try:
        resume_item = ResumeItem.objects\
            .filter(user=request.user)\
            .get(id=resume_item_id)
    except ResumeItem.DoesNotExist:
        raise Http404

    template_dict = {}

    if request.method == 'POST':
        if 'delete' in request.POST:
            resume_item.delete()
            return redirect(resume_view)

        form = ResumeItemForm(request.POST, instance=resume_item)
        if form.is_valid():
            form.save()
            form = ResumeItemForm(instance=resume_item)
            template_dict['message'] = 'Resume item updated'
    else:
        form = ResumeItemForm(instance=resume_item)

    template_dict['form'] = form

    return render(request, 'resume/resume_item_edit.html', template_dict)
