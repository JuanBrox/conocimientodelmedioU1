import random
from datetime import date

import streamlit as st

st.set_page_config(
    page_title="El Reino Mágico de la Naturaleza 🦄",
    page_icon="🦄",
    layout="centered",
)

# ──────────────────────────────────────────────────────────────
#  ESTILO: hadas y unicornios
# ──────────────────────────────────────────────────────────────
CSS = """
@import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@400;600;800&display=swap');

html, body, [class*="css"], .stApp, .stMarkdown, p, label, li {
    font-family: 'Baloo 2', 'Comic Sans MS', sans-serif !important;
}
.stApp {
    background: linear-gradient(135deg, #ffe3f1 0%, #ece0ff 50%, #d9f1ff 100%);
    background-attachment: fixed;
    color: #4a2c6d;
}
header[data-testid="stHeader"] { background: transparent; }
.block-container { padding-top: 1.2rem; max-width: 760px; }

.floaty span {
    position: fixed; font-size: 2rem; opacity: .28; pointer-events: none;
    z-index: 0; animation: bob 6s ease-in-out infinite;
}
@keyframes bob { 0%,100% { transform: translateY(0) rotate(-4deg); }
                 50% { transform: translateY(-14px) rotate(4deg); } }

.hero {
    text-align: center; padding: 14px 10px 6px 10px;
}
.hero h1 {
    font-size: 2.1rem; font-weight: 800; margin: 0; line-height: 1.15;
    background: linear-gradient(90deg, #ec4899, #a855f7, #3b82f6);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
}
.hero p { margin: 4px 0 0 0; font-size: 1.05rem; color: #7c3aed; }

.card {
    background: rgba(255,255,255,.92); border-radius: 22px;
    padding: 16px 20px; margin: 10px 0;
    box-shadow: 0 6px 18px rgba(168, 85, 247, .18);
    border: 2px solid #f5d0fe;
}
.card.q { font-size: 1.2rem; font-weight: 600; border-color: #d8b4fe; }
.card.count { text-align: center; font-size: 1.15rem; }
.card.count b { font-size: 2.2rem; color: #db2777; }
.item { background: #fdf4ff; border: 2px solid #f0abfc; border-radius: 16px;
        padding: 8px 12px; font-weight: 600; text-align: center; }
.stars { text-align: right; font-weight: 800; color: #d97706; font-size: 1.1rem; }
.tip { background: #fef9c3; border: 2px dashed #facc15; border-radius: 16px;
       padding: 10px 14px; margin: 8px 0; }

.stButton > button {
    background: linear-gradient(90deg, #ec4899, #a855f7);
    color: white; border: none; border-radius: 999px;
    padding: .55rem 1.4rem; font-weight: 800; font-size: 1.05rem;
    box-shadow: 0 4px 12px rgba(168, 85, 247, .35);
}
.stButton > button:hover { transform: scale(1.04); color: white; border: none; }
.stButton > button:disabled { opacity: .5; }

div[data-testid="stRadio"] label p { font-size: 1.05rem; }
div[data-testid="stExpander"] {
    background: rgba(255,255,255,.9); border-radius: 18px;
    border: 2px solid #f5d0fe;
}
div[data-testid="stExpander"] summary p { font-weight: 800; font-size: 1.1rem; }
"""
st.markdown("<style>" + CSS + "</style>", unsafe_allow_html=True)
st.markdown(
    """<div class="floaty">
    <span style="left:3%;top:14%">🦄</span><span style="right:4%;top:22%">🧚‍♀️</span>
    <span style="left:6%;top:62%">🌈</span><span style="right:6%;top:70%">✨</span>
    <span style="left:45%;top:88%">🦋</span></div>""",
    unsafe_allow_html=True,
)

# ──────────────────────────────────────────────────────────────
#  CONTENIDO: preguntas
# ──────────────────────────────────────────────────────────────
TOPICS = {
    "vivos": "🌸 Seres vivos e inertes",
    "funciones": "💫 Funciones vitales",
    "eco": "🌿 Ecosistemas",
    "reinos": "🦋 Los cinco reinos",
    "paisajes": "🏞️ Paisajes",
}


def Q(topic, text, answer, wrong, why):
    return {"topic": topic, "text": text, "answer": answer,
            "options": [answer] + wrong, "why": why}


