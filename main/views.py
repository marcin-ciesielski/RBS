from django.db.models import Q
from main.models import Room, Booking
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.views import View
from django.shortcuts import render, get_object_or_404
import datetime

class RoomListView(ListView):
    model = Room
    ordering = ['-capacity']


class MyRoomListView(View):
    template_name = 'main/room_list.html'
    queryset = Room.objects.all()
    date = datetime.datetime.now().date()

    def get(self, request, *args, **kwargs):
        context = {
            'room_list': self.queryset,
            'date': self.date, # date.strftime('%Y-%m-%d'),
        }
        return render(request, self.template_name, context)


class RoomDetailView(DetailView):
    model = Room


class RoomUpdateView(UpdateView):
    model = Room
    fields = '__all__'
    template_name = 'main/room_form.html'
    success_url = reverse_lazy('room-list')


class RoomDeleteView(DeleteView):
    model = Room
    template_name = 'main/room_confirm_delete.html'
    success_url = reverse_lazy('room-list')


class RoomCreateView(CreateView):
    model = Room
    fields = '__all__'
    template_name = 'main/room_form.html'
    success_url = reverse_lazy('room-list')


class BookingCreateView(CreateView):
    model = Booking
    fields = '__all__'
    template_name = 'main/booking_form.html'
    success_url = reverse_lazy('room-list')


class SearchRoomView(ListView):
    model = Room
    #template_name = "products/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None) # method_dict['q']
        print(query)
        if query is not None:
            lookups = Q(name__icontains = query) | Q(capacity__icontains = query)
            return Room.objects.filter(lookups).distinct()
        return Room.objects.all().order_by('-capacity')

        # __icontains = field contains this
        #__iexact = fields is exactly this

