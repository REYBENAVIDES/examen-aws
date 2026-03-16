# Examen Práctico: Programación en la Nube ☁️

**Estudiante:** Edwin Rey  
**Institución:** UTEQ  
**Repositorio:** [https://github.com/REYBENAVIDES/examen-aws.git](https://github.com/REYBENAVIDES/examen-aws.git)

## 📄 Frontend
La lógica del frontend se encuentra en el archivo [index.html](https://github.com/REYBENAVIDES/examen-aws/blob/main/index.html).

## 📄 Documentación Oficial
Puedes revisar el informe detallado del proceso aquí:
**[Descargar PDF de Documentación](https://github.com/user-attachments/files/26039042/exaamenNube.pdf)**

## 📝 Descripción del Proyecto
Este proyecto consiste en el desarrollo e integración de una arquitectura en la nube utilizando AWS. El objetivo principal es clasificar imágenes mediante Inteligencia Artificial y persistir los resultados en una base de datos a través de una API REST.

---

## 🛠️ Tecnologías y Servicios
* **Backend:** Django & Django REST Framework (Desplegado en Elastic Beanstalk).
* **IA:** Amazon Rekognition (Servicio de etiquetado de imágenes).
* **Serverless:** AWS Lambda (Procesamiento lógico y conexión).
* **API Gateway:** HTTP API (Punto de enlace para el Frontend).
* **Frontend:** HTML5, JavaScript (Fetch API) y Bootstrap.

---

## 📂 Proceso de Desarrollo

### 1. Backend (Django)
* **Configuración:** Se habilitó `django-cors-headers` para permitir peticiones externas.
* **Modelo de Datos:** Se implementó el modelo `Imagen` con campos para `nombre`, `tipo_detectado`, `descripcion` y el archivo físico.
* **Despliegue:** Implementado en AWS Elastic Beanstalk (Python 3.12).

### 2. Procesamiento (AWS Lambda & Rekognition)
* **Función:** Se creó la función `clasificador-imagenes-examen` para recibir imágenes en Base64.
* **IA:** Uso de `boto3` para conectar con Amazon Rekognition y obtener etiquetas de la imagen.
* **Clasificación:** Lógica para categorizar imágenes como Documentos, Facturas, Personas o Animales.
* **Persistencia:** La función realiza un POST automático hacia la API de Django tras procesar la imagen.

### 3. Integración Final (API Gateway & Frontend)
* **Endpoint:** Configuración de una HTTP API con soporte completo de CORS.
* **Cliente Web:** Interfaz que permite al usuario cargar archivos, enviarlos a la nube y recibir la confirmación de guardado exitoso (Status 201).
* **Codigo:** El codigo se encuentra en el archivo index.html

---

## ✅ Conclusión
La arquitectura implementada demuestra una integración fluida entre servicios administrados (Elastic Beanstalk), servicios serverless (Lambda) y servicios de inteligencia artificial (Rekognition), cumpliendo con los requisitos de escalabilidad y desacoplamiento de componentes.

---
**UTEQ - 2026**
