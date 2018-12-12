from main.models import Room
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView


class RoomListView(ListView):
    model = Room
    ordering = ['-capacity']


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


class SearchRoomView(ListView):
    model = Room
    #template_name = "products/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None) # method_dict['q']
        print(query)
        if query is not None:
            return Room.objects.filter(capacity__icontains=query)
        return Room.objects.all().order_by('-capacity')
        '''
        __icontains = field contains this
        __iexact = fields is exactly this
        '''