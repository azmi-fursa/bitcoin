pipeline {
    agent any 
        environment {
		DOCKERHUB_CREDENTIALS=credentials('azmiabu')
	} 
        stages {
		stage('Building our image') {
            steps{
                script {
                    sh 'sudo -s docker build -t bitcoin-flask .'
         	       }
            	 }
        	}
        stage('Login') {

			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | sudo docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		} 
	stage('Tag') {

			steps {
			    sh 'sudo docker tag bitcoin-flask azmiabu/bitcoin-flask'
			}
		}
 	}
}
