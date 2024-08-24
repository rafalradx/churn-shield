# Prognozowanie Rezygnacji Klientów dla Firmy Telekomunikacyjnej

# Predicting Customer Churn for a Telecommunications Company

## Wstęp / Introduction

Celem tego projektu jest opracowanie modelu predykcyjnego, który pozwoli przewidzieć prawdopodobieństwo rezygnacji klientów z usług telekomunikacyjnych na podstawie analizy historycznych danych. Projekt ten stanowi kompleksowe podejście do analizy danych i uczenia maszynowego, obejmujące każdy kluczowy etap – od wstępnej eksploracji danych, przez ich przetwarzanie, budowę i ocenę modelu, aż po wdrożenie go w formie aplikacji. Dzięki temu model będzie nie tylko skuteczny, ale także gotowy do praktycznego zastosowania, wspierając firmę w podejmowaniu proaktywnych działań na rzecz utrzymania klientów.

The goal of this project is to develop a predictive model that can forecast the likelihood of customers discontinuing telecommunication services based on the analysis of historical customer data. This project represents a comprehensive approach to data analysis and machine learning, encompassing every key stage—from initial data exploration, through data preprocessing, model development, and evaluation, to the deployment of the model in the form of an application. As a result, the model will not only be effective but also ready for practical application, helping the company take proactive measures to retain customers.

## Język / Language

