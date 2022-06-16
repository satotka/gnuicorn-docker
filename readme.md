# Sample for gnuicorn on docker

## usage

0. fix Influxdb IP in ```app/app.py```

1. Build image.

```bash
make build
```

2. test1: Run Container without gunicorn.

```bash
make test1
```

It will be completed, and container will be removed itself.

3. test2: Run web Container and check console output.

```bash
$ make test2
[2022-06-15 14:09:01 +0000] [6] [INFO] Starting gunicorn 20.1.0
[2022-06-15 14:09:01 +0000] [6] [INFO] Listening at: http://0.0.0.0:800 (6)
[2022-06-15 14:09:01 +0000] [6] [INFO] Using worker: sync
[2022-06-15 14:09:01 +0000] [7] [INFO] Booting worker with pid: 7
```

Open another shell, access to web container.

```bash
$ curl localhost:8050
Hello, World!
```

4. Clean up

Stop Container with ```Ctrl+C```.

Delete built image with ```make clean```
