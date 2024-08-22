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

def get_result(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    if isJson(output):
        data = json.loads(output)
        if 'contactUrl' in data and 'requestId' in data and 'status' in data and data['status'] >= 400:
            print(f"Error occured!!")
            print(f"==== command: {command}")
            print(f"==== status: {data['status']}")
            print(f"==== code: {data['code']}")
            print(f"==== message: {data['message']}")
            print(f"==== requestId: {data['requestId']}")
            raise Exception(f"status: {data['status']}<br>code: {data['code']}<br>message: {data['message']}")
        return data
    else:
        print(f"Error occured when result decode!!")
        print(f"==== result: {result}")
        print(f"==== traceback: {traceback.format_exc()}")
        raise Exception(f"status: result parsing error<br>result: {result}")

def execute_api(offering, sub_url, access_key, secret_key, type, params=None, payload=None, success=None, fail=None, getall=True, data_key=None):
    os.environ['PROJECT_ID'] = ""
    os.environ['CMP_URL'] = ""
    os.environ['ACCESS_KEY'] = access_key
    os.environ['SECRET_KEY'] = secret_key

    result = subprocess.run(f"REQ_URL='{sub_url}' scp-api", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    if isJson(output):
        data = json.loads(output)
        if 'contactUrl' in data and 'requestId' in data and 'status' in data and data['status'] >= 400:
            print(f"Error occured!!")
            print(f"==== command: {command}")
            print(f"==== status: {data['status']}")
            print(f"==== code: {data['code']}")
            print(f"==== message: {data['message']}")
            print(f"==== requestId: {data['requestId']}")
            raise Exception(f"status: {data['status']}<br>code: {data['code']}<br>message: {data['message']}")
        return data
    else:
        print(f"Error occured when result decode!!")
        print(f"==== result: {result}")
        print(f"==== traceback: {traceback.format_exc()}")
        raise Exception(f"status: result parsing error<br>result: {result}")

def main():
    with st.sidebar:
        st.header("Account Configuration")
        offering = st.selectbox("Offering", ["For Samsung", "For Enterprise"], key='offering', on_change=change_offering, args=(), index=None, placeholder="Select Offering")
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
