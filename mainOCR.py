import os
import pytesseract
from PIL import Image

# Configuration : définir le chemin vers l'exécutable Tesseract si nécessaire
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


def lire_cartes_repertoire(repertoire):
    """
    Parcourt toutes les images dans le répertoire donné et extrait le texte.

    :param repertoire: Chemin du répertoire contenant les images des cartes d'identité
    :return: Dictionnaire contenant les noms des fichiers et leur texte extrait
    """
    resultats = {}
    
    # Vérifier si le répertoire existe
    if not os.path.isdir(repertoire):
        print(f"Le répertoire {repertoire} n'existe pas.")
        return resultats

    # Parcourir les fichiers dans le répertoire
    for fichier in os.listdir(repertoire):
        chemin_complet = os.path.join(repertoire, fichier)

        # Vérifier si le fichier est une image
        if os.path.isfile(chemin_complet) and fichier.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            try:
                # Ouvrir l'image et extraire le texte
                with Image.open(chemin_complet) as img:
                    texte = pytesseract.image_to_string(img, lang='fra')  # 'fra' pour français
                    # texte = pytesseract.image_to_string(img, lang='fra')  # 'fra' pour français
                    resultats[fichier] = texte

            except Exception as e:
                print(f"Erreur lors de la lecture de {fichier} : {e}")

    return resultats

def afficher_resultats(resultats):
    """
    Affiche les textes extraits des fichiers.

    :param resultats: Dictionnaire contenant les noms des fichiers et leur texte extrait
    """
    for fichier, texte in resultats.items():
        print(f"\n--- Contenu extrait de {fichier} ---")
        print(texte)

if __name__ == "__main__":
    # Chemin vers le répertoire contenant les images des cartes
    repertoire_cartes = "cartes/fr"

    # Extraire les textes des cartes
    resultats_extraits = lire_cartes_repertoire(repertoire_cartes)

    # Afficher les résultats
    afficher_resultats(resultats_extraits)
