pipeline {
    agent any 
        environment {
		DOCKERHUB_CREDENTIALS=credentials('dockerhub-ahmadsk')
	} 
        stages {
		stage('Building our image') {
            steps{
                script {
                    sh 'sudo -s docker build -t bitcoin-flask .'
         	       }
            	 }
        	}
 	}
}
