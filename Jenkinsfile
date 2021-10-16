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
                    dockerImage = sudo -s docker build -t bitcoin-flask .
         	       }
            	 }
        	}
 	}
}
