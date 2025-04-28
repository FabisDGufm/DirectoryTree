import os
from tree import Tree, Node

opath = "C:/Users/fabio/OneDrive/Imágenes/Feedback"
carpetas = ""

root = Tree(os.path.basename(opath))
puntero = root

listaArchivos = os.listdir(opath)

def hijos(archivo):
    global carpetas
    global puntero

    if carpetas != "":
        npath = opath + "/" + carpetas + "/" + archivo
    else:
        npath = opath + "/" + archivo

    if os.path.isdir(npath):
        nlistaArchivos = os.listdir(npath)
        subcarpeta = Tree(archivo)
        puntero.insert_child(subcarpeta)
        
        original_puntero = puntero
        original_carpetas = carpetas

        puntero = subcarpeta
        if carpetas == "":
            carpetas = archivo
        else:
            carpetas = carpetas + "/" + archivo

        for subarchivo in nlistaArchivos:
            hijos(subarchivo)

        carpetas = original_carpetas
        puntero = original_puntero

    else:
        try:
            with open(npath, "r", encoding="utf-8") as f:
                contenido = f.readlines()
        except Exception as e:
            contenido = [f"[ERROR AL LEER ARCHIVO: {e}]"]
        
        archi = Node(archivo, contenido)
        puntero.insert_child(archi)

# ChatGPT. (2025, abril). Visual de un buscador de archivos en python. OpenAI. https://chat.openai.com/
# Promt: Chat, puedes hacerme un código en python donde, se usan nodos y trees, quiero que diferencies entre carpetas (trees) y archivos, que lo muestres como un buscador de archivos, donde se presentan en jerarquías
# Se modificó el código que se recibió
def print_tree(node, prefix=""):
    if isinstance(node, Tree):
        print(prefix + "📂 " + node.name)
        for child in node.get_children():
            print_tree(child, prefix + "    ")
    else:
        print(prefix + "📝 " + node.name)
        if node.content != "":
            print(prefix + "  ℹ️ " + " Se tiene guardado el contenido de este archivo")

  

def main():
    for archivo in listaArchivos:
            hijos(archivo)
    print_tree(root)
    
if __name__ == "__main__":
    main()