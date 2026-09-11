import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Crónicas de Ambarino",
    page_icon="🤠",
    layout="centered"
)

# Cargar FontAwesome para íconos vectoriales de alta calidad
st.markdown(
    '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">',
    unsafe_allow_html=True
)

# CSS Personalizado: Tema Far West / Vintage Premium
st.markdown("""
    <style>
    /* Estilo de fondo principal con gradiente oscuro y elegante */
    .stApp {
        background: linear-gradient(135deg, #1a1612 0%, #2c221a 50%, #120f0d 100%);
        color: #e6d7c3;
        font-family: 'Georgia', serif;
    }
    
    /* Título Principal */
    .hero-title {
        text-align: center;
        font-size: 2.8rem;
        font-weight: 800;
        color: #d4a359;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.8);
        padding: 10px 0;
        letter-spacing: 2px;
    }
    
    .hero-subtitle {
        text-align: center;
        font-size: 1.1rem;
        color: #a8947d;
        font-style: italic;
        margin-bottom: 25px;
    }

    /* Estilizado del Sidebar (Menú Lateral) */
    [data-testid="stSidebar"] {
        background-color: #120e0b !important;
        border-right: 1px solid #3d2f23;
    }
    
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] label, [data-testid="stSidebar"] h3 {
        color: #d4a359 !important;
    }

    /* Tarjetas de contenido (Capítulos) */
    .chapter-card {
        background: rgba(40, 32, 26, 0.65);
        border: 1px solid #4a3828;
        border-radius: 12px;
        padding: 25px;
        margin-bottom: 30px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(5px);
    }
    
    /* Encabezado del capítulo */
    .chapter-header {
        color: #f1c40f;
        font-size: 1.8rem;
        border-bottom: 1px dashed #5c4531;
        padding-bottom: 10px;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        gap: 12px;
    }
    
    /* Párrafos del texto */
    .paragraph-text {
        font-size: 1.12rem;
        line-height: 1.85;
        color: #e2d3c1;
        text-align: justify;
        margin-bottom: 15px;
    }

    /* Iconos personalizados con FontAwesome */
    .custom-icon {
        color: #d4a359;
    }
    </style>
""", unsafe_allow_html=True)

# Título y presentación
st.markdown('<div class="hero-title"><i class="fa-solid fa-hat-cowboy custom-icon"></i> CRÓNICAS DE AMBARINO</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle"><i class="fa-solid fa-scroll custom-icon"></i> Relatos de forajidos, nieve y supervivencia</div>', unsafe_allow_html=True)
st.write("---")

# Base de datos de los capítulos con íconos vectoriales asociados
capitulos = [
    {
        "numero": 1,
        "titulo": "Capítulo 1: El Salto y el Silencio de Ambarino",
        "icono": "fa-solid fa-train-subway",
        "imagen": "imagenes/cap1.jpg",
        "texto": [
            "La adrenalina aún bombardeaba sus corazones mientras corrían por el techo congelado del vagón de cola. Detrás, el tren seguía su marcha inexorable, silbando vapor hacia el cielo plomizo de las montañas Ambarino. Arthur Morgan lideraba el camino, con su abrigo rojo sucio agitando al viento gélido. Hosea Matthews, el estratega mayor, y Bill Williamson, el músculo, lo seguían de cerca, cada uno cargando con un fardo de botín que parecía pesar más que su propia conciencia.",
            "\"¡Rápido! No podemos permitir que nos alcancen!\" gritó Arthur, su voz apenas un susurro frente al rugido del tren y el viento. \"Ya nos han identificado, los federales no tardarán en movilizarse!\"",
            "\"¡Ese salto es una locura, Arthur!\" exclamó Hosea, mirando el precipicio que se abría a su lado, cubierto de nieve fresca y rocas afiladas.",
            "\"¡O saltamos o nos encierran para siempre!\" replicó Arthur, sin detenerse. \"¡Confíen en mí, vamos!\"",
            "Y saltaron. Tres siluetas negras contra la inmensidad blanca de Ambarino, flotando momentáneamente en el aire antes de rodar por la ladera, hundiéndose en la nieve profunda. El tren siguió su camino, ajeno al drama que se desarrollaba en su estela.",
            "Horas más tarde, tras caminar penosamente por la nieve hasta la cintura, encontraron un refugio precario en una pequeña cueva oculta entre los pinos helados. El silencio en Ambarino era absoluto, solo interrumpido por el crujido de la madera en el pequeño fuego que Arthur había logrado encender.",
            "\"Bueno, eso fue... intenso,\" dijo Hosea, frotándose las manos sobre las llamas, con su rostro curtido reflejando el calor. \"No habíamos tenido un atraco tan apretado desde Blackwater.\"",
            "\"Pero el botín, Hosea, ¡mira el botín!\" exclamó Bill, desenrollando uno de los fardos para revelar lingotes de oro y fajos de billetes. \"Valió la pena el riesgo.\"",
            "\"Vale la pena si sobrevivimos para gastarlo, Bill,\" recordó Arthur, con su mirada fija en el fuego. \"No sabemos cuántos agentes de la ley hay en la zona. Nos han identificado, Arthur. Eso significa que somos hombres marcados.\"",
            "\"Siempre hemos sido hombres marcados, Arthur,\" dijo Hosea con una sonrisa amarga. \"Solo que ahora la recompensa por nuestras cabezas es mayor.\"",
            "Se quedaron en silencio por un momento, cada uno sumido en sus propios pensamientos. El frío comenzaba a colarse en la cueva, recordándoles la fragilidad de su situación.",
            "\"Hosea, ¿crees que...\" comenzó Arthur, pero no terminó la frase.",
            "\"Sé lo que vas a preguntar, Arthur,\" dijo Hosea, poniéndole una mano en el hombro. \"Y la respuesta es sí, creo que Dutch y los demás están bien. Son supervivientes, igual que nosotros.\"",
            "\"Pero ellos estaban en el otro tren, Hosea. El que iba a Valentine,\" recordó Arthur con preocupación.",
            "\"Lo sé, Arthur. Pero Dutch siempre tiene un plan. Confía en él,\" dijo Hosea, aunque su voz no sonaba tan convencida como quería parecer.",
            "Bill, ajeno a la conversación, estaba ocupado contando el botín. \"¡Casi cinco mil dólares en efectivo! Y el oro... ¡Dutch se pondrá furioso cuando sepa que nos quedamos con todo!\"",
            "\"No nos quedamos con todo, Bill,\" corrigió Arthur. \"Le daremos su parte a Dutch. Siempre lo hacemos.\"",
            "\"Pero...\" comenzó Bill, pero la mirada de Arthur lo silenció.",
            "\"Descansaremos unas horas y mañana seguiremos moviéndonos,\" dijo Arthur, levantándose. \"No podemos quedarnos aquí por mucho tiempo. Los federales no se rendirán tan fácilmente.\"",
            "\"¿Adónde vamos, Arthur?\" preguntó Bill, con temor en la voz.",
            "\"Hacia el oeste. A través de la nieve y las montañas. Encontraremos un lugar seguro para escondernos y planear nuestro próximo movimiento,\" dijo Arthur, mirando hacia la oscuridad que rodeaba la cueva.",
            "Hosea asintió en silencio. \"Hacia el oeste. Es nuestra única opción.\"",
            "Se acomodaron como pudieron en la cueva, buscando el calor del fuego y de sus propios cuerpos. El sonido del viento aullando entre los pinos era un recordatorio constante de la implacable naturaleza de Ambarino.",
            "\"Mañana será un día largo,\" dijo Arthur, cerrando los ojos. \"Mañana seguiremos huyendo por la nieve y las montañas. Huyendo de la ley, de nuestros pasados y de nosotros mismos.\""
        ]
    },
    {
        "numero": 2,
        "titulo": "Capítulo 2: Sangre en la Nieve",
        "icono": "fa-solid fa-person-rifle",
        "imagen": "imagenes/cap2.jpg",
        "texto": [
            "El amanecer trajo consigo un viento helado que cortaba la piel como navajas. Arthur, Hosea y Bill abandonaron la cueva a pie, abriéndose paso con dificultad entre la nieve densa de las montañas de Ambarino. Caminar sin montura en ese infierno blanco era una sentencia de muerte lenta, y lo sabían.",
            "\"Necesitamos caballos o moriremos congelados antes de que los federales miren este valle\", gruñó Bill, tiritando violentamente mientras se ajustaba el abrigo.",
            "La suerte —o la desgracia— no tardó en cruzarse en su camino. Cerca de un paso montañoso, interceptaron a un pequeño grupo de cazadores locales que acampaban junto a la senda. No hubo espacio para la diplomacia. Acorralados por la desesperación, desenfundaron. El estruendo de los revólveres retumbó en el silencio del valle, marcando la nieve fresca con manchas rojas. En cuestión de segundos, los tres hombres yacían inmóviles sobre el manto blanco. Arthur apretó los dientes, sintiendo el peso de lo que acababan de hacer, pero no había tiempo para remordimientos: montaron las bestias aún agitadas y continuaron hacia el oeste.",
            "Con los caballos al trote, avanzaron hasta llegar a un pequeño asentamiento de cabañas cubiertas de carámbanos. Pero el alivio duró poco. Del interior de los establos y de la casa principal salieron hombres armados con ponchos y sombreros desgastados.",
            "\"¡O'Driscolls!\", gritó Hosea, desenfundando con rapidez veloz.",
            "\"¡Maldita sea, Colm y sus perros están por todas partes!\", vociferó Arthur mientras desmontaba de un salto y se parapetaba tras una cerca de madera.",
            "El aire se llenó del silbido de las balas y el olor acre de la pólvora. Los O'Driscoll los superaban en número, disparando desde las ventanas de las cabañas. Arthur abatió a dos que intentaban flanquearlos, mientras Hosea cubría la retaguardia con su carabina. Sin embargo, Bill, impulsivo y cegado por la rabia, avanzó demasiado al descubierto.",
            "Un disparo seco resonó sobre el tiroteo. Bill soltó un alarido de dolor y cayó sobre la nieve, sujetándose el hombro derecho, donde la sangre comenzaba a empapar su chaqueta.",
            "\"¡Me dieron! ¡Maldita sea, Arthur, me dieron!\", bramó Bill entre dientes.",
            "\"¡Cúbreme, Hosea!\", ordenó Arthur.",
            "Avanzó entre el fuego cruzado, agarró a Bill por el cuello del abrigo y lo arrastró de regreso tras el parapeto de tablas. Con disparos precisos, Arthur y Hosea lograron abatir al último de los emboscadores, dejando el campamento de cabañas sumido en un silencio sepulcral, interrumpido solo por los quejidos de Bill.",
            "Hosea usó un pedazo de tela limpia para vendar apretadamente el brazo herido de Bill. \"La bala pasó de largo, Bill, pero vas a necesitar un médico si no quieres perder el brazo por una infección\".",
            "\"Puedo continuar...\", masculló Bill, pálido y sudando frío a pesar del clima gélido.",
            "Apoyaron a Bill sobre su caballo y apretaron el paso, dejando atrás el rastro de casquillos y cuerpos. El terreno comenzó a descender paulatinamente, bordeando un camino flanqueado por pinos cubiertos de nieve.",
            "A lo lejos, recortadas contra el paisaje blanco, dos figuras a caballo los aguardaban en medio de la senda. Arthur llevó de inmediato la mano al revólver, pero Hosea levantó una mano para detenerlo.",
            "Al acercarse, la tensión se disipó. Sobre un elegante caballo oscuro, envuelto en su abrigo negro y con esa mirada magnética que podía convencer a cualquiera, estaba Dutch van der Linde. A su lado, luciendo su característica chaqueta clara y una sonrisa torcida sobre su bigote, aguardaba Micah Bell.",
            "\"Pensé que las montañas se los habían tragado, muchachos\", dijo Dutch con una sonrisa cálida que contrastaba con el frío del entorno. \"Nos enteramos del lío en el tren. Buen trabajo al salir con vida\".",
            "\"Casi no lo contamos, Dutch\", respondió Arthur, aliviado pero exhausto, dejando ver la herida de Bill. \"Y traemos a la ley y a los O'Driscoll pisándonos los talones\".",
            "Micah soltó una risita burlona mientras ajustaba sus pistolas en las fundas. \"Vaya, parece que la fiesta estuvo buena y nos la perdimos, ¿eh?\".",
            "\"Silencio, Micah\", lo cortó Dutch con firmeza, para luego mirar a Arthur y Hosea con serenidad absoluta. \"Tranquilos. Estamos juntos de nuevo. Ahora buscaremos un lugar donde establecernos, curaremos a Bill y planearemos nuestro próximo movimiento. Este país todavía es nuestro, muchachos... solo tenemos que saber cómo tomarlo\"."
        ]
    },
    {
        "numero": 3,
        "titulo": "Capítulo 3: Sombras en el Crepúsculo",
        "icono": "fa-solid fa-campground",
        "imagen": "imagenes/cap3.jpg",
        "texto": [
            "El lento deshielo comenzaba a notarse a medida que la caravana descendía de los picos helados. El cielo del atardecer se teñía de un dorado rojizo que se filtraba entre los densos pinos, pero el calor seguía siendo un privilegio lejano. Los cascos de los caballos retumbaban suavemente contra la nieve apelmazada, acompañando el crujido constante de los carros donde viajaba Bill, malherido pero estable gracias a los cuidados de Hosea.",
            "Mientras Dutch marchaba al frente junto a Micah, marcando el paso de la comitiva, Arthur se replegó unos metros hacia atrás para cabalgar en paralelo a Hosea. La distancia con el grupo principal les daba una estrecha burbuja de privacidad.",
            "\"El brazo de Bill no se va a gangrenar\", comenzó Hosea con voz baja, ajustándose las riendas de su caballo. \"Pero nos va a tomar al menos dos semanas tenerlo listo para disparar otra vez\".",
            "\"Eso es lo de menos ahora, Hosea\", murmuró Arthur, echando una mirada fugaz hacia la figura de Micah, que cabalgaba erguido en la vanguardia junto a Dutch, riendo exageradamente de algún comentario del líder. \"Lo que me preocupa es cómo los O'Driscoll y los agentes sabían exactamente por dónde nos moveríamos. Nos estaban esperando en las cabañas. Y antes de eso, los federales aparecieron demasiado rápido en el tren\".",
            "Hosea guardó silencio durante varios segundos, observando las sombras que se alargaban sobre el manto blanco. Su rostro maduro denotaba una pesadez que no venía solo del cansancio físico.",
            "\"Yo también lo he pensado, Arthur\", admitió Hosea, casi en un susurro para que el viento no llevara sus palabras. \"Desde que Micah se unió a nosotros hace apenas cinco meses, cada movimiento grande ha terminado en un baño de sangre o en una emboscada\".",
            "\"¿Cómo fue exactamente que Dutch lo conoció?\", preguntó Arthur, quien nunca había terminado de digerir la repentina presencia del forajido de la chaqueta clara.",
            "\"Un bar en las afueras de Crevasse\", respondió Hosea, negando levemente con la cabeza. \"Micah le salvó la vida a Dutch en una pelea de borrachos por un botín miserable. Dutch vio en él a un 'alma libre', un tipo leal por puro instinto de supervivencia. Pero tú y yo sabemos que Micah no tiene lealtad a nada que no sea su propio pellejo\".",
            "\"No me gusta cómo le habla al oído a Dutch\", encuadró Arthur, apretando el agarre sobre las riendas de su montura. \"Le vende ideas grandiosas, lo incita a tomar riesgos innecesarios. Y extrañamente, cada vez que las cosas salen mal, Micah siempre resulta ser el único que sale totalmente ileso, sin un solo rasguño... como si supiera exactamente de dónde van a venir los disparos\".",
            "\"Ten cuidado con lo que dices y dónde lo dices, Arthur\", advirtió Hosea, mirando de reojo hacia la delantera. \"Dutch está bajo mucha presión. Para él, cuestionar a Micah en este momento es como cuestionar su propio juicio. Y sabes cuán peligroso se vuelve Dutch cuando siente que dudamos de él\".",
            "A lo lejos, la voz de Micah resonó entre la arboleda, aguda y burlona. \"¡Miren allá abajo, muchachos! ¡Ya casi dejamos atrás este maldito infierno helado! Mañana mismo estaremos pisando hierba verde\".",
            "Arthur observó detenidamente a Micah. Notó algo sutil pero inquietante: mientras el resto de la banda caminaba extenuado y alerta ante cualquier peligro, Micah no dejaba de revisar su alforja personal, acariciando una pequeña libreta de cuero con una extraña sonrisa de satisfacción. No parecía un hombre huyendo por su vida; parecía un hombre contando los días para cobrar una recompensa.",
            "Llegaron a un pequeño claro para montar el campamento nocturno, el último antes de abandonar definitivamente la nieve de las montañas. Arthur se desmontó, mirando hacia las llanuras que se vislumbraban a lo lejos bajo la luz moribunda del sol.",
            "\"Falta poco para salir de la nieve, Hosea\", dijo Arthur, mientras desenganchaba su montura. \"Pero tengo el presagio de que el verdadero peligro no se quedó en las cumbres\".",
            "Hosea lo miró, en silencio, y no se atrevió a llevarle la contraria."
        ]
    },
    {
        "numero": 4,
        "titulo": "Capítulo 4: Caza en el Valle",
        "icono": "fa-solid fa-crosshairs",
        "imagen": "imagenes/cap4.jpg",
        "texto": [
            "El frío gélido de Ambarino por fin dio tregua cuando la banda alcanzó las verdes llanuras de las tierras bajas. Tras semanas alimentándose de raciones rancias y charqui seco, el olor a tierra húmeda y pino fresco les devolvió un atisbo de humanidad. Sin embargo, con el cambio de clima vinieron nuevas urgencias: las provisiones estaban agotadas y la herida de Bill necesitaba carne fresca y caldo caliente para ganar fuerzas.",
            "Arthur y Micah se adentraron a caballo en el bosque con las carabinas al hombro para cazar. El aire era limpio y el silencio del valle solo se rompía por el crujido de las hojas secas bajo los cascos de los caballos.",
            "\"Acelera el paso, Morgan\", dijo Micah con brusquedad, escupiendo al suelo. \"No tenemos todo el día. Si no llevamos algo de comer, Dutch empezará con sus discursos de lealtad y unidad, y sinceramente me tienen harto\".",
            "\"Esa gente que ves atrás es la familia de Dutch, Micah\", respondió Arthur sin mirarlo, manteniendo la vista fija en el rastro de la arboleda. \"Si no te gusta el grupo, la carretera es bastante ancha para que te vayas solo\".",
            "Micah soltó una carcajada seca, desafilada. \"Familia... qué palabra tan tierna. Tienes a un viejo filósofo que ya no sirve para disparar, a un borracho herido que es un lastre y a Dutch, soñando con un paraíso que no existe. Tarde o temprano hay que cortar las ramas secas para que el árbol no se caiga, Arthur. Tarde o temprano\".",
            "Arthur detuvo a su caballo de golpe y clavó sus ojos en Micah. La tensión se palpó en el aire, con ambos hombres con las manos inquietantemente cerca de las fundas de sus revólveres. Antes de que las palabras pasaran a mayores, el crujido de una rama al borde del río interrumpió el enfrentamiento: un venado macho de gran cornamenta bebía agua ajeno a su presencia.",
            "Arthur levantó despacio su fusil, apuntó al codillo con calma y apretó el gatillo. El disparo retumbó limpio en el valle y el animal cayó al instante.",
            "\"Lindo tiro, Morgan\", dijo Micah, con una sonrisa helada que no le llegaba a los ojos. \"Es una pena que toda esa habilidad la gastes protegiendo a débiles\".",
            "Cargaron la presa en el caballo de Arthur y emprendieron el regreso. Sin embargo, al acercarse al punto donde habían dejado acampados a Dutch, Hosea y Bill, el rastro de humo del campamento no venía solo. Un par de caballos desconocidos estaban atados a las afueras.",
            "Arthur desmontó en silencio y desenfundó su revólver, haciéndole una seña a Micah para que abriera camino por el flanco derecho. Pero Micah, en lugar de preparar sus pistolas, dio un paso atrás, manteniéndose oculto entre los matorrales lejanos, observando con los brazos cruzados y esa misma sonrisa indescifrable en el rostro.",
            "Arthur avanzó solo hasta el claro. Allí, dos hombres vestidos con abrigos elegantes de paño oscuro y sombreros de copa baja conversaban pacíficamente con Dutch y Hosea. No eran agoreros ni pistoleros; llevaban insignias doradas en las solapas: la Agencia Nacional de Detectives Pinkerton.",
            "\"Solo estamos de paso, caballeros\", decía el agente de voz áspera, un hombre de bigote canoso llamado Andrew Milton. \"Buscamos a los responsables del asalto al tren en las montañas. Sabemos que la banda de Van der Linde está por la zona. Hay una recompensa sustancial... y la garantía de inmunidad para quien nos entregue a Dutch van der Linde\".",
            "Dutch, manteniendo su porte imponente, sonrió con naturalidad. \"Temo que se han equivocado de grupo, agente. Solo somos simples viajeros tratando de abrirnos paso hacia el oeste\".",
            "Milton miró a Dutch fijamente, luego a Arthur que salía de la vegetación con la carabina en mano, y finalmente echó una mirada calculadora hacia el bosque, justo en la dirección donde Micah estaba escondido.",
            "\"Claro... simples viajeros\", dijo Milton, tocándose el ala del sombrero con gesto burlón. \"Tengan un buen viaje. Nos volveremos a ver muy pronto\".",
            "Los Pinkerton montaron y se alejaron al trote. El silencio en el campamento era ensordecedor. Dutch respiró hondo, tratando de disimular la furia en sus ojos.",
            "Fue entonces cuando Micah salió tranquilamente de entre las sombras de los árboles, guardando un trozo de papel dentro de su diario de cuero antes de guardarlo en la alforja.",
            "\"Estuvo cerca, ¿eh, Dutch?\", dijo Micah con tono desanimado, casi ensayado. \"Suerte que no sospecharon nada\".",
            "Arthur miró a Hosea, y luego clavó una mirada de pura desconfianza sobre Micah. Los Pinkerton no los habían atacado ni arrestado. Habían venido a dar un mensaje... o a verificar que alguien dentro del campamento estuviera haciendo su trabajo."
        ]
    },
    {
        "numero": 5,
        "titulo": "Capítulo 5: El Paso del Cañón",
        "icono": "fa-solid fa-mountain",
        "imagen": "imagenes/cap5.jpg",
        "texto": [
            "Con la sombra de los Pinkerton planeando sobre el grupo y las tensiones internas al límite, Arthur tomó la iniciativa antes del amanecer. Dejó a Hosea a cargo del grupo en las llanuras y se adentró en solitario hacia el cañón del río Cumberland, buscando una ruta de escape segura que los llevara más al sur, lejos de las miradas de los agentes federales.",
            "El sendero era estrecho y traicionero, tallado directamente sobre las paredes de piedra caliza. A la izquierda, imponentes acantilados de roca desnuda se alzaban hacia un cielo azul despejado; a la derecha, un abismo vertical caía en picado hacia un río de aguas bravas que rugía con fuerza entre las piedras. El deshielo de Ambarino alimentaba la corriente, convirtiendo el fondo del barranco en una trampa mortal.",
            "Arthur desmontó de su caballo blanco en una de las cornisas más altas para evaluar el terreno. Apoyado sobre las riendas, contempló el horizonte: las cumbres heladas que tanto sufrimiento les habían causado quedaban atrás, pero el terreno que se abría frente a ellos no parecía más indulgente. La soledad del cañón le ofreció a Arthur un respiro para reflexionar sobre las advertencias de Hosea y las actitudes sospechosas de Micah.",
            "Siguiendo el borde del acantilado, descubrió una antigua cueva parcialmente oculta por pinos silvestres. En su interior, abandonado por algún trampero años atrás, halló un rudimentario mapa de la región grabado en cuero y los restos de una fogata apagada hace días. Sin embargo, lo que más llamó su atención no fue el refugio, sino lo que vio al asomarse con sus catalejos hacia la otra orilla del río.",
            "Al otro lado del desfiladero, un contingente de hombres fuertemente armados levantaba un puesto de vigilancia. No eran cazadores ni forajidos local: llevaban los emblemáticos uniformes oscuros de la Agencia Pinkerton y estaban instalando un telégrafo de campaña. Estaban bloqueando el paso principal antes de que la banda siquiera intentara cruzarlo.",
            "El descubrimiento le heló la sangre. Los Pinkerton no estaban rastreando sus huellas desde atrás; se estaban anticipando a sus movimientos con una precisión inquietante. Sabiendo que regresar por donde vinieron significaba caer en las garras de Colm O'Driscoll y continuar implicaba caminar directo hacia la emboscada federal, Arthur apretó las riendas y montó de nuevo.",
            "Tenía que regresar rápido al campamento improvisado. La banda de Dutch van der Linde ya no solo estaba huyendo de la ley: estaba atrapada en una pinza invisible que se cerraba lentamente sobre ellos."
        ]
    },
    {
        "numero": 6,
        "titulo": "Capítulo 6: La Sombra en la Loma (1899)",
        "icono": "fa-solid fa-fire",
        "imagen": "imagenes/cap6.jpg",
        "texto": [
            "El aire de noviembre de 1899 cortaba como vidrio viejo en las colinas. Era el año en que los forajidos de verdad empezaban a sobrar en un mundo que ya no tenía espacio para ellos, donde los sellos de imprenta, los telégrafos y los detectives privados arrinconaban a los hombres libres contra el precipicio.",
            "Alrededor del fuego del campamento provisional, la ilusión de hermandad se sostenía por pura inercia. Dutch van der Linde intentaba mantener ese brillo mesiánico en los ojos, recitando discursos sobre 'el margen' y 'la última gran puntuación' que les permitiera comprar un terreno bajo el sol de Tahití, negándose a aceptar que el siglo XX les pisa los talones.",
            "Pero Micah Bell no estaba brindando con alegría. Estaba a un costado, limpiando el cañón de su revólver con una parsimoniosidad que revuelve las tripas. Mastica su tabaco y suelta sonrisitas socarronas, dejando entrever que sabe demasiado.",
            "\"Los tiempos cambiaron, jefe\", dijo Micah en voz alta, escupiendo cerca de las botas de Dutch. \"Los federales de la Pinkerton no rastrean carretas; rastrean mentalidades débiles. Y acá adentro... hay demasiados opinólogos y poca eficacia.\"",
            "Arthur Morgan lo observaba desde las sombras con esa tos seca que ya no puede disimular, sintiendo el pecho cargado de plomo. Sabe perfectamente que Micah se ha estado reuniendo en secreto con forasteros al otro lado del arroyo, cerca de la vieja cabaña abandonada en el bosque.",
            "En lugar de un enfrentamiento a tiros limpio, la traición se gesta de forma quirúrgica. Micah no ataca a Dutch por la espalda en medio de una balacera; lo compra y lo manipula psicológicamente. En una charla a solas junto al refugio, le siembra a Dutch la semilla de la paranoia absoluta, haciéndole creer que hay un soplón en la banda y apuntando sutilmente hacia quienes cuestionan su liderazgo.",
            "Acorralado por su propio ego y por la presión de que su utopía fracasó, Dutch prefiere creerle al lamerculos más peligroso antes que a su propia gente. Dutch empieza a aislarse y a mirar a los suyos con recelo, entregándole el timón moral a Micah sin que nadie lo note del todo... hasta que ya es demasiado tarde."
        ]
    }
]

# Menú lateral estilizado
st.sidebar.markdown('### <i class="fa-solid fa-compass custom-icon"></i> Navegación', unsafe_allow_html=True)
opcion = st.sidebar.radio(
    "Selecciona la lectura:",
    ["Ver Historia Completa"] + [c["titulo"] for c in capitulos]
)

# Renderizado de la historia con tarjetas CSS y FontAwesome
for cap in capitulos:
    if opcion == cap["titulo"] or opcion == "Ver Historia Completa":
        st.markdown(f'''
            <div class="chapter-card">
                <div class="chapter-header">
                    <i class="{cap['icono']} custom-icon"></i> {cap['titulo']}
                </div>
        ''', unsafe_allow_html=True)
        
        # Cargar imagen con borde redondeado
        try:
            st.image(cap["imagen"], use_container_width=True)
        except:
            st.info("*(Imagen no encontrada en imagenes/)*")
            
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Párrafos estilizados
        for p in cap["texto"]:
            st.markdown(f'<p class="paragraph-text">{p}</p>', unsafe_allow_html=True)
            
        st.markdown('</div>', unsafe_allow_html=True)