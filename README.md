# Analyseur de Sécurité IoT

Un scanner de réseau basé sur Python qui identifie les appareils connectés, les ports ouverts et les risques de sécurité sur les réseaux locaux.

## Fonctionnalités
- Scan du réseau local
- Détection des appareils connectés
- Identification des ports ouverts
- Analyse des risques de sécurité

## Technologies utilisées
- Python
- Nmap
- Socket

## Installation

### Prérequis
- Python 3.7+
- Nmap installé sur votre système

### Configuration
1. Clonez le repository:
```bash
git clone https://github.com/bediahamza659-del/Iot-scanner.git
cd Iot-scanner
```

2. Installez les dépendances:
```bash
pip install -r requirements.txt
```

3. Installez Nmap:
   - **Windows**: Téléchargez depuis https://nmap.org/download.html
   - **Linux**: `sudo apt-get install nmap`
   - **Mac**: `brew install nmap`

## Utilisation
```bash
python main.py
```

## Dépendances
Voir `requirements.txt` pour les dépendances du projet.

## Remarques
- Nmap doit être installé sur votre système pour que le projet fonctionne
- Assurez-vous d'avoir la permission avant de scanner des réseaux