QUESTIONS = [
    # ── Seres vivos e inertes ──
    Q("vivos", "¿Cuál de estos es un ser vivo? 🔎", "🦝 Un mapache",
      ["🏖️ La arena", "☁️ Una nube", "💎 Un mineral verde"],
      "Los mapaches están formados por células y realizan las funciones vitales. "
      "La arena, las nubes y los minerales son seres inertes."),
    Q("vivos", "¿De qué están formados los seres vivos?", "De células",
      ["De piedras", "De aire", "De arena"],
      "La materia de los seres vivos se organiza en células, unas estructuras "
      "complejas que no se encuentran en los seres inertes."),
    Q("vivos", "Los seres inertes...",
      "No están formados por células y no hacen las funciones vitales",
      ["Nacen y crecen", "Se reproducen", "Están formados por células"],
      "Los seres inertes no tienen células ni realizan las funciones vitales."),
    Q("vivos", "Un ser vivo unicelular tiene...", "Una sola célula",
      ["Muchísimas células", "Ninguna célula", "Dos células exactas"],
      "Unicelulares: una sola célula. Pluricelulares: un gran número de células."),
    Q("vivos", "Un ser vivo pluricelular tiene...", "Un gran número de células",
      ["Una sola célula", "Ninguna célula", "Solo tres células"],
      "Pluricelulares: muchas células. Por ejemplo, un animal o un roble."),
    Q("vivos", "El agua es un ser inerte, pero...",
      "Es imprescindible para que los seres vivos hagan sus funciones vitales",
      ["Es un ser vivo pequeñito", "No sirve para nada", "Solo la usan las plantas"],
      "Algunos seres inertes, como el agua, son imprescindibles para los seres vivos."),
    Q("vivos", "¿Qué característica tienen TODOS los seres vivos?",
      "Responden a los cambios de su entorno",
      ["No necesitan agua", "No tienen células", "Nunca se reproducen"],
      "Los seres vivos están formados por células, realizan las funciones vitales, "
      "necesitan agua y nutrientes y responden a los cambios de su entorno."),
    Q("vivos", "¿Qué dos seres inertes son fundamentales para los seres vivos?",
      "El agua y el aire", ["Una moneda y un lápiz", "Un coche y un tren", "Una goma y un cuaderno"],
      "El agua, el aire y el suelo son seres inertes que los seres vivos necesitan."),
    # ── Funciones vitales ──
    Q("funciones", "¿Cuáles son las tres funciones vitales?",
      "Nutrición, relación y reproducción",
      ["Comer, dormir y jugar", "Nutrición, movimiento y sueño", "Relación, respiración y crecimiento"],
      "Todos los seres vivos realizan nutrición, relación y reproducción."),
    Q("funciones", "Un flamenco mete el pico en el agua para comer. ¿Qué función vital es? 🦩",
      "Nutrición", ["Relación", "Reproducción", "Ninguna"],
      "Con la nutrición se obtienen los nutrientes necesarios para crecer y mantenerse vivos."),
    Q("funciones", "Una araña sale corriendo al notar un ruido. ¿Qué función vital es? 🕷️",
      "Relación", ["Nutrición", "Reproducción", "Ninguna"],
      "Con la función de relación, los seres vivos perciben los cambios de su entorno "
      "y elaboran respuestas."),
    Q("funciones", "Una flamenca tiene un polluelo. ¿Qué función vital es?",
      "Reproducción", ["Nutrición", "Relación", "Ninguna"],
      "La reproducción permite a los seres vivos tener descendencia."),
    Q("funciones", "¿Qué función vital permite tener descendencia (hijos)?",
      "Reproducción", ["Nutrición", "Relación", "Respiración"],
      "La reproducción puede ser asexual o sexual."),
    Q("funciones", "La reproducción puede ser...", "Asexual o sexual",
      ["Rápida o lenta", "Grande o pequeña", "Dulce o salada"],
      "Asexual o sexual, según cómo se tenga la descendencia."),
    Q("funciones", "¿Qué función vital permite percibir los cambios del entorno?",
      "Relación", ["Nutrición", "Reproducción", "Ninguna"],
      "Gracias a la relación percibimos los cambios y respondemos a ellos."),
    Q("funciones", "Un koala come hojas de eucalipto. ¿Qué función vital realiza? 🐨",
      "Nutrición", ["Relación", "Reproducción", "Ninguna"],
      "Comer es parte de la nutrición: obtiene nutrientes para crecer y mantenerse vivo."),
    Q("funciones", "Un girasol gira hacia el sol. ¿Se desplaza o se mueve? 🌻",
      "Se mueve, pero no se desplaza",
      ["Se desplaza, pero no se mueve", "Se desplaza y se mueve", "Ni se mueve ni se desplaza"],
      "Moverse es mover una parte del cuerpo. Desplazarse es cambiar de un lugar a otro. "
      "Las plantas se mueven, pero no se desplazan."),
    Q("funciones", "¿Todos los animales se desplazan?", "Casi todos",
      ["Sí, absolutamente todos", "Ninguno", "Solo los vertebrados"],
      "El libro dice que casi todos los animales son capaces de desplazarse."),
    # ── Ecosistemas ──
    Q("eco", "¿Qué es un ecosistema?",
      "El lugar donde habitan los seres vivos y las relaciones que se establecen entre ellos",
      ["Un tipo de planta", "Solo el agua de un lago", "Un animal muy grande"],
      "Un ecosistema incluye el lugar, los seres vivos y sus relaciones."),
    Q("eco", "¿Cuáles son los dos componentes de un ecosistema?",
      "El componente vivo y el componente inerte",
      ["El grande y el pequeño", "El animal y el vegetal", "El frío y el caliente"],
      "Componente vivo + componente inerte."),
    Q("eco", "¿Cuál de estos forma parte del componente VIVO?", "Las bacterias 🦠",
      ["El agua", "El suelo", "El aire"],
      "El componente vivo lo forman animales, plantas y otros seres vivos como las bacterias."),
    Q("eco", "¿Cuál de estos forma parte del componente INERTE?", "El suelo",
      ["Un pato", "Un nenúfar", "Las bacterias"],
      "El componente inerte es el medio físico: agua, suelo y aire."),
    Q("eco", "Una selva y una charca son ejemplos de...", "Ecosistemas",
      ["Paisajes transformados", "Reinos", "Funciones vitales"],
      "La selva es un ecosistema grande y la charca uno pequeño."),
    Q("eco", "Pedro dice que el patio del colegio es un ecosistema y Paula dice que no. "
             "¿Quién tiene razón?",
      "Pedro: hay seres vivos, seres inertes y relaciones entre ellos",
      ["Paula: los ecosistemas solo existen en la selva", "Paula: en el patio no hay agua",
       "Ninguno de los dos"],
      "Los ecosistemas pueden ser grandes o pequeños. En el patio hay plantas, insectos, "
      "aves, suelo, aire... ¡y se relacionan entre sí!"),
    Q("eco", "El componente inerte de un ecosistema es...",
      "El medio físico que ocupan los seres vivos",
      ["Los animales que viven allí", "Las plantas que crecen allí", "Las bacterias"],
      "El agua, el suelo y el aire forman el componente inerte."),
    # ── Reinos ──
    Q("reinos", "¿En cuántos grandes reinos se clasifican los seres vivos?", "Cinco",
      ["Dos", "Tres", "Siete"],
      "Los clasificamos en grupos llamados reinos para conocerlos mejor."),
    Q("reinos", "¿Cuáles son los cinco reinos?",
      "Moneras, protoctistas, hongos, plantas y animales",
      ["Moneras, peces, hongos, plantas y aves", "Bacterias, insectos, setas, árboles y peces",
       "Animales, plantas, minerales, agua y aire"],
      "Moneras, protoctistas, hongos, plantas y animales."),
    Q("reinos", "Las bacterias pertenecen al reino...", "Moneras",
      ["Protoctistas", "Hongos", "Plantas"],
      "Son seres microscópicos. Algunas son útiles (yogur) y otras producen enfermedades."),
    Q("reinos", "Las algas y los protozoos pertenecen al reino...", "Protoctistas",
      ["Moneras", "Plantas", "Animales"], "Habitan en el agua. Algunos son microscópicos."),
    Q("reinos", "Las setas y los mohos pertenecen al reino...", "Hongos 🍄",
      ["Plantas", "Moneras", "Animales"],
      "Los hongos no se desplazan y se alimentan de restos de otros seres vivos."),
    Q("reinos", "El roble y la hortensia pertenecen al reino...", "Plantas",
      ["Hongos", "Animales", "Protoctistas"],
      "Las plantas elaboran su propio alimento."),
    Q("reinos", "La cebra y la mariposa pertenecen al reino...", "Animales",
      ["Plantas", "Hongos", "Moneras"], "Los animales tienen órganos de los sentidos."),
    Q("reinos", "¿Qué reino se alimenta de restos de otros seres vivos y no se desplaza?",
      "Hongos", ["Plantas", "Animales", "Moneras"],
      "Los hongos carecen de órganos de los sentidos, no se desplazan y se alimentan "
      "de restos de otros seres vivos."),
    Q("reinos", "¿Qué reino elabora su propio alimento y no se desplaza, aunque sí se mueve?",
      "Plantas", ["Animales", "Hongos", "Moneras"],
      "Las plantas elaboran su propio alimento."),
    Q("reinos", "¿Qué seres vivos tienen órganos de los sentidos y casi todos se desplazan?",
      "Los animales", ["Las plantas", "Los hongos", "Las bacterias"],
      "Además, se alimentan de otros seres vivos."),
    Q("reinos", "¿Cuál de estas es una planta SIN flores?", "El helecho 🌿",
      ["El lirio", "La sabina", "La margarita"],
      "Las plantas sin flores no se reproducen por semillas: el musgo y el helecho."),
    Q("reinos", "¿Cuál de estos animales es invertebrado?", "El pulpo 🐙",
      ["El tiburón", "La tortuga", "La cebra"],
      "Invertebrados: no tienen columna vertebral (anémona, pulpo). "
      "Vertebrados: tiburón, tortuga..."),
    Q("reinos", "Los animales vertebrados tienen...", "Esqueleto interno y columna vertebral",
      ["Solo una concha", "Seis patas siempre", "Ninguna columna vertebral"],
      "Los invertebrados son los que carecen de columna vertebral."),
    Q("reinos", "Los animales ovíparos nacen...", "De huevos",
      ["Del vientre de su madre", "De semillas", "De una nube"],
      "Los vivíparos nacen del vientre de su madre."),
    Q("reinos", "Las algas fabrican su propio alimento como las plantas. ¿A qué reino pertenecen?",
      "Protoctistas", ["Plantas", "Hongos", "Moneras"],
      "¡Cuidado! Las algas son protoctistas, no plantas."),
    Q("reinos", "Los protozoos se alimentan...", "De otros seres vivos",
      ["Fabricando su alimento", "De rocas", "De luz de luna"],
      "Las algas fabrican su alimento; los protozoos se alimentan de otros seres vivos."),
    Q("reinos", "¿Para qué clasificamos los seres vivos en reinos?", "Para conocerlos mejor",
      ["Para que no se escapen", "Porque son todos iguales", "Para ponerles nombres de reyes"],
      "Existen multitud de organismos y agruparlos nos ayuda a conocerlos."),
    Q("reinos", "Algunas bacterias transforman la leche en yogur. ¿Cómo son?",
      "Útiles", ["Peligrosas", "Plantas", "Hongos"],
      "Otras bacterias, en cambio, pueden producir enfermedades como la pulmonía."),
    Q("reinos", "¿Qué animal vive en el agua, nada y pone huevos con aletas? 🐠",
      "El pez payaso", ["La iguana", "La rana", "El mirlo"],
      "El pez payaso tiene aletas y pone huevos."),
    # ── Paisajes ──
    Q("paisajes", "¿Qué es un paisaje?",
      "El aspecto que presenta el terreno al ser observado desde un lugar",
      ["Un tipo de animal", "Un ser inerte pequeñito", "Una función vital"],
      "Paisaje = aspecto del terreno observado desde un lugar determinado."),
    Q("paisajes", "¿De qué dos tipos pueden ser los paisajes?", "Naturales y transformados",
      ["Grandes y pequeños", "Vivos e inertes", "De día y de noche"],
      "Naturales (sin intervención humana) y transformados (modificados por el ser humano)."),
    Q("paisajes", "En un paisaje natural...", "No hay intervención humana",
      ["Hay muchas ciudades", "Hay carreteras", "Hay fábricas"],
      "En ellos se aprecian el agua, el relieve y las plantas."),
    Q("paisajes", "En un paisaje transformado...",
      "Se ven modificaciones hechas por el ser humano",
      ["No hay agua", "Solo hay montañas", "No hay ningún ser vivo"],
      "Las personas modifican el entorno para vivir, aprovechar recursos o desplazarse."),
    Q("paisajes", "El relieve lo componen...",
      "Las distintas formas del terreno: montañas, llanuras, valles...",
      ["Los animales", "Los ríos y los lagos", "Las nubes"],
      "En la costa también hay playas y acantilados."),
    Q("paisajes", "¿Qué dos cosas pueden verse en un paisaje de COSTA?", "Playas y acantilados",
      ["Lagos y lagunas", "Minas y cultivos", "Ríos y valles"],
      "La costa es la zona donde el agua de mares y océanos toca la tierra."),
    Q("paisajes", "En un paisaje de INTERIOR el agua se encuentra en...", "Ríos, lagos y lagunas",
      ["Mares y océanos", "Playas", "Acantilados"],
      "Los mares y océanos están en la costa."),
    Q("paisajes", "¿Por qué las plantas son diferentes en cada zona?",
      "Porque dependen de la temperatura, las lluvias y la humedad",
      ["Porque les gusta cambiar", "Porque no necesitan agua", "Porque las plantan los niños"],
      "Cada zona tiene su temperatura, lluvias y humedad del terreno."),
    Q("paisajes", "¿Para qué se construye un embalse?",
      "Para almacenar agua y hacerla llegar a la población",
      ["Para cultivar patatas", "Para sacar minerales", "Para que aterricen aviones"],
      "Los embalses almacenan el agua y los canales la distribuyen."),
    Q("paisajes", "¿Para qué sirve una mina? ⛏️", "Para obtener materiales",
      ["Para almacenar agua", "Para viajar más rápido", "Para criar animales"],
      "Los materiales se usan para construir edificios y fabricar objetos."),
    Q("paisajes", "Los campos de cultivo, las granjas y los establos sirven para...",
      "Obtener alimentos", ["Obtener agua", "Comunicarse", "Construir carreteras"],
      "La obtención de alimentos altera el entorno al sustituir el medio natural."),
    Q("paisajes", "Carreteras, puertos, aeropuertos y puentes son...",
      "Vías de comunicación", ["Embalses", "Minas", "Campos de cultivo"],
      "Sirven para desplazarse y transportar mercancías."),
    Q("paisajes", "Viviendas, hospitales, comercios, colegios y fábricas son...",
      "Edificaciones", ["Vías de comunicación", "Embalses", "Plantas"],
      "Se agrupan formando pueblos o ciudades."),
    Q("paisajes", "Una explotación forestal sirve para obtener...",
      "Materiales, como la madera", ["Agua", "Alimentos de granja", "Peces"],
      "Las minas y las explotaciones forestales proporcionan materiales."),
]

