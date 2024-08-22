import streamlit as st

st.set_page_config(page_title="GitHub Migration", layout="wide", page_icon="🚀")
spinner_placeholder = st.empty()

SPINNER_HTML = """
<style>
@keyframes spinner {
  to {transform: rotate(360deg);}
}
.overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(255, 255, 255, 0.8);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
  opacity: 0.6;
}
.spinner {
  width: 60px;
  height: 60px;
  border: 10px solid #ccc;
  border-top-color: #333;
  border-radius: 50%;
  animation: spinner .6s linear infinite;
}
</style>
<div class="overlay">
  <div class="spinner"></div>
</div>
"""

# Main UI
st.markdown("""
<style>
.block-container
{
    padding-top: 2rem;
    padding-bottom: 2rem;
}
div[data-testid="stPopoverBody"] {
    min-width: 1700px;
    min-height: 750px;
}
</style>
""", unsafe_allow_html=True)

st.title("API Test")
source_div, blank1, target_div, blank2, log_div = st.columns([1, 0.1, 1, 0.1, 0.5])

def change_offering():
    print("")

def execute_api(offering, sub_url, access_key, secret_key, type, params=None, payload=None, success=None, fail=None, getall=True, data_key=None):
    headers = {
        "Authorization": f"token {access_key}",
        "Accept": "application/vnd.github+json"
    }

def main():
    with st.sidebar:
        st.header("Account Configuration")
        offering = st.selectbox("Offering", ["For Samsung", "For Enterprise"], key='offering', on_change=change_offering, args=(,), index=None, placeholder="Select Offering")
        access_key = st.text_input("Account Key")
        secret_key = st.text_input("Secret Key", type="password")

        if st.button("Get Project List", type="primary"):
            st.session_state['project_list'] = []
            if access_key and secret_key:
                set_loading("show")
                projects = execute_api(offering, "project/v1/projects", access_key, secret_key, "GET", fail={"prefix":"fail", "message":"fetch source organizations"}, success={"prefix":"success", "message":"fetch source organizations"})["contents"]
                if projects:
                    st.session_state['project_list'] = [project['projectName'] for project in projects]
                else:
                    log_message(prefix="fail", message="no source organizations")
                set_loading("hide")
            else:
                log_message(prefix="warn", message="Please ensure Project Name and Source and Target GitHub Configuration.")

if __name__ == '__main__':
    main()
