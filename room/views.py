from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from .models import Room, Message

__author__ = 'BENZNANA Mohamed : benznana.med@gmail.com'


class RoomsView(TemplateView):
    http_method_names = ['get', ]
    template_name = "room/rooms.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(RoomsView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(RoomsView, self).get_context_data(**kwargs)

        rooms = Room.objects.all()

        context.update({
            'rooms': rooms
        })

        return context


class RoomView(TemplateView):
    http_method_names = ['get', ]
    template_name = "room/room.html"
    room = None

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        room_slug = kwargs.get('slug')

        try:
            self.room = Room.objects.get(slug=room_slug)
        except Room.DoesNotExist:
            messages.error(self.request, "Room matching query does not exist!")
            return redirect('room:rooms')

        return super(RoomView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(RoomView, self).get_context_data(**kwargs)

        list_messages = Message.objects.filter(room=self.room)[0:25]

        context.update({
            'room': self.room,
            'messages': list_messages
        })

        return context
