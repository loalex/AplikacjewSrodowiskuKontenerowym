Odpalic dockera i dockerhub na internecie
1. plik script + dockerfile
docker build -t my-python-app .
docker run -t my-python-app .            lub docker run my-python-app

jak nie działa: docker run -it my-python-app /bin/bash 
ls /app/code
python /app/code/script.py
2. najpierw sprawdzamy sobie docker ps -a



3.  docker ps -a (pokazuje kontenery przeszle tez, bo mamy plik, ktory sie wywoluje i konczy dzialanie)
docker cp data.txt numer kontenera:/app/data.txt    kopiuje plik do kontenera  

docker cp <container_id>:/app/data.txt ./retrieved_data.txt - kopiuje plik z powrotem do hosta

4. ENTRYPOINT pozwala ustawić domyślną komendę uruchamianą w kontenerze. Przykład już widziałeś w Dockerfile.
CMD określa domyślne argumenty dla ENTRYPOINT.
 
oba są w dockerfile

nowy projekt zad4

mamy script + dockerfile

polecenia: 
docker build -t combined-example .
docker run combined-example

nadpisanie CMD: docker run combined-example custom_arg1 custom_arg2

5. tworzymy pliczek docker-compose
w terminalu: docker-compose up -d
łączymy się z bazą danych w terminalu za pomocą:
docker exec -it zaliczenie-db-1 mysql -u user -p (bo nie mam sql na kompie)

6. ADD obsługuje pliki i archiwa:
w dockerfile)
ADD my_archive.tar.gz /app
COPY kopiuje pliki bez rozpakowywania:
w dockerfile)
COPY my_file.txt /app

jest osobny folder na to i tam dockerfile + archive + data + script

 docker build -t add-copy-workdir-example .

 docker run add-copy-workdir-example


7. do docker-compose dodalem:   app:
    build: .
    depends_on:
      - db
    ports:
      - "8000:8000"
i wywolanie: 
      - docker-compose up --build

8. Sprawdź szczegóły kontenera:

docker inspect <container_id>
Sprawdź logi kontenera:

docker logs <container_id>

9. Sieci w Dockerze są mechanizmem umożliwiającym kontenerom komunikowanie się ze sobą oraz z otoczeniem. Docker zapewnia różne typy sieci, które można wykorzystać w zależności od wymagań projektu. Główne typy sieci w Dockerze to:

Bridge – Domyślna sieć dla kontenerów, która pozwala na komunikację między nimi w ramach tego samego hosta.
Host – Używa sieci hosta, co oznacza, że kontener korzysta z adresu IP hosta.
None – Kontener nie ma dostępu do sieci.
Overlay – Umożliwia komunikację między kontenerami na różnych hostach, idealne dla Docker Swarm i Kubernetes.
Container – Pozwala kontenerowi na dzielenie sieci z innym kontenerem.

Domyślna sieć typu bridge umożliwia komunikację między kontenerami.

networks:
  app_net:
services:
  db:
    networks:
      - app_net
  app:
    networks:
      - app_net


2 pliczki w folderze 

docker-compose up -d

docker network ls

docker network zad9_my_network

docker logs mysql-db 

10.Obraz (Image):

Jest to niezmienna, "statyczna" warstwa zawierająca wszystkie niezbędne dane do uruchomienia aplikacji (kod aplikacji, zależności, system plików).
Obraz jest "szablonem" dla kontenerów. Można tworzyć wiele kontenerów z jednego obrazu.
Kontener (Container):

Jest to uruchomiona instancja obrazu. Kontener działa jako proces w izolowanym środowisku.
Kontener jest "dynamiczny" — aplikacja w nim działa, przetwarza dane i można wprowadzać zmiany (chociaż zmiany te nie zapisują się w obrazie).
Obraz to szablon. Możesz go zbudować:

docker build -t my-image .
Kontener to uruchomiona instancja obrazu:

docker run my-image

11. Wejdź do kontenera:
docker ps
docker exec -it <container_id> /bin/bash

echo "This is a persistent file." > \app\my-file.txt

Aby dane były dostępne po ponownym uruchomieniu kontenera, można zastosować wolumeny.

docker run -d --name my-container -v /path/to/host/directory:/app my-python-app

docker exec -it my-container /bin/bash

echo "This is a persistent file." > /app/my-file.txt

po wyjsciu:
cat /path/to/host/directory/my-file.txt
12. Dockerhub:

docker build -t my-python-app:1.0 .
budujemy i nadajemy tag

docker login
logujemy się

dodajemy obraz:
docker tag my-python-app:1.0 wowpek/my-python-app:1.0

docker push wowpek/my-python-app:1.0

usuwanie lokalnie:
docker rmi wowpek/my-python-app:1.0

docker ps  -sprawdzamy

docker pull wowpek/my-python-app:1.0

uruchamiamy obraz aby upewnic sie, ze dziala poprawnie: 
docker run --rm wowpek/my-python-app:1.0



docker tag my-python-app your_dockerhub_username/my-python-app:latest
Opublikuj:

docker push your_dockerhub_username/my-python-app:latest
Usuń lokalnie i pobierz:

docker rmi your_dockerhub_username/my-python-app:latest
docker pull your_dockerhub_username/my-python-app:latest
