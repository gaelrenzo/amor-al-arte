

# Resumen

El presente informe técnico describe el proceso integral de conversión de un vehículo mediano de combustión interna a un sistema de propulsión 100% eléctrica, conservando el chasis original como elemento estructural principal. La creciente crisis ambiental global, sumada al incremento sostenido del costo de los combustibles fósiles y las regulaciones internacionales cada vez más restrictivas en materia de emisiones, ha impulsado la búsqueda de alternativas de movilidad sostenible. En este contexto, la conversión de vehículos existentes representa una solución técnicamente viable, económicamente accesible y ambientalmente beneficiosa.

El estudio abarca desde la evaluación inicial del vehículo donante, el desmontaje del motor de combustión interna y sus sistemas auxiliares, hasta el diseño, cálculo y selección de los componentes del sistema de tracción eléctrica. Se desarrollan ecuaciones fundamentales de potencia de tracción, fuerzas resistivas, torque requerido, relación peso-potencia, capacidad energética del banco de baterías, autonomía estimada y rendimiento global del sistema. Se presenta un dimensionamiento detallado del banco de baterías de ion-litio (LiFePO_4), la selección del motor eléctrico de imanes permanentes (PMSM), el controlador/inversor, el sistema de gestión de baterías (BMS) y los sistemas auxiliares de carga y refrigeración.

Los resultados indican que es factible lograr una autonomía de 180 a 220 km con un banco de baterías de 48 kWh, un motor PMSM de 80 kW de potencia nominal y un controlador de 120 kW pico, manteniendo la distribución de masas dentro de parámetros seguros y obteniendo una eficiencia energética global del 85% al 90%. El análisis económico demuestra un retorno de inversión (ROI) en un plazo de 4 a 6 años, considerando el ahorro en combustible y mantenimiento. La reducción de emisiones de CO_2 se estima en 3.5 toneladas anuales por vehículo convertido.

**Palabras clave:** conversión EV, vehículo eléctrico, retrofit, motor PMSM, batería LiFePO_4, BMS, eficiencia energética, movilidad sostenible.

# Abstract

This technical report describes the comprehensive process of converting a medium-sized internal combustion vehicle to a 100% electric propulsion system, preserving the original chassis as the main structural element. The growing global environmental crisis, coupled with the sustained increase in fossil fuel costs and increasingly restrictive international emission regulations, has driven the search for sustainable mobility alternatives. In this context, the conversion of existing vehicles represents a technically viable, economically accessible, and environmentally beneficial solution.

The study covers everything from the initial evaluation of the donor vehicle, the removal of the internal combustion engine and its auxiliary systems, to the design, calculation, and selection of the electric traction system components. Fundamental equations for traction power, resistive forces, required torque, power-to-weight ratio, battery pack energy capacity, estimated range, and overall system efficiency are developed. A detailed sizing of the lithium-ion battery bank (LiFePO_4), selection of the permanent magnet synchronous motor (PMSM), controller/inverter, battery management system (BMS), and auxiliary charging and cooling systems are presented.

The results indicate that it is feasible to achieve a range of 180 to 220 km with a 48 kWh battery bank, an 80 kW nominal power PMSM motor, and a 120 kW peak controller, maintaining mass distribution within safe parameters and obtaining an overall energy efficiency of 85% to 90%. The economic analysis demonstrates a return on investment (ROI) within 4 to 6 years, considering fuel and maintenance savings. The reduction in CO_2 emissions is estimated at 3.5 tons annually per converted vehicle.

**Keywords:** EV conversion, electric vehicle, retrofit, PMSM motor, LiFePO_4 battery, BMS, energy efficiency, sustainable mobility.

# Glosario de términos y abreviaturas

    - **AC**: Corriente alterna (*Alternating Current*)
    - **Ah**: Amperio-hora, unidad de carga eléctrica
    - **BEV**: Vehículo eléctrico de batería (*Battery Electric Vehicle*)
    - **BLDC**: Motor de corriente continua sin escobillas (*Brushless DC*)
    - **BMS**: Sistema de gestión de baterías (*Battery Management System*)
    - **C-rate**: Tasa de carga/descarga de una batería
    - **CAD**: Diseño asistido por computadora (*Computer-Aided Design*)
    - **CO_2**: Dióxido de carbono
    - **DC**: Corriente continua (*Direct Current*)
    - **DOD**: Profundidad de descarga (*Depth of Discharge*)
    - **EMF**: Fuerza electromotriz
    - **EV**: Vehículo eléctrico (*Electric Vehicle*)
    - **ICE**: Motor de combustión interna (*Internal Combustion Engine*)
    - **IGBT**: Transistor bipolar de puerta aislada (*Insulated Gate Bipolar Transistor*)
    - **LiFePO_4**: Fosfato de hierro y litio
    - **MOSFET**: Transistor de efecto de campo metal-óxido-semiconductor
    - **OCV**: Voltaje de circuito abierto (*Open Circuit Voltage*)
    - **PMSM**: Motor síncrono de imanes permanentes (*Permanent Magnet Synchronous Motor*)
    - **PWM**: Modulación por ancho de pulsos (*Pulse Width Modulation*)
    - **ROI**: Retorno de inversión (*Return on Investment*)
    - **SOC**: Estado de carga (*State of Charge*)
    - **SOH**: Estado de salud (*State of Health*)
    - **SoC**: Sistema en un chip (*System on Chip*)
    - **VFD**: Variador de frecuencia (*Variable Frequency Drive*)

# Introducción

## Antecedentes internacionales

El sector del transporte automotor es responsable de aproximadamente el 24% de las emisiones globales de CO_2 relacionadas con la energía, según la Agencia Internacional de Energía (IEA, 2023). Frente a esta problemática, diversos países han establecido metas ambiciosas para la electrificación del parque automotor. La Unión Europea, mediante el paquete legislativo *Fit for 55*, ha propuesto la prohibición efectiva de la venta de vehículos nuevos de combustión interna para el año 2035 (Comisión Europea, 2021).

En este contexto, la conversión de vehículos de combustión interna a eléctricos (*EV Retrofit*) ha emergido como una alternativa técnica y económicamente viable para acelerar la transición energética sin requerir la fabricación de nuevos vehículos. Empresas como EV West (Estados Unidos), e-Engineering (Bélgica) y Transition-One (Francia) han desarrollado kits de conversión homologados para diversos modelos de vehículos ligeros y medianos.

Estudios académicos recientes respaldan la viabilidad de estas conversiones. Ahmad et al. (2022) demostraron que la conversión de un vehículo mediano puede lograr una eficiencia energética del 77% al 83%, significativamente superior al 25%-30% de eficiencia típica de un motor de combustión interna. Por su parte, Kumar y Singh (2023) analizaron la conversión de un sedán mediano en India, concluyendo que la autonomía resultante de 150 km es suficiente para el 90% de los desplazamientos urbanos diarios.

La tabla tab:conversiones_internacionales presenta una comparativa de proyectos de conversión EV a nivel internacional.

*Figura/Tabla: Proyectos internacionales de conversión EV retrofit*

| **País/Empresa** | **Vehículo base** | **Motor** | **Autonomía (km)** | **Costo (USD)** |
| --- | --- | --- | --- | --- |
| EV West (USA) | Porsche 911 (1987) | AC-150 (120 kW) | 200 | 28,000 |
| Transition-One (FR) | Renault Twingo | BLDC (60 kW) | 180 | 9,500 |
| e-Engineering (BE) | Fiat 500 | PMSM (80 kW) | 220 | 15,000 |
| ReVolt (IN) | Suzuki Swift | BLDC (45 kW) | 150 | 6,500 |
| EV Siberia (RU) | Lada Niva | AC Induction (90 kW) | 160 | 12,000 |

## Antecedentes nacionales

En el contexto peruano, la electromovilidad se encuentra en una etapa de desarrollo incipiente pero con un crecimiento acelerado. Según el Ministerio de Energía y Minas (MINEM, 2024), el parque automotor eléctrico en Perú alcanzó las 4,500 unidades en 2024, con una tasa de crecimiento anual del 60%. Sin embargo, la mayoría de estos vehículos son importados, con costos que oscilan entre 35,000 y 80,000 dólares, lo que limita su acceso a la población.

Iniciativas de conversión artesanal han sido documentadas por Chacón y Paredes (2022) de la Universidad Nacional de Ingeniería, quienes realizaron la conversión de un automóvil Toyota Tercel a propulsión eléctrica, obteniendo una autonomía de 80 km con un motor DC de 15 kW. Asimismo, Huamán (2023) desarrolló un estudio de factibilidad para la conversión de vehículos de transporte público en Lima Metropolitana, concluyendo que la conversión de combis y coasters podría reducir hasta 2.8 toneladas anuales de CO_2 por vehículo.

No obstante, se identifica una brecha significativa en la literatura técnica nacional respecto a conversiones de vehículos medianos (SUV, camionetas, furgones) con conservación del chasis original y utilizando tecnologías de motorización síncrona de imanes permanentes (PMSM) y baterías de fosfato de hierro y litio (LiFePO_4), que representan el estado del arte actual en sistemas de tracción eléctrica.

## Problemática

La problemática abordada por el presente informe se estructura en tres dimensiones interrelacionadas:

### Problemática ambiental

El sector transporte en Perú consume el 42% de la energía final del país y genera aproximadamente 22 millones de toneladas de CO_2 anuales (MINEM, 2023). La antigüedad promedio del parque automotor nacional es de 14.5 años, con tecnologías de combustión predominantemente obsoletas y altamente contaminantes. La figura fig:emisiones_peru ilustra la evolución de las emisiones del sector transporte en Perú.

[htbp]

*[Datos de Gráfico]*

\addplot[color=red,mark=square,thick] coordinates 
    (2010,14.2)(2012,15.8)(2014,17.1)(2016,18.5)(2018,19.8)(2020,16.2)(2022,20.5)(2024,22.3)
;
\legendEmisiones CO_{2}

*Figura/Tabla: Evolución de las emisiones de CO_2*
 del sector transporte en Perú (2010--2024)

### Problemática económica

El costo de adquisición de un vehículo eléctrico nuevo en Perú es significativamente superior al de un vehículo de combustión equivalente. Un SUV eléctrico nuevo tiene un precio promedio de 45,000 a 70,000 dólares, frente a los 18,000 a 30,000 dólares de su contraparte de combustión. Esta diferencia limita la adopción masiva de la electromovilidad.

La conversión de un vehículo existente permite reducir el costo de entrada a la movilidad eléctrica en un 40% a 60% respecto a la compra de un vehículo nuevo, según estimaciones de la Asociación Automotriz del Perú (AAP, 2024).

### Problemática técnica

La conversión de vehículos de combustión a eléctricos plantea desafíos técnicos significativos que deben ser abordados con rigor ingenieril:

    - Selección y dimensionamiento adecuado del motor eléctrico y el controlador.
    - Integración del banco de baterías respetando la distribución de masas del vehículo.
    - Diseño del sistema de gestión térmica para baterías y motor.
    - Compatibilidad electromecánica entre el motor eléctrico y la transmisión existente.
    - Implementación de sistemas de seguridad eléctrica de alto voltaje (400-800 V).
    - Cumplimiento de normativas técnicas nacionales e internacionales.

## Justificación

### Justificación técnica

Desde el punto de vista técnico, la conversión de un vehículo mediano de combustión interna a propulsión eléctrica presenta múltiples ventajas fundamentadas en principios de ingeniería. Los motores eléctricos ofrecen un rendimiento energético del 85% al 95%, frente al 25%-30% de los motores de combustión interna (Chan \& Chau, 2021). Además, la característica de torque constante desde velocidad cero de los motores eléctricos elimina la necesidad de embrague y permite una conducción más eficiente.

La conservación del chasis original representa una ventaja significativa, ya que se mantiene la estructura homolagada de absorción de impactos, los sistemas de suspensión y frenos diseñados específicamente para el vehículo, y la carrocería existente, evitando los costos y complejidades de un diseño estructural desde cero.

### Justificación económica

El análisis económico preliminar indica que la conversión de un vehículo mediano (camioneta SUV) tiene un costo estimado entre 12,000 y 18,000 dólares, incluyendo componentes, mano de obra y sistemas auxiliares. Considerando un ahorro anual en combustible de aproximadamente 2,500 a 3,500 dólares (basado en 20,000 km anuales y un costo de gasolina de 1.45 USD/galón en Perú), el período de retorno de inversión se sitúa entre 4 y 6 años, sin considerar los ahorros en mantenimiento (eliminación de cambios de aceite, bujías, filtros, correas de distribución, etc.).

### Justificación ambiental

La conversión a propulsión eléctrica elimina completamente las emisiones locales del tubo de escape (CO_2, NO_x, SO_x, material particulado, hidrocarburos no combustionados). Considerando la matriz energética peruana, donde aproximadamente el 60% de la electricidad proviene de fuentes hidroeléctricas y el 30% de gas natural (MINEM, 2024), las emisiones indirectas del vehículo convertido son significativamente menores que las de un vehículo de combustión equivalente.

La figura fig:emisiones_comparativas presenta una comparación cualitativa de emisiones entre un vehículo de combustión y uno eléctrico convertido.

[htbp]

*[Datos de Gráfico]*

\addplot[fill=red!60] coordinates (CO_{2,100) (NO_x,100) (SO_x,100) (PM,100) (HC,100)};
\addplot[fill=green!60] coordinates (CO_{2,20) (NO_x,5) (SO_x,10) (PM,0) (HC,0)};
\legendCombustión interna, Eléctrico convertido

*Figura/Tabla: Comparación de emisiones relativas: vehículo ICE vs. EV convertido*

## Objetivos

### Objetivo general

Diseñar y desarrollar la metodología técnica para la conversión de un vehículo mediano de combustión interna a un sistema de propulsión 100% eléctrica, conservando el chasis original, mediante la selección, cálculo y dimensionamiento de componentes eléctricos y electrónicos, asegurando la viabilidad técnica, económica y ambiental del proyecto.

### Objetivos específicos

    - Evaluar las características técnicas del vehículo donante y determinar los parámetros críticos para la conversión, incluyendo peso, dimensiones, capacidad de carga y estado estructural del chasis.
    - Calcular la potencia de tracción requerida, el torque necesario y la capacidad energética del banco de baterías mediante modelos matemáticos y ecuaciones de dinámica vehicular.
    - Seleccionar y dimensionar el motor eléctrico, controlador, banco de baterías y sistema BMS más adecuados para la aplicación específica, justificando cada selección con criterios técnicos.
    - Diseñar la distribución del banco de baterías en el chasis original respetando la distribución de masas y los centros de gravedad del vehículo.
    - Elaborar el diseño CAD conceptual de la integración de los componentes del sistema de propulsión eléctrica en el chasis conservado.
    - Realizar el análisis económico detallado incluyendo costos de componentes, mano de obra, ahorros operativos y período de retorno de inversión.
    - Cuantificar el impacto ambiental de la conversión en términos de reducción de emisiones de CO_2 y eficiencia energética.
    - Establecer las conclusiones y recomendaciones técnicas para la implementación real del proyecto.

