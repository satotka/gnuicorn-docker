# Sample for gnuicorn on docker

## usage

1. Build image.

```bash
docker build  --tag my-web .
```

2. Run Container and check console output.

```bash
$ docker run -it --rm --name web1 -p 8050:800 my-web
[2022-06-15 14:09:01 +0000] [6] [INFO] Starting gunicorn 20.1.0
[2022-06-15 14:09:01 +0000] [6] [INFO] Listening at: http://0.0.0.0:800 (6)
[2022-06-15 14:09:01 +0000] [6] [INFO] Using worker: sync
[2022-06-15 14:09:01 +0000] [7] [INFO] Booting worker with pid: 7
```

3. open another shell, access to web container.

```bash
$ curl localhost:8050
Hello, World!
```

4. Clean up

Stop Container with ```Ctrl+C```, or ```docker rm -f web1``` from another shell.

Delete built image with ```docker rmi my-web```
