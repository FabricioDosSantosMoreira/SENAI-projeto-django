from datetime import datetime
from typing import Optional
from dateutil.relativedelta import relativedelta
import pytz
from django.conf import settings


def obter_data_atual() -> datetime:
    return datetime.now(pytz.timezone(settings.TIME_ZONE))


def obter_data_do_proximo_ano() -> datetime:
    return obter_data_atual() + relativedelta(years=+1)


def obter_data_do_proximo_mes() -> datetime:
    return obter_data_atual() + relativedelta(months=+1)


def obter_data_resumida(
        objeto: datetime, 
        timezone: Optional[str] = settings.TIME_ZONE, 
        formato:  Optional[str] = "%d/%m/%Y, %H:%M:%S", 
    ) -> datetime:

    return objeto.astimezone(pytz.timezone(timezone)).strftime(formato)
