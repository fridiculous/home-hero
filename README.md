## Home Hewo

### SET UP

```
docker build -f Dockerfile.base -t api-base .

docker build -t api .
```


### Running

```
# as bash
docker run -p 80:8000 -it --rm -v $(pwd):/code api bash


# as a server
docker run -p 8000:8000 -it --rm -v $(pwd)/hero:/code api python3 manage.py migrate

docker run -p 8000:8000 -it --rm -v $(pwd)/hero:/code api python3 manage.py runserver 0.0.0.0:8000
```
