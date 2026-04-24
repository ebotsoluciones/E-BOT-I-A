from datetime import datetime
from storage import cargar_json, guardar_json
from config  import ADMINS, MODO_TEST, MENSAJES_FILE
from services import (
    generar_horarios, normalizar_hora,
    horario_bloqueado, bloquear_horario,
    obtener_turnos, guardar_turnos, turnos_usuario,
    horarios_libres, agregar_turno, cancelar_turno,
    guardar_mensaje,
)

from ia import interpretar_mensaje

ESTADO_KEY = "estados_usuarios"

MENU_PACIENTE = """🦙 E-Bot

1 Turno
2 Mis turnos
3 Mensaje
4 Urgencia
5 Informes
6 Salir"""

MENU_ADMIN = """🛠 ADMIN

1 Turnos hoy
2 Próximos turnos
3 Mensajes
4 Nuevo turno
5 Cancelar turno
6 Bloquear agenda
7 Salir"""

def get_estado():
    return cargar_json(ESTADO_KEY)

def save_estado(data):
    guardar_json(ESTADO_KEY, data)

def set_user_state(numero, key, value):
    estado = get_estado()
    estado.setdefault(numero, {})
    estado[numero][key] = value
    save_estado(estado)

def get_user_state(numero, key, default=None):
    return get_estado().get(numero, {}).get(key, default)

def clear_user(numero):
    estado = get_estado()
    estado[numero] = {}
    save_estado(estado)

def procesar(numero, body, resp):
    texto  = body.lower().strip()
    msg    = resp.message()
    estado = get_user_state(numero, "estado", "MENU")

    # 🧠 IA SOLO EN MENU
    if estado == "MENU":
        resultado = interpretar_mensaje(body)

        intent  = resultado["intent"]
        mensaje = resultado["mensaje"]

        if mensaje:
            msg.body(f"🤖 {mensaje}")

        if intent == "crear_turno":
            _iniciar_turno(numero, msg)
            return

        elif intent == "ver_turnos":
            _mis_turnos(numero, msg)
            return

        elif intent == "cancelar_turno":
            msg.body("Indicá fecha del turno a cancelar (dd/mm/yyyy)")
            set_user_state(numero, "estado", "ADMIN_CANCEL_FECHA")
            return

        elif intent == "consulta_general":
            msg.body(mensaje)
            return

    # RESET
    if texto in ["menu", "/start"]:
        clear_user(numero)
        msg.body(MENU_PACIENTE)
        return

    if estado == "MENU":
        manejar_menu(numero, body, msg)
        return

    if estado == "MENSAJE":
        guardar_mensaje("Paciente", numero, body)
        msg.body("✅ Mensaje recibido")
        set_user_state(numero, "estado", "MENU")
        return

    if estado == "TURNO_NOMBRE":
        set_user_state(numero, "nombre", body)
        set_user_state(numero, "estado", "TURNO_FECHA")
        msg.body("Ingresá la fecha (dd/mm/yyyy)")
        return

    if estado == "TURNO_FECHA":
        _flujo_turno_fecha(numero, body, msg)
        return

    if estado == "TURNO_HORA":
        _flujo_turno_hora(numero, body, msg)
        return

    msg.body(MENU_PACIENTE)

# ───────────────────────────────

def manejar_menu(numero, body, msg):
    opciones = {
        "1": _iniciar_turno,
        "2": _mis_turnos,
        "3": _iniciar_mensaje,
    }
    accion = opciones.get(body.strip())
    if accion:
        accion(numero, msg)
    else:
        msg.body(MENU_PACIENTE)

def _iniciar_turno(numero, msg):
    set_user_state(numero, "estado", "TURNO_NOMBRE")
    msg.body("¿Nombre y apellido?")

def _mis_turnos(numero, msg):
    lista = turnos_usuario(numero)
    if not lista:
        msg.body("No tenés turnos.")
    else:
        msg.body("\n".join(f"{t['fecha']} {t['hora']}" for t in lista))

def _iniciar_mensaje(numero, msg):
    set_user_state(numero, "estado", "MENSAJE")
    msg.body("Escribí tu mensaje.")

def _flujo_turno_fecha(numero, body, msg):
    try:
        fecha = datetime.strptime(body.strip(), "%d/%m/%Y").date()
    except:
        msg.body("Formato inválido")
        return

    fecha_str = fecha.strftime("%d/%m/%Y")
    set_user_state(numero, "fecha", fecha_str)

    libres = horarios_libres(fecha_str)
    if not libres:
        msg.body("Sin disponibilidad")
        set_user_state(numero, "estado", "MENU")
        return

    set_user_state(numero, "estado", "TURNO_HORA")
    msg.body("Horarios:\n" + "\n".join(libres))

def _flujo_turno_hora(numero, body, msg):
    hora = normalizar_hora(body)
    if not hora:
        msg.body("Hora inválida")
        return

    fecha = get_user_state(numero, "fecha")
    nombre = get_user_state(numero, "nombre")

    agregar_turno(nombre, numero, fecha, hora)
    msg.body(f"Turno confirmado {fecha} {hora}")
    clear_user(numero)
