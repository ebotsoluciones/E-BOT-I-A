from datetime import datetime, time
from storage import cargar_json, guardar_json

TURNOS_FILE   = "turnos.json"
BLOQUEOS_FILE = "bloqueos.json"

# ── CONFIG HORARIOS ───────────────────────
HORA_INICIO = time(9, 0)
HORA_FIN    = time(19, 0)
INTERVALO   = 60  # minutos

def generar_horarios():
    horarios = []
    h, m = HORA_INICIO.hour, HORA_INICIO.minute

    while (h, m) <= (HORA_FIN.hour, HORA_FIN.minute):
        horarios.append(f"{h:02d}:{m:02d}")
        m += INTERVALO
        h += m // 60
        m %= 60

    return horarios

def normalizar_hora(texto: str):
    texto = texto.strip().replace(".", ":").replace("-", ":")
    if ":" not in texto:
        texto += ":00"
    try:
        h, m = map(int, texto.split(":"))
        return f"{h:02d}:{m:02d}"
    except:
        return None

# ── TURNOS ───────────────────────────────

def obtener_turnos():
    return cargar_json(TURNOS_FILE).get("data", [])

def guardar_turnos(turnos):
    guardar_json(TURNOS_FILE, {"data": turnos})

def agregar_turno(nombre, telefono, fecha, hora):
    turnos = obtener_turnos()
    turnos.append({
        "nombre": nombre,
        "telefono": telefono,
        "fecha": fecha,
        "hora": hora,
        "creado_en": datetime.now().isoformat()
    })
    guardar_turnos(turnos)

def turnos_usuario(telefono):
    hoy = datetime.now().date()
    return [
        t for t in obtener_turnos()
        if t["telefono"] == telefono
        and datetime.strptime(t["fecha"], "%d/%m/%Y").date() >= hoy
    ]

# ── BLOQUEOS ─────────────────────────────

def _obtener_bloqueos():
    return cargar_json(BLOQUEOS_FILE).get("data", [])

def horario_bloqueado(fecha, hora):
    return any(
        b["fecha"] == fecha and b["hora"] == hora
        for b in _obtener_bloqueos()
    )

# ── DISPONIBILIDAD ───────────────────────

def horarios_libres(fecha):
    turnos = {t["hora"] for t in obtener_turnos() if t["fecha"] == fecha}
    bloqueos = {b["hora"] for b in _obtener_bloqueos() if b["fecha"] == fecha}
    ocupados = turnos | bloqueos
    return [h for h in generar_horarios() if h not in ocupados]