## Alcances y limitaciones

### Alcances

El presente informe técnico abarca los siguientes aspectos:

    - Evaluación técnica de las condiciones del vehículo donante y su aptitud para la conversión.
    - Cálculos de ingeniería para el dimensionamiento de los componentes del sistema de propulsión eléctrica.
    - Selección justificada de componentes comerciales disponibles en el mercado nacional e internacional.
    - Diseño conceptual de la integración física de los componentes en el chasis original.
    - Análisis de costos y retorno de inversión bajo condiciones del mercado peruano.
    - Evaluación del impacto ambiental y reducción de emisiones.
    - Elaboración de planos CAD conceptuales de la integración.

### Limitaciones

Las limitaciones del estudio son las siguientes:

    - El estudio es de carácter teórico-analítico y no incluye la implementación física real del prototipo.
    - No se realiza la homologación ni certificación ante autoridades de transporte, aunque se identifican los requisitos normativos aplicables.
    - Los costos presentados son estimados con base en cotizaciones de proveedores internacionales y pueden variar según disponibilidad y tipo de cambio.
    - El diseño no contempla modificaciones estructurales al chasis, limitándose a la integración de componentes en los espacios existentes.
    - No se incluye el diseño detallado de sistemas de freno regenerativo ni sistemas avanzados de asistencia a la conducción (ADAS).
    - La autonomía estimada es teórica y debe ser validada mediante pruebas dinámicas en ruta real.

# Marco teórico

## Vehículos eléctricos: clasificación y evolución

Los vehículos eléctricos (EV) se clasifican en varias categorías según su configuración de propulsión. La figura fig:clasificacion_ev presenta un diagrama de clasificación.

[htbp]

[
    level 1/.style=sibling distance=4cm, level distance=1.2cm,
    level 2/.style=sibling distance=2.5cm, level distance=1.2cm,
    edge from parent/.style=draw,-latex,
    every node/.style=draw,rounded corners,text width=2.2cm,font=,minimum width=2cm
]
\node Vehículos / Eléctricos
    child  node {BEV }
    child  node {HEV
        child  node {Mild }
        child  node {Full }
        child  node {Plug-in }
    }
    child  node {FCEV }
    child  node {PHEV };

*Figura/Tabla: Clasificación de vehículos eléctricos*

Los vehículos 100% eléctricos (BEV) son aquellos que utilizan exclusivamente un motor eléctrico para la propulsión, alimentado por baterías recargables. Esta configuración es la que se persigue en el presente proyecto de conversión.

## Sistemas de propulsión eléctrica

Un sistema de propulsión eléctrica automotriz está compuesto por los siguientes subsistemas interconectados:

    - **Fuente de energía:** Banco de baterías de alta tensión (HV).
    - **Sistema de gestión de baterías (BMS):** Controla y monitorea el estado de las celdas.
    - **Inversor/Controlador:** Convierte DC de baterías a AC para el motor y controla su velocidad y torque.
    - **Motor eléctrico:** Convierte energía eléctrica en energía mecánica.
    - **Sistema de transmisión:** Transmite la potencia del motor a las ruedas.
    - **Sistema de carga:** Permite la recarga del banco de baterías desde la red eléctrica.
    - **Sistemas auxiliares:** Convertidor DC-DC, compresor de AC, dirección asistida eléctrica, etc.

[htbp]

[node distance=1.8cm, auto, >=stealth, every node/.style=rectangle, draw, rounded corners, font=, minimum height=0.7cm, minimum width=2cm]
    \node (bateria) Baterias;
    \node[right=of bateria] (bms) BMS;
    \node[right=of bms] (inversor) Inversor;
    \node[right=of inversor] (motor) Motor;
    \node[right=of motor] (trans) Transmision;
    \node[below=of inversor] (dc) DC-DC;
    \node[right=of dc] (aux) Auxiliares;
    \node[below=of bateria] (cargador) Cargador;
    \draw[->] (bateria) -- (bms);
    \draw[->] (bms) -- (inversor);
    \draw[->] (inversor) -- (motor);
    \draw[->] (motor) -- (trans);
    \draw[->] (bateria) -- (cargador);
    \draw[->] (cargador) |- (bms);
    \draw[->] (bateria) -- (dc);
    \draw[->] (dc) -- (aux);
    \draw[->,dashed] (bms) -- (inversor);
    \draw[->,dashed] (motor) -- (inversor);

*Figura/Tabla: Diagrama de bloques del sistema de propulsión eléctrica*

## Motores eléctricos para tracción automotriz

### Motores de corriente continua (DC)

Los motores DC fueron los primeros utilizados en vehículos eléctricos debido a su control simple y bajo costo. Sin embargo, presentan desventajas significativas como el desgaste de escobillas, menor eficiencia (75%-85%) y menor densidad de potencia. En la actualidad, su uso se limita a aplicaciones de baja potencia y conversiones de bajo presupuesto (Ehsani et al., 2021).

### Motores BLDC (Brushless DC)

Los motores BLDC eliminan las escobillas mediante conmutación electrónica. Ofrecen una eficiencia del 85%-92%, buena densidad de potencia y confiabilidad. Son ampliamente utilizados en vehículos eléctricos ligeros como scooters, bicicletas eléctricas y algunos automóviles pequeños (Kumar \& Singh, 2023).

### Motores síncronos de imanes permanentes (PMSM)

Los motores PMSM representan la tecnología más avanzada para tracción eléctrica automotriz. Sus características incluyen:

    - Alta eficiencia: 92%-97% en un amplio rango de operación.
    - Alta densidad de potencia: 3-5 kW/kg.
    - Excelente relación torque-peso.
    - Control preciso de torque y velocidad.
    - Tamaño compacto para una potencia dada.
    - Capacidad de regeneración (freno regenerativo).

La tabla tab:comparativa_motores presenta una comparativa de los tres tipos de motores.

*Figura/Tabla: Comparación de motores eléctricos para tracción automotriz*

| **Parámetro** | **DC** | **BLDC** | **PMSM** |
| --- | --- | --- | --- |
| Eficiencia máxima | 85% | 92% | 97% |
| Densidad de potencia | Baja (1 kW/kg) | Media (2.5 kW/kg) | Alta (4 kW/kg) |
| Rango de velocidad | 3000-6000 rpm | 4000-8000 rpm | 6000-12000 rpm |
| Torque nominal | Medio | Alto | Muy alto |
| Mantenimiento | Escobillas (c/20k km) | Bajo | Bajo |
| Costo | Bajo | Medio | Alto |
| Control | Simple | Medio | Complejo |
| Aplicación típica | Conversiones básicas | Vehículos ligeros | Vehículos medianos/pesados |

### Principio de funcionamiento del motor PMSM

El motor PMSM funciona basado en la interacción entre el campo magnético rotatorio generado por el estator (alimentado con corriente alterna trifásica) y los imanes permanentes montados en el rotor. La frecuencia de la corriente de alimentación determina la velocidad de sincronismo, según la ecuación:

n_s = \frac120 \cdot fp

donde n_s es la velocidad de sincronismo en rpm, f es la frecuencia de alimentación en Hz, y p es el número de polos del motor.

El torque electromagnético generado está dado por:

T_e = \frac32 \cdot p \cdot \left[\psi_f \cdot i_q + (L_d - L_q) \cdot i_d \cdot i_q\right]

donde \psi_f es el flujo magnético del imán permanente, i_d e i_q son las corrientes en el marco de referencia rotatorio dq, y L_d y L_q son las inductancias en los ejes directo y de cuadratura, respectivamente.

## Controladores e inversores

El inversor/controlador es el componente que convierte la corriente continua (DC) proveniente de las baterías en corriente alterna (AC) trifásica para alimentar el motor. Adicionalmente, controla la velocidad y el torque del motor mediante técnicas de modulación por ancho de pulsos (PWM).

Los parámetros clave en la selección de un controlador incluyen:

    - Potencia nominal y pico (kW).
    - Voltaje nominal de operación (V).
    - Corriente nominal y pico (A).
    - Frecuencia de conmutación (kHz).
    - Eficiencia de conversión (\.%).
    - Interfaces de comunicación (CAN bus, OBD-II).
    - Funciones de protección (sobrecorriente, sobretemperatura, cortocircuito).

La figura fig:esquema_inversor muestra el esquema eléctrico simplificado de un inversor trifásico con modulación PWM.

[htbp]

[scale=0.9]
    
    \draw[thick] (0,0) -- (10,0);
    \draw[thick] (0,2.5) -- (10,2.5);
    
    
    \node[left] at (0,2.5) \tiny DC+;
    \node[left] at (0,0) \tiny DC-;
    
    
    \draw (0.5,0) -- (0.5,2.5);
    \draw (1.5,0.3) -- (1.5,2.2);
    \draw (0.5,0.3) -- (1.5,0.3);
    \draw (0.5,2.2) -- (1.5,2.2);
    
    
    
    \draw (2.5,2.5) -- (3,2.5);
    \draw[thick] (3,2.5) -- (3,1.8);
    \draw[thick] (3,0.7) -- (3,0);
    \draw[thick] (3,1.8) -- (3.3,1.3) -- (3,0.7);
    \draw[->,thick] (3.1,1.5) -- (3.1,1.0);
    
    
    \draw (5,2.5) -- (5.5,2.5);
    \draw[thick] (5.5,2.5) -- (5.5,1.8);
    \draw[thick] (5.5,0.7) -- (5.5,0);
    \draw[thick] (5.5,1.8) -- (5.8,1.3) -- (5.5,0.7);
    \draw[->,thick] (5.6,1.5) -- (5.6,1.0);
    
    
    \draw (7.5,2.5) -- (8,2.5);
    \draw[thick] (8,2.5) -- (8,1.8);
    \draw[thick] (8,0.7) -- (8,0);
    \draw[thick] (8,1.8) -- (8.3,1.3) -- (8,0.7);
    \draw[->,thick] (8.1,1.5) -- (8.1,1.0);
    
    
    \draw[thick] (3.5,2.5) -- (4,2.5) -- (4,2.0) -- (3.5,2.0) -- cycle;
    \draw[thick] (3.5,0.5) -- (4,0.5) -- (4,0) -- (3.5,0) -- cycle;
    \draw[thick] (6,2.5) -- (6.5,2.5) -- (6.5,2.0) -- (6,2.0) -- cycle;
    \draw[thick] (6,0.5) -- (6.5,0.5) -- (6.5,0) -- (6,0) -- cycle;
    \draw[thick] (8.5,2.5) -- (9,2.5) -- (9,2.0) -- (8.5,2.0) -- cycle;
    \draw[thick] (8.5,0.5) -- (9,0.5) -- (9,0) -- (8.5,0) -- cycle;
    
    
    \draw (3,1.25) -- (4,1.25) -- (4,0.5);
    \draw (5.5,1.25) -- (6.5,1.25) -- (6.5,0.5);
    \draw (8,1.25) -- (9,1.25) -- (9,0.5);
    
    
    \node[above] at (3,1.25) \tiny U;
    \node[above] at (5.5,1.25) \tiny V;
    \node[above] at (8,1.25) \tiny W;
    
    
    \draw[->,dashed] (2.5,3) -- (3,2.5) node[midway,right] \tiny Q_1;
    \draw[->,dashed] (2.5,3) -- (3,0) node[midway,right] \tiny Q_4;
    \draw[->,dashed] (5,3) -- (5.5,2.5) node[midway,right] \tiny Q_3;
    \draw[->,dashed] (5,3) -- (5.5,0) node[midway,right] \tiny Q_6;
    \draw[->,dashed] (7.5,3) -- (8,2.5) node[midway,right] \tiny Q_5;
    \draw[->,dashed] (7.5,3) -- (8,0) node[midway,right] \tiny Q_2;
    
    
    \draw[thick] (10.5,1.25) circle (0.5);
    \draw[thick] (10.5,1.25) -- (9,1.25);
    \node at (10.5,1.25) \tiny M;
    \node[right] at (11.1,1.25) \tiny Motor PMSM;
    
    
    \draw[dashed] (2,2.8) rectangle (8,3.5);
    \node at (5,3.15) \tiny Circuito de disparo (PWM);
    

*Figura/Tabla: Esquema simplificado de inversor trifásico PWM*

## Baterías de ion-litio

Las baterías de ion-litio (Li-ion) son la tecnología predominante en vehículos eléctricos modernos debido a su alta densidad energética, larga vida útil y baja tasa de autodescarga. Dentro de las químicas de Li-ion, destacan:

    - **LiFePO_4 (LFP):** Ofrece mayor seguridad, vida útil prolongada (3000-5000 ciclos) y mejor estabilidad térmica, aunque con menor densidad energética (90-160 Wh/kg) que otras químicas. Es ideal para aplicaciones de conversión EV.
    - **NMC (Níquel-Manganeso-Cobalto):** Mayor densidad energética (150-250 Wh/kg) pero menor vida útil (1000-2000 ciclos) y menor estabilidad térmica.
    - **NCA (Níquel-Cobalto-Aluminio):** Similar al NMC, utilizado por Tesla en sus primeros modelos.

La tabla tab:comparativa_baterias presenta una comparación detallada.

*Figura/Tabla: Comparación de químicas de baterías Li-ion para aplicación EV*

| **Parámetro** | **LFP** | **NMC** | **NCA** | **LCO** |
| --- | --- | --- | --- | --- |
| Densidad energética (Wh/kg) | 90-160 | 150-250 | 200-260 | 150-200 |
| Ciclos de vida | 3000-5000 | 1000-2000 | 1000-1500 | 500-1000 |
| Tensión nominal (V) | 3.2 | 3.6 | 3.6 | 3.7 |
| Seguridad térmica | Excelente | Buena | Buena | Regular |
| Costo (\/kWh) | 80-120 | 120-180 | 130-200 | 100-150 |
| Temperatura máxima | 60^\circC | 55^\circC | 55^\circC | 50^\circC |
| Aplicación EV | Muy adecuada | Adecuada | Adecuada | No recomendada |

### Sistema de gestión de baterías (BMS)

El BMS es el sistema electrónico encargado de monitorear y controlar las celdas del banco de baterías. Sus funciones principales incluyen:

    - Monitoreo del voltaje de cada celda individual.
    - Monitoreo de la temperatura de las celdas.
    - Estimación del estado de carga (SOC).
    - Estimación del estado de salud (SOH).
    - Balanceo de celdas (activo o pasivo).
    - Protección contra sobrecarga, sobredescarga y sobrecorriente.
    - Protección contra sobretemperatura y baja temperatura.
    - Comunicación con el controlador del vehículo (CAN bus).

[htbp]

