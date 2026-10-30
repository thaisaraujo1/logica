import datetime
import calendar

meses = [
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro",
]

dias_semanas = [
    "segunda-feira",
    "terça-feira",
    "quarta-feira", 
    "quinta-feira",
    "sexta-feira",
    "sábado", 
    "domingo"
]

#21/12/2024
data = datetime.date(2024,12,21)

print(data)

hoje = datetime.date.today()
print(hoje)
print(hoje.strftime("%d/%m/%Y"))
print(f"São Paulo, {dias_semanas} {hoje.weekday()}{hoje.day} de {meses[hoje.month - 1]} de {hoje.year}")

print(f"1972 é Bissexto: {calendar.isleap(2027)}")

print(f"É o último da do mês? {calendar.monthrange(2026, 10)[1]}")