# Projet_13_OpenClassrooms
## Mettez à l'échelle une application Django en utilisant une architecture modulaire
Orange County Lettings est une start-up dans le secteur de la location de biens immobiliers. La start-up est en pleine phase d’expansion aux États-Unis. 

###Description du projet :



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
### Postman documentation

Suivre les  indications detaillé dans le site suivant:
https://documenter.getpostman.com/view/21036516/2s8YmRQ2nC
#### Cette commande sera obligatoire à chaque fois que vous voudrez travailler avec le cours. Dans le même terminal, tapez maintenant
```
pip install -r requirements.txt
```
###Vérifier la qualité du code :
Pour lancer la vérification de la qualité du code : 
```
flake8 --format=html --htmldir=flake-report --exclude=env --max-line-length=119
```
### Contributeurs
- Yacine Djabela
- Stephane Didier