FRASES = [
    ("En un paisaje de costa, el agua se encuentra en los ríos y las lagunas.", False,
     "En la costa el agua está en mares y océanos. Los ríos y las lagunas son del paisaje de interior."),
    ("En un paisaje de interior se pueden observar lagos y playas.", False,
     "En un paisaje de interior hay ríos, lagos y lagunas. Las playas son de la costa."),
    ("El relieve lo componen las distintas formas del terreno.", True,
     "¡Correcto! Montañas, llanuras, valles..."),
    ("En un paisaje natural puede haber carreteras y vías de tren.", False,
     "En un paisaje natural no hay intervención humana. Las carreteras son de un paisaje transformado."),
    ("Las explotaciones forestales transforman el paisaje natural.", True,
     "¡Correcto! Son una intervención humana para obtener materiales."),
    ("Los seres inertes realizan las funciones vitales.", False,
     "Los seres vivos realizan las funciones vitales. Los inertes no."),
    ("Los animales, las plantas y las rocas son seres vivos.", False,
     "Los animales y las plantas son seres vivos, pero las rocas son seres inertes."),
    ("Una gaviota es un organismo unicelular.", False,
     "Una gaviota es pluricelular: tiene un gran número de células."),
    ("La función de nutrición permite percibir los cambios en el entorno.", False,
     "Eso lo hace la función de relación. La nutrición sirve para obtener nutrientes."),
]

