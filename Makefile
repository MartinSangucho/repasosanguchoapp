
APP_NAME=sanguchoapp
STACK_FILE=stack.yml

build:
	docker build -t royecto_quintoa_img:latest .

deploy:
	docker stack deploy --with-registry-auth -c stack.yml quinto

rm:
	docker stack rm quinto
