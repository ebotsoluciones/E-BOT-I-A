# E-BOT-I-A
E-BOT BASIC 🦙 — Bot de turnos WhatsApp con JSON en disco Inteligencia artificial
# 🧠 E-BOT I.A

### Automatización inteligente de turnos por WhatsApp

E-BOT I.A es un sistema de automatización diseñado para negocios que necesitan gestionar turnos de forma simple, profesional y escalable, integrando inteligencia artificial sin perder control operativo.

---

## 🚀 ¿Qué es E-BOT I.A?

Es un bot de WhatsApp que permite:

* 📅 Agendar turnos automáticamente
* ❌ Cancelar turnos
* 📋 Consultar turnos existentes
* 💬 Recibir mensajes de clientes
* 🤖 Interpretar lenguaje natural con IA

Todo funcionando con una arquitectura simple, robusta y lista para producción ligera.

---

## 🧠 IA integrada (enfoque profesional)

La inteligencia artificial en E-BOT NO reemplaza el sistema.

👉 Actúa como:

* Intérprete de mensajes
* Detector de intención
* Generador de respuestas breves

Esto permite que el usuario escriba de forma natural:

> “che tenés algo mañana tipo 3?”

Y el sistema responda correctamente sin romper el flujo estructurado.

---

## ⚙️ Arquitectura

El sistema está diseñado bajo un modelo:

### 🧱 Single Tenant (1 cliente = 1 instancia)

Cada negocio tiene:

* Su propio bot
* Su propia base de datos (JSON o futura DB)
* Su propio número de WhatsApp

Esto garantiza:

✔ Simplicidad
✔ Aislamiento
✔ Fácil mantenimiento
✔ Escalabilidad comercial

---

## 🧩 Componentes principales

```bash
handlers.py    # Lógica de flujo y estados
services.py    # Reglas de negocio (turnos, horarios, validaciones)
storage.py     # Persistencia en JSON
config.py      # Configuración general
ia.py          # Interpretación con inteligencia artificial
```

---

## 🔁 Flujo del sistema

1. Usuario envía mensaje por WhatsApp
2. IA interpreta intención (crear turno, cancelar, etc.)
3. El sistema activa el flujo correspondiente
4. Se validan datos (fecha, hora, disponibilidad)
5. Se confirma o responde al usuario

---

## 📲 Ejemplo real

Usuario:

```
quiero turno mañana a la tarde
```

Respuesta:

```
🤖 Buscando disponibilidad para mañana por la tarde.

📅 Horarios disponibles:
14:00
15:00
16:00
```

---

## 🛠 Tecnologías utilizadas

* Python 3
* Flask
* Twilio (WhatsApp API)
* OpenAI API (IA)
* JSON (persistencia simple)

---

## ⚡ Instalación

### 1. Clonar repositorio

```bash
git clone https://github.com/ebotsoluciones/E-BOT-I-A.git
cd E-BOT-I-A
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Configurar variables de entorno

Crear archivo `.env`:

```env
MODO_TEST=true
TWILIO_ACCOUNT_SID=...
TWILIO_AUTH_TOKEN=...
TWILIO_WHATSAPP_FROM=whatsapp:+14155238886
OPENAI_API_KEY=...
```

### 4. Ejecutar

```bash
python app.py
```

---

## 🔐 Modo admin

Acceso a funciones avanzadas:

* Ver turnos
* Crear turnos manualmente
* Cancelar turnos
* Bloquear agenda

---

## 💡 Casos de uso

* Clínicas médicas
* Consultorios odontológicos
* Centros estéticos
* Profesionales independientes
* Servicios con agenda

---

## 💼 Modelo de negocio

E-BOT I.A está diseñado como producto:

👉 1 cliente = 1 bot independiente

Permite:

* Implementación rápida
* Personalización por cliente
* Venta como servicio

---

## 🧠 Filosofía del sistema

> La IA no reemplaza la estructura.
> La IA mejora la experiencia.

---

## 🔮 Próximas mejoras

* Base de datos (Supabase)
* Multi-canal (Web + WhatsApp)
* Reportes automáticos
* IA con memoria contextual

---

## 📄 Licencia

Uso privado / comercial bajo E-BOT Soluciones.

---

## 👤 Autor

**E-BOT Soluciones**
Automatización inteligente para negocios reales