FRASES_Q = [
    {"topic": "frases",
     "text": f"«{f}»<br><span style='font-size:1rem'>¿Es verdadera o falsa?</span>",
     "answer": "Verdadera ✅" if v else "Falsa ❌",
     "options": ["Verdadera ✅", "Falsa ❌"],
     "why": why}
    for f, v, why in FRASES
]

VIVO, INERTE = "Ser vivo 🌱", "Ser inerte 🪨"
ITEMS_VIVO = {
    "🏖️ Arena": INERTE, "☁️ Nube": INERTE, "🦝 Mapache": VIVO, "🦎 Iguana": VIVO,
    "🪨 Roca": INERTE, "💧 Agua": INERTE, "🍄 Seta": VIVO, "🐸 Rana": VIVO,
    "💎 Mineral": INERTE, "🌳 Roble": VIVO, "🦠 Bacteria": VIVO, "🐠 Pez payaso": VIVO,
}

REINOS = ["Moneras", "Protoctistas", "Hongos", "Plantas", "Animales"]
ITEMS_REINOS = {
    "🦠 Bacteria": "Moneras", "🌊 Alga": "Protoctistas", "🔬 Protozoo": "Protoctistas",
    "🍄 Seta": "Hongos", "🍞 Moho del pan": "Hongos", "🌳 Roble": "Plantas",
    "🌿 Helecho": "Plantas", "🌸 Hortensia": "Plantas", "🐙 Pulpo": "Animales",
    "🦈 Tiburón": "Animales", "🦓 Cebra": "Animales", "🦋 Mariposa": "Animales",
}

