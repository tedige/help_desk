from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Problem
from .forms import ProblemForm
from django.contrib.auth.models import Group

@login_required
def create_problem(request):
    if request.method == 'POST':
        form = ProblemForm(request.POST)
        if form.is_valid():
            problem = form.save(commit=False)
            problem.user = request.user
            problem.save()
            return redirect('problem_list')
    else:
        form = ProblemForm()
    return render(request, 'helpdesk/create_problem.html', {'form': form})
    reception_users = User.objects.filter(groups__name='Reception')
    if reception_users.exists():
        problem.assigned_user = reception_users.first()
        problem.save()

    return render(request, 'helpdesk/create_problem.html', {'form': form})


@login_required
def problem_list(request):
    user = request.user
    if user.groups.filter(name='Tester').exists():
        problems = Problem.objects.filter(Q(assigned_user=user) | Q(status='confirmed')).exclude(status='resolved')
    else:
        problems = Problem.objects.filter(assigned_user=user).exclude(status='resolved')

    return render(request, 'helpdesk/problem_list.html', {'problems': problems})


@login_required
def view_problem(request, problem_id):
    problem = get_object_or_404(Problem, id=problem_id)

    if request.method == 'POST':
        form = ProblemForm(request.POST, instance=problem)
        if form.is_valid():
            problem = form.save(commit=False)
            problem.user = request.user
            problem.save()


            if problem.status == 'resolved':
                tester_users = User.objects.filter(groups__name='Tester')
                if tester_users.exists():
                    problem.assigned_user = tester_users.first()
                    problem.resolved_user = request.user
                    problem.save()

            return redirect('problem_list')
    else:
        form = ProblemForm(instance=problem)

    return render(request, 'helpdesk/view_problem.html', {'problem': problem, 'form': form})

