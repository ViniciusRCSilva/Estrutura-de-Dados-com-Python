from datetime import date, datetime, timedelta, timezone

d = date(2023, 7, 19) 
print(d) # 2023-07-19

# Traz a data (aaa-mm-dd) de agora
today_date = date.today()
print(today_date)

# Traz a data (aaa-mm-dd) e hora (hh:mm:ss:ms) de agora
today_date_hour = datetime.now()
print(today_date_hour)

# Define ano, mês, dia, hora, min, seg, miliseg, timezoneinfo (tzinfo)
d = datetime(2023, 7, 19, 13, 45)
print(d) # 2023-07-19 13:45:00

# Intervalo de tempo de 1 semana
d += timedelta(weeks=1)
print(d) # 2023-07-26 13:45:00

# -------------------------------------------------------------

# Exemplo de uso "timedelta"
tipo_carro = 'P'
tempo_p = 30
tempo_m = 45
tempo_g = 60

data_atual = datetime.now()

if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_p)
    print(f"Carro chegou: {data_atual}")
    print(f"O carro ficará pronto: {data_estimada}")
elif tipo_carro == 'M':
    data_estimada = data_atual + timedelta(minutes=tempo_m)
    print(f"Carro chegou: {data_atual}")
    print(f"O carro ficará pronto: {data_estimada}")
else:
    data_estimada = data_atual + timedelta(minutes=tempo_g)
    print(f"Carro chegou: {data_atual}")
    print(f"O carro ficará pronto: {data_estimada}")

# -------------------------------------------------------------

result = datetime(2023, 7, 25, 10, 19, 20) - timedelta(hours=1)
# Vai imprimir somente o tempo do resultado
print(result.time())

# Retorna e imprime somente a data de agora
print(datetime.now().date())

# -------------------------------------------------------------

# Formatação e conversão de datas com "strftime" (string format time) e "strptime" (string parse time)
d = datetime.now()

# Formatando data e hora
print(d.strftime("%d/%m/%Y %H:%M"))

# Convertendo string para datetime
date_string = "20/07/2023 15:30"
d = datetime.strptime(date_string, "%d/%m/%Y %H:%M")
print(d)

# -------------------------------------------------------------

# Trabalhando com "timezone"

# pip install pytz
import pytz # python timezone

# Criando datetime com timezone
d_sao_paulo = datetime.now(pytz.timezone("America/sao_paulo"))
d_new_york = datetime.now(pytz.timezone("America/new_york"))

print(d_sao_paulo)
print(d_new_york)

# Criando datetime com timezone
d_sao_paulo = datetime.now(timezone(timedelta(hours=3)))
d_new_york = datetime.now(timezone(timedelta(hours=4)))

print(d_sao_paulo)
print(d_new_york)

d = datetime.now(timezone(timedelta(hours=5), "BRT"))

print(d)

# Convertendo para outro timezone
d_utc = d.astimezone(timezone.utc)
print(d_utc)