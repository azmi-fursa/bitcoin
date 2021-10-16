# BITCOIN APP:
This is a python (flask) app that helps its users see the value of bitcoin in USD ($), and also presents to them its average value in the last 10 minutes

## To use the application locally:
1) first you will need to clone the app: git clone https://github.com/azmi-fursa/bitcoin.git
2) secondly you will need to move the directory bitcoin: cd bitcoin
3) next, install the requirements folder that has flask and requests in it: pip install -r requirements.txt
4) finally, run the app using: python main.py
the app is now accessible to you, go to: http://localhost:5000/

## Build and run the app in docker:
1) clone the project clone https://github.com/azmi-fursa/bitcoin.git
2) build the docker image: docker build -t bitcoin .
3) to run the image that we created in the previous step: docker run -itdp 80:80 bitcoin
4) the app is now accessible, visit http://localhost:5000/ to view the content

### Pushing app to dockerhub
if you want to push the application to dockerhub, you will first need to tag your docker image: docker tag bitcoin azmiabu/bitcoin
then you need to login to your dockerhub account, to do so: "docker login" and enter your username and password
now that you're logged in, push it using the command: docker push azmiabu/bitcoin

after pushing the image you can now logout of your dockerhub using docker logout


