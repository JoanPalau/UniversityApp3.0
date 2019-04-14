# UniversityApp1.0

UniversityApp és una aplicació web que permet consultar informació sobre diverses universitats, els seus graus i les seves assignatures, el qual pot ajudar a futurs alumnes a elegir una universitat.   

Cal destacar que en aquesta primera entrega, el lloc web és 1.0, és a dir, els usuaris no produiran contingut a la web, sinó que solament visitaran el contingut introduït pels administradors.

El codi font d'aquest projecte està disponible en el següent enllaç:
[https://github.com/ntorrent/UniversityApp1.0](https://github.com/ntorrent/UniversityApp1.0)

[![Deployment Status](https://...)](https://....)

Com executar l'aplicació
========================

Modificar !!!

Des del directori arrel del projecte executar:
```bash
$ pip3 install -r requirements.txt
```
Fer les migracions
```bash
$ python3 manage.py makemigrations

$ python3 manage.py migrate
```
Executar el servidor
```bash
$ python manage.py runserver
```

Model de Dades
==============
![Data Model](/docs/UML.png)

Tal com es veu en el diagrama, el model de dades està format principalment per les entitats University, Degree i Subject. Una universitat pot tenir un o multiples graus, i un grau pot tenir una o múltiples assignatures.

- Universitats
Representades per la entitat **University**. D'una universitat cal el seu nom, telèfon de contacte i localització. A les locatitzacions se la representa amb l'entitat **Location**, i està formada per els atributs address, areacode, city, i country que formen l'adreça textual, i la latitud i la longitud. Latitud i longitud caldran en la versió 2.0 en la qual es podrà mostrat en un mapa on es troba la universitat.

- Graus
Representats per l'entitat **Degree**. Estàn formats pel nom del grau, el total de crèdits ects que s'han de superar en tot el grau i una breu descripció d'en què consisteix el grau.

- Assignatures

Representades per l'entitat **Subject**.

És només l'entitat Subject la que té comentaris i una qualificació global (els quals es representen com a Comment i SubjectQualification en el model). Per tant, es permetrà que cada assignatura tingui un o més comentaris i la seva qualificació global. Els comentaris estan representats per l'entitat **Comment**, i poden tenir una llargada màxima de 250 caràcters. Les qualificacions globals estan representades per l'entitat **SubjectQualification**, i estan formades per una nota numèrica entre 0 i 10, la dificultat, el volum de treball, i un comptador que denota el nombre de qualificacions que hi ha hagut (recordar que l'entitat representa la mitjana de totes les qualificacions). Cal destacar que la dificultat (atribut difficulty) i el volum de treball (atribut workVolume) només poden tenir un valor dels tres possibles (Low, Medium, High) representats per l'enum EVolume.

Les assignatures pertanyen a un curs de cada grau, el qual es representa en l'entitat **Course**. Els cursos poden estar només entre 1r i 5è (es considera que cap grau té més de 5 cursos).

Modificacions respecte el model de dades entregat al *preassignment*
====================================================================

En aquesta entrega s’ha modificat lleugerament el model de dades presentat en el *preassignment*:

En primer lloc, en comptes de dir que un grau pertany a una facultat es considera, de manera més genèrica, que un grau pertany a una universitat. Per tant, en comptes d’aparèixer la classe School apareix la classe University. D’aquesta classe University, se n’ha extret els atributs latitude i longitude, que representen la locatització de la universitat, i s’ha creat una classe específica Location, on a part d’aquests dos atributs latitude i longitude s’afegeixen atributs que representen l’adreça de manera textual. L’adreça textual s’introdueix al model, ja que serà la que es presentarà a l'usuari, en canvi la latitud i la longitud serviran sobretot per representar la localització en un mapa (el qual es preveu fer en la següent entrega, en la versió 2.0).

En segon lloc, s’ha eliminat la classe Teacher i les classes que depenien de Teacher (TeacherComment i TeacherQualification), ja que afegia una complexitat innecessària en el model de dades, i se segueix satisfent l’objectiu de l’aplicació i els requisits del projecte.

Deployment
================