NAT, TRANS = "Natural 🌲", "Transformado 🏗️"
ITEMS_PAISAJE = {
    "🏞️ Río con bosque a los lados": NAT, "🏖️ Playa tranquila": NAT,
    "🌊 Acantilado": NAT, "⛰️ Montaña sin edificios": NAT,
    "🌴 Costa con palmeras y rocas": NAT,
    "💦 Embalse (presa)": TRANS, "🏙️ Ciudad": TRANS, "⛏️ Mina": TRANS,
    "🌾 Campo de cultivo": TRANS, "✈️ Aeropuerto": TRANS, "🛣️ Autopista": TRANS,
    "🪵 Explotación forestal": TRANS, "🏘️ Pueblo con viñedos": TRANS,
}

PRAISE = ["¡Magnífico! 🦄", "¡Brillante como una hada! 🧚", "¡Súper! ⭐", "¡Eso es! 🌈",
          "¡Qué lista eres! ✨", "¡Perfecto! 💖"]
ENCOURAGE = ["¡Casi! Fíjate bien 👀", "No pasa nada, así se aprende 💜",
             "¡Ánimo! La próxima va bien 🍀", "Uy, esta era difícil 🌸"]

# ──────────────────────────────────────────────────────────────
#  MOTOR DE PREGUNTAS
# ──────────────────────────────────────────────────────────────
S = st.session_state
S.setdefault("stars", 0)


def reset(prefix):
    for k in [k for k in S.keys() if k.startswith(prefix + "__")]:
        del S[k]


def _check(key):
    i = S[f"{key}__i"]
    choice = S.get(f"{key}__r{i}")
    if choice is None:
        S[f"{key}__warn"] = True
        return
    q = S[f"{key}__qs"][i]
    ok = choice == q["answer"]
    S[f"{key}__warn"] = False
    S[f"{key}__checked"] = True
    S[f"{key}__ok"] = ok
    S[f"{key}__msg"] = random.choice(PRAISE if ok else ENCOURAGE)
    if ok:
        S[f"{key}__score"] += 1
        S["stars"] += 1


def _next(key):
    S[f"{key}__i"] += 1
    S[f"{key}__checked"] = False
    S[f"{key}__warn"] = False


def final_message(pct):
    if pct >= 0.9:
        return "🦄 ¡Eres una Hada Maestra de la Naturaleza! ¡Estás lista para el examen!"
    if pct >= 0.7:
        return "🧚 ¡Muy bien! Repasa los fallos y estarás lista."
    if pct >= 0.5:
        return "🌈 Vas por buen camino. Repasa en «Aprende» y vuelve a intentarlo."
    return "🌸 Hoy toca repasar un poquito más. ¡Tú puedes!"


