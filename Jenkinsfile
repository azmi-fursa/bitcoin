pipeline {
    agent any
        stages {
		stage('Building our image') {
            steps{
                script {
                    sh 'docker build -t bitcoin-flask .'
         	       }
            	 }
        	}
 	}
}
