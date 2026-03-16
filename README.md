# Examen Práctico: Programación en la Nube ☁️

[cite_start]**Estudiante:** Edwin Rey [cite: 1]  
[cite_start]**Repositorio:** [https://github.com/REYBENAVIDES/examen-aws.git](https://github.com/REYBENAVIDES/examen-aws.git) [cite: 2]  
[cite_start]**Proyecto:** Integración de Aplicación Web con AWS Lambda y Rekognition [cite: 4]

## 📝 Descripción
[cite_start]Desarrollo e integración de una aplicación desplegada en AWS para determinar el tipo de imagen cargada por el usuario mediante IA, almacenando automáticamente la descripción en una base de datos a través de una API backend[cite: 4, 5].

---

## 🚀 Parte 1: Backend con Django
[cite_start]Se implementó un backend robusto utilizando **Django Rest Framework**[cite: 6, 9]:

1. [cite_start]**Configuración Inicial**: Se instalaron dependencias clave como `django-cors-headers` y `pillow` para el manejo de imágenes[cite: 9].
2. [cite_start]**Modelo de Datos**: Se definió el modelo `Imagen` en la aplicación `catalogo` con los campos[cite: 35]:
   * [cite_start]`nombre`: CharField para el nombre del archivo[cite: 37].
   * [cite_start]`tipo_detectado`: CharField para la categoría de la IA[cite: 39].
   * [cite_start]`descripcion`: TextField para las etiquetas detalladas[cite: 41].
   * [cite_start]`archivo`: ImageField para el almacenamiento físico[cite: 44].
3. [cite_start]**API REST**: Se crearon serializadores (`ImagenSerializer`) y vistas (`ImagenViewSet`) para exponer los endpoints de la aplicación[cite: 86, 104].
4. [cite_start]**Despliegue**: La aplicación se desplegó en **AWS Elastic Beanstalk** utilizando Python 3.12[cite: 193, 220].
   * [cite_start]**URL API:** `http://catalogo-examen-env.eba-kfq5p8y2.us-east-1.elasticbeanstalk.com/api/imagenes/` [cite: 224]

---

## 🧠 Parte 2: Función Lambda y Clasificación de Imágenes
[cite_start]Se configuró una función serverless para procesar la inteligencia artificial[cite: 243]:

1. [cite_start]**Configuración de AWS Lambda**: Creación de la función `clasificador-imagenes-examen`[cite: 245].
2. [cite_start]**Permisos IAM**: Se asignó la política `AmazonRekognitionFullAccess` para permitir el uso del modelo de etiquetado[cite: 279].
3. **Lógica de Clasificación**:
   * [cite_start]Recepción de imagen en formato Base64[cite: 289].
   * [cite_start]Procesamiento con **Amazon Rekognition** (`detect_labels`)[cite: 289].
   * [cite_start]Clasificación lógica en categorías: *Documento, Factura, Foto de Persona, Foto de Animal* o *Imagen General*[cite: 289].
   * [cite_start]Envío automático de resultados al backend de Django mediante una petición POST[cite: 289].

---

## 🌐 Parte 3: Integración y Frontend
[cite_start]Para conectar al usuario final con la lógica de nube se realizaron los siguientes pasos[cite: 290]:

1. [cite_start]**API Gateway**: Se configuró una **HTTP API** para exponer la función Lambda, permitiendo peticiones desde el navegador mediante la configuración de **CORS**[cite: 291, 299].
2. **Interfaz Web (HTML/JS)**: 
   * [cite_start]Formulario para selección de archivos[cite: 315].
   * [cite_start]Conversión dinámica a Base64 y envío a la API Gateway[cite: 313].
   * [cite_start]Visualización de resultados en tiempo real, incluyendo el estado de confirmación de la base de datos (Status 201 Created)[cite: 321].

---

## ✅ Resultados
[cite_start]La aplicación logra clasificar exitosamente etiquetas como *Person, Face, Dimples, Smile* y asignar el tipo **Foto de Persona**, guardando la información con éxito en el backend desplegado[cite: 318, 321].

---
**UTEQ - 2026**
