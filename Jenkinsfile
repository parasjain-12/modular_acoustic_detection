#!/usr/bin/env groovy

/**
 * Jenkinsfile
 */

pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('Install Requirements') {
            steps {
                sh 'python binary_model.py'
            }
        }
    }
}
