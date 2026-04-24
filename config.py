import os

MODO_TEST = True

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

TURNOS_FILE   = "turnos.json"
BLOQUEOS_FILE = "bloqueos.json"
MENSAJES_FILE = "mensajes.json"
