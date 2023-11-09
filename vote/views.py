from .forms import RegistrationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from .models import Position, Candidate, UserVote
from django.contrib.admin.views.decorators import staff_member_required


def index_view(request):
    title = "E - Voting Portal"
    return render(request, 'index.html', {'title': title})


def register_view(request):
    title = "Register | E - Voting Portal"
    return render(request, 'register.html', {'title': title})


def login_view(request):
    title = "Logina | E - Voting Portal"
    return render(request, 'login.html', {'title': title})


def otp_view(request):
    title = "OTP | E - Voting Portal"
    return render(request, 'otp.html', {'title': title})


def vote_view(request):
    title = 'Vote | E - Voting Portal'
    return render(request, 'vote.html', {'title': title, "positions": Position.objects.all(), "candidates": Candidate.objects.all()})


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # Replace with your redirection URL
        else:
            # Handle form errors
            # You can pass the form with errors to the template
            return render(request, 'registration.html', {'form': form})
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('otp')  # Replace with your redirection URL
            else:
                # Handle invalid login
                # Add a custom error message
                form.add_error(None, 'Invalid login credentials')
        else:
            pass
            # Handle form errors
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def vote_page(request):
    # Your code to filter user_votes, candidates, and positions
    v_data = {}
    user_votes = UserVote.objects.filter(
        user=request.user)  # Adjust this based on your model
    # Replace YourCandidateModel with your actual model
    candidates = Candidate.objects.all()
    # Replace YourPositionModel with your actual model
    positions = Position.objects.all()

    # Additional logic to prepare data for rendering
    if (request.method == "POST"):
        print(request.POST)
        user_vote2 = UserVote(user=request.user, candidate=Candidate.objects.get(pk=int(request.POST.get(
            "candidate_id", 0)[0])), position=Position.objects.get(pk=int(request.POST.get("position_id", 0))))
        user_vote2.save()
        # modify db
    for i in candidates:
        user_number = len(UserVote.objects.filter(candidate=i))
        v_data[i.id] = user_number

    print(user_votes)
    return render(request, 'vote.html', {
        'user_votes': user_votes,
        'votes': UserVote.objects.all(),
        'votez': v_data,
        'candidates': candidates,
        'positions': positions,
    })


@staff_member_required
def admin_results_view(request):
    votes = UserVote.objects.all()

    context = {
        'votes': votes,
    }
    return render(request, 'admin_results.html', context)
