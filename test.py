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

st.title("🍟GitHub Migration")
source_div, blank1, target_div, blank2, log_div = st.columns([1, 0.1, 1, 0.1, 0.5])


if __name__ == '__main__':
    main()