- [Polski / Polish](#spis-treści)
- [Angielski / English](#table-of-contents)

## Spis treści

- [Wymagane zależności](#wymagane-zależności)
- [Instalacja](#instalacja)
- [Uruchomienie aplikacji](#uruchomienie-aplikacji)
- [Przykład użycia](#Przykład-użycia)
- [Licencja](#licencja)
- [Autorzy](#autorzy)
- [Kontakt](#kontakt)

## Wymagane zależności

Upewnij się, że na Twoim komputerze zainstalowany jest Python 3.11 lub nowszy.

Aplikacja korzysta z następujących bibliotek:

- `fastapi`
- `flet`
- `jinja2`
- `numpy`
- `pandas`
- `scikit-learn`
- `tensorflow`
- `uvicorn[standard]`
- `openai`

## Instalacja

### 1. Pobierz repozytorium:

```
git clone https://github.com/rafalradx/to-churn-or-not-to-churn
```

### 2. Przejdź do katalogu z aplikacją np.:

```
cd to-churn-or-not-to-churn
```

### 3. Instalacja zależności:

Dla aplikacji `FastAPI` zainstaluj zależności:

`pip install -r requirements.txt`

Dla aplikacji `flet` zainstaluj zależnoci:

`pip install -r requiremenst-flet.txt`

## Konfiguracja do pracy z API openAI

Aplikacja FastAPI może komunikować się z ChatGPT za pomocą API openAI, aby uzyskać rekomendacje. Aby skorzystać z tej funkcjonalności, zmień nazwę pliku `env` na `.env` i umieścić w nim klucz API openAI:

`OPENAI_API_KEY=your_super_secret_open_AI_api_key`

## Uruchomienie aplikacji:

### Uruchamianie aplikacji Flet

Aby uruchomić aplikację Flet, użyj następującego polecenia:

```
flet run interface.py
```

### Uruchamianie aplikacji FastAPI

Aby uruchomić aplikację FastAPI, użyj następującego polecenia:

```
uvicorn main:app --reload
```

### Uruchamianie notatnika Jupyter

Uruchom serwer notatnika Jupyter, aby uruchomić analizę:

```
jupyter-notebook noteboks/project.ipynb
```

### Uruchamianie aplikacji FastAPI jako kontenera Docker

Aplikację FastAPI można również uruchomić w kontenerze Docker. Aby to zrobić, najpierw zbuduj obraz Docker:

`docker build -t ml-churn-fastapi .`

To polecenie tworzy obraz Docker o nazwie `ml-churn-fastapi`, używając Ubuntu 24.04 jako bazowego systemu. Proces trwa około 10 minut, a wynikowy obraz ma około 3 GB.

Aby uruchomić aplikację w kontenerze, użyj następującego polecenia:

`docker run -d -p 8000:8000 ml-churn-fastapi`

Aplikacja będzie dostępna w przeglądarce pod adresem:

`localhost:8000`

## Przykład użycia

### Przykład użycia aplikacji FastAPI

Predykcja modelu:

![Screenshot from 2024-08-24 19-09-11](https://github.com/user-attachments/assets/705cfe33-bd3f-410f-b679-1908144698dc)

Rekomendacja GPT:

![Screenshot from 2024-08-24 19-11-00](https://github.com/user-attachments/assets/5a75a2d9-8ef8-4c49-9ce8-02e5e7fc7abb)


## Licencja

Ta aplikacja jest udostępniana na licencji MIT.

## Autorzy

- 'Alex Kruh'
- 'Beata Chrząszcz'
- 'Dawid Radzimski'
- 'Kamil Grundas'
- 'Katarzyna Czempiel'
- 'Katarzyna Drajok'
- 'Paweł Sakowicz'
- 'Rafał Pietras'
- 'Sabina Limmer'

## Kontakt

Jeśli masz pytania, sugestie lub chciałbyś się skontaktować w sprawie aplikacji, skontaktuj się z nami:

- GitHub Alex Kruh: [OlekKruh](https://github.com/OlekKruh)
- GitHub Beata Chrząszcz: [BettyBeetle](https://github.com/BettyBeetle)
- GitHub Dawid Radzimski: [DawidRadzimski](https://github.com/DawidRadzimski)
- GitHub Kamil Grundas: [KamilGrundas](https://github.com/KamilGrundas)
- GitHub Katarzyna Czempiel: [kachnna](https://github.com/kachnna)
- GitHub Katarzyna Drajok: [drajkata](https://github.com/drajkata)
- GitHub Paweł Sakowicz: [pawel544](https://github.com/pawel544)
- GitHub Rafał Pietras: [rafalradx](https://github.com/rafalradx)
- GitHub Sabina Limmer: [SabinaLimmer](https://github.com/SabinaLimmer)

## Table of Contents

- [Configuration](#Configuration)
- [Installation](#installation)
- [Running the application](#running-the-application)
- [Usage example](#Usage-example)
- [Licence](#licence)
- [Authors](#Authors)
- [Contact](#Contact)

Make sure Python 3.11 or later is installed on your computer.

The application uses the following packages:

- `fastapi`
- `flet`
- `jinja2`
- `numpy`
- `pandas`
- `scikit-learn`
- `tensorflow`
- `uvicorn[standard]`
- `openai`


## Installation

### 1. Clone the Repository:

```
git clone https://github.com/rafalradx/to-churn-or-not-to-churn
```

### 2. Navigate to the Application Directory:

```
cd to-churn-or-not-to-churn
```

### 3. Install Dependencies:

To use `FastAPI` application install requirements from file:

`pip install -r requirements.txt`

To use `flet` app install requirements from file:

`pip install -r requirements-flet.txt`

## Configuration to work with openAI API

The FastAPI application can interact with ChatGPT via the OpenAI API to obtain recommendations. To use this functionality, you need to rename the configuration file from `env` to `.env` and include your OpenAI API key:

`OPENAI_API_KEY=your_super_secret_open_AI_api_key`

### 

## Running the Application:

### Running the Flet Application

To start the Flet application, use the following command:

```
flet run interface.py
```

### Running the FastAPI Application

To start the FastAPI application, use the following command:

```
uvicorn main:app --reload
```

### Running the Jupyter Notebook

Start the Jupyter notebook server to run the analysis:

```
jupyter-notebook notebooks/project.ipynb
```

### Running the FastAPI app as a docker container

The FastAPI app can be alternatively run in docker container.
To do so, first build the Docker image:

`docker build -t ml-churn-fastapi .`

This command creates a docker image named `ml-churn-fastapi` with ubuntu 24.04 as the base. The process takes around 10 minutes and the resulting image is approximately 3GB in size.

To start the app in a container, run the following command:

`docker run -d -p 8000:8000 ml-churn-fastapi`

The app can be accessed in your browser at:

`localhost:8000`

## Usage example

### Usage example FastAPI

Model prediction:

![Screenshot from 2024-08-24 19-09-11](https://github.com/user-attachments/assets/705cfe33-bd3f-410f-b679-1908144698dc)

GPT recommendation:

![Screenshot from 2024-08-24 19-11-00](https://github.com/user-attachments/assets/5a75a2d9-8ef8-4c49-9ce8-02e5e7fc7abb)

## Licence

This application is provided under the MIT license.

## Authors

- 'Alex Kruh'
- 'Beata Chrząszcz'
- 'Dawid Radzimski'
- 'Kamil Grundas'
- 'Katarzyna Czempiel'
- 'Katarzyna Drajok'
- 'Paweł Sakowicz'
- 'Rafał Pietras'
- 'Sabina Limmer'

## Contact

If you have any questions, suggestions, or would like to get in touch regarding the application, feel free to contact us:

- GitHub Alex Kruh: [OlekKruh](https://github.com/OlekKruh)
- GitHub Beata Chrząszcz: [BettyBeetle](https://github.com/BettyBeetle)
- GitHub Dawid Radzimski: [DawidRadzimski](https://github.com/DawidRadzimski)
- GitHub Kamil Grundas: [KamilGrundas](https://github.com/KamilGrundas)
- GitHub Katarzyna Czempiel: [kachnna](https://github.com/kachnna)
- GitHub Katarzyna Drajok: [drajkata](https://github.com/drajkata)
- GitHub Paweł Sakowicz: [pawel544](https://github.com/pawel544)
- GitHub Rafał Pietras: [rafalradx](https://github.com/rafalradx)
- GitHub Sabina Limmer: [SabinaLimmer](https://github.com/SabinaLimmer)
