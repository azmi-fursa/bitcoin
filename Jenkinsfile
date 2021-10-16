pipeline {
    agent any
        stages {
		stage('Building our image') {
            steps{
                script {
                    sh 'sudo docker build -t bitcoin-flask .'
         	       }
            	 }
        	}
 	}
}
