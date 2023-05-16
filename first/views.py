from django.shortcuts import render
import random

def lotto_index(request):
    return render(request, 'first/lotto_index.html')

def lotto_result(request):
    lotto_number = list()
    game = request.GET.get('game', 1)
    pull_number = [index for index in range(1, 46)]

    for _ in range(int(game)):
        lotto_number.append(random.sample(pull_number,6))

    return render(request, 'first/lotto_result.html', {'lotto_number': lotto_number, 'game': game})