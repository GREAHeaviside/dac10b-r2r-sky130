# DAC R-2R: Simulador Analítico

Este directorio contiene un entorno de simulación analítica desarrollado en Python, destinado a estudiar el comportamiento teórico y estadístico de un conversor Digital-Analógico (DAC) con arquitectura R-2R. 

El código ha sido desarrollado como parte de las herramientas de estudio y validación teórica para la Práctica Profesional Supervisada (PPS) de Ingeniería Electrónica, de UTN FRLR.

A diferencia de las extracciones post-layout, este entorno no evalúa el circuito físico, sino que actúa como un marco de experimentación matemática para predecir cómo las variaciones de diseño afectan el rendimiento del conversor.

## Objetivos del Entorno

1. **Simulación Estocástica de Mismatch:** Introducir tolerancias y variaciones estadísticas en la red de resistencias (R y 2R) para observar la degradación de la curva de transferencia ideal.
2. **Evaluación de Métricas:** Calcular matemáticamente el impacto de estas variaciones en las métricas estáticas (DNL, INL) y dinámicas (ENOB).
3. **Análisis Paramétrico y Trade-offs:** Generar curvas de tendencia para evaluar los límites de la arquitectura, tales como:
   * Resolución vs. DNL/INL Máximo.
   * Resolución vs. ENOB.
   * Análisis de yield frente a las especificaciones buscadas (INL/DNL).

## Estructura de Scripts

El entorno está modularizado en diferentes scripts según el fenómeno a analizar:

* `dac_simulator.py`: Motor principal para la generación de la matriz de transferencia y cálculo de las tensiones de salida.
* `mismatch_simulation.py`: Inyección de tolerancias aleatorias (distribución normal siguiendo la ley de Pelgrom) en los componentes de la red.
* `dac_transfer_graphs.py` / `dnl_inl_graphs.py`: Herramientas de visualización de la curva de transferencia y diagramas de barras discretos para la no-linealidad.
* `bits_vs_nl.py`: Análisis de barrido paramétrico para observar cómo empeora el DNL e INL máximo al aumentar la cantidad de bits.
* `enob_vs_bits.py` / `enob_test.py`: Scripts dedicados al análisis de degradación de la resolución efectiva (ENOB) bajo condiciones de error estático.
* `yield_dnl_inl.py`: Simulación de Monte Carlo para estimar el porcentaje de chips viables dado un requerimiento estricto de DNL/INL.

## Requisitos e Instalación

Para ejecutar las simulaciones y generar los gráficos, se requiere un entorno de Python 3 con las siguientes dependencias:

```bash
pip install numpy matplotlib scipy