def quiz(key, pool, n):
    if f"{key}__qs" not in S:
        chosen = random.sample(pool, min(n, len(pool)))
        S[f"{key}__qs"] = [dict(q, options=random.sample(q["options"], len(q["options"])))
                           for q in chosen]
        S[f"{key}__i"] = 0
        S[f"{key}__score"] = 0
        S[f"{key}__checked"] = False
        S[f"{key}__ok"] = False
        S[f"{key}__warn"] = False
    qs, i = S[f"{key}__qs"], S[f"{key}__i"]
    total = len(qs)

    if i >= total:
        score = S[f"{key}__score"]
        pct = score / total
        st.markdown(
            f"<div class='card count'>Has acertado<br><b>{score} / {total}</b><br>"
            f"{'⭐' * round(pct * 5)}</div>", unsafe_allow_html=True)
        st.success(final_message(pct))
        if pct >= 0.9 and not S.get(f"{key}__fin"):
            S[f"{key}__fin"] = True
            st.balloons()
        st.button("🔄 Jugar otra vez", on_click=reset, args=(key,), key=f"{key}__again")
        return

    checked = S[f"{key}__checked"]
    st.progress(i / total, text=f"Pregunta {i + 1} de {total}  ·  aciertos: {S[f'{key}__score']}")
    q = qs[i]
    st.markdown(f"<div class='card q'>{q['text']}</div>", unsafe_allow_html=True)
    st.radio("Elige tu respuesta", q["options"], index=None, key=f"{key}__r{i}",
             disabled=checked, label_visibility="collapsed")

    if checked:
        if S[f"{key}__ok"]:
            st.success(f"{S[f'{key}__msg']}  \n{q['why']}")
        else:
            st.error(f"{S[f'{key}__msg']}  \n**Respuesta correcta:** {q['answer']}  \n{q['why']}")
        last = (i + 1 == total)
        st.button("Ver mi resultado 🏆" if last else "Siguiente ➡️", on_click=_next,
                  args=(key,), key=f"{key}__next{i}")
    else:
        if S.get(f"{key}__warn"):
            st.warning("Elige una respuesta primero 🧚")
        st.button("Comprobar ✨", on_click=_check, args=(key,), key=f"{key}__chk{i}")


def _check_cls(key):
    names = [n for n, _ in S[f"{key}__items"]]
    if any(S.get(f"{key}__s_{n}") is None for n in names):
        S[f"{key}__warn"] = True
        return
    S[f"{key}__warn"] = False
    S[f"{key}__done"] = True
    good = sum(S[f"{key}__s_{n}"] == c for n, c in S[f"{key}__items"])
    S[f"{key}__good"] = good
    S["stars"] += good


def classify(key, items, cats, n, intro):
    if f"{key}__items" not in S:
        S[f"{key}__items"] = random.sample(list(items.items()), min(n, len(items)))
        S[f"{key}__done"] = False
        S[f"{key}__warn"] = False
    chosen, done = S[f"{key}__items"], S[f"{key}__done"]
    st.markdown(f"<div class='card'>{intro}</div>", unsafe_allow_html=True)
    for name, cat in chosen:
        c1, c2 = st.columns(2)
        c1.markdown(f"<div class='item'>{name}</div>", unsafe_allow_html=True)
        c2.selectbox(name, cats, index=None, placeholder="Elige...",
                     key=f"{key}__s_{name}", label_visibility="collapsed", disabled=done)
        if done:
            mine = S.get(f"{key}__s_{name}")
            if mine == cat:
                c2.caption("✅ ¡Bien!")
            else:
                c2.caption(f"❌ Era: **{cat}**")
    if done:
        good, total = S[f"{key}__good"], len(chosen)
        st.markdown(f"<div class='card count'>Has acertado<br><b>{good} / {total}</b></div>",
                    unsafe_allow_html=True)
        st.success(final_message(good / total))
        if good == total and not S.get(f"{key}__fin"):
            S[f"{key}__fin"] = True
            st.balloons()
        st.button("🔄 Otra ronda", on_click=reset, args=(key,), key=f"{key}__again")
    else:
        if S.get(f"{key}__warn"):
            st.warning("Elige una respuesta en todas las filas 🧚")
        st.button("Comprobar ✨", on_click=_check_cls, args=(key,), key=f"{key}__chk")


# ──────────────────────────────────────────────────────────────
#  PÁGINAS
# ──────────────────────────────────────────────────────────────
st.markdown(
    "<div class='hero'><h1>🦄 El Reino Mágico<br>de la Naturaleza 🧚‍♀️</h1>"
    "<p>Conocimiento del Medio · Unidad 1 · 3.º de Primaria</p></div>",
    unsafe_allow_html=True,
)
st.markdown(f"<div class='stars'>⭐ {S['stars']} estrellas mágicas</div>", unsafe_allow_html=True)

PAGES = ["🏰 Inicio", "📖 Aprende", "🎮 Juega", "🏆 Examen final"]
page = st.radio("Menú", PAGES, horizontal=True, label_visibility="collapsed", key="page")

