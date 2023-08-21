from .serializers import StatisticSerializer
from .models import Statistic
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist


@csrf_exempt
@api_view(['POST'])
def add_statistic(request):
    serializer = StatisticSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    try:
        Statistic.objects.get(date=serializer.validated_data['date'])
        response = {'info': 'Такая дата уже существует'}
        return Response(response, status=200)

    except ObjectDoesNotExist:
        statistic_day = Statistic.objects.create(
            date=serializer.validated_data['date'],
            views=serializer.validated_data['views'],
            clicks=serializer.validated_data['clicks'],
            cost=serializer.validated_data['cost']
        )

        serializer = StatisticSerializer(statistic_day)
        return Response(serializer.data, status=200)


@api_view(['POST'])
def get_statistic(request):
    date_from = request.POST.get('date_from')
    date_to = request.POST.get('date_to')
    order = request.POST.get('order')
    statistics = Statistic.objects.filter(date__gte=date_from, date__lte=date_to).order_by(order)
    statistic_params = [{
        'date': statistic.date,
        'views': f'{statistic.views} шт',
        'clicks': f'{statistic.clicks} шт',
        'cost': f'{statistic.cost} руб',
        'cpc': round(statistic.cost/statistic.clicks, 2),
        'cpm': round(statistic.cost/statistic.views * 1000, 2)}
        for statistic in statistics]
    response = {'statistic': statistic_params}
    return Response(response, status=200)


@api_view(['POST'])
def clear_statistic(request):
    date_from = request.POST.get('date_from')
    date_to = request.POST.get('date_to')
    clear_all = request.POST.get('clear_all')
    if clear_all:
        Statistic.objects.all().delete()
        response = {'statistic': 'Вся статистика очищена'}
        return Response(response, status=200)
    else:
        Statistic.objects.filter(date__gte=date_from, date__lte=date_to).delete()
    response = {'statistic': 'Cтатистика по выбранным датам очищена'}
    return Response(response, status=200)
