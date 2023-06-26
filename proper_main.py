try:
    import requests
    import os
    import subprocess as sp
    from bs4 import BeautifulSoup
    from nbconvert import PythonExporter
    import shutil

except Exception as e:
    print("Some modules are missing:", e)
    print("Do you want to install them via this Python program?")
    option = input("Y or N: ")
    if option.lower() not in ["y", "n"]:
        exit()
    elif option.lower() == "n":
        exit()
    elif option.lower() == "y":
        print("Make sure your internet connection is active; otherwise, it may throw an error. Press 'N' to exit.")
        curr_dir = os.getcwd()
        os.system("pip install -r " + curr_dir + "/requirements.txt")


# All the options like cloning and cleaning of data and find the complex repo are done here


def web_scrape(user_url,st): # This function gets the repo from the user profile 
    username=user_url[19:]
    if username.endswith("/"):
    	username=username[:-1]
    print(username)
    base_url = f"https://api.github.com/users/{username}/repos"
    
    response = requests.get(base_url)
    if response.status_code != 200:
        return ("Please provide a valid link.",1)
    st.text("Extracting the Repos")
    repos = []
    repositories = response.json()
    for repo in repositories:
    	
    	repo_name = repo["name"]
    	
    	repos.append("https://github.com/"+username + "/" +repo_name)
    return repos,0


def data_cloning(repos,st): # this function clones the repository
    
    if os.path.isdir("/tmp/repos"):
    	shutil.rmtree("/tmp/repos")
    
    os.mkdir("/tmp/repos")
    
    
    st.text("Cloning the Repos")
    os.chdir("/tmp/repos")
    for i in repos:
        sp.run(["git", "clone", i], stdout=sp.DEVNULL, stderr=sp.DEVNULL)

    return os.getcwd()


def data_cleaning(directory,st): # this functions deletes the all the files exculding python and jupter notebook files
    exporter = PythonExporter()
    st.text("Cleaning the Repos")
    
    if len(os.listdir(os.getcwd())) ==0:
    	st.text("Not a Valid Repo")
    	return

    for root, dirs, files in os.walk(directory, topdown=False):
        for filename in files:
            file_path = os.path.join(root, filename)

            #if filename.endswith(".ipynb"):
                #output, _ = exporter.from_filename(file_path)
                #with open(os.path.join(root, filename[:-6] + ".py"), "w") as script_file:
                #    script_file.write(output)
                #os.remove(file_path)

            if not (filename.endswith(".py") or filename.endswith(".ipynb")):
                os.remove(file_path)

        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)


def analyse(st): # here we are using radon library to analyse the cyclomatic complexity of the python files
    project_and_grades = {}
    report_analysis = {}
    st.text("Analysing...")
    if len(os.listdir(os.getcwd())) ==0:
    	st.text("Not a Valid Repo")
    	return

    for file in os.listdir(os.getcwd()):
        print(file)
        path = os.getcwd() + "/" + file
        
        cmd = ["radon", "cc", "--total-average","--include-ipynb", file]
        res = sp.check_output(cmd)
        index = res.decode().find("Average")
        if index <= 0:
            grade = "A"
            score = 0.5
        else:
            grade = res.decode()[index:]
            score = grade[23:-1]
            score = score[:3]
            grade=grade[20]
            

        project_and_grades["Repo " + file] = " Score " + str(score)
        report_analysis["Repo " + file] = [float(score)]
    shutil.rmtree('/tmp/repos')

    return project_and_grades,report_analysis
    
    
    
def self_analysis(report_analysis): # Here the basic analysis done to determine the complex repo without asking chatgpt
	score= max(report_analysis.values())
	for keyss in report_analysis:
		if report_analysis[keyss]==score:
			repo = keyss
	return repo,score



"""def main():
	web_scrape()
	curr_path=data_cloning()
	data_cleaning(curr_path)
	report=analyse()
	print(report)
	
if __name__ == main():
	main()
"""