# ── INICIO ───────────────────────────────────────────────────
if page == PAGES[0]:
    days = (date(2026, 11, 2) - date.today()).days
    if days > 1:
        txt = f"Faltan<br><b>{days}</b><br>días para la prueba del lunes 2 de noviembre"
    elif days == 1:
        txt = "¡<b>Mañana</b> es la prueba!<br>Repaso suave y a dormir pronto 🌙"
    elif days == 0:
        txt = "¡<b>Hoy</b> es la prueba!<br>Tú puedes, Carla 💖"
    else:
        txt = "La prueba ya pasó. ¡Seguro que lo hiciste genial! 🌟"
    st.markdown(f"<div class='card count'>{txt}</div>", unsafe_allow_html=True)

    st.markdown("""
<div class='card'>
<b>¿Qué entra en la prueba?</b> (Tema 1: Seres vivos)<br>
🌸 Seres vivos y seres inertes<br>
💫 Las funciones vitales<br>
🌿 Los ecosistemas<br>
🦋 Los cinco reinos<br>
🏞️ Paisajes naturales y transformados
</div>
<div class='card'>
<b>🗓️ Plan mágico de repaso</b><br>
<b>Miércoles:</b> seres vivos y funciones vitales<br>
<b>Jueves:</b> ecosistemas y reinos (moneras, protoctistas, hongos)<br>
<b>Viernes:</b> plantas y animales<br>
<b>Sábado:</b> paisajes naturales y transformados<br>
<b>Domingo:</b> Examen final de práctica 🏆<br>
<i>Cada día: lee «Aprende» y juega 10 minutitos.</i>
</div>
""", unsafe_allow_html=True)
    st.info("Pulsa **📖 Aprende** para repasar y **🎮 Juega** para practicar.")

# ── APRENDE ──────────────────────────────────────────────────
elif page == PAGES[1]:
    st.markdown("<div class='card'>Abre cada tarjeta mágica y léela con calma. "
                "¡Luego juega para comprobar lo que has aprendido! ✨</div>",
                unsafe_allow_html=True)

    with st.expander("🌸 Seres vivos y seres inertes", expanded=True):
        st.markdown("""
**Seres vivos** 🦝🌳🍄
- Están formados por **células**.
- Realizan las **funciones vitales** (nacer, crecer, reproducirse y adaptarse).
- Necesitan **agua y nutrientes**.
- **Responden a los cambios** de su entorno.
- Pueden ser **unicelulares** (una sola célula) o **pluricelulares** (muchísimas células).

**Seres inertes** 🪨☁️💧
- **No** están formados por células.
- **No** realizan las funciones vitales.
- Algunos, como el **agua**, son imprescindibles para los seres vivos.
""")
    with st.expander("💫 Las funciones vitales"):
        st.markdown("""
Todo ser vivo hace **tres funciones vitales**:

| Función | ¿Para qué sirve? | Ejemplo |
|---|---|---|
| 🍽️ **Nutrición** | Obtener los nutrientes para crecer y mantenerse vivo | Un flamenco comiendo |
| 👀 **Relación** | Percibir los cambios del entorno y responder | Una araña huye de un ruido |
| 🐣 **Reproducción** | Tener descendencia (asexual o sexual) | Una flamenca con su polluelo |

<div class='tip'>🧚 <b>Truco:</b> <b>N</b>utrición = comer · <b>R</b>elación = notar y responder · <b>R</b>eproducción = tener hijos.</div>

**Desplazarse o moverse**
- **Desplazarse** = cambiar de un lugar a otro (un caballo corre 🐎).
- **Moverse** = mover alguna parte del cuerpo (un girasol 🌻 gira hacia el sol, pero no se desplaza).
- Casi todos los animales se desplazan. Las plantas no se desplazan, pero sí se mueven.
""", unsafe_allow_html=True)
    with st.expander("🌿 Los ecosistemas"):
        st.markdown("""
Un **ecosistema** es el lugar donde habitan los seres vivos, e incluye las **relaciones** que hay entre ellos.
Puede ser **grande** (una selva 🌴) o **pequeño** (una charca 🐸).

Tiene **dos componentes**:
- 🌱 **Componente vivo:** animales, plantas y otros seres vivos como las bacterias.
- 💧 **Componente inerte:** el medio físico: **agua, suelo y aire**.

<div class='tip'>🧚 El patio del colegio también es un ecosistema: tiene seres vivos, seres inertes y relaciones entre ellos.</div>
""", unsafe_allow_html=True)
    with st.expander("🦋 Los cinco reinos"):
        st.markdown("""
Los seres vivos se clasifican en **cinco grandes reinos** para conocerlos mejor:

| Reino | Cómo son | Ejemplos |
|---|---|---|
| 🦠 **Moneras** | Microscópicos. Viven en diferentes medios. Algunas son útiles (yogur) y otras producen enfermedades | Bacterias |
| 🌊 **Protoctistas** | Habitan en el agua. Algunos son microscópicos | **Algas** (fabrican su alimento) y **protozoos** (se alimentan de otros seres vivos) |
| 🍄 **Hongos** | Sin órganos de los sentidos. No se desplazan. Se alimentan de restos de otros seres vivos | Setas y mohos |
| 🌳 **Plantas** | Sin órganos de los sentidos. No se desplazan, pero sí se mueven. Elaboran su alimento | Con flores: sabina, lirio · Sin flores: musgo, helecho |
| 🐙 **Animales** | Tienen órganos de los sentidos. Casi todos se desplazan. Se alimentan de otros seres vivos | Vertebrados e invertebrados |

**Animales:**
- 🦈 **Vertebrados:** esqueleto interno y columna vertebral (tiburón, tortuga).
- 🐙 **Invertebrados:** sin columna vertebral (anémona, pulpo).
- 🥚 **Ovíparos:** nacen de huevos. 🤰 **Vivíparos:** nacen del vientre de su madre.

**Plantas:**
- 🌷 **Con flores:** se reproducen por semillas.
- 🌿 **Sin flores:** no se reproducen por semillas.

<div class='tip'>🧚 <b>Ojo:</b> las algas fabrican su comida como las plantas, pero son <b>protoctistas</b>, ¡no plantas!</div>
""", unsafe_allow_html=True)
    with st.expander("🏞️ Paisajes naturales y transformados"):
        st.markdown("""
El **paisaje** es el aspecto que presenta el terreno al ser observado desde un lugar determinado.

**🌲 Paisajes naturales:** no hay intervención humana. Se aprecian el agua, el relieve y las plantas.
- 💧 **Agua:** en la **costa** (mares y océanos) · en el **interior** (ríos, lagos y lagunas).
- ⛰️ **Relieve:** las formas del terreno: montañas, llanuras, valles... En la costa: playas y acantilados.
- 🌿 **Plantas:** son distintas en cada zona según la temperatura, las lluvias y la humedad.

**🏗️ Paisajes transformados:** se ven las modificaciones que hace el ser humano para vivir, aprovechar recursos o desplazarse.
- 🏘️ **Edificaciones:** viviendas, hospitales, comercios, colegios, fábricas → forman **pueblos o ciudades**.
- 🌾 **Alimentos:** campos de cultivo, granjas y establos.
- 💦 **Agua:** **embalses** (almacenan agua) y **canales** (la distribuyen).
- ⛏️ **Materiales:** minas y explotaciones forestales.
- 🛣️ **Vías de comunicación:** carreteras, puertos, aeropuertos y puentes.
""", unsafe_allow_html=True)
    with st.expander("✏️ Preguntas del libro con su respuesta"):
        st.markdown("""
- **¿Qué es un ser inerte fundamental para los seres vivos?** El agua (y el aire y el suelo).
- **¿Todos los seres vivos se desplazan?** No: las plantas y los hongos no se desplazan.
- **¿Qué función vital es más importante?** Ninguna: las tres son necesarias para vivir.
- **¿Qué tienen en común un elefante, una medusa y una bacteria?** Son seres vivos: tienen células y hacen las funciones vitales.
- **¿Por qué no hay las mismas plantas en todo el planeta?** Porque dependen de la temperatura, las lluvias y la humedad.
- **Construcciones que modifican el paisaje:** presa/embalse (almacena agua), mina (materiales), autopista (comunicación) y central/fábrica (producir).
- **Una cosa en común y una diferencia entre paisaje natural y transformado:** En común: ambos tienen agua, relieve y plantas. Diferencia: en el transformado hay modificaciones hechas por el ser humano.
""")

