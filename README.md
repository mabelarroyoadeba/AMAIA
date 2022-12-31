# AMAIA

Este repositorio incluye los Notebook correspondientes al Trabajo Fin de Master: **ChatBot empático basado en BERT, GPT-3 y aprendizaje por refuerzo.**

siendo:

**01 Preprocesado BD ED :** Desarrollo del preprocesado y limpieza de la base de datos EMPATHETICDIALOGUES que se utiliza como fuente de datos para el proyecto. Esta base de datos es un repositorio de más de 25k diálogos cortos en inglés enmarcados en situaciones emocionales.

**02 Modulo de recompensas :** Aquí se encuentra la codificación del módulo de recompensas del modelo de aprendizaje por refuerzo que se desarrolla en el proyecto. Se trata de un clasificador basado en BERT (un modelo de procesamiento natural preentrenado desarrollado por Google)

**03 Reentrenamiento GPT-3:** Para la implementación de la política del agente, se utiliza el modelo de OpenAI GPT-3. En este Notebook se realiza su reentrenamiento utilizando la base de datos preprocesada al principio.

**04 Entrenamiento chatbot:** Por último, una vez construido el modelo en los apartados anteriores, se procede a entrenar el agente mediante el algoritmo de gradientes de política REINFORCE.

En el directorio **Ficheros intermedios** se encuentran los ficheros .csv que se generaron durante el entrenamiento del chatbot: 

    **agentn.csv:** Contiene los turnos de conversación con los datos de recompensa, nivel de emoción etc. que se generan durante el entrenamiento episódico.

    **bettern.csv** Contiene las lineas que generan mejor nivel de emoción. Este fichero se utiliza para reentrenar el modelo GPT-3 en cada episodio.

    **trained_models.csv:** Este fichero contiene los nombres de los modelos que se crean en cada episodio de forma recursiva. Estos modelos intermedios se utilizan para realizar inferencias y ver la evolución de las respuestas.


