import streamlit as st
import requests

st.set_page_config(page_title="GitHub Analyzer", layout="centered")

st.title("🔍 GitHub Repository Analyzer")

repo_url = st.text_input("Enter GitHub Repository URL:")

if st.button("Analyze Repository"):
    if repo_url:
        try:
            parts = repo_url.strip("/").split("/")
            owner = parts[-2]
            repo = parts[-1]

            api_url = f"https://api.github.com/repos/{owner}/{repo}"
            response = requests.get(api_url)
            data = response.json()

            if response.status_code == 200:
                st.success("Repository Found!")

                col1, col2 = st.columns(2)

                with col1:
                    st.metric("⭐ Stars", data['stargazers_count'])
                    st.metric("🍴 Forks", data['forks_count'])

                with col2:
                    st.metric("👀 Watchers", data['watchers_count'])
                    st.metric("🐞 Open Issues", data['open_issues_count'])

                st.write("📦 Size:", data['size'], "KB")
                st.write("🗓 Created At:", data['created_at'])
                st.write("🔄 Last Updated:", data['updated_at'])

            else:
                st.error("Repository not found!")

        except:
            st.error("Invalid URL format!")
    else:
        st.warning("Please enter a repository URL.")