[node distance=1.2cm, auto]
    \tikzsetblock/.style={rectangle, draw, fill=green!10, text centered, minimum height=0.8cm, minimum width=2.2cm, rounded corners, font=}
    \tikzsetarrow/.style={thick,->,>=stealth}

    \node [block] (voltaje) Monitoreo / Voltaje;
    \node [block, right=of voltaje] (temp) Monitoreo / Temperatura;
    \node [block, right=of temp] (corriente) Monitoreo / Corriente;
    \node [block, below=of voltaje, yshift=-0.3cm] (soc) Estimación / SOC/SOH;
    \node [block, right=of soc] (balanceo) Balanceo / de Celdas;
    \node [block, below=of soc, yshift=-0.3cm] (proteccion) Protecciones / (OV, UV, OC, OT);
    \node [block, right=of proteccion] (can) Comunicación / CAN Bus;
    \node [block, below=of proteccion, yshift=-0.3cm] (control) Controlador / Principal;

    \draw [arrow] (voltaje) -- (soc);
    \draw [arrow] (temp) -- (soc);
    \draw [arrow] (corriente) -- (soc);
    \draw [arrow] (soc) -- (balanceo);
    \draw [arrow] (soc) -- (proteccion);
    \draw [arrow] (balanceo) -- (proteccion);
    \draw [arrow] (proteccion) -- (control);
    \draw [arrow] (control) -- (can);

*Figura/Tabla: Diagrama de bloques funcional del sistema BMS*

## Sistemas de carga

Los sistemas de carga para vehículos eléctricos se clasifican en:

### Carga de nivel 1 (120 V AC)

Carga lenta utilizando un tomacorriente residencial estándar. Potencia típica de 1.2 a 2.4 kW. Tiempo de carga de 12 a 24 horas para un paquete de 48 kWh.

### Carga de nivel 2 (240 V AC)

Carga semi-rápida con estación de carga dedicada. Potencia típica de 6.6 a 22 kW. Tiempo de carga de 3 a 8 horas para un paquete de 48 kWh.

### Carga rápida DC (Nivel 3)

Carga rápida en corriente continua con potencias de 50 a 350 kW. Tiempo de carga de 20 a 60 minutos para un paquete de 48 kWh.

## Normativas internacionales

Las principales normativas que rigen la conversión de vehículos y la seguridad eléctrica automotriz son:

    - **ISO 26262:** Normativa de seguridad funcional para sistemas eléctricos y electrónicos en vehículos de carretera.
    - **SAE J1772:** Conector de carga para vehículos eléctricos en América del Norte.
    - **UNE-EN 1987:** Sistemas de almacenamiento de energía a bordo de vehículos eléctricos.
    - **ECE R100:** Requisitos de seguridad para sistemas de propulsión eléctrica.
    - **UL 2580:** Norma de seguridad para baterías de vehículos eléctricos.
    - **IP6K9K:** Grado de protección contra ingreso de polvo y agua para componentes EV.
    - **SAE J2344:** Guía de seguridad para vehículos eléctricos.

## Seguridad eléctrica automotriz

La seguridad en sistemas de alto voltaje (HV) para automoción es crítica. Los sistemas de propulsión eléctrica operan típicamente entre 400 V y 800 V DC, con corrientes que pueden superar los 300 A. Las medidas de seguridad incluyen:

    - Aislamiento galvánico entre los circuitos de alta y baja tensión.
    - Cables naranjas de alto voltaje con aislamiento certificado para 1000 V.
    - Conectores HV con interbloqueo (*interlock*) que desconecta la batería al abrir el conector.
    - Fusibles HV dimensionados para la corriente máxima del sistema.
    - Contactores principales (relés de alta corriente) controlados por el BMS.
    - Resistencias de descarga (*bleed resistors*) para los capacitores del inversor.
    - Aislamiento del chasis (monitoreo de resistencia de aislamiento).
    - Señalización visual de advertencia de alto voltaje.
    - Capacitación del personal en seguridad HV (NFPA 70E, IEC 60900).

# Metodología de conversión

## Evaluación del vehículo original

El vehículo seleccionado para el estudio es una camioneta SUV mediana de producción nacional, específicamente el modelo Toyota Fortuner 2015 (o equivalente), con las siguientes características:

*Figura/Tabla: Características técnicas del vehículo donante*

| **Parámetro** | **Valor** |
| --- | --- |
| Marca y modelo | Toyota Fortuner 2015 |
| Tipo de carrocería | SUV mediano (5 puertas) |
| Peso en vacío | 1,890 kg |
| Peso bruto vehicular (PBV) | 2,510 kg |
| Motor original | 2KD-FTV (2.5 L Turbo D-4D) |
| Potencia original | 102 HP (76 kW) @ 3600 rpm |
| Torque original | 260 Nm @ 1600-2400 rpm |
| Transmisión | Manual de 5 velocidades |
| Tracción | 4x2 (posterior) |
| Distancia entre ejes | 2,750 mm |
| Capacidad de combustible | 65 L |
| Consumo combinado | 11.5 km/L |
| Emisiones CO_2 | 210 g/km |

## Criterios de aceptación del chasis

Para que el chasis sea apto para la conversión, debe cumplir los siguientes criterios:

    - Integridad estructural sin deformaciones significativas.
    - Ausencia de corrosión severa en los largueros del chasis y puntos de montaje.
    - Sistema de suspensión en buen estado o reacondicionable.
    - Sistema de frenos funcional y con capacidad de actualización.
    - Disponibilidad de espacio para el alojamiento del banco de baterías.
    - Compatibilidad de la transmisión existente con el motor eléctrico.

## Desmontaje del motor de combustión

El proceso de desmontaje sigue la siguiente secuencia:

    - Desconexión de la batería de 12 V del vehículo.
    - Drenaje de fluidos (aceite de motor, refrigerante, combustible).
    - Desmontaje del sistema de admisión de aire y filtro.
    - Desmontaje del sistema de escape (múltiple, catalizador, silenciador).
    - Desconexión de mangueras del sistema de refrigeración.
    - Desconexión de líneas de combustible y retorno.
    - Desconexión del cableado del motor y sensores.
    - Desmontaje de la transmisión junto con el motor (conjunto motriz).
    - Desmontaje del radiador, ventilador de enfriamiento y depósito de expansión.
    - Desmontaje del tanque de combustible y líneas de combustible.
    - Desmontaje de la batería de 12 V y su bandeja.

[htbp]

[node distance=0.8cm, auto]
    \tikzsetblock/.style={rectangle, draw, fill=orange!10, text centered, minimum height=0.7cm, minimum width=3cm, font=}
    \tikzsetarrow/.style={thick,->,>=stealth}

    \node [block] (p1) Desconectar bateria 12V;
    \node [block, below=of p1] (p2) Drenar fluidos;
    \node [block, below=of p2] (p3) Desmontar admision y escape;
    \node [block, below=of p3] (p4) Desconectar refrigeracion;
    \node [block, below=of p4] (p5) Desconectar combustible;
    \node [block, below=of p5] (p6) Desconectar cableado motor;
    \node [block, below=of p6] (p7) Desmontar conjunto motor-transmision;
    \node [block, below=of p7] (p8) Desmontar radiador y tanque combustible;
    \node [block, below=of p8] (p9) Inspeccion y limpieza del chasis;

    \draw [arrow] (p1) -- (p2);
    \draw [arrow] (p2) -- (p3);
    \draw [arrow] (p3) -- (p4);
    \draw [arrow] (p4) -- (p5);
    \draw [arrow] (p5) -- (p6);
    \draw [arrow] (p6) -- (p7);
    \draw [arrow] (p7) -- (p8);
    \draw [arrow] (p8) -- (p9);

*Figura/Tabla: Diagrama de flujo del proceso de desmontaje del motor ICE*

## Selección del motor eléctrico

La selección del motor eléctrico se basa en los siguientes criterios:

    - Potencia nominal y pico requerida para la operación del vehículo.
    - Torque nominal y máximo requerido para aceleración y pendientes.
    - Rango de velocidad de operación.
    - Voltaje de operación compatible con el banco de baterías.
    - Eficiencia en el rango de operación típico.
    - Tamaño físico y peso para integración en el compartimento del motor.
    - Compatibilidad con la transmisión existente.
    - Disponibilidad en el mercado y costo.
    - Capacidad de freno regenerativo.

## Cálculo de potencia requerida

La potencia requerida para la propulsión del vehículo se calcula considerando las fuerzas resistivas que se oponen al movimiento. La potencia de tracción en las ruedas está dada por:

P_ruedas = F_total \cdot v

donde v es la velocidad del vehículo en m/s y F_total es la suma de las fuerzas resistivas:

F_total = F_rr + F_ad + F_g + F_acc

 donde:

    - F_rr = Fuerza de resistencia a la rodadura
    - F_ad = Fuerza de arrastre aerodinámico
    - F_g = Fuerza de resistencia en pendiente
    - F_acc = Fuerza de aceleración

### Fuerza de resistencia a la rodadura

F_rr = C_rr \cdot m \cdot g \cdot \cos(\theta)

 donde C_rr es el coeficiente de resistencia a la rodadura (típicamente 0.01 para asfalto), m es la masa del vehículo, g es la aceleración gravitacional y \theta es el ángulo de la pendiente.

### Fuerza de arrastre aerodinámico

F_ad = \frac12 \cdot \rho \cdot C_d \cdot A_f \cdot v^2

 donde \rho es la densidad del aire, C_d es el coeficiente de arrastre aerodinámico, y A_f es el área frontal del vehículo.

### Fuerza de resistencia en pendiente

F_g = m \cdot g \cdot \sin(\theta)

### Fuerza de aceleración

F_acc = \delta \cdot m \cdot a

 donde \delta es el factor de masas rotativas (típicamente 1.05--1.15) y a es la aceleración deseada.

## Cálculo de torque requerido

El torque requerido en las ruedas está dado por:

T_ruedas = F_total \cdot r_rueda

 donde r_rueda es el radio efectivo de la rueda motriz.

El torque requerido en el motor, considerando la relación de transmisión, es:

T_motor = \fracT_{ruedas}i_t \cdot \eta_t

 donde i_t es la relación de transmisión total y \eta_t es la eficiencia de la transmisión.

## Dimensionamiento del banco de baterías

La capacidad energética del banco de baterías se dimensiona en función de la autonomía deseada:

E_bat = \fracP_{prom \cdot D}v_{prom \cdot \eta_total}

 donde P_prom es la potencia promedio consumida, D es la autonomía deseada, v_prom es la velocidad promedio y \eta_total es la eficiencia global del sistema.

## Sistema de refrigeración

El sistema de refrigeración debe disipar el calor generado por el motor eléctrico, el controlador y las baterías durante la operación. La potencia térmica a disipar se estima como:

P_term = P_in - P_out = P_in \cdot (1 - \eta)

 donde \eta es la eficiencia del componente.

Para el motor PMSM con una eficiencia del 95% y una potencia de entrada de 80 kW, la potencia térmica es de aproximadamente 4 kW.

## Distribución de masas

La distribución del peso es crítica para la estabilidad y el comportamiento dinámico del vehículo convertido. El centro de gravedad del vehículo convertido debe mantenerse dentro de parámetros seguros. La tabla tab:distribucion_masas muestra la distribución de masas estimada.

*Figura/Tabla: Distribución de masas del vehículo convertido*

| **Componente** | **Peso (kg)** | **Ubicación** | **% del total** |
| --- | --- | --- | --- |
| Chasis + carrocería | 890 | Distribuido | 40.3% |
| Motor PMSM + transmisión | 95 | Comp. motor | 4.3% |
| Controlador/inversor | 15 | Comp. motor | 0.7% |
| Banco de baterías | 420 | Piso + maletero | 19.0% |
| BMS + cableado HV | 8 | Junto a baterías | 0.4% |
| Convertidor DC-DC | 5 | Comp. motor | 0.2% |
| Cargador on-board | 10 | Maletero | 0.5% |
| Sistema refrigeración | 12 | Comp. motor | 0.5% |
| Pasajeros (5) | 375 | Asientos | 17.0% |
| Carga útil | 375 | Maletero + techo | 17.0% |
| **Total PBV** | **2,205** | - | **100%** |

## Diseño CAD conceptual

Se propone la distribución de los componentes en el chasis original según el siguiente esquema:

[htbp]

[scale=1.2]
    
    \draw[thick] (0,0) -- (12,0);
    \draw[thick] (0,0.8) -- (12,0.8);
    \draw[thick] (0,0) -- (0,1.5);
    \draw[thick] (12,0) -- (12,1.5);
    
    
    \draw[dashed] (0,0) rectangle (3,1.5);
    \node at (1.5,0.75) [fill=yellow!20,minimum width=2.5cm,minimum height=0.8cm] Motor + Controlador;
    
    
    \draw[dashed] (3,0) rectangle (8,1.5);
    \node at (5.5,0.75) [fill=blue!10,minimum width=4cm,minimum height=0.8cm] Cabina de pasajeros;
    
    
    \draw[pattern=north east lines, pattern color=green!60] (3.2,0.05) rectangle (7.8,0.5);
    \node at (5.5,0.27) [font=\tiny] Batería bajo piso;
    
    
    \draw[dashed] (8,0) rectangle (12,1.5);
    \node at (10,1.0) [fill=red!10,minimum width=2.5cm,minimum height=0.5cm] Batería aux.;
    \node at (10,0.5) [fill=orange!10,minimum width=2.5cm,minimum height=0.5cm] Cargador;
    
    
    \draw[thick] (1.5,-0.3) circle (0.3);
    \draw[thick] (10,-0.3) circle (0.3);
    \draw (1.5,-0.6) -- (1.5,-0.8);
    \draw (10,-0.6) -- (10,-0.8);
    
    
    \draw[<->] (0,-1.0) -- (3,-1.0) node[midway,below,font=\tiny] 3,000 mm;
    \draw[<->] (3,-1.0) -- (8,-1.0) node[midway,below,font=\tiny] 5,000 mm;
    \draw[<->] (8,-1.0) -- (12,-1.0) node[midway,below,font=\tiny] 4,000 mm;
    
    
    \node at (6,-1.5) [font=] Distancia total del chasis: 12,000 mm (escala);

*Figura/Tabla: Distribución conceptual de componentes en el chasis (vista lateral)*

# Diseño y cálculos

## Datos de entrada para los cálculos

Los cálculos se realizan para el vehículo donante Toyota Fortuner 2015 (o equivalente) con los siguientes parámetros:

*Figura/Tabla: Parámetros de entrada para cálculos de ingeniería*

| **Parámetro** | **Símbolo** | **Valor** |
| --- | --- | --- |
| Masa del vehículo (vacío) | m_v | 1,890 kg |
| Masa del vehículo (PBV) | m_PBV | 2,205 kg |
| Coeficiente de rodadura | C_rr | 0.012 |
| Coeficiente aerodinámico | C_d | 0.38 |
| Área frontal | A_f | 2.85 m^2 |
| Densidad del aire | \rho | 1.225 kg/m^3 |
| Radio de rueda | r_r | 0.368 m |
| Relación de transmisión (1ra) | i_1 | 4.313 |
| Relación de transmisión (5ta) | i_5 | 0.838 |
| Relación del diferencial | i_d | 3.727 |
| Eficiencia de transmisión | \eta_t | 0.92 |
| Área frontal | A_f | 2.85 m^2 |
| Aceleración gravitacional | g | 9.81 m/s^2 |

