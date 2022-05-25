pipeline{
    
    agent any
    stages
    {
        stage('Clone Repo'){
            steps{
                script{
                    if(fileExists('/home/jenkins/.jenkins/workspace/consolegame/')){
                        dir('consolegame'){ sh 'git pull https://github.com/Khurram-Bukhari/consolegame.git main'}
                    }
                    else{
                        sh 'git clone https://github.com/Khurram-Bukhari/consolegame.git'
                    }
                }
            }
        }
        stage('Installs'){
            steps{
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Testing'){
            steps{
                sh 'cd service1 && python3 -m pytest --cov=application'
                sh 'cd service2 && python3 -m pytest --cov=application'
                sh 'cd service3 && python3 -m pytest --cov=application'
                sh 'cd service4 && python3 -m pytest --cov=application'
            }
        }
        stage('Build & Deploy'){
            steps{
                sh 'sudo docker-compose build'
                sh 'sudo docker-compose push'
            }
        }
        stage('Deploy'){
            steps{
                sh 'sudo docker-compose up -d'
            }
        }
    }
}