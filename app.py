from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def home():
    html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Aplicación Flask Moderna</title>
        <style>
            body {
                margin: 0;
                font-family: 'Roboto', sans-serif;
                background-color: #f4f7f6; /* Fondo gris claro */
                color: #333;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                min-height: 100vh;
                text-align: center;
            }
            .card {
                background-color: white;
                border-radius: 15px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15); /* Sombra elegante */
                padding: 40px;
                max-width: 400px;
                width: 90%;
            }
            h1 {
                font-size: 2.5em;
                color: #007bff; /* Color primario azul */
                margin-bottom: 10px;
            }
            .subtitle {
                color: #6c757d; /* Gris secundario */
                margin-bottom: 25px;
                font-size: 1.1em;
            }
            .cta-button {
                background: linear-gradient(45deg, #007bff, #00bfff); /* Gradiente azul/celeste */
                border: none;
                color: white;
                padding: 12px 25px;
                border-radius: 50px;
                font-size: 1em;
                font-weight: bold;
                cursor: pointer;
                transition: transform 0.3s, box-shadow 0.3s;
            }
            .cta-button:hover {
                transform: translateY(-3px);
                box-shadow: 0 5px 15px rgba(0, 123, 255, 0.4);
            }
            .footer {
                margin-top: 30px;
                font-size: 0.9em;
                color: #999;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 Proyecto Flask</h1>
            <p class="subtitle">¡El backend está funcionando perfectamente!</p>
            <p>Este es el resultado de usar Python con Flask para generar una interfaz de usuario limpia y moderna.</p>
            <button class="cta-button" onclick="alert('¡Hola desde el servidor! 🎉')">Ver Detalles</button>
        </div>
        <div class="footer">
            Desarrollado en la clase de Quinto A.
        </div>
    </body>
    </html>
    """
    return Response(html, mimetype='text/html')

if __name__ == '__main__':
    # Ejecuta el servidor Flask en el puerto 80
    app.run(host='0.0.0.0', port=80, debug=True)