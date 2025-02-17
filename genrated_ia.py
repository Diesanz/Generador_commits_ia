import google.generativeai as genai
import argparse
import json
   
def configurar_api():
    """Configura la API de Gemini utilizando una clave API segura."""
    # Obtener la clave API desde una variable de entorno
    api_key = ""
    
    if not api_key:
        raise ValueError("La clave API no está definida. Asegúrate de configurar GEMINI_API_KEY como variable de entorno.")
    
    # Configurar la API de Gemini
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(model_name='gemini-1.5-flash')

def obtener_respuesta(model, pregunta, modo):
    """Genera una respuesta a partir del modelo generativo de Gemini."""
    prompt = f"{pregunta}\n"

    # Generar la respuesta usando Gemini
    try:
        response = model.generate_content(prompt)
        _message = response.text.strip()  # Asegúrate de limpiar cualquier espacio en blanco

        # Confirmar los cambios con el mensaje generado
        if not _message:  # Asegúrate de que el mensaje no esté vacío
            print("El mensaje generado está vacío.")
            return
        
        if modo == 'text':
            print(_message)
        elif modo == 'json':
            salida = {
                "respuesta": _message
            }
            # Convertir a JSON con formato
            json_salida = json.dumps(salida, ensure_ascii=False, indent=2)
            print(json_salida)
        else:
            print("Modo de respuesta no válido. Use 'text' o 'json'.")

    except Exception as e:
        print(f"Error al generar el mensaje: {str(e)}")

def main():
    """Punto de entrada principal del script."""
    # Configurar argparse
    parser = argparse.ArgumentParser(description='Genera una respuesta a una pregunta utilizando Gemini.')
    parser.add_argument('pregunta', type=str, help='La pregunta que deseas hacer.')
    parser.add_argument('--modo', choices=['text', 'json'] , default='text', help='Modo de respuesta (opcional).')

    args = parser.parse_args()

    # Ahora puedes acceder a los argumentos:
    pregunta = args.pregunta
    modo = args.modo

    print(f'Pregunta: {pregunta}')
    print(f'Modo: {modo}')

    # Configurar y usar el modelo
    model = configurar_api()

    obtener_respuesta(model, pregunta, modo)

if __name__ == "__main__":
    main()

