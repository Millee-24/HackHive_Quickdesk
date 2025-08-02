from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Ticket, TicketComment, User
from .forms import RegisterForm, TicketForm, CommentForm
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Count, Q

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'helpdesk/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    return render(request, 'helpdesk/register.html', {'form': form})

@login_required
def dashboard(request):
    user = request.user
    if user.role == 'user':
        tickets = Ticket.objects.filter(user=user)
        return render(request, 'helpdesk/user_dashboard.html', {'tickets': tickets})
    elif user.role == 'agent':
        tickets = Ticket.objects.all()
        return render(request, 'helpdesk/agent_dashboard.html', {'tickets': tickets})
    elif user.role == 'admin':
        users = User.objects.all()
        return render(request, 'helpdesk/admin_dashboard.html', {'users': users})
    return redirect('login')

@login_required
def create_ticket(request):
    form = TicketForm()
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            send_mail(
                subject='New Ticket Created',
                message=f'Your ticket "{ticket.subject}" has been created.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[request.user.email],
                fail_silently=True,
            )
            return redirect('dashboard')
    return render(request, 'helpdesk/create_ticket.html', {'form': form})

@login_required
def ticket_detail(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    comments = ticket.comments.all()
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.ticket = ticket
            comment.save()
            return redirect('ticket_detail', ticket_id=ticket.id)

    return render(request, 'helpdesk/ticket_detail.html', {
        'ticket': ticket,
        'comments': comments,
        'form': form
    })
