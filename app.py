import streamlit as st
from resource import *
from proper_main import *
from resource import llm_chain
import time

# Here in the mail function the GPT model and the rest of the function in other files are called here

def main():
    st.title("Github Automated Repo Analysis")

    # User input
    user_url = st.text_input("Enter the Github URL")
    
    option = st.radio("What you want me to do",["Python Analysis","GPT Evaluation"])

    # Generate response
    if st.button("Submit"):

        st.text("Please wait Automation is Processing")
        strttime=time.time()
        repos, status = web_scrape(user_url,st)
        
        #task_progress = st.progress(0)
        #task_progress.progress("Tools is taking action please wait")
        if status == 0:
            repo_path = data_cloning(repos,st)
            data_cleaning(repo_path,st)
            query,report_analysis = analyse(st)
            if len(query) == 0:
            	st.write("The given User's URL doesnt Contain Python Repository")
            if option == "Python Analysis":
            	repo_name,score=self_analysis(report_analysis)
            	output="The Complex Repo is "+ str(repo_name)+" Because the Complexity Score is "+str(score)
            	#st.write("The Complex Repo is",repo_name," Because the Complexity Score is",score)
            	st.text_area("Bot Response:", value=output, height=100)
            	time.sleep(15)
            	
            elif option == "GPT Evaluation":
            	response_gpt = llm_chain([str(query)])
            	# Display the response
            	st.text_area("Bot Response:", value=response_gpt['text'], height=100)
            	elapsed_time = time.time() - strttime
            	st.text(f"Execution time: {elapsed_time:.2f} seconds")
        else:
            output = st.empty()
            output.error(f"Error occurred. Please contact the admin {repos}.")
            time.sleep(5)

if __name__ == "__main__":
    main()

