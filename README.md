# CVE Vulnerabilities Api

Es una api que entrega resultado mediante los siguientes endpoints:

* query?q=String_CVE
* cveid?id=CVE-XXXX-[XXXX|XXXXX|XXXXXXX]
* date?YYYY-MM-DD


## Cómo ejecutar

1. Usando Docker

* Un imagen del proyecto está disponible en Docker, obtener la imagen.

```
sudo docker pull kurotom/python_dev:django_app-1_1
```

* Entrar en el directorio y ejecutar el comando.
```
sudo docker compose -f app.yml up -d
```

* Ir a la dirección `http://127.0.0.1:8000/doc/` para consultar la documentación.



