pipeline {
    agent any
environment { 
        registry = "azmiabu/bitcoin" 
        registryCredential = 'azmiabu' 
        dockerImage = '' 
    }
        stages {
		stage('Building our image') {
            steps{
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
         	       }
            	 }
        	}
 	}
}
