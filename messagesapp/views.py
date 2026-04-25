# Author: Mariam El-Mansouri Abaich
# ID: w2074138
# Contribution: Backend Logic for Messages Management (CWK2)

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from team_registry.models import Team
from .models import Message
from .forms import MessageForm


def inbox(request):
    current_user = request.user

    inbox_messages = Message.objects.filter(
        message_status='sent',
        team__manager=current_user
    )

    return render(request, 'messagesapp/inbox.html', {
        'messages': inbox_messages
        
    })

def new_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)

        if form.is_valid():
            msg = form.save(commit=False)

            # Temporary test sender user
            #msg.sender = User.objects.get(username="1.Mariam_W2074138")
            current_user = request.user

            action = request.POST.get('action')

            if action == 'draft':
                msg.message_status = 'draft'
                msg.save()
                return redirect('drafts')

            elif action == 'send':
                msg.message_status = 'sent'
                msg.save()
                return redirect('/messages/sent/?sent=1')

    else:
        form = MessageForm()

    return render(request, 'messagesapp/new_message.html', {
        'form': form
    })


def sent(request):
    success_message = None

    if request.GET.get('sent') == '1':
        success_message = "Message sent successfully"

    sent_messages = Message.objects.filter(
        message_status='sent',
        sender=request.user
    )

    return render(request, 'messagesapp/sent.html', {
        'success_message': success_message,
        'messages': sent_messages
    })

def drafts(request):
    draft_messages = Message.objects.filter(
        message_status='draft',
        sender=request.user
    )

    return render(request, 'messagesapp/drafts.html', {
        'messages': draft_messages
    })