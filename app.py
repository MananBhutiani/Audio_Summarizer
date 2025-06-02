import os
import tempfile
import whisper
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

ffmpeg_path = r"C:\Users\MANAN BHUTIANI\Documents\FFMPEG\ffmpeg-2025-06-02-git-688f3944ce-full_build\bin" 
os.environ["PATH"] += os.pathsep + ffmpeg_path


st.set_page_config(
    page_title="🎙️ AI Meeting Assistant",
    page_icon="🎙️",
    layout="wide"
)

load_dotenv()  # Load .env file


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
gemini_model = genai.GenerativeModel('gemini-1.5-flash')


@st.cache_resource
def load_whisper_model():
    return whisper.load_model("base")  # Use "small" for better accuracy

model = load_whisper_model()


def save_uploaded_file(uploaded_file):
    """Saves uploaded file with proper extension"""
    try:
        suffix = os.path.splitext(uploaded_file.name)[1]
        with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as tmp:
            tmp.write(uploaded_file.getbuffer())
            return tmp.name
    except Exception as e:
        st.error(f"❌ File save failed: {str(e)}")
        return None

def transcribe_audio(audio_path):
    """Transcribes audio using Whisper"""
    try:
        result = model.transcribe(audio_path, fp16=False)  # fp16=False for CPU
        return result["text"]
    except Exception as e:
        st.error(f"❌ Transcription failed: {str(e)}")
        return None

def generate_summary(text):
    """Generates summary using Gemini"""
    try:
        prompt = f"""
        Summarize this meeting transcript into 3-5 concise bullet points.
        Highlight decisions, action items, and key discussions.

        Transcript:
        {text}
        """
        response = gemini_model.generate_content(prompt)
        return response.text
    except Exception as e:
        st.error(f"❌ Summarization failed: {str(e)}")
        return None


st.title("🎙️ AI Meeting Assistant")


uploaded_file = st.file_uploader(
    "Upload meeting audio (MP3/WAV/M4A)", 
    type=["mp3", "wav", "m4a"]
)

if uploaded_file:
    audio_path = save_uploaded_file(uploaded_file)
    
    if audio_path and os.path.exists(audio_path):
       
        col1, col2 = st.columns([3, 1])
        
        with col1:
            with st.spinner("🔍 Transcribing audio..."):
                transcript = transcribe_audio(audio_path)
                
            if transcript:
                st.success("✅ Transcription complete!")
                
                
                transcript_container = st.container()
                with transcript_container:
                    st.subheader("📝 Full Transcript")
                    st.text_area("Transcript", transcript, height=300, label_visibility="collapsed")
                
                if st.button("✨ Generate Summary"):
                    with st.spinner("📖 Generating summary..."):
                        summary = generate_summary(transcript)
                        if summary:
                            st.subheader("📌 Meeting Summary")
                            st.write(summary)
        
        
        try:
            os.unlink(audio_path)
        except:
            pass
    else:
        st.error("⚠️ Failed to process uploaded file")


with st.sidebar:
    st.markdown("## How to Use")
    st.markdown("1. Upload meeting audio\n2. Wait for transcription\n3. Generate summary")
    st.markdown("---")
    st.markdown("**Models Used:**")
    st.markdown("- 🎤 Whisper (Local)\n- ✨ gemini-1.5-flash")