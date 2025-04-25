Consultas de Tablas de Pérdidas de Transformadores
🚀 Aplicación desarrollada en Python usando Streamlit para consultar valores de pérdidas (sin carga, con carga y totales) de transformadores de distribución, interpolando los valores si la potencia solicitada no existe exactamente en las tablas normadas.

📄 Descripción del proyecto
Esta herramienta permite:

Seleccionar una norma técnica nacional o internacional.

Ingresar la potencia nominal del transformador.

Consultar los parámetros de pérdidas asociados.

Obtener los valores interpolados cuando la potencia solicitada no coincide con una potencia estándar.

Visualizar la tabla completa de referencia cargada.

Normas soportadas:

Norma INEN 2115 - 3F Aceite

Norma INEN 2114 - 1F Aceite

Norma NTC 3445 - 3F Seco

Norma RVR - 3F Petróleos

🛠️ Tecnologías usadas
Python 3.11+

Streamlit

Pandas

⚙️ Instalación local
Clona el repositorio:

bash
Copiar
Editar
git clone https://github.com/Jlbb89/Consultas_tablas_perdidas_trafos.git
cd Consultas_tablas_perdidas_trafos
Crea un entorno virtual (opcional pero recomendado):

bash
Copiar
Editar
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
Instala las dependencias:

bash
Copiar
Editar
pip install -r requirements.txt
Ejecuta la aplicación:

bash
Copiar
Editar
streamlit run app_streamlit.py
🌍 Publicación en la Web
Esta aplicación puede ser desplegada de manera gratuita usando Streamlit Cloud.

👨‍💻 Autor
Ing. Jose Luis Barreto B.
💼 Especialista en Transformadores y Análisis de Pérdidas
✉️ [Tu email aquí si quieres ponerlo]

📝 Licencia
Este proyecto está licenciado bajo los términos de la Licencia MIT.

📌 Notas adicionales
Los datos de pérdidas corresponden a documentos normativos oficiales.

El programa es adaptable para integrar más normas o ampliaciones futuras.

🚀 ¡Gracias por usar la aplicación!
