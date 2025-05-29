pipeline {
    agent any
    triggers {
        pollSCM("H/15 * * * *")
    }
    stages{
        stage ("build") {
            steps {echo "############"

            sh '''
            echo "Build stage"
            echo "Building ..."
            echo "Build complete"'''

            echo "############"}
        }
        stage("tests") {
            steps {echo "*************"
            sh '''echo "Test stage"
            echo "testing ..."
            echo "tests complete"'''
            echo "*************"}
        }
        stage("merge") {
            steps {echo "@@@@@@@@@@@@"
            sh '''echo "Merge stage"
            echo "Test status: success"
            echo "Thus merging branches"
            echo "..."
            echo "Merge complete!"
            echo "Pipeline finished"'''
            echo "@@@@@@@@@@@@"}
        }
    }
     
}