
build:
	docker build --tag my-image .

test1:
	docker run -it --rm --name test-python my-image python app/app.py

test2:
	docker run -it --rm --name test-web -p 8050:800 my-image

clean:
	docker rmi my-image