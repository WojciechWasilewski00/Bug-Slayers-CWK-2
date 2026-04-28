# Author: Mariam El-Mansouri Abaich
# ID: w2074138
# Contribution: Backend Logic for Messages Management (CWK2)

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Message
from .forms import MessageForm


@login_required
def inbox(request):
    # Show messages sent to teams managed by the logged-in user
    inbox_messages = Message.objects.filter(
        message_status='sent',
        team__manager=request.user
    )

    return render(request, 'messagesapp/inbox.html', {
        'messages': inbox_messages
    })


@login_required
def new_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)

        if form.is_valid():
            msg = form.save(commit=False)

            # Set the sender as the logged-in user
            msg.sender = request.user

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


@login_required
def sent(request):
    success_message = None

    if request.GET.get('sent') == '1':
        success_message = "Message sent successfully"

    # Show only messages sent by the logged-in user
    sent_messages = Message.objects.filter(
        message_status='sent',
        sender=request.user
    )
    return render(request, 'messagesapp/sent.html', {
        'success_message': success_message,
        'messages': sent_messages
    })


@login_required
def drafts(request):
    # Show only drafts created by the logged-in user
    draft_messages = Message.objects.filter(
        message_status='draft',
        sender=request.user
    )

    return render(request, 'messagesapp/drafts.html', {
        'messages': draft_messages
    })