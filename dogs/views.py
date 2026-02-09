from django.shortcuts import render

from dogs.models import Breed, Dog

def index(request):
    context = {
        'objects_list': Breed.objects.all()[:3],
        'title': 'Питомник - Главная'
    }
    return render(request, 'dogs/index.html', context)


def breeds_list_view(request):
    context = {
        'object_list': Breed.objects.all(),
        'title': 'Питомник - Все наши породы'
    }
    return  render(request, 'dogs/breeds.html', context)

def breeds_dogs_list_view(request, pk: int):
    breeds_item = Breed.objects.get(pk=pk)
    context = {
        'object_list': Dog.objects.filter(breed_id=pk),
        'title': f'Собаки породы - {breeds_item}',
        'breed_pk': breeds_item.pk,
    }
    return render(request, 'dogs/dogs.html', context)

def dogs_list_view(request):
    context = {
        'object': Dog.objects.all(),
        'title': 'Питомник все наши собаки'
    }
    return render(request, 'dogs/dogs.html', context)