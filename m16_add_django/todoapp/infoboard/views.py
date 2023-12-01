from datetime import datetime, timedelta

from dateutil import parser
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect

from .mongodb.connect import db
from .tasks import work_process


# Create your views here.


def main(request):
    page = request.GET.get('page', 1)  # Отримуємо номер сторінки з GET запиту
    per_page = 10  # Кількість елементів на сторінці
    skip_amount = (int(page) - 1) * per_page

    # Використання методів skip і limit для пагінації на рівні MongoDB
    results = db.moskali.find().sort("date", -1).skip(skip_amount).limit(per_page)
    # Отримання загальної кількості записів для пагінації
    total_results = db.moskali.count_documents({})
    # Ручне створення даних для пагінації
    paginator = Paginator(range(total_results), per_page)
    try:
        results_page = paginator.page(page)
    except PageNotAnInteger:
        results_page = paginator.page(1)
    except EmptyPage:
        results_page = paginator.page(paginator.num_pages)
    # Перетворення даних для шаблону
    transformed_results = [
        (
            datetime.strftime(parser.parse(el['date']), '%d.%m.%Y'),
            [(k, v) for k, v in el.items() if k not in ['_id', 'date']]
        )
        for el in results
    ]

    return render(request, 'infoboard/losses-list.html', {"results": transformed_results, "page": results_page})


def sync_losses_list(request):
    last_result = db.moskali.find_one(sort=[("date", -1)])
    print(last_result)
    if last_result is not None:
        date = last_result["date"]
        last_date = parser.parse(date)
        now_date = datetime.now()
        period = now_date - last_date
        search_list = []
        for day in range(1, period.days + 1):
            next_date = last_date + timedelta(days=day)
            search_list.append(datetime.strftime(next_date, "%d.%m.%Y"))
        print(f'{search_list}')
        work_process.delay(search_list)  # CELERY TASK
        print('------------------ sync_losses_list -------------')
    return redirect("losses")