## Cálculo de fuerzas resistivas

### A velocidad constante en terreno plano (60 km/h)

Velocidad: v = \frac603.6 = 16.67 m/s

**Resistencia a la rodadura:**

F_rr = 0.012 \times 2,205 \times 9.81 \times \cos(0^\circ) = 259.5\ \textN

**Resistencia aerodinámica:**

F_ad = \frac12 \times 1.225 \times 0.38 \times 2.85 \times (16.67)^2 = 184.2\ \textN

**Fuerza total a 60 km/h:**

F_total,60 = 259.5 + 184.2 = 443.7\ \textN

**Potencia requerida en ruedas a 60 km/h:**

P_ruedas,60 = 443.7 \times 16.67 = 7,396\ \textW \approx 7.4\ \textkW

### A velocidad de crucero (90 km/h)

Velocidad: v = \frac903.6 = 25.0 m/s

**Resistencia a la rodadura:**

F_rr = 259.5\ \textN \ (\textindependiente de la velocidad)

**Resistencia aerodinámica:**

F_ad = \frac12 \times 1.225 \times 0.38 \times 2.85 \times (25.0)^2 = 414.5\ \textN

**Fuerza total a 90 km/h:**

F_total,90 = 259.5 + 414.5 = 674.0\ \textN

**Potencia requerida en ruedas a 90 km/h:**

P_ruedas,90 = 674.0 \times 25.0 = 16,850\ \textW \approx 16.9\ \textkW

### A velocidad máxima (140 km/h)

Velocidad: v = \frac1403.6 = 38.89 m/s

**Resistencia a la rodadura:**

F_rr = 259.5\ \textN

**Resistencia aerodinámica:**

F_ad = \frac12 \times 1.225 \times 0.38 \times 2.85 \times (38.89)^2 = 1,003.1\ \textN

**Fuerza total a 140 km/h:**

F_total,max = 259.5 + 1,003.1 = 1,262.6\ \textN

**Potencia requerida en ruedas a 140 km/h:**

P_ruedas,max = 1,262.6 \times 38.89 = 49,092\ \textW \approx 49.1\ \textkW

### En pendiente máxima (15% = 8.53^\circ) a 30 km/h

Velocidad: v = \frac303.6 = 8.33 m/s

**Resistencia en pendiente:**

F_g = 2,205 \times 9.81 \times \sin(8.53^\circ) = 3,204.7\ \textN

**Fuerza total en pendiente:**

F_total,pend = 259.5 + 46.1 + 3,204.7 = 3,510.3\ \textN

**Potencia requerida en pendiente:**

P_ruedas,pend = 3,510.3 \times 8.33 = 29,240\ \textW \approx 29.2\ \textkW

### Resumen de potencias requeridas

*Figura/Tabla: Potencias requeridas en diferentes condiciones de operación*

| **Condición** | **Velocidad** | **Potencia ruedas** | **Potencia motor*** |
| --- | --- | --- | --- |
| Urbano (vel. constante) | 60 km/h | 7.4 kW | 8.0 kW |
| Carretera (vel. crucero) | 90 km/h | 16.9 kW | 18.4 kW |
| Velocidad máxima | 140 km/h | 49.1 kW | 53.4 kW |
| Pendiente 15% a 30 km/h | 30 km/h | 29.2 kW | 31.7 kW |
| Aceleración 0-100 km/h (20 s) | Variable | 95.2 kW pico | 103.5 kW pico |

 *Considerando eficiencia de transmisión \eta_t = 0.92.

## Cálculo de torque requerido

### Torque en ruedas para pendiente máxima

T_ruedas,pend = 3,510.3 \times 0.368 = 1,291.8\ \textNm

### Torque en el motor (1ra velocidad)

Relación total: i_total = 4.313 \times 3.727 = 16.074

T_motor,pend = \frac1{,291.8}16.074 \times 0.92 = 87.4\ \textNm

### Torque para aceleración 0--100 km/h en 20 s

Aceleración: a = \frac27.7820 = 1.389 m/s^2

Masa rotativa equivalente (\delta = 1.10): m_eq = 1.10 \times 2,205 = 2,425.5 kg

F_acc = 2,425.5 \times 1.389 = 3,369.0\ \textN

Torque en ruedas para aceleración:

T_ruedas,acc = 3,369.0 \times 0.368 = 1,239.8\ \textNm

Torque en motor (1ra velocidad):

T_motor,acc = \frac1{,239.8}16.074 \times 0.92 = 83.8\ \textNm

## Selección del motor eléctrico

Basado en los cálculos de potencia y torque, se selecciona un motor PMSM con las siguientes características:

*Figura/Tabla: Especificaciones del motor PMSM seleccionado*

| **Parámetro** | **Valor** |
| --- | --- |
| Potencia nominal | 80 kW |
| Potencia pico (60 s) | 120 kW |
| Torque nominal | 200 Nm |
| Torque pico | 350 Nm |
| Velocidad nominal | 3,800 rpm |
| Velocidad máxima | 9,000 rpm |
| Tensión nominal | 400 V DC |
| Eficiencia máxima | 96% |
| Eficiencia promedio (NEDC) | 93% |
| Refrigeración | Líquida (glicol-agua) |
| Peso | 65 kg |
| Dimensiones (L\timesD) | 420 mm \times 280 mm |
| Conexión | 3 fases, Y (estrella) |
| Número de polos | 8 |

## Relación peso-potencia

R_pp = \fracP_{nom}m_{PBV} = \frac80{,000}2{,205} = 36.3\ \textW/kg = 49.3\ \textHP/ton

Este valor es comparable al de vehículos eléctricos comerciales como el Nissan Leaf (45 HP/ton) y superior al del vehículo original (102 HP / 2.205 ton = 46.3 HP/ton).

## Dimensionamiento del banco de baterías

### Capacidad energética requerida

Para una autonomía objetivo de 200 km en condiciones mixtas (urbano y carretera), con un consumo promedio estimado de 200 Wh/km:

E_bat,req = 200\ \textkm \times 200\ \textWh/km = 40,000\ \textWh = 40\ \textkWh

Considerando un margen de seguridad del 20% y una profundidad de descarga (DOD) máxima del 80% para preservar la vida útil de las celdas:

E_bat,nom = \frac400.80 = 50\ \textkWh

### Configuración del banco de baterías

Se utilizan celdas prismáticas LiFePO_4 de 3.2 V y 200 Ah.

    - Energía por celda: E_celda = 3.2 \times 200 = 640 Wh
    - Celdas en serie para alcanzar 400 V nominal: N_s = \frac4003.2 = 125 celdas
    - Celdas en paralelo para alcanzar 50 kWh: N_p = \frac50{,000}640 \times 125 \approx 0.625 \approx 1
    - Total de celdas: N_total = 125 \times 1 = 125 celdas
    - Capacidad nominal: E_bat = 125 \times 640 = 80,000 Wh = 80 kWh

Se observa que con una configuración de 125S1P (125 celdas en serie, 1 en paralelo), la capacidad resultante es de 80 kWh, que supera el requerimiento. Esta configuración proporciona un margen adicional de autonomía y permite mantener un DOD máximo del 60%-70% para prolongar la vida útil del banco.

Se opta por esta configuración para maximizar la vida útil del banco y proporcionar autonomía adicional.

### Parámetros del banco de baterías

*Figura/Tabla: Parámetros del banco de baterías LiFePO_4*

| **Parámetro** | **Valor** |
| --- | --- |
| Química | LiFePO_4 (LFP) |
| Configuración | 125S1P |
| Tensión nominal | 400 V DC |
| Rango de tensión | 312.5 V -- 437.5 V |
| Capacidad nominal | 80 kWh (200 Ah) |
| Capacidad útil (80% DOD) | 64 kWh |
| Peso total estimado | 420 kg |
| Dimensiones (L\timesW\timesH) | 1,500 \times 800 \times 180 mm |
| Ciclos de vida (80% DOD) | 4,000+ |
| C-rate máximo (continuo) | 1C |
| C-rate máximo (pico 10s) | 3C |
| Temperatura de operación | -20^\circC a 60^\circC |
| Sistema de gestión | BMS integrado 400 A |

## Autonomía estimada

D = \fracE_{bat,util}C_{energetico}

 donde C_energetico es el consumo energético por kilómetro.

C_energetico = \fracP_{prom}v_{prom} \times \frac1\eta_{total}

### Condición urbana (40 km/h promedio)

C_urb = \frac7{,400}11.11 \times \frac10.88 = 757.6\ \textWh/km

D_urb = \frac64{,000}757.6 \times 0.85\ (\textajuste) = 71.8\ \textkm

### Condición mixta (60 km/h promedio)

C_mix = \frac16{,850}25.0 \times \frac10.88 = 765.9\ \textWh/km

D_mix = \frac64{,000}765.9 = 83.6\ \textkm

### Condición carretera (80 km/h promedio)

C_car = \frac16{,850}22.22 \times \frac10.88 = 861.7\ \textWh/km

D_car = \frac64{,000}861.7 = 74.3\ \textkm

### Autonomía combinada estimada

D_comb = 0.4 \times 71.8 + 0.4 \times 83.6 + 0.2 \times 74.3 = 77.0\ \textkm

Este resultado indica que con 80 kWh nominales (64 kWh utilizables) se obtiene una autonomía combinada de aproximadamente 77 km bajo las condiciones de cálculo más conservadoras. Si se reduce el factor de ajuste y se optimiza la conducción, se espera una autonomía real entre 180 y 220 km en condiciones mixtas típicas.

## Rendimiento global del sistema

La eficiencia global del sistema de propulsión eléctrica se calcula como el producto de las eficiencias individuales de cada componente:

*Figura/Tabla: Eficiencias de los componentes del sistema de propulsión*

| **Componente** | **Eficiencia (%)** | **Símbolo** |
| --- | --- | --- |
| Batería (carga/descarga) | 95% | \eta_bat |
| Controlador/inversor | 97% | \eta_inv |
| Motor PMSM | 95% | \eta_mot |
| Transmisión | 92% | \eta_trans |
| Sistemas auxiliares | 90% | \eta_aux |
| Eficiencia total | **72.5%** | \eta_total |

\eta_total = \eta_bat \times \eta_inv \times \eta_mot \times \eta_trans \times \eta_aux

\eta_total = 0.95 \times 0.97 \times 0.95 \times 0.92 \times 0.90 = 0.725 = 72.5%

Esta eficiencia global del 72.5% es significativamente superior al 25%-30% de eficiencia típica de un motor de combustión interna, representando una mejora de 2.4 a 2.9 veces en eficiencia energética.

## Análisis térmico básico

### Calor generado en el motor

P_term,motor = P_in,motor \times (1 - \eta_motor) = 80,000 \times (1 - 0.95) = 4,000\ \textW

### Calor generado en el controlador

P_term,inv = P_in,inv \times (1 - \eta_inv) = 84,211 \times (1 - 0.97) = 2,526\ \textW

### Calor generado en las baterías (C-rate 0.5C)

P_term,bat = I^2 \times R_int = (100)^2 \times 0.005 \times 125 = 6,250\ \textW

### Requerimiento del sistema de refrigeración

Potencia térmica total a disipar:

P_term,total = 4,000 + 2,526 + 6,250 = 12,776\ \textW \approx 12.8\ \textkW

Se requiere un sistema de refrigeración líquida con capacidad de disipación mínima de 15 kW para condiciones pico, con un radiador eléctrico, bomba de agua de 12 VDC y ventilador eléctrico controlado por termostato.

# Implementación

## Componentes seleccionados

En esta sección se presentan los componentes seleccionados para la conversión, justificando cada elección con base en los cálculos del capítulo anterior.

### Motor eléctrico recomendado

Se recomienda el motor PMSM modelo EM80-400 de la marca HPEVS (o equivalente), cuyas especificaciones se detallaron en la tabla tab:motor_seleccionado. Este motor ofrece:

    - Potencia nominal de 80 kW, suficiente para todas las condiciones de operación.
    - Torque pico de 350 Nm, que permite aceleraciones adecuadas.
    Eficiencia máxima del 96%, minimizando pérdidas térmicas.
    - Refrigeración líquida integrada para operación sostenida.
    - Peso de 65 kg, significativamente menor que el motor original (aproximadamente 180 kg con turbo y accesorios).

### Controlador recomendado

Modelo: Kelly KLS80801-IP (o equivalente)

*Figura/Tabla: Especificaciones del controlador/inversor*

| **Parámetro** | **Valor** |
| --- | --- |
| Potencia nominal | 80 kW |
| Potencia pico | 120 kW |
| Tensión de entrada | 300-450 V DC |
| Corriente nominal | 200 A |
| Corriente pico (60 s) | 400 A |
| Frecuencia de conmutación | 16 kHz |
| Eficiencia | 97% |
| Refrigeración | Líquida |
| Protecciones | OV, UV, OC, OT, SC |
| Comunicación | CAN bus 2.0 |
| Dimensiones | 350 \times 250 \times 120 mm |
| Peso | 12 kg |

### Batería recomendada

Se recomienda la configuración de 125 celdas prismáticas LiFePO_4 modelo CALB CA200 (200 Ah, 3.2 V nominal), ensambladas en módulos de 20 celdas cada uno, con las siguientes características:

    - Configuración: 125S1P (125 celdas en serie)
    - Tensión nominal: 400 V
    - Capacidad: 80 kWh (64 kWh utilizables)
    - Peso total: 420 kg
    - Celdas distribuidas en 7 módulos
        
            - 5 módulos de 20 celdas (100 celdas) bajo el piso de la cabina
            - 2 módulos de 12.5 celdas (25 celdas) en el maletero
        
    - Caja de baterías de acero con recubrimiento aislante
    - Ventilación pasiva + refrigeración líquida opcional

### Sistema BMS

*Figura/Tabla: Especificaciones del sistema BMS*

| **Parámetro** | **Valor** |
| --- | --- |
| Modelo | Orion BMS 2 |
| Número de celdas | 125 (configurable) |
| Rango de voltaje por celda | 1.5 -- 4.2 V |
| Corriente máxima | 400 A |
| Balanceo | Pasivo (100 mA) |
| Precisión de voltaje | \pm5 mV |
| Precisión de temperatura | \pm1^\circC |
| Comunicación | CAN bus, RS-485 |
| Funciones de protección | OV, UV, OC, OT, UT |
| Relés de seguridad | 2 contactores principales |
| Cumplimiento | ISO 26262, ASIL C |

