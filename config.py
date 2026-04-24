import os

# Modo test (permite usar "adm")
MODO_TEST = os.getenv("MODO_TEST", "true").lower() == "true"

# Admins (opcional)
ADMINS = []

# Archivos JSON
TURNOS_FILE   = "turnos.json"
BLOQUEOS_FILE = "bloqueos.json"
MENSAJES_FILE = "mensajes.json"
