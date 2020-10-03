[![Codacy Badge](https://api.codacy.com/project/badge/Grade/b26668c721c44a149e230326ab2758d1)](https://app.codacy.com/manual/wilson.forero/django-api?utm_source=github.com&utm_medium=referral&utm_content=wjfatuan/django-api&utm_campaign=Badge_Grade_Settings)

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/wjfatuan/django-api)

# Sample application

This is a sample application exposing a generic API to store data in a JSON field. Data has an id and a name that cab be used to categorize the data you are storing. this can be used to store any JSON data in a simple way. 

This application has been built with Django 3 and DRF and is intended to be used as example in laboratories where we need to store data using a RestFul API.

## Usage

This API allow the storage of a JSON payload including a name and a key, e.g.

```json
{
    "id": 20,
    "name": "my data",
    "data": ["here you can include whatever you want as a JSON"]
}
```

To store data use a POST method like

```bash
curl -X POST -H 'Content-Type: application/json' \
     -d '{"name":"my_data","data":[]}' \
     https://server/api/1.0/data/
```

To get all data available use a GET method like

```bash
curl -X GET -H 'Accept: application/json; indent=2' \
     https://server/api/1.0/data/
```

To get a specific register use a GET method including the respective id, like

```bash
curl -X GET -H 'Accept: application/json; indent=2' \
     https://server/api/1.0/data/1/
```

You can also update your data using 

```bash
curl -X PATCH -H 'Content-Type: application/json' \
     -d '{"name":"my_data","data":{"a":"b"}}' \
     https://server/api/1.0/data/3/
```
