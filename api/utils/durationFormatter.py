from datetime import timedelta

def timedeltaAString(duracion: timedelta):
    valores = []
    valores.append({"value":duracion.days, "plural_key":"dias", "singular_key": "día"})
    horas, res = divmod(duracion.total_seconds(), 3600)
    valores.append({"value":int(horas), "plural_key":"horas", "singular_key": "hora"})
    minutos, segundos = divmod(res, 60)
    valores.append({"value":int(minutos), "plural_key":"minutos", "singular_key": "minuto"})
    valores.append({"value":round(segundos, 2), "plural_key":"segundos", "singular_key": "segundo"})
    valoresString = [generarValorString(valor) for valor in valores if valor["value"]>0]
    return ', '.join(valoresString)

def generarValorString(valor):
    if valor["value"] > 1:
        return f'{valor["value"]} {valor["plural_key"]}'
    return f'{valor["value"]} {valor["singular_key"]}'