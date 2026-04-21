# Author: Mariam El-Mansouri Abaich
# ID: w2074138
# Contribution: Backend Logic for Messages Management (CWK2)

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Message
from .forms import MessageForm


def inbox(request):
    # temporary user (same as used when sending messages)
    current_user = User.objects.first()

    inbox_messages = Message.objects.filter(
        message_status='sent'
    ).exclude(sender=current_user)

    return render(request, 'messagesapp/inbox.html', {
        'messages': inbox_messages
    })


def new_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)

        if form.is_valid():
            msg = form.save(commit=False)

            # Temporary user (until login fully used)
            msg.sender = User.objects.last()

            # Get extra fields (not saved)
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')

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

    sent_messages = Message.objects.filter(message_status='sent')

    return render(request, 'messagesapp/sent.html', {
        'success_message': success_message,
        'messages': sent_messages
    })


def drafts(request):
    draft_messages = Message.objects.filter(message_status='draft')

    return render(request, 'messagesapp/drafts.html', {
        'messages': draft_messages
    })