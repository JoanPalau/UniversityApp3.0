# UniversityApp1.0

UniversityApp és una aplicació web que permet consultar informació sobre diverses universitats, els seus graus i les seves assignatures, el qual pot ajudar a futurs alumnes a elegir una universitat.   

Cal destacar que en aquesta primera entrega, el lloc web és 1.0, és a dir, els usuaris no produiran contingut a la web, sinó que solament visitaran el contingut introduït pels administradors.

El codi font en producció d'aquest projecte està disponible en el següent enllaç:

[https://github.com/ntorrent/UniversityApp1.0](https://github.com/ntorrent/UniversityApp1.0)

Podeu trobar l'aplicació en funcionament a:

[Web desplegada](https://univoting.herokuapp.com/)

Com executar l'aplicació (entorn desenvolupament)
=================================================

1. Des del directori arrel del projecte executar per tenir el software que necessita l' aplicació:
```bash
$ pip3 install -r requirements.txt
```
**En cas de voler executar l'aplicació sense dades**

2. Fer les migracions
```bash
$ python3 manage.py makemigrations

$ python3 manage.py migrate
```

**En cas de voler executar l'aplicació amb dades de prova**

2. La segúent comanda s'encarrega de borrar les dades actuals, generar-ne de noves, fer les migracions i crear un superusuari amb nom **admin** i contrasenya **password**
```bash
$ bash tools/generate_db.sh
```

3 Executar el servidor
```bash
$ python manage.py runserver
```



Modificacions respecte el model de dades entregat al *preassignment*
====================================================================

En aquesta entrega s’ha modificat lleugerament el model de dades presentat en el *preassignment*:

En primer lloc, en comptes de dir que un grau pertany a una facultat es considera, de manera més genèrica, que un grau pertany a una universitat. Per tant, en comptes d’aparèixer la classe School apareix la classe University. D’aquesta classe University, se n’ha extret els atributs latitude i longitude, que representen la locatització de la universitat, i s’ha creat una classe específica Location, on a part d’aquests dos atributs latitude i longitude s’afegeixen atributs que representen l’adreça de manera textual. L’adreça textual s’introdueix al model, ja que serà la que es presentarà a l'usuari, en canvi la latitud i la longitud serviran sobretot per representar la localització en un mapa (el qual es preveu fer en la següent entrega, en la versió 2.0).

En segon lloc, s’ha eliminat la classe Teacher i les classes que depenien de Teacher (TeacherComment i TeacherQualification), ja que afegia una complexitat innecessària en el model de dades, i se segueix satisfent l’objectiu de l’aplicació i els requisits del projecte.


Model de Dades
==============
![Data Model](/docs/Act1-WP.png)

Tal com es veu en el diagrama, el model de dades està format principalment per les entitats University, Degree i Subject. Una universitat pot tenir un o multiples graus, i un grau pot tenir una o múltiples assignatures.

- Universitats

Representades per la entitat **University**. D'una universitat cal el seu nom, telèfon de contacte i localització. A les locatitzacions se la representa amb l'entitat **Location**, i està formada per els atributs address, areacode, city, i country que formen l'adreça textual, i la latitud i la longitud. Latitud i longitud caldran en la versió 2.0 en la qual es podrà mostrat en un mapa on es troba la universitat.

- Graus

Representats per l'entitat **Degree**. Estàn formats pel nom del grau, el total de crèdits ects que s'han de superar en tot el grau i una breu descripció d'en què consisteix el grau.

- Assignatures

Representades per l'entitat **Subject**.

És només l'entitat Subject la que té comentaris i una qualificació global (els quals es representen com a Comment i SubjectQualification en el model). Per tant, es permetrà que cada assignatura tingui un o més comentaris i la seva qualificació global. Els comentaris estan representats per l'entitat **Comment**, i poden tenir una llargada màxima de 250 caràcters. Les qualificacions globals estan representades per l'entitat **SubjectQualification**, i estan formades per una nota numèrica (atribut mark), la dificultat (atribut difficulty), el volum de treball (atribut workVolume), i un comptador que denota el nombre de qualificacions que hi ha hagut (atribut amount, recordar que l'entitat representa la mitjana de totes les qualificacions). Cal destacar que el volum de treball només pot tenir un valor dels tres possibles (Low, Medium, High) representats per l'enum EVolume.

Les assignatures pertanyen a un curs de cada grau, el qual es representa en l'entitat **Course**. Els cursos poden estar només entre 1r i 5è (es considera que cap grau té més de 5 cursos).


Deployment a Heroku (entorn producció)
======================================

Per tal de fer el deploy a Heroku s'ha especificat en el fitxer [Procfile](./Procfile) el tipus de servidor que ha d'executar django.

A més a més s'ha emprat una aplicació externa, django_heroku que s'encarrega d'obtenir la informació descrita a heroku i als settings de l'aplicació per realitzar el deploy més fàcilment.

Per tal de poder tenir els entorns de producció i desenvolupament separats, s'ha fixat a heroku la variable d'entorn DJANGO_SETTINGS_MODULE per executar el fitxer [settings_heroku.py](./University/settings_heroku.py)

Un cop realitzat el deploy a l'aplicació cal executar la comanda següent per generar una bbdd pseudoaleatòria d'exemple a partir de les dades en els fitxers .data i un superusuari amb nom **admin** i contrasenya **password** per tal de poder accedir al panell d'administració de l'aplicació.
```bash
$ heroku run bash tools/generate_db.sh
```

Deployment amb Docker (entorn producció)
========================================

Per tal de fer un deploy amb Docker s'ha creat un fitxer [Dockerfile](./Dockerfile) i un fitxer [docker-compose-yml](./docker-compose.yml)

La conjunció d'aquest dos fitxers crea un contenidor pel servidor de django i un altre contenidor pel servidor de la BBDD postgres.

A més a més, en el contenidor de django s'ha fixat la variable DJANGO_MODULE_SETTINGS per a executar el fitxer de settings [settings_docker.py](./University/seetings_docker.py) i així tenir els entorns de producció i desenvolupament separats.

Altres dades que ara mateix es troben en el fitxer de settings haurien de ser també incloses en variables d'entorn si es tractés d'una aplicació real.

### Com fer el deploy amb docker

Des del directori arrel del projecte (/UniversityApp1.0), creem els contenidors

```bash
$ docker compose up -d
```

Podem observar com s'han creat correctament i estan executant-se, per un costat tindrem el nom contenidor web i el nom contenidor bbdd

```bash
docker ps
```

Per tal de generar les dades de la bbdd, com en un entorn real no ho faríem directament a la construcció del docker, cal executar un script en bash que ens generarà la bbdd amb les dades de prova pseudoaleatòries dels .data i genera un superusuari de nom **admin** amb contrasenya **password**:

Aquest procés triga una estona, entre 30s i 1 min 30 s en els ordinadors on s'ha provat.

```bash
docker exec -d <nom contenidor web> bash tools/generate_db.sh
```

Un cop generada la bbdd, ja podem anar al localhost, port 8000 i ja ens trobarem a la pàgina web
