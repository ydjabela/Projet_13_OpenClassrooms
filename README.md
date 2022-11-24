# Projet_13_OpenClassrooms
## Mettez à l'échelle une application Django en utilisant une architecture modulaire
Orange County Lettings est une start-up dans le secteur de la location de biens immobiliers. La start-up est en pleine phase d’expansion aux États-Unis. 

###Description du projet :
- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).



### Récupérer le projet :

```
git clone https://github.com/ydjabela/Projet_13_Openclassrooms
```

### Création de l'environnement virtuel

Assurez-vous d'avoir installé python et de pouvoir y accéder via votre terminal, en ligne de commande.

Si ce n'est pas le cas : https://www.python.org/downloads/

```
python -m venv Projet_13
```

### Activation de l'environnement virtuel du projet

Windows :

```
Projet_13\Scripts\activate.bat
```

MacOS/Linux :
```
source Projet_12/bin/activate
```

### Installation des packages necessaire pour ce projet
```
pip install -r requirements.txt
```

### Fonctionnement:
Une fois activé, pour démarrer le serveur local, il faudra utiliser la commande :
```
python manage.py runserver 
```
#### Tests unitaires
```
python manage.py test home.tests
python manage.py test profiles.tests
python manage.py test letting.tests
```
#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`
#### Cette commande sera obligatoire à chaque fois que vous voudrez travailler avec le cours. Dans le même terminal, tapez maintenant
```
pip install -r requirements.txt
```
###Vérifier la qualité du code :
Pour lancer la vérification de la qualité du code : 
```
flake8 --format=html --exclude=env --max-line-length=119
```
### Contributeurs
- Yacine Djabela
- Stephane Didier


python -m venv Projet_13
Projet_13\Scripts\activate.bat
python manage.py runserver 
