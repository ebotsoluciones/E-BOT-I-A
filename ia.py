import json
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

PROMPT_BASE = """
Sos un asistente de WhatsApp para gestión de turnos de un negocio.

Tu función NO es conversar libremente ni tomar decisiones finales.
Tu función es interpretar mensajes de usuarios y devolver información estructurada.

Intenciones posibles:
- crear_turno
- ver_turnos
- cancelar_turno
- consulta_general
- desconocido

Extraer:
- fecha
- hora

Responder SIEMPRE en JSON:

{
  "intent": "",
  "fecha": "",
  "hora": "",
  "mensaje": ""
}
"""

def interpretar_mensaje(texto_usuario: str) -> dict:
    try:
        response = client.chat.completions.create(
            model="gpt-5-mini",
            messages=[
                {"role": "system", "content": PROMPT_BASE},
                {"role": "user", "content": texto_usuario}
            ],
            temperature=0.2
        )

        contenido = response.choices[0].message.content.strip()

        if contenido.startswith("```"):
            contenido = contenido.split("```")[1]

        data = json.loads(contenido)

        return {
            "intent": data.get("intent", "desconocido"),
            "fecha": data.get("fecha", ""),
            "hora": data.get("hora", ""),
            "mensaje": data.get("mensaje", "")
        }

    except Exception:
        return {
            "intent": "desconocido",
            "fecha": "",
            "hora": "",
            "mensaje": ""
        }
