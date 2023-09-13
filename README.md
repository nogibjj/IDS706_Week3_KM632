[![cicd](https://github.com/nogibjj/IDS706_Template_KM632/actions/workflows/python.yml/badge.svg)](https://github.com/nogibjj/IDS706_Template_KM632/actions/workflows/python.yml)

This repo is created as a template for my data engineering course. 

 The repo includes skeletons of following:

 * Basic workflow actions (testing, linting, formatting)
 * Makefile
 * requirements.txt
 * VS Code Dev Containers
 * basic main file along with its test file

 Usage: 

 Add workflow actions: 

 1. Add actions to add under steps of init_build job
 2. Add commands for your actions in Makefile
 3. Add any neccessary libraries to be used for your actions in requirements.txt

 The template is set up in a way that when you push or pull request, CI/CD is automatically executed. 
 If the workflow actions added succesully pass the CI/CD, you will be green check mark on the Action tab.