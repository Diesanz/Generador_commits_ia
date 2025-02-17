import git
import google.generativeai as genai
import argparse
import os

def configurar_api():
    """Configura la API de Gemini utilizando una clave API segura."""
    # Obtener la clave API desde una variable de entorno
    api_key = ""
    
    if not api_key:
        raise ValueError("La clave API no está definida. Asegúrate de configurar GEMINI_API_KEY como variable de entorno.")
    
    # Configurar la API de Gemini
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(model_name='gemini-1.5-flash')

def obtener_respuesta(model, pregunta):
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
        
        return _message

    except Exception as e:
        print(f"Error al generar el mensaje: {str(e)}")

def make_commit(repo, _message):
    """Realiza un commit con el mensaje de commit generado."""
    try:
        repo.git.add(A=True)  # Añade los archivos modificados al índice
        repo.index.commit(_message)  # Realiza el commit con el mensaje de commit generado
        print("Commit realizado exitosamente.")
    except Exception as e:
        print(f"Error al realizar el commit: {str(e)}")

def main():
    #obtener el directorio del script
    parser = argparse.ArgumentParser(description='Rutas del current directory')
    parser.add_argument('ruta', type=str, help='Ruta')
    
    args = parser.parse_args()

    repo = git.Repo(args.ruta)  # Define el repositorio

    diff = repo.git.diff()  # Obtiene la diferencia

    if diff:
        pregunta = f"¿Qué resumen conciso darías para describir los cambios realizados en este {diff}, enfocándote en qué se modificó y el propósito de esos cambios y las líneas afectadas? Solo dame la respuesta, es decir, no añadas más comentarios tuyos que no estén relacionados con el commit y siempre dime los archivos modificados."
    
        # Configurar y usar el modelo
        model = configurar_api()

        _message = obtener_respuesta(model, pregunta)
    
        if _message:
            make_commit(repo, _message)
    else:
        print("No hay cambios")

if __name__ == "__main__":
    main()