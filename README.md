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
docker run -p 80:8000 -it --rm -v $(pwd):/code api python3 hero/manage.py runserver 0.0.0.0:8000
```