# ── JUEGA ────────────────────────────────────────────────────
elif page == PAGES[2]:
    GAMES = ["🧠 Preguntas por temas", "🌱 ¿Vivo o inerte?", "🦄 Clasifica los reinos",
             "🏞️ Natural o transformado", "🔍 Verdadero o falso"]
    game = st.selectbox("¿A qué quieres jugar?", GAMES)
    st.divider()
    if game == GAMES[0]:
        tkey = st.selectbox("Elige un tema", list(TOPICS.keys()), format_func=TOPICS.get)
        pool = [q for q in QUESTIONS if q["topic"] == tkey]
        quiz(f"q_{tkey}", pool, 8)
    elif game == GAMES[1]:
        classify("cls_vivo", ITEMS_VIVO, [VIVO, INERTE], 8,
                 "¿Es un <b>ser vivo</b> o un <b>ser inerte</b>? 🔎")
    elif game == GAMES[2]:
        classify("cls_reinos", ITEMS_REINOS, REINOS, 8,
                 "¿A qué <b>reino</b> pertenece cada uno? 🦋")
    elif game == GAMES[3]:
        classify("cls_paisaje", ITEMS_PAISAJE, [NAT, TRANS], 8,
                 "¿Es un paisaje <b>natural</b> o <b>transformado</b> por el ser humano? 🏞️")
    else:
        quiz("frases", FRASES_Q, len(FRASES_Q))

# ── EXAMEN FINAL ─────────────────────────────────────────────
else:
    st.markdown("<div class='card'>🏆 <b>Examen final de práctica</b>: 15 preguntas de todo el tema, "
                "mezcladas. ¡Como si fuera el examen de verdad!</div>", unsafe_allow_html=True)
    quiz("examen", QUESTIONS + FRASES_Q, 15)

st.markdown("<br><center style='opacity:.7'>Hecho con 💖, unicornios y hadas 🦄🧚‍♀️</center>",
            unsafe_allow_html=True)
