# **OCR Carte IDentité – Système d’Extraction Automatique de Données**

**Un projet Python basé sur l'IA pour détecter, extraire et traiter les informations des cartes d'identités en utilisant YOLO et EasyOCR.**

## **Fonctionnalités Clés**

✩ **Détection des cartes d’identité** – Identifie et recadre automatiquement les cartes d'identité dans les images.  
✩ **Reconnaissance de texte (OCR)** – Utilise EasyOCR pour extraire les textes des champs comme :

- Nom complet
- Date de naissance
- Numéro de la carte
- Nationalité

✩ **Interface Web Interactive** – Une interface utilisateur conviviale avec Streamlit pour télécharger et traiter facilement les cartes d'identité.

## **Processus**

1. **Téléchargement d’image** – Chargez une image de carte d'identité via l'interface.
2. **Détection AI** – Le système localise les champs importants sur la carte.
3. **Extraction de données** – Les textes des champs sont extraits et structurés.
4. **Résultat** – Affiche les données structurées et les textes extraits.

![Processus Exemple](demo/demo1.png)
![Processus Exemple](demo/demo2.png)
![Processus Exemple](demo/demo3.png)

## **Guide d’Installation**

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/ThiernodioData/ProjetOCR.git
   ```
2. **Se rendre dans le dossier du projet** :
   ```bash
   cd interfaceOCR
   ```
3. **Créer un environnement virtuel** (recommandé) :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows : venv\Scripts\activate
   ```
4. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```
5. **Lancer l'application** :
   ```bash
   streamlit run app.py
   ```

## **Modèles Utilisés**

- **YOLOv8** – Pour la détection des zones d’intérêt (champs de la carte).
- **EasyOCR** – Pour la reconnaissance optique de caractères avec une haute précision.

## **Packages Principaux**

- `OpenCV` : Prétraitement des images.
- `YOLOv8` : Détection des zones d'intérêt.
- `EasyOCR` : Extraction de texte.
- `Streamlit` : Interface web.
- `Pandas`, `NumPy` : Traitement et manipulation des données.

## **Pourquoi ce Système ?**

✅ **Précision élevée** – Détection et reconnaissance des champs avec fiabilité.  
✅ **Rapide et automatisé** – Réduit le temps de traitement des documents.  
✅ **Accessible** – Une interface simple et intuitive pour tout utilisateur.  

## **Contributions**

Les contributions sont les bienvenues ! Forkez le dépôt et soumettez une pull request avec vos améliorations. Assurez-vous que votre code respecte les normes du projet et inclut des tests.

## **Contact & Support**

Pour toute question ou suggestion, ouvrez une issue ou contactez :

- **GitHub** : [Votre GitHub](https://github.com/ThiernodioData/)

---

**Remerciements**  
Ce projet utilise :
- [YOLO](https://github.com/ultralytics/yolov8) pour la détection d'objets.  
- [EasyOCR](https://github.com/JaidedAI/EasyOCR) pour la reconnaissance de texte.  
- [Streamlit](https://streamlit.io/) pour l’interface utilisateur.

---

**!Note**  
Pour réaliser ce projet, je me suis largement inspiré d’un dépôt existant : [https://github.com/NASO7Y/ocr_egyptian_ID.git](https://github.com/NASO7Y/ocr_egyptian_ID.git). Ce projet est à but éducatif et sert uniquement à l'apprentissage de concepts en intelligence artificielle.
