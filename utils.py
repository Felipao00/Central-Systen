from datetime import datetime
from zoneinfo import ZoneInfo

def is_business_hours():
    """Verifica se está no horário de funcionamento (Horário de Brasília)"""
    brasilia_tz = ZoneInfo("America/Sao_Paulo")
    now = datetime.now(brasilia_tz)
    
    weekday = now.weekday()  # 0 = Segunda, 6 = Domingo
    hour = now.hour
    minute = now.minute
    current_time = hour + minute / 60
    
    # Verifica feriados (adicione as datas no formato MM-DD)
    holidays = [
        "01-01",  # Ano Novo
        "04-21",  # Tiradentes
        "05-01",  # Dia do Trabalho
        "09-07",  # Independência
        "10-12",  # Nossa Senhora
        "11-02",  # Finados
        "11-15",  # Proclamação da República
        "12-25",  # Natal
    ]
    
    today_str = now.strftime("%m-%d")
    is_holiday = today_str in holidays
    
    if is_holiday:
        # Feriados: horário flexível (10:00 às 17:00)
        return 10 <= current_time < 17
    elif weekday < 5:  # Segunda a Sexta
        return 9.5 <= current_time < 22  # 09:30 às 22:00
    else:  # Sábado e Domingo
        return 10 <= current_time < 17  # 10:00 às 17:00

def get_business_hours_message():
    """Retorna mensagem personalizada para fora de horário"""
    brasilia_tz = ZoneInfo("America/Sao_Paulo")
    now = datetime.now(brasilia_tz)
    weekday = now.weekday()
    
    if weekday < 5:
        return "Segunda a Sexta das 09:30 às 22:00"
    else:
        return "Sábado e Domingo das 10:00 às 17:00"

def get_current_time_brasilia():
    """Retorna hora atual de Brasília formatada"""
    brasilia_tz = ZoneInfo("America/Sao_Paulo")
    now = datetime.now(brasilia_tz)
    return now.strftime("%H:%M")

def get_current_day_brasilia():
    """Retorna dia da semana atual em português"""
    brasilia_tz = ZoneInfo("America/Sao_Paulo")
    now = datetime.now(brasilia_tz)
    
    days = {
        0: "Segunda-feira",
        1: "Terça-feira",
        2: "Quarta-feira",
        3: "Quinta-feira",
        4: "Sexta-feira",
        5: "Sábado",
        6: "Domingo"
    }
    
    return days[now.weekday()]