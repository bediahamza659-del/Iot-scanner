# Analyseur de Sécurité IoT

Un programme Python avec interface web qui scanne un réseau et trouve les appareils connectés.

## Ce que ça fait
- Scanne le réseau local
- Trouve les appareils connectés
- Voir les ports ouverts
- Interface web pour utiliser le programme

## Comment installer

### Avant de commencer
- Avoir Python installé
- Installer Nmap (https://nmap.org/download.html)

### Étapes
1. Ouvrez le terminal
2. Allez dans votre dossier du projet:
```bash
cd votre-dossier
```

3. Installez tout:
```bash
pip install -r requirements.txt
```

## Comment utiliser

```bash
python app.py
```

Puis ouvrez votre navigateur et allez à:
```
http://localhost:5000
```

## Outils utilisés
- Python
- Flask
- Nmap
