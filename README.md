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

- `absl-py~=2.1.0`
- `annotated-types~=0.7.0`
- `anyio~=4.4.0`
- `arrow~=1.3.0`
- `astunparse~=1.6.3`
- `binaryornot~=0.4.4`
- `certifi~=2024.7.4`
- `chardet~=5.2.0`
- `charset-normalizer~=3.3.2`
- `click~=8.1.7`
- `cookiecutter~=2.6.0`
- `fastapi~=0.112.1`
- `flatbuffers~=24.3.25`
- `flet~=0.23.2`
- `flet-core~=0.23.2`
- `flet-runtime~=0.23.2`
- `gast~=0.6.0`
- `google-pasta~=0.2.0`
- `grpcio~=1.65.5`
- `h11~=0.14.0`
- `h5py~=3.11.0`
- `httpcore~=1.0.5`
- `httptools~=0.6.1`
- `httpx~=0.27.0`
- `idna~=3.7`
- `jinja2~=3.1.4`
- `joblib~=1.4.2`
- `keras~=3.5.0`
- `libclang~=18.1.1`
- `markdown~=3.7`
- `markdown-it-py~=3.0.0`
- `markupsafe~=2.1.5`
- `mdurl~=0.1.2`
- `ml-dtypes~=0.4.0`
- `namex~=0.0.8`
- `numpy~=1.26.4`
- `oauthlib~=3.2.2`
- `opt-einsum~=3.3.0`
- `optree~=0.12.1`
- `packaging~=23.2`
- `pandas~=2.2.2`
- `protobuf~=4.25.4`
- `pydantic~=2.8.2`
- `pydantic-core~=2.20.1`
- `pygments~=2.18.0`
- `pypng~=0.20220715.0`
- `python-dateutil~=2.9.0`
- `python-dotenv~=1.0.1`
- `python-slugify~=8.0.4`
- `pytz~=2024.1`
- `pyyaml~=6.0.2`
- `qrcode~=7.4.2`
- `repath~=0.9.0`
- `requests~=2.32.3`
- `rich~=13.7.1`
- `scikit-learn~=1.5.1`
- `scipy~=1.14.0`
- `setuptools~=72.2.0`
- `six~=1.16.0`
- `sniffio~=1.3.1`
- `starlette~=0.38.2`
- `tensorboard~=2.17.1`
- `tensorboard-data-server~=0.7.2`
- `tensorflow~=2.17.0`
- `tensorflow-io-gcs-filesystem~=0.31.0`
- `termcolor~=2.4.0`
- `text-unidecode~=1.3`
- `threadpoolctl~=3.5.0`
- `types-python-dateutil~=2.9.0.20240316`
- `typing-extensions~=4.12.2`
- `tzdata~=2024.1`
- `urllib3~=2.2.2`
- `uvicorn[standard]~=0.30.6`
- `watchdog~=4.0.2`
- `watchfiles~=0.23.0`
- `websockets~=12.0`
- `werkzeug~=3.0.3`
- `wheel~=0.44.0`
- `wrapt~=1.16.0`


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

`pip install -r requirements.txt`

To polecenie instaluje wszystkie zależności wymagane przez projekt, korzystając z pliku **requirements.txt**.

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
jupyter notebook
```

## Przykład użycia

### Przykład użycia aplikacji Flask

### Przykład użycia aplikacji FastAPI

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

## Configuration

Make sure Python 3.11 or later is installed on your computer.

The application uses the following packages:

- `absl-py~=2.1.0`
- `annotated-types~=0.7.0`
- `anyio~=4.4.0`
- `arrow~=1.3.0`
- `astunparse~=1.6.3`
- `binaryornot~=0.4.4`
- `certifi~=2024.7.4`
- `chardet~=5.2.0`
- `charset-normalizer~=3.3.2`
- `click~=8.1.7`
- `cookiecutter~=2.6.0`
- `fastapi~=0.112.1`
- `flatbuffers~=24.3.25`
- `flet~=0.23.2`
- `flet-core~=0.23.2`
- `flet-runtime~=0.23.2`
- `gast~=0.6.0`
- `google-pasta~=0.2.0`
- `grpcio~=1.65.5`
- `h11~=0.14.0`
- `h5py~=3.11.0`
- `httpcore~=1.0.5`
- `httptools~=0.6.1`
- `httpx~=0.27.0`
- `idna~=3.7`
- `jinja2~=3.1.4`
- `joblib~=1.4.2`
- `keras~=3.5.0`
- `libclang~=18.1.1`
- `markdown~=3.7`
- `markdown-it-py~=3.0.0`
- `markupsafe~=2.1.5`
- `mdurl~=0.1.2`
- `ml-dtypes~=0.4.0`
- `namex~=0.0.8`
- `numpy~=1.26.4`
- `oauthlib~=3.2.2`
- `opt-einsum~=3.3.0`
- `optree~=0.12.1`
- `packaging~=23.2`
- `pandas~=2.2.2`
- `protobuf~=4.25.4`
- `pydantic~=2.8.2`
- `pydantic-core~=2.20.1`
- `pygments~=2.18.0`
- `pypng~=0.20220715.0`
- `python-dateutil~=2.9.0`
- `python-dotenv~=1.0.1`
- `python-slugify~=8.0.4`
- `pytz~=2024.1`
- `pyyaml~=6.0.2`
- `qrcode~=7.4.2`
- `repath~=0.9.0`
- `requests~=2.32.3`
- `rich~=13.7.1`
- `scikit-learn~=1.5.1`
- `scipy~=1.14.0`
- `setuptools~=72.2.0`
- `six~=1.16.0`
- `sniffio~=1.3.1`
- `starlette~=0.38.2`
- `tensorboard~=2.17.1`
- `tensorboard-data-server~=0.7.2`
- `tensorflow~=2.17.0`
- `tensorflow-io-gcs-filesystem~=0.31.0`
- `termcolor~=2.4.0`
- `text-unidecode~=1.3`
- `threadpoolctl~=3.5.0`
- `types-python-dateutil~=2.9.0.20240316`
- `typing-extensions~=4.12.2`
- `tzdata~=2024.1`
- `urllib3~=2.2.2`
- `uvicorn[standard]~=0.30.6`
- `watchdog~=4.0.2`
- `watchfiles~=0.23.0`
- `websockets~=12.0`
- `werkzeug~=3.0.3`
- `wheel~=0.44.0`
- `wrapt~=1.16.0`


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

`pip install -r requirements.txt`

This command installs all dependencies required by the project using the **requirements.txt file**.

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
jupyter notebook
```

## Usage example

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
