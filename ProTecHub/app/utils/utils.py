from datetime import datetime, date
from dateutil.relativedelta import relativedelta
import pytz
from django.conf import settings


def obter_data_atual() -> datetime:
    obj = datetime.now(pytz.timezone(settings.TIME_ZONE))
    return obj


def obter_data_do_proximo_ano() -> date:
    obj = obter_data_atual() + relativedelta(years=+1)
    return date(obj.year, obj.month, obj.day)


def obter_data_do_proximo_mes() -> datetime:
    obj = obter_data_atual() + relativedelta(months=+1)
    return obj


def obter_data_resumida(
        objeto: date | datetime, 
    ) -> datetime:

    timezone = settings.TIME_ZONE

    if type(objeto) == date:
        formato = "%d/%m/%Y"
        return objeto.strftime(formato)
    elif type(objeto) == datetime:
        formato = "%d/%m/%Y, %H:%M:%S"
        return objeto.astimezone(pytz.timezone(timezone)).strftime(formato)
    else: 
        return 'NULO'
