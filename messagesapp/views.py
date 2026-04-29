# Author: Mariam El-Mansouri Abaich
# ID: w2074138
# Contribution: Backend Logic for Messages Management (CWK2)

from django.shortcuts import render, redirect
# Used to render HTML pages and redirect between views
from django.contrib.auth.decorators import login_required
# Ensures only logged-in users can access these views
from .models import Message
# Import Message model (database table)
from .forms import MessageForm
# Import form used to create new messages


@login_required
def inbox(request):
    # This view shows messages received by the logged-in user’s team
    # Filter messages:
    # - Only messages with status "sent"
    # - Only messages where the team manager is the logged-in user
    inbox_messages = Message.objects.filter(
        message_status='sent',
        team__manager=request.user
    )

    # Send messages to the inbox template
    return render(request, 'messagesapp/inbox.html', {
        'messages': inbox_messages
    })


@login_required
def new_message(request):
    # This view handles creating and sending new messages

    if request.method == 'POST':
        # Get form data submitted by the user
        form = MessageForm(request.POST)

        if form.is_valid():
            # Create message object but do not save yet
            msg = form.save(commit=False)
            # Set sender as the logged-in user (secure, not from form input)
            msg.sender = request.user
            # Get action from button (send or save draft)
            action = request.POST.get('action')

            if action == 'draft':
                # Save message as draft
                msg.message_status = 'draft'
                msg.save()
                return redirect('drafts')

            elif action == 'send':
                # Save message as sent
                msg.message_status = 'sent'
                msg.save()
                return redirect('/messages/sent/?sent=1')

    else:
        # If not POST, show empty form
        form = MessageForm()

    # Render the new message page with form
    return render(request, 'messagesapp/new_message.html', {
        'form': form
    })


@login_required
def sent(request):
    # This view shows messages sent by the logged-in user

    success_message = None
    # Check if redirected after sending a message
    if request.GET.get('sent') == '1':
        success_message = "Message sent successfully"
    # Filter messages:
    # - Only messages with status "sent"
    # - Only messages sent by the logged-in user
    sent_messages = Message.objects.filter(
        message_status='sent',
        sender=request.user
    )
    # Render sent messages page
    return render(request, 'messagesapp/sent.html', {
        'success_message': success_message,
        'messages': sent_messages
    })


@login_required
def drafts(request):
    # This view shows draft messages created by the logged-in user
    # Filter messages:
    # - Only messages with status "draft"
    # - Only messages created by the logged-in user
    draft_messages = Message.objects.filter(
        message_status='draft',
        sender=request.user
    )

    # Render drafts page
    return render(request, 'messagesapp/drafts.html', {
        'messages': draft_messages
    })