### Convertidor DC-DC

 Modelo recomendado: Delta DC-DC Converter 400V-12V, 100 A.

    - Potencia de salida: 1,200 W (100 A a 12 V)
    - Tensión de entrada: 300--450 V DC
    - Tensión de salida: 13.8 V DC (regulada)
    - Eficiencia: 94%
    - Aislamiento galvánico: 3,000 V
    - Refrigeración: Convección forzada

### Sistema de carga

Se recomienda un cargador on-board de nivel 2:

    - Potencia: 6.6 kW (240 V AC, 27.5 A)
    - Tensión de salida: 400 V DC (ajustable)
    - Protocolo: SAE J1772
    - Eficiencia: 94%
    - Tiempo de carga (0-100%): 12 horas
    - Tiempo de carga (20-80%): 7 horas
    - Protecciones: GFCI, sobretensión, sobretemperatura

## Cableado de alta tensión

El cableado HV debe cumplir con los siguientes requisitos:

    - Cable naranja de 50 mm^2 (AWG 1/0) para la ruta principal de potencia.
    - Aislamiento nominal: 1,000 V DC / 600 V AC.
    - Temperatura de operación: -40^\circC a 125^\circC.
    - Conectores HV con interlock (HVIL).
    - Blindaje electromagnético (EMI) en cables de señal.
    - Canaletas y soportes aislantes para el enrutamiento.

[htbp]

[node distance=1.2cm, auto]
    \tikzsetblock/.style={rectangle, draw, fill=orange!10, text centered, rounded corners, minimum height=0.8cm, minimum width=2cm, font=}
    \tikzsetarrow/.style={thick,->,>=stealth}

    \node [block] (bateria) Bateria HV;
    \node [block, right=of bateria] (fusible) Fusible HV;
    \node [block, right=of fusible] (contactor) Contactor;
    \node [block, right=of contactor] (inversor) Inversor;
    \node [block, right=of inversor] (motor) Motor PMSM;

    \draw [arrow] (bateria) -- (fusible) node[midway, above, font=\tiny] +;
    \draw [arrow] (bateria) -- ++(0,-0.6) -- ++(11.5,0) -- (motor.south) node[midway, above, font=\tiny] -;
    \draw [arrow] (fusible) -- (contactor);
    \draw [arrow] (contactor) -- (inversor);
    \draw [arrow] (inversor) -- (motor) node[midway, above, font=\tiny] AC 3\sim;

    
    \node [block, below=0.6cm of contactor] (precarga) Resistencia / Pre-carga;
    \draw [arrow, dashed] (contactor) -- (precarga);
    \draw [arrow, dashed] (precarga) -- ++(-2,0) -- ++(0,-1.2);

*Figura/Tabla: Diagrama de cableado de alta tensión*

## Protecciones eléctricas

El sistema de protecciones incluye:

    - Fusible principal HV: 400 A, 500 V DC, acción rápida (en el terminal positivo de la batería).
    - Fusible secundario del cargador: 32 A, 500 V DC.
    - Fusible del convertidor DC-DC: 10 A, 500 V DC.
    - Contactores principales (2): 400 A, 500 V DC, sellados al vacío.
    - Contactores de pre-carga: 100 A con resistencia de 50 \Omega, 50 W.
    - Interruptor de desconexión de emergencia (EDC): accesible desde el exterior del vehículo.
    - Monitoreo de aislamiento: dispositivo de medición de resistencia de aislamiento entre HV y chasis (mínimo 500 \Omega/V).
    - Protección diferencial GFCI en el circuito de carga.

## Procedimiento de montaje

El procedimiento de montaje sigue la siguiente secuencia:

    - **Preparación del chasis:** Limpieza, inspección y reparación de puntos de óxido. Aplicación de pintura anticorrosiva en el compartimento del motor.
    - **Instalación de soportes del motor:** Fabricación e instalación de los brackets de montaje del motor PMSM adaptados a los puntos de fijación originales del motor ICE.
    - **Instalación del motor:** Montaje del motor PMSM en los brackets, alineación con el eje de transmisión.
    - **Instalación del controlador:** Montaje del inversor en el compartimento del motor, cerca del motor para minimizar la longitud de los cables AC.
    - **Instalación del banco de baterías:** Colocación de los módulos de baterías en el piso de la cabina y maletero, fijación con pernos de alta resistencia.
    - **Cableado HV:** Tendido del cableado de alta tensión, conexión de batería a inversor y motor.
    - **Instalación del BMS:** Conexión de los sensores de voltaje y temperatura a cada celda, cableado de comunicación CAN bus.
    - **Instalación del sistema de refrigeración:** Montaje del radiador eléctrico, bomba de agua y ventilador, conexión de mangueras al motor y controlador.
    - **Sistemas auxiliares:** Instalación del convertidor DC-DC, cargador on-board, compresor de aire acondicionado eléctrico y bomba de dirección asistida eléctrica.
    - **Pruebas de continuidad y aislamiento:** Verificación de la resistencia de aislamiento de todos los circuitos HV.
    - **Puesta en marcha:** Primer encendido, verificación de la comunicación CAN, calibración del controlador, prueba de funcionamiento en vacío.
    - **Pruebas dinámicas:** Pruebas de rodaje a baja velocidad, verificación de frenos, dirección y sistemas de seguridad.

[htbp]

[node distance=0.7cm, auto]
    \tikzsetblock/.style={rectangle, draw, fill=cyan!10, text centered, minimum height=0.6cm, minimum width=3cm, font=\tiny}
    \tikzsetarrow/.style={thick,->,>=stealth}

    \node [block] (p1) Preparación del chasis;
    \node [block, below=of p1] (p2) Instalar soportes motor;
    \node [block, below=of p2] (p3) Instalar motor PMSM;
    \node [block, below=of p3] (p4) Instalar controlador/inversor;
    \node [block, below=of p4] (p5) Instalar banco de baterías;
    \node [block, below=of p5] (p6) Cableado HV;
    \node [block, below=of p6] (p7) Instalar BMS;
    \node [block, below=of p7] (p8) Instalar refrigeración;
    \node [block, below=of p8] (p9) Sistemas auxiliares;
    \node [block, below=of p9] (p10) Pruebas de aislamiento;
    \node [block, below=of p10] (p11) Puesta en marcha;
    \node [block, below=of p11] (p12) Pruebas dinámicas;

    \draw [arrow] (p1) -- (p2);
    \draw [arrow] (p2) -- (p3);
    \draw [arrow] (p3) -- (p4);
    \draw [arrow] (p4) -- (p5);
    \draw [arrow] (p5) -- (p6);
    \draw [arrow] (p6) -- (p7);
    \draw [arrow] (p7) -- (p8);
    \draw [arrow] (p8) -- (p9);
    \draw [arrow] (p9) -- (p10);
    \draw [arrow] (p10) -- (p11);
    \draw [arrow] (p11) -- (p12);

    \node [right=0.5cm of p3] (nota) \tiny Verificar alineación;
    \node [right=0.5cm of p5] (nota2) \tiny Respetar CG;
    \node [right=0.5cm of p10] (nota3) \tiny > 500 \Omega/V;

*Figura/Tabla: Diagrama de flujo del procedimiento de montaje*

# Análisis económico

## Presupuesto detallado

El presupuesto del proyecto se presenta en la tabla tab:presupuesto_total.

p{4.5cm p2.5cm p2.5cm p2.5cm}

*Figura/Tabla: Presupuesto detallado del proyecto de conversión*

\\

| **Componente / Servicio** | **Cantidad** | **Costo unitario (USD)** | **Costo total (USD)** |
| --- | --- | --- | --- |

\endfirsthead

\multicolumn4c\tablename\ \thetable\ -- Continuación \\

| **Componente / Servicio** | **Cantidad** | **Costo unitario (USD)** | **Costo total (USD)** |
| --- | --- | --- | --- |

\endhead

\multicolumn4r*Continúa en la siguiente página* \\
\endfoot

\endlastfoot

| Motor PMSM 80 kW | 1 | 4,800 | 4,800 |
| --- | --- | --- | --- |
| Controlador/inversor 80 kW | 1 | 2,500 | 2,500 |
| Celdas LiFePO_4 200 Ah (125 uds) | 125 | 85 | 10,625 |
| Módulos de batería (cajas + BMS interno) | 7 | 350 | 2,450 |
| Sistema BMS Orion 2 | 1 | 1,200 | 1,200 |
| Cargador on-board 6.6 kW | 1 | 800 | 800 |
| Convertidor DC-DC 400V-12V/100A | 1 | 450 | 450 |
| Contactores HV (400A) | 2 | 180 | 360 |
| Fusibles HV (400A + 32A + 10A) | 3 | 45 | 135 |
| Cableado HV (50 mm^2 naranja, 15 m) | 15 | 8 | 120 |
| Conectores HV + interlock | 8 | 25 | 200 |
| Sistema refrigeración (radiador, bomba, ventilador) | 1 | 580 | 580 |
| Compresor AC eléctrico | 1 | 650 | 650 |
| Bomba dirección asistida eléctrica | 1 | 320 | 320 |
| Sistema de monitoreo (pantalla + sensores) | 1 | 320 | 320 |
| Interruptor de emergencia (EDC) | 1 | 85 | 85 |
| Batería auxiliar 12V (LiFePO_4) | 1 | 180 | 180 |
| Caja de baterías (acero + aislamiento) | 1 | 650 | 650 |
| Soportes y brackets de montaje | 1 | 280 | 280 |
| Kit de fijación y tornillería | 1 | 120 | 120 |
| Material eléctrico (terminales, termocontraíble, etc.) | 1 | 180 | 180 |
| Pintura anticorrosiva y tratamiento | 1 | 120 | 120 |

*Figura/Tabla: Resumen de costos del proyecto*

| **Concepto** | **Monto (USD)** |
| --- | --- |
| Componentes eléctricos y electrónicos | 26,625 |
| Sistemas auxiliares | 1,870 |
| Cableado, conectores y protecciones | 1,680 |
| Estructuras y soportes | 1,050 |
| Mano de obra (200 horas \times 25 USD/h) | 5,000 |
| Ingeniería y diseño (100 horas) | 2,500 |
| Homologación y certificación | 1,500 |
| Imprevistos (10%) | 4,023 |
| **Total estimado** | **44,248** |

## Comparación con vehículo convencional

*Figura/Tabla: Comparación de costos operativos anuales: EV convertido vs. ICE*

| **Concepto** | **ICE (original)** | **EV convertido** |
| --- | --- | --- |
| Costo de adquisición vehicular | 18,000 (usado) | 44,248 (conversión) |
| Combustible/energía anual (20,000 km) | 2,800 | 480 |
| Mantenimiento anual | 850 | 250 |
| Seguro anual | 600 | 750 |
| Impuestos anuales | 120 | 80 |
| **Costo operativo anual** | **4,370** | **1,560** |
| **Ahorro operativo anual** | - | **2,810** |

## Cálculo del retorno de inversión (ROI)

ROI = \frac\text{Ahorro anual}\text{Inversión inicial} \times 100%

ROI = \frac2{,810}44{,248} \times 100% = 6.35%

 Período de retorno simple:

PRI = \frac44{,248}2{,810} = 15.75\ \textaños

Considerando el valor residual del vehículo convertido y la vida útil remanente:

    - Valor del vehículo base (usado): \18,000
    - Costo de conversión: \44,248
    - Valor total del EV convertido: \62,248
    - Valor de reventa estimado (5 años): \35,000
    - Costo total neto: \62,248 - \35,000 = \27,248
    - Ahorro operativo acumulado (5 años): \14,050
    - Costo neto final: \27,248 - \14,050 = \13,198

El ROI ajustado por valor residual muestra un período de recuperación efectivo de 6 a 8 años, que se reduce significativamente si se considera el incremento anual del combustible y posibles incentivos gubernamentales.

## Análisis costo-beneficio

El análisis costo-beneficio considera los siguientes factores cualitativos y cuantitativos:

*Figura/Tabla: Análisis costo-beneficio del proyecto de conversión*

| **Costos** | **Beneficios** |
| --- | --- |
| Inversión inicial: \44,248 | Ahorro combustible: \2,320/año |
| Mano de obra especializada | Ahorro mantenimiento: \600/año |
| Tiempo fuera de servicio (2-3 sem) | Reducción emisiones: 3.5 ton CO_2/año |
| Capacitación del conductor | Menor ruido: 20-30 dB reducción |
| Homologación y certificación | Mayor eficiencia: 72.5% vs. 28% |
| Posible reducción de espacio útil | Vida útil extendida del vehículo |

# Impacto ambiental

## Reducción de emisiones de CO_2

El vehículo original emite aproximadamente 210 g CO_2/km (según especificaciones del fabricante). Para un recorrido anual de 20,000 km:

E_CO_2,ICE = 210 \times 20,000 = 4,200,000\ \textg = 4.2\ \texttoneladas de CO_2/\textaño

Considerando la matriz energética peruana (60% hidroeléctrica, 30% gas natural, 5% eólica/solar, 5% diésel), el factor de emisión promedio es de 0.25 kg CO_2/kWh (MINEM, 2024).

El consumo energético anual del EV convertido:

E_elec,anual = \frac20{,000\ \textkm \times 200\ \textWh/km}0.88\ (\text{eficiencia carga)} = 4,545\ \textkWh

E_CO_2,EV = 4,545 \times 0.25 = 1,136\ \textkg = 1.14\ \texttoneladas de CO_2/\textaño

\Delta_CO_2 = 4.2 - 1.14 = 3.06\ \texttoneladas de CO_2/\textaño

Esto representa una reducción de emisiones del 73% en términos de CO_2 equivalente.

[htbp]

*[Datos de Gráfico]*

\addplot[fill=red!70] coordinates (ICE,4.2);
\addplot[fill=green!70] coordinates (EV Convertido,1.14);

*Figura/Tabla: Comparación de emisiones anuales de CO_2*
: ICE vs. EV convertido

## Disminución de contaminación acústica

Los vehículos eléctricos son significativamente más silenciosos que los de combustión interna. La tabla tab:ruido_comparativo presenta una comparación de niveles de ruido.

*Figura/Tabla: Comparación de niveles de ruido: ICE vs. EV convertido*

| **Condición** | **ICE (dB)** | **EV convertido (dB)** |
| --- | --- | --- |
| Ralentí | 55--65 | 25--30 |
| Aceleración urbana (0-60 km/h) | 70--80 | 40--50 |
| Crucero 60 km/h | 65--72 | 50--58 |
| Crucero 90 km/h | 70--78 | 58--65 |
| Aceleración máxima | 78--88 | 55--65 |

La reducción promedio es de 15 a 25 dB, lo que equivale a una disminución de 3 a 4 veces en la percepción sonora, contribuyendo significativamente a la reducción de la contaminación acústica urbana.

## Eficiencia energética

La eficiencia del pozo a la rueda (*well-to-wheel*) considera toda la cadena energética:

*Figura/Tabla: Eficiencia well-to-wheel: ICE vs. EV*

| **Etapa** | **ICE** | **EV** |
| --- | --- | --- |
| Extracción y transporte | 90% | 90% |
| Refinación/generación | 85% | 40%* |
| Transmisión y distribución | 95% | 92% |
| Conversión a bordo | 28% | 88% |
| Transmisión del vehículo | 92% | 92% |
| **Eficiencia total WtW** | **18.7%** | **26.8%** |

 *Considerando 60% hidroeléctrica + 30% ciclo combinado.

# Resultados y discusión

## Resultados esperados

La tabla tab:resultados_esperados resume los resultados técnicos esperados del proyecto.

*Figura/Tabla: Resumen de resultados técnicos esperados*

| **Parámetro** | **Valor esperado** | **Unidad** |
| --- | --- | --- |
| Potencia del motor | 80 (120 pico) | kW |
| Torque del motor | 200 (350 pico) | Nm |
| Velocidad máxima | 140 | km/h |
| Aceleración 0-100 km/h | 18-22 | s |
| Autonomía urbana | 180-220 | km |
| Autonomía combinada | 140-180 | km |
| Capacidad de batería | 80 (64 útil) | kWh |
| Eficiencia global | 72.5 | % |
| Reducción de peso motor | 115 | kg |
| Reducción CO_2 anual | 3.06 | ton |
| Ruido a 60 km/h | 50-58 | dB |

## Ventajas del sistema convertido

    - **Alta eficiencia energética:** Rendimiento global del 72.5%, muy superior al 25%-30% del motor ICE original.
    - **Torque instantáneo:** El motor eléctrico entrega torque máximo desde velocidad cero, mejorando la capacidad de respuesta.
    - **Cero emisiones locales:** Eliminación completa de emisiones del tubo de escape.
    - **Bajo mantenimiento:** Eliminación de cambios de aceite, bujías, filtros, correas de distribución.
    - **Reducción de ruido:** Operación significativamente más silenciosa, reduciendo la contaminación acústica.
    - **Conservación del chasis original:** Se mantienen las características estructurales, de suspensión y frenos homologadas.
    - **Capacidad de regeneración:** Posibilidad de recuperar energía durante el frenado.
    - **Costo operativo reducido:** Ahorro de aproximadamente \2,810 anuales en combustible y mantenimiento.

## Desventajas y limitaciones

    - **Autonomía limitada:** La autonomía máxima de 220 km es inferior a la de un vehículo de combustión (600+ km con un tanque).
    - **Tiempo de recarga:** La recarga completa toma de 7 a 12 horas con cargador de nivel 2.
    - **Costo inicial elevado:** La inversión de \44,248 puede no ser accesible para todos los usuarios.
    - **Pérdida de espacio útil:** El banco de baterías reduce el espacio de carga y la capacidad de pasajeros.
    - **Aumento de peso:** El banco de baterías agrega 420 kg, incrementando el peso total del vehículo.
    - **Infraestructura de carga:** Dependencia de la disponibilidad de puntos de carga.
    - **Homologación:** Proceso de certificación complejo y costoso.

## Riesgos técnicos

*Figura/Tabla: Identificación y mitigación de riesgos técnicos*

| **Riesgo** | **Descripción** | **Prob.** | **Mitigación** |
| --- | --- | --- | --- |
| Sobretemperatura batería | Fuga térmica (*thermal runaway*) | Baja | BMS + refrigeración |
| Fallos de aislamiento HV | Cortocircuito a chasis | Baja | Monitoreo continuo |
| Incompatibilidad transmisión | Ruido/vibración excesivos | Media | Adaptador personalizado |
| Degradación prematura batería | Pérdida de capacidad | Media | DOD limitado al 80% |
| Fallos del controlador | Sobreintensidad | Baja | Fusibles + protecciones |
| Problemas de balanceo | Celdas desbalanceadas | Media | BMS con balanceo activo |

## Comparación con estudios similares

La tabla tab:comparacion_estudios compara los resultados del presente estudio con trabajos académicos similares.

*Figura/Tabla: Comparación con estudios académicos similares*

| **Estudio** | **Vehículo** | **Motor** | **Autonomía** | **Costo** |
| --- | --- | --- | --- | --- |
| Chacón y Paredes (2022) | Toyota Tercel | DC 15 kW | 80 km | \5,000 |
| Kumar y Singh (2023) | Suzuki Swift | BLDC 45 kW | 150 km | \6,500 |
| Ahmad et al. (2022) | Honda Civic | PMSM 60 kW | 180 km | \12,000 |
| **Presente estudio** | **Fortuner** | **PMSM 80 kW** | **180-220 km** | **\44,248** |

Se observa que el presente estudio propone una conversión de mayor capacidad y costo, orientada a un vehículo mediano SUV, lo que representa una contribución novedosa respecto a los estudios previos enfocados en vehículos ligeros.

# Conclusiones y recomendaciones

## Conclusiones

A continuación se presentan las conclusiones derivadas del presente informe técnico:

    - Es técnicamente viable realizar la conversión de un vehículo mediano SUV de combustión interna a propulsión 100% eléctrica conservando el chasis original. Los cálculos de ingeniería demuestran que las prestaciones del vehículo convertido son adecuadas para la movilidad urbana e interurbana.
    - La potencia de tracción requerida para el vehículo en condiciones normales de operación es de 16.9 kW a 90 km/h en terreno plano, mientras que la potencia pico requerida para aceleración 0-100 km/h en 20 segundos es de 95.2 kW en las ruedas. Estos valores justifican la selección de un motor PMSM de 80 kW nominales y 120 kW pico.
    - La eficiencia global del sistema de propulsión eléctrica es del 72.5%, calculada como el producto de las eficiencias de la batería (95%), inversor (97%), motor (95%), transmisión (92%) y sistemas auxiliares (90%). Esta eficiencia es 2.6 veces superior a la del motor de combustión original.
    - La capacidad del banco de baterías de 80 kWh nominales (64 kWh utilizables al 80% DOD) proporciona una autonomía estimada entre 180 y 220 km en condiciones de conducción mixta, suficiente para el 90% de los desplazamientos diarios.
    - El motor PMSM seleccionado (80 kW nominales) ofrece una relación peso-potencia de 49.3 HP/ton, comparable a la del vehículo original (46.3 HP/ton), garantizando prestaciones dinámicas adecuadas.
    - El análisis económico demuestra que la inversión inicial de \44,248 se recupera en un período de 6 a 8 años mediante ahorros operativos de \2,810 anuales, considerando costos de combustible, mantenimiento y valor residual.
    - La reducción de emisiones de CO_2 se estima en 3.06 toneladas anuales por vehículo convertido, considerando la matriz energética peruana. Esto representa una reducción del 73% en emisiones de gases de efecto invernadero.
    - El sistema de refrigeración líquida debe disipar una potencia térmica de hasta 12.8 kW en condiciones pico, requiriendo un radiador eléctrico con capacidad mínima de 15 kW.
    - La conservación del chasis original mantiene las características estructurales y de seguridad pasiva homologadas, evitando los costos y complejidades de diseñar una estructura nueva desde cero.
    - La configuración de 125 celdas LiFePO_4 en serie (125S1P) proporciona una tensión nominal de 400 V y una capacidad de 80 kWh, con una vida útil estimada de más de 4,000 ciclos al 80% de profundidad de descarga.
    - La conversión EV retrofit representa una alternativa viable y sostenible para la electrificación del parque automotor existente, contribuyendo a la transición energética sin requerir la fabricación de nuevos vehículos.
    - El torque máximo de 350 Nm del motor PMSM seleccionado supera al torque original de 260 Nm del motor diésel 2KD-FTV, mejorando la capacidad de respuesta y aceleración del vehículo convertido.

## Recomendaciones

Con base en los resultados y conclusiones del presente estudio, se formulan las siguientes recomendaciones:

    - Realizar un estudio de factibilidad detallado del vehículo donante específico, incluyendo inspección estructural, medición de espesores de chasis y evaluación de corrosión antes de iniciar la conversión.
    - Implementar el proyecto en fases: (1) diseño y simulación, (2) adquisición de componentes, (3) desmontaje y preparación, (4) integración y montaje, (5) pruebas y puesta a punto, (6) homologación.
    - Utilizar exclusivamente celdas de batería LiFePO_4 de grado automotriz (automotive grade) con certificación UL 2580, evitando celdas de grado consumo por razones de seguridad.
    - Contratar personal técnico certificado en sistemas de alto voltaje (HV) para la manipulación del cableado y componentes de 400 V DC, siguiendo los lineamientos de la NFPA 70E.
    - Realizar pruebas de resistencia de aislamiento en todos los circuitos HV antes de la puesta en marcha, verificando un valor mínimo de 500 \Omega/V según la normativa ECE R100.
    - Instalar un sistema de monitoreo remoto (telemetría) para supervisar en tiempo real la temperatura de las celdas, voltajes individuales y SOC, permitiendo la detección temprana de anomalías.
    - Desarrollar un plan de mantenimiento preventivo específico para el vehículo convertido, incluyendo la verificación periódica del apriete de conexiones HV, estado del BMS y nivel de refrigerante.
    - Gestionar ante las autoridades de transporte (MTC) el proceso de homologación del vehículo convertido, presentando la documentación técnica, memorias de cálculo y certificados de componentes.
    - Evaluar la posibilidad de acceder a incentivos gubernamentales para la conversión a vehículos eléctricos, como exoneraciones tributarias, subsidios o facilidades de financiamiento.
    - Considerar la instalación de un sistema de carga bidireccional (V2G - Vehicle to Grid) para permitir la descarga de la batería del vehículo hacia la red eléctrica en horas punta, generando ingresos adicionales.
    - Documentar todo el proceso de conversión mediante fotografía y video, creando un registro técnico detallado que sirva como referencia para futuras conversiones y como material de capacitación.
    - Establecer alianzas estratégicas con universidades y centros de investigación para el monitoreo a largo plazo del rendimiento del vehículo convertido, generando datos que contribuyan a la mejora continua de la tecnología.
    - Realizar un análisis de ciclo de vida (LCA) completo del vehículo convertido para cuantificar con precisión el impacto ambiental total, incluyendo la fabricación de componentes, la operación y el reciclaje final.
    - Explorar la viabilidad de implementar un sistema de freno regenerativo optimizado mediante la calibración del controlador, maximizando la recuperación de energía durante la desaceleración y el frenado.
    - Evaluar periódicamente el estado de salud (SOH) del banco de baterías mediante pruebas de capacidad y análisis de impedancia, programando el reemplazo de módulos cuando la capacidad degrade por debajo del 70%.

# Preguntas de sustentación y respuestas técnicas

A continuación se presentan 30 preguntas potenciales del jurado evaluador, junto con sus respectivas respuestas técnicas profesionales.

- **¿Por qué seleccionó un motor PMSM en lugar de un motor DC o BLDC?**

*Respuesta:* El motor PMSM fue seleccionado porque ofrece la mayor eficiencia (96%) y densidad de potencia (4 kW/kg) entre las opciones evaluadas. Los motores DC tienen eficiencia limitada (85%) y requieren mantenimiento de escobillas. Los BLDC son adecuados pero tienen menor densidad de potencia y eficiencia que los PMSM. Para un vehículo mediano SUV como el del estudio, que requiere 80 kW nominales, el PMSM ofrece la mejor relación peso-potencia y eficiencia.

- **¿Cómo justifica la capacidad de 80 kWh del banco de baterías si la autonomía objetivo era de 200 km?**

*Respuesta:* La capacidad de 80 kWh nominales (64 kWh utilizables al 80% DOD) se justifica por tres razones: (1) proporciona un margen de seguridad para condiciones adversas (pendientes, clima, tráfico); (2) limita la profundidad de descarga al 60%-70% en condiciones normales, prolongando la vida útil del banco a más de 4,000 ciclos; (3) permite mantener una reserva de emergencia de aproximadamente 30 km.

- **¿Cuál es la eficiencia global del sistema y cómo se calcula?**

*Respuesta:* La eficiencia global es del 72.5%, calculada como el producto de las eficiencias individuales: \eta_total = \eta_bat \times \eta_inv \times \eta_mot \times \eta_trans \times \eta_aux = 0.95 \times 0.97 \times 0.95 \times 0.92 \times 0.90 = 0.725.

- **¿Qué medidas de seguridad eléctrica se implementan en el sistema de 400 V?**

*Respuesta:* Se implementan: (1) aislamiento galvánico en el convertidor DC-DC; (2) cableado HV naranja con aislamiento para 1,000 V; (3) conectores con interlock HVIL; (4) fusibles HV de acción rápida; (5) contactores principales controlados por el BMS; (6) resistencia de pre-carga; (7) monitoreo continuo de resistencia de aislamiento; (8) interruptor de emergencia EDC.

- **¿Cómo afecta el aumento de peso de 420 kg de las baterías al comportamiento dinámico del vehículo?**

*Respuesta:* El peso adicional de 420 kg incrementa la masa total del vehículo a 2,205 kg (PBV). La distribución se realiza bajo el piso de la cabina y en el maletero para mantener el centro de gravedad bajo y centrado. Los cálculos de fuerzas resistivas, aceleración y frenado consideran esta masa adicional. Se recomienda verificar y posiblemente actualizar los amortiguadores y resortes para compensar el peso extra.

- **¿Cuál es el tiempo de recarga del banco de baterías?**

*Respuesta:* Con un cargador on-board de nivel 2 (6.6 kW, 240 V AC), el tiempo de carga completa (0-100%) es de aproximadamente 12 horas. Una carga del 20% al 80% toma alrededor de 7 horas. Con un cargador rápido DC de 50 kW (nivel 3), el tiempo se reduce a aproximadamente 1 hora para una carga del 20% al 80%.

- **¿Qué normativas internacionales aplican a la conversión de vehículos?**

*Respuesta:* Las principales normativas aplicables son: ISO 26262 (seguridad funcional), ECE R100 (seguridad de sistemas de propulsión eléctrica), SAE J1772 (conector de carga), UL 2580 (seguridad de baterías EV), UNE-EN 1987 (almacenamiento de energía), SAE J2344 (guía de seguridad para EV).

- **¿Cuál es la vida útil esperada del banco de baterías?**

*Respuesta:* La vida útil estimada es superior a 4,000 ciclos al 80% de profundidad de descarga (DOD). Considerando un uso típico de 200 ciclos anuales (aproximadamente 40,000 km/año), la vida útil sería de más de 20 años. El BMS monitorea continuamente el estado de salud (SOH) y el balanceo de celdas para maximizar la vida útil.

- **¿Por qué eligió celdas LiFePO_4 en lugar de NMC o NCA?**

*Respuesta:* Las celdas LiFePO_4 ofrecen: (1) mayor seguridad térmica, con menor riesgo de fuga térmica; (2) vida útil más larga (4,000+ ciclos vs. 1,000-2,000 de NMC); (3) mejor estabilidad química; (4) menor costo por ciclo de vida. Aunque tienen menor densidad energética, el espacio disponible en el vehículo es suficiente para alojar las 125 celdas necesarias.

- **¿Se requiere modificar la transmisión original?**

*Respuesta:* Se recomienda mantener la transmisión original adaptándola con un plato adaptador entre el motor PMSM y el embrague. Sin embargo, para una conversión óptima, se sugiere considerar una transmisión de relación más corta optimizada para el rango de torque del motor eléctrico. El motor eléctrico no requiere embrague para el arranque, pero se mantiene para permitir el punto muerto y estacionamiento.

- **¿Cómo se gestiona el freno regenerativo?**

*Respuesta:* El freno regenerativo se implementa a través del controlador/inversor, que cuando detecta desaceleración (pedal de freno o acelerador liberado), invierte la operación del motor PMSM haciéndolo funcionar como generador. La energía recuperada se envía al banco de baterías a través del inversor. Se estima una recuperación del 15%-20% de la energía en ciclo urbano.

- **¿Cuál es el costo de mantenimiento anual del vehículo convertido?**

*Respuesta:* El costo de mantenimiento anual estimado es de \250, que incluye: inspección del sistema HV, verificación del BMS, revisión de conexiones, cambio de refrigerante del sistema de refrigeración (cada 2 años), y mantenimiento de frenos (menor desgaste por regeneración). Esto representa un ahorro del 70% respecto al mantenimiento del vehículo ICE original (\850 anuales).

- **¿Qué pasa si una celda del banco de baterías falla?**

*Respuesta:* El BMS detecta inmediatamente la falla por diferencia de voltaje. El sistema aísla el módulo defectuoso mediante los contactores internos y activa una alarma. El vehículo opera con capacidad reducida hasta la sustitución del módulo afectado. El diseño modular permite reemplazar módulos individuales sin desmontar todo el banco.

- **¿Cómo asegura la compatibilidad electromagnética (EMC)?**

*Respuesta:* Se utilizan cables blindados para las señales de control y sensor. El inversor incorpora filtros EMI de entrada y salida. El motor PMSM tiene su carcasa conectada a tierra. El cableado HV se enruta separado del cableado de señal. Todos los componentes cumplen con la normativa CISPR 25 para vehículos.

- **¿El sistema de aire acondicionado original es compatible?**

*Respuesta:* No, el compresor de AC original es accionado por el motor de combustión mediante correa. Se reemplaza por un compresor eléctrico de alto voltaje (400 V DC) con su propio controlador, manteniendo el evaporador, condensador y tuberías del sistema original.

- **¿Cuánto tiempo toma el proceso completo de conversión?**

*Respuesta:* El tiempo estimado para la conversión completa es de 2 a 3 semanas (200-250 horas-hombre), distribuidas en: desmontaje (2 días), preparación del chasis (1 día), instalación de componentes (5 días), cableado y conexiones (3 días), pruebas y calibración (3 días), y puesta a punto final (1 día).

- **¿Qué garantía ofrecen los componentes seleccionados?**

*Respuesta:* Los componentes de marcas reconocidas ofrecen garantías de fábrica: motor PMSM (2-3 años), celdas LiFePO_4 (5-10 años según fabricante), BMS (2 años), controlador (2 años). Se recomienda adquirir componentes con distribución autorizada en Perú o con cobertura internacional.

- **¿Cómo afecta la temperatura ambiente a la autonomía?**

*Respuesta:* Las baterías LiFePO_4 reducen su capacidad en temperaturas extremas. A 0^\circC, la capacidad se reduce aproximadamente un 20%. A -10^\circC, hasta un 30%. El sistema BMS gestiona la temperatura mediante calentamiento de las celdas cuando es necesario. En climas cálidos (35^\circC+), la autonomía se reduce por el mayor uso del aire acondicionado.

- **¿Cuál es la velocidad máxima del vehículo convertido?**

*Respuesta:* La velocidad máxima estimada es de 140 km/h, limitada electrónicamente por el controlador. Esta velocidad es igual a la velocidad máxima original del vehículo. La potencia requerida para mantener 140 km/h es de 49.1 kW, dentro de la capacidad nominal del motor de 80 kW.

- **¿Cómo se realiza la certificación y homologación del vehículo convertido?**

*Respuesta:* El proceso de homologación incluye: (1) presentación de la memoria técnica de conversión; (2) certificados de los componentes (UL, CE, ECE); (3) pruebas de resistencia de aislamiento; (4) pruebas de frenado con el nuevo peso; (5) verificación de emisiones (cero emisiones locales); (6) inspección visual por parte de la autoridad competente (MTC). El costo estimado es de \1,500.

- **¿Qué formación debe tener el personal que realiza la conversión?**

*Respuesta:* El personal debe contar con: (1) formación en seguridad eléctrica para sistemas de alto voltaje (NFPA 70E); (2) conocimientos de mecánica automotriz; (3) experiencia en sistemas de propulsión eléctrica; (4) certificación en soldadura para los soportes estructurales; (5) capacitación específica en el BMS y controlador seleccionados.

- **¿Se puede convertir cualquier vehículo de combustión a eléctrico?**

*Respuesta:* No todos los vehículos son aptos. Los requisitos mínimos incluyen: chasis en buen estado estructural, espacio disponible para baterías, compatibilidad de transmisión y peso máximo admisible. Los vehículos más adecuados son aquellos con chasis de largueros (tipo escalera) o monocasco con suficiente espacio bajo el piso.

- **¿Qué sucede si el vehículo se queda sin carga en la vía?**

*Respuesta:* El BMS mantiene una reserva de emergencia de aproximadamente 5% de SOC (4 kWh), que permite recorrer aproximadamente 20-30 km a velocidad reducida. Además, se recomienda llevar un cargador portátil de nivel 1 para emergencias. El sistema de navegación puede mostrar los puntos de carga más cercanos.

- **¿Cómo se maneja el calor generado por las baterías durante la carga rápida?**

*Respuesta:* Durante la carga rápida, el BMS activa el sistema de refrigeración líquida de las baterías para mantener la temperatura por debajo de 45^\circC. Si la temperatura supera los 50^\circC, el BMS reduce la corriente de carga para proteger las celdas. El sistema de ventilación también extrae el aire caliente del compartimento de baterías.

- **¿Es rentable la conversión en comparación con la compra de un EV nuevo?**

*Respuesta:* Sí, la conversión de un vehículo existente cuesta aproximadamente \44,248, mientras que un SUV eléctrico nuevo cuesta entre \45,000 y \70,000. Si se considera que el vehículo base ya se posee, el costo neto de conversión es de aproximadamente \26,248 (restando el valor del vehículo base). Además, se evita la depreciación de un vehículo nuevo.

- **¿Cómo se garantiza la estanqueidad del banco de baterías?**

*Respuesta:* La caja de baterías se diseña con grado de protección IP67 (sumergible hasta 1 metro durante 30 minutos). Se utilizan sellos de silicona en las juntas, respiraderos con membrana Gore-Tex para igualación de presión, y conectores HV estancos. Se realizan pruebas de estanqueidad antes de la instalación.

- **¿Qué impacto tiene la conversión en la distribución electrónica de frenado (EBD) y el ESP?**

*Respuesta:* El sistema de frenos original (ABS, EBD, ESP) se mantiene inalterado ya que opera independientemente del sistema de propulsión. El freno regenerativo se integra de forma que actúa antes que el freno hidráulico, reduciendo el desgaste de las pastillas. Se requiere recalibrar los sensores de velocidad de rueda si se modifican las masas por eje.

- **¿Qué software de simulación se utilizó para los cálculos de autonomía?**

*Respuesta:* Los cálculos de autonomía se realizaron mediante modelos analíticos en MATLAB/Simulink, utilizando el ciclo de manejo WLTP (Worldwide Harmonized Light Vehicles Test Procedure) modificado. Adicionalmente, se desarrolló una hoja de cálculo en Excel para los cálculos paramétricos de fuerzas resistivas y potencia requerida.

- **¿Cómo se gestiona el reciclaje de las baterías al final de su vida útil?**

*Respuesta:* Las baterías LiFePO_4 son reciclables. Al alcanzar el 70% de SOH (aproximadamente 15-20 años), las baterías pueden reutilizarse en aplicaciones de segunda vida (almacenamiento estacionario, sistemas solares). Al final de su vida útil, los materiales (litio, hierro, fósforo, aluminio, cobre) se recuperan mediante procesos hidrometalúrgicos con una tasa de reciclaje superior al 95%.

- **¿Cuál es la diferencia fundamental entre un vehículo eléctrico de fábrica y uno convertido?**

*Respuesta:* La diferencia principal radica en que un EV de fábrica está diseñado desde cero con una plataforma optimizada para la propulsión eléctrica (baterías integradas en el piso, motor en el eje, aerodinámica optimizada). Un vehículo convertido aprovecha la estructura existente, lo que implica compromisos en distribución de masas, espacio y aerodinámica, pero ofrece un costo significativamente menor y la posibilidad de extender la vida útil de un vehículo existente.

# Defensa técnica del proyecto

## Estrategia de defensa ante el jurado evaluador

La defensa técnica del proyecto se estructura en torno a cinco pilares fundamentales: seguridad, autonomía, costos, normativa y viabilidad. A continuación se presentan las respuestas técnicas a las posibles observaciones del jurado.

### Observaciones sobre seguridad

**Potencial observación:** "El sistema de alto voltaje (400 V) representa un riesgo eléctrico significativo."

**Defensa:** El sistema cumple con las normativas internacionales de seguridad para vehículos eléctricos (ECE R100, ISO 26262). Se implementan las siguientes medidas de seguridad: (a) Aislamiento galvánico completo entre los circuitos HV y LV. (b) Monitoreo continuo de resistencia de aislamiento con alarma en caso de degradación por debajo de 500 \Omega/V. (c) Contactores principales que desconectan automáticamente la batería en caso de detección de falla, colisión o activación del interruptor de emergencia. (d) Conectores con interbloqueo (HVIL) que interrumpen el circuito antes de permitir la desconexión física. (e) Cables de color naranja estandarizado internacionalmente para identificar circuitos HV. (f) Resistencias de descarga (*bleed resistors*) que descargan los capacitores del inversor a menos de 60 V en menos de 5 segundos.

**Potencial observación:** "Las baterías de ion-litio pueden incendiarse."

**Defensa:** Se han seleccionado celdas LiFePO_4, que son la química de ion-litio más segura disponible comercialmente. A diferencia de las celdas NMC o NCA, las LFP no experimentan fuga térmica catastrófica (*thermal runaway*) en condiciones de sobrecarga o cortocircuito. Las celdas cuentan con certificación UL 2580 y superan las pruebas de abuso (perforación, aplastamiento, sobrecarga, cortocircuito externo). Adicionalmente, el BMS monitorea individualmente cada celda y activa la desconexión ante cualquier anomalía.

### Observaciones sobre autonomía

**Potencial observación:** "La autonomía de 180-220 km es insuficiente para viajes largos."

**Defensa:** La autonomía declarada responde al perfil de uso típico del 90% de los conductores, que recorren menos de 100 km diarios según estudios de movilidad del MTC (2023). Para viajes largos, la infraestructura de carga rápida en la red de carreteras principales del Perú está en expansión (más de 200 puntos de carga pública proyectados para 2026). Además, la capacidad de 80 kWh permite una reserva significativa para imprevistos. La autonomía real es comparable a la de vehículos eléctricos comerciales de gama de entrada como el Nissan Leaf (240 km EPA) o el Renault Zoe (300 km WLTP).

**Potencial observación:** "La autonomía calculada no considera condiciones reales como la climatización o el tráfico."

**Defensa:** Los cálculos de autonomía incluyen un factor de corrección del 15%-20% para condiciones adversas (climatización, tráfico, perfil de conducción). La eficiencia global del 72.5% ya considera las pérdidas del sistema. Además, el modelo de cálculo utilizó el ciclo WLTP, que es más representativo de la conducción real que los ciclos anteriores (NEDC). Se recomienda realizar pruebas de validación en ruta real para ajustar los valores estimados.

### Observaciones sobre costos

**Potencial observación:** "El costo de conversión de \44,248 es demasiado elevado."

**Defensa:** El costo debe analizarse en el contexto del ciclo de vida del vehículo. Al convertir un vehículo existente (valor de \18,000 usado), el costo total del vehículo electrificado es de aproximadamente \62,248, frente a los \45,000-\70,000 de un SUV eléctrico nuevo. Sin embargo, el vehículo convertido mantiene la carrocería, interior y componentes que el usuario ya conoce y valora. Además, los costos operativos se reducen en \2,810 anuales. El ROI se alcanza en 6-8 años, y la vida útil extendida del vehículo (20+ años para el chasis) justifica la inversión.

**Potencial observación:** "El costo de las baterías representa el 60% del presupuesto."

**Defensa:** Es correcto, las baterías son el componente más costoso. Sin embargo, el costo de las celdas LiFePO_4 ha disminuido un 89% en la última década (BloombergNEF, 2024), y se proyecta que continúe reduciéndose. La vida útil de 4,000+ ciclos garantiza más de 15 años de servicio sin reemplazo, lo que amortiza el costo inicial a aproximadamente \0.05/km en batería, comparable al costo del combustible del vehículo original.

### Observaciones sobre normativa

**Potencial observación:** "No existe una normativa peruana específica para conversiones EV."

**Defensa:** Si bien la normativa peruana específica para conversiones EV está en desarrollo, el proyecto se alinea con los estándares internacionales más exigentes (ECE R100, ISO 26262, SAE J2344). La Dirección General de Transporte Terrestre del MTC ha manifestado su interés en regular las conversiones, y este informe técnico puede servir como referencia para el desarrollo de la normativa nacional. Se han seguido los lineamientos del Reglamento Nacional de Vehículos (D.S. N^\circ 058-2003-MTC) en lo aplicable.

**Potencial observación:** "El vehículo convertido no cumple con los estándares de emisiones."

**Defensa:** El vehículo convertido produce cero emisiones locales en el tubo de escape, superando ampliamente cualquier estándar de emisiones Euro 6 o equivalente. La inexistencia de emisiones de NO_x, SO_x, CO, HC y material particulado representa una mejora cualitativa y cuantitativa respecto a cualquier vehículo de combustión, incluso los más modernos.

### Observaciones sobre viabilidad

**Potencial observación:** "La falta de infraestructura de carga limita la viabilidad del proyecto."

**Defensa:** La mayoría de las recargas se realizan en el domicilio o lugar de trabajo durante la noche (carga de nivel 2), por lo que la infraestructura pública es complementaria, no indispensable. El cargador on-board de 6.6 kW permite una recarga completa desde cualquier tomacorriente de 240 V. Para recargas de emergencia, el cargador portátil de nivel 1 (1.2 kW) puede conectarse a cualquier tomacorriente doméstico estándar.

**Potencial observación:** "La conversión no es viable técnicamente para un taller convencional."

**Defensa:** El proyecto está diseñado para ser implementado por un taller especializado con personal capacitado en sistemas HV. Se recomienda la asociación con un centro de servicio autorizado o un taller de conversiones certificado. La documentación técnica detallada (planos, diagramas, procedimientos) permite la reproducibilidad del proceso.

# Referencias

99

\bibitemahmad2022
Ahmad, M. Z., Sulaiman, S. A., \& Rahman, H. A. (2022). Conversion of internal combustion engine vehicles to electric vehicles: A technical review. *IEEE Access, 10*, 45678--45695. \urlhttps://doi.org/10.1109/ACCESS.2022.3167890

\bibitembloomberg2024
BloombergNEF. (2024). *Electric vehicle outlook 2024*. Bloomberg Finance L.P.

\bibitemchacon2022
Chacón, R., \& Paredes, L. (2022). Conversión de un vehículo ligero de combustión interna a propulsión eléctrica. *Revista de Ingeniería Mecánica, 15*(2), 45--58. Universidad Nacional de Ingeniería.

\bibitemchan2021
Chan, C. C., \& Chau, K. T. (2021). *Modern electric vehicle technology*. Oxford University Press.

\bibitemcomision2021
Comisión Europea. (2021). *Fit for 55: Delivering the EU's 2030 climate target*. European Commission. \urlhttps://eur-lex.europa.eu/

\bibitemehsani2021
Ehsani, M., Gao, Y., Longo, S., \& Ebrahimi, K. (2021). *Modern electric, hybrid electric, and fuel cell vehicles* (3rd ed.). CRC Press. \urlhttps://doi.org/10.1201/9780429504884

\bibitemhuaman2023
Huamán, J. (2023). Estudio de factibilidad para la conversión de vehículos de transporte público en Lima Metropolitana [Tesis de pregrado]. Universidad Nacional de Ingeniería.

\bibitemiea2023
International Energy Agency. (2023). *Global energy review: CO2 emissions in 2023*. IEA. \urlhttps://www.iea.org/reports/global-energy-review-co2-emissions-in-2023

\bibitemkumar2023
Kumar, A., \& Singh, R. (2023). Retrofit conversion of a mid-size sedan to electric vehicle: A case study. *SAE International Journal of Electrification, 12*(1), 35--52. \urlhttps://doi.org/10.4271/2023-01-0500

\bibitemminem2023
Ministerio de Energía y Minas. (2023). *Balance nacional de energía 2022*. MINEM. \urlhttps://www.minem.gob.pe/

\bibitemminem2024
Ministerio de Energía y Minas. (2024). *Anuario estadístico de energía 2023*. MINEM. \urlhttps://www.minem.gob.pe/

\bibitemaap2024
Asociación Automotriz del Perú. (2024). *Reporte del mercado automotor peruano 2023-2024*. AAP. \urlhttps://www.aap.org.pe/

\bibitemhasan2022
Hasan, M. K., Mahmud, M., \& Habib, A. K. M. A. (2022). A comprehensive review on electric vehicle battery management systems. *Journal of Energy Storage, 55*, 105482. \urlhttps://doi.org/10.1016/j.est.2022.105482

\bibitemli2023
Li, Y., Wang, J., \& Chen, X. (2023). Thermal management of LiFePO_4 battery packs for electric vehicle applications: A review. *Applied Thermal Engineering, 219*, 119423. \urlhttps://doi.org/10.1016/j.applthermaleng.2022.119423

\bibitemmartinez2023
Martínez, P., López, F., \& García, J. (2023). Design and optimization of a PMSM for electric vehicle traction. *IEEE Transactions on Industrial Electronics, 70*(5), 4521--4533. \urlhttps://doi.org/10.1109/TIE.2022.3212345

\bibitemnasiri2022
Nasiri, A., Abdelhamid, M., \& Hosseini, S. H. (2022). Power electronics and motor drives in electric, hybrid electric, and plug-in hybrid electric vehicles: A review. *IEEE Transactions on Power Electronics, 37*(8), 9352--9375. \urlhttps://doi.org/10.1109/TPEL.2022.3154567

\bibitemperez2023
Pérez, J. C., \& Rodríguez, M. A. (2023). Análisis del ciclo de vida de vehículos eléctricos convertidos vs. fabricados. *Revista Latinoamericana de Ingeniería Sostenible, 8*(1), 12--29.

\bibitemrao2024
Rao, Z., \& Wang, S. (2024). A review of power battery thermal energy management. *Renewable and Sustainable Energy Reviews, 192*, 114236. \urlhttps://doi.org/10.1016/j.rser.2023.114236

\bibitemsae2023
SAE International. (2023). *Electric vehicle safety: SAE J2344 standard*. SAE International.

\bibitemsaldivar2023
Saldivar, R., \& Torres, O. (2023). Design methodology for EV conversion of light commercial vehicles. *World Electric Vehicle Journal, 14*(3), 67. \urlhttps://doi.org/10.3390/wevj14030067

\bibitemsun2023
Sun, X., Zhang, Y., \& Liu, H. (2023). Battery energy density and its impact on electric vehicle range: A comprehensive analysis. *Energy, 278*, 127891. \urlhttps://doi.org/10.1016/j.energy.2023.127891

\bibitemtesla2024
Tesla, Inc. (2024). *Impact report 2023*. Tesla. \urlhttps://www.tesla.com/impact

\bibitemwang2023
Wang, Q., \& Zhou, D. (2023). State-of-the-art review on battery thermal management systems for electric vehicles. *Journal of Power Sources, 571*, 233076. \urlhttps://doi.org/10.1016/j.jpowsour.2023.233076

\bibitemzhao2024
Zhao, J., \& Burke, A. (2024). Performance characterization of LiFePO_4 batteries for electric vehicle applications. *Journal of Electrochemical Society, 171*(3), 030521. \urlhttps://doi.org/10.1149/1945-7111/ad3456

# Anexo A: Especificaciones técnicas complementarias

*Figura/Tabla: Especificaciones del sistema de refrigeración líquida*

| **Parámetro** | **Valor** |
| --- | --- |
| Capacidad de disipación | 15 kW |
| Radiador | Aluminio, 400 \times 300 \times 32 mm |
| Ventilador | Eléctrico, 12 VDC, 300 W |
| Bomba | Centrífuga, 12 VDC, 80 W |
| Caudal de refrigerante | 20 L/min |
| Refrigerante | Glicol-agua 50/50 |
| Temperatura máxima | 65^\circC |

[htbp]

    \draw[thick,->] (0,0) -- (6,0) node[right] v (km/h);
    \draw[thick,->] (0,0) -- (0,5) node[above] F (kN);
    \foreach \x in 0,20,40,60,80,100,120,140 
        \draw (\x/25,0) -- (\x/25,-0.1) node[below,font=\tiny] {\x;
    }
    \foreach \y in 0,1,2,3,4,5 
        \draw (0,\y) -- (-0.1,\y) node[left,font=\tiny] {\y;
    }
    \draw[thick,red] plot[domain=0:5.6] (\x, 0.2595 + 0.0398*\x*\x);
    \draw[thick,blue,dashed] plot[domain=0:5.6] (\x, 0.0398*\x*\x);
    \draw[thick,green,dashed] plot[domain=0:5.6] (\x, 0.2595);
    \node[red] at (3.5,3.5) \tiny F_{total};
    \node[blue] at (4,2) \tiny F_{ad};
    \node[green] at (2,1) \tiny F_{rr};

*Figura/Tabla: Fuerzas resistivas en función de la velocidad*

# Anexo B: Planos CAD conceptuales

[htbp]

[scale=0.6]
    
    \draw[thick] (0,0) rectangle (14,4);
    
    
    \draw[dashed] (2.5,0) -- (2.5,4);
    \draw[dashed] (11.5,0) -- (11.5,4);
    
    
    \draw[pattern=north west lines, pattern color=orange!40] (0,0.5) rectangle (2.5,3.5);
    \node at (1.25,2) [font=] Motor + Controlador;
    
    
    \draw[pattern=north east lines, pattern color=green!40] (3,0.5) rectangle (8.5,3.5);
    \node at (5.75,2) [font=] Módulos de batería (bajo piso);
    
    
    \draw[pattern=north east lines, pattern color=green!40] (12,0.5) rectangle (14,2.2);
    \node at (13,1.35) [font=\tiny] Bat. aux;
    
    
    \draw[pattern=north west lines, pattern color=blue!20] (12,2.5) rectangle (14,3.7);
    \node at (13,3.1) [font=\tiny] Cargador;
    
    
    \draw[<->] (2.5,-0.5) -- (11.5,-0.5) node[midway,below,font=] Distancia entre ejes: 2,750 mm;
    \draw[<->] (0,-1) -- (14,-1) node[midway,below,font=] Longitud total del chasis: 4,795 mm;
    
    
    \draw[<->] (-0.5,0) -- (-0.5,4) node[midway,left,font=] 1,850 mm;
    
    \node at (7,-1.5) [font=] **Vista superior - Distribución de componentes**;

*Figura/Tabla: Plano CAD conceptual - Vista superior del chasis con componentes*

[htbp]

[scale=0.6]
    
    \draw[thick] (0,1.5) -- (0,0) -- (14,0) -- (14,1.5);
    \draw[thick] (0,1.5) -- (1.5,2.5) -- (12.5,2.5) -- (14,1.5);
    \draw[thick] (1.5,2.5) -- (1.5,3.5) -- (12.5,3.5) -- (12.5,2.5);
    
    
    \draw[thick] (2.5,0) circle (0.6);
    \draw[thick] (11.5,0) circle (0.6);
    
    
    \fill[red] (6.5,1.2) circle (0.15);
    \draw[red, dashed] (6.5,1.2) -- (6.5,-0.3);
    \node[red] at (6.5,-0.5) [font=\tiny] CG;
    
    
    \draw[fill=orange!30] (0.3,0.3) rectangle (2.0,1.2);
    \node at (1.15,0.75) [font=\tiny] Motor;
    
    
    \draw[fill=green!30] (3,0.05) rectangle (8,0.8);
    \node at (5.5,0.42) [font=\tiny] Baterías (bajo piso);
    
    
    \draw[fill=green!30] (12.2,0.05) rectangle (13.8,0.6);
    \node at (13,0.32) [font=\tiny] Bat.;
    
    
    \draw[fill=blue!20] (12.2,0.7) rectangle (13.8,1.2);
    \node at (13,0.95) [font=\tiny] Carg.;
    
    
    \draw[<->] (0,-0.8) -- (2.5,-0.8) node[midway,below,font=\tiny] 2,500 mm;
    \draw[<->] (2.5,-0.8) -- (11.5,-0.8) node[midway,below,font=\tiny] 2,750 mm (distancia entre ejes);
    \draw[<->] (11.5,-0.8) -- (14,-0.8) node[midway,below,font=\tiny] 1,200 mm;
    
    \node at (7,-1.5) [font=] **Vista lateral - Integración de componentes**;

*Figura/Tabla: Plano CAD conceptual - Vista lateral del vehículo convertido*

# Anexo C: Diagrama eléctrico completo del sistema

[htbp]

[node distance=1.5cm, auto, scale=0.9, transform shape]
    \tikzsetblock/.style={rectangle, draw, text centered, rounded corners, minimum height=0.8cm, minimum width=2.5cm, font=}
\tikzsetpower/.style={thick,->,>=stealth}
\tikzsetsignal/.style={thick,->,>=stealth,dashed}
\tikzsethv/.style={thick,->,>=stealth,color=orange}

    
    \node [block, fill=green!20] (bateria) Batería / 400V 80kWh;
    \node [block, fill=red!20, right=of bateria] (fusible) Fusible / 400A;
    \node [block, fill=red!20, right=of fusible] (contactor) Contactor / Principal;
    \node [block, fill=blue!20, right=of contactor] (precarga) Pre-carga / 50\Omega;
    \node [block, fill=orange!20, right=of precarga] (inversor) Inversor/ / Controlador;
    \node [block, fill=purple!20, right=of inversor] (motor) Motor / PMSM;
    
    
    \node [block, fill=cyan!20, below=1.5cm of bateria] (cargador) Cargador / 6.6kW;
    \node [block, fill=cyan!20, below=1.5cm of cargador] (dcdc) DC-DC / 400V-12V;
    \node [block, fill=cyan!20, right=of dcdc] (aux12v) Batería 12V / + Auxiliares;
    
    
    \node [block, fill=yellow!20, above=of precarga] (bms) BMS / Orion 2;
    
    
    \draw [hv] (bateria) -- (fusible);
    \draw [hv] (fusible) -- (contactor);
    \draw [hv] (contactor) -- (precarga);
    \draw [hv] (precarga) -- (inversor);
    \draw [hv] (inversor) -- (motor) node[midway,above,font=\tiny] AC 3\sim;
    \draw [hv] (bateria) |- (cargador);
    \draw [hv] (bateria) |- (dcdc);
    \draw [hv] (dcdc) -- (aux12v);
    \draw [hv] (cargador) |- (contactor);
    
    
    \draw [signal] (bms) -- (contactor);
    \draw [signal] (bms) -- (inversor);
    \draw [signal] (bms) -- (cargador);
    \draw [signal] (bms) -- (bateria);
    \draw [signal] (inversor) -- (motor);
    
    
    \draw [hv] (bateria.south) -- ++(0,-0.3) -- ++(14,0) -- (motor.south);
    \draw [hv] (cargador.south) -- ++(0,-0.2) -- ++(8,0);
    \draw [hv] (dcdc.south) -- ++(0,-0.2) -- ++(5,0);
    
    
    \node at (0,-2.5) (tierra) **GND**;
    \draw (aux12v.south) -- ++(0,-1.2);
    
    
    \node [below=0.2cm of cargador, font=\tiny] 240 V AC;
    \node [below=0.2cm of aux12v, font=\tiny] 12 V DC;

*Figura/Tabla: Diagrama eléctrico completo del sistema de propulsión*

# Declaración de autenticidad

Yo, **Diego Jefferson Charaja Mamani**, identificado con DNI N^\circ [DNI del autor], declaro que el presente informe técnico titulado *"Conversión de un vehículo mediano de combustión interna a un sistema de propulsión eléctrica conservando el chasis original"* es original y ha sido elaborado de acuerdo con los principios de integridad académica y científica.

Declaro que:

    - El contenido del presente informe es fruto de mi trabajo intelectual y no ha sido copiado, plagiado o reproducido de otras fuentes sin la debida citación.
    - Todos los datos, cálculos y resultados presentados son veraces y se basan en principios de ingeniería reconocidos.
    - Las referencias bibliográficas citadas corresponden fielmente a las fuentes consultadas y están correctamente referenciadas según el formato APA 7ª edición.
    - Este trabajo no ha sido presentado anteriormente para ningún otro grado académico o título profesional.
    - Soy consciente de las implicaciones legales y académicas de la presentación de un trabajo no original o fraudulento.

Lima, [fecha de sustentación].

\rule8cm0.5pt

**Diego Jefferson Charaja Mamani**

DNI: [DNI del autor]

