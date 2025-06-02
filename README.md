# AI Audio Transcription & Summarization Tool
This tool provides an automated pipeline for converting meeting audio recordings into text transcripts and generating concise summaries of key discussion points. The system combines OpenAI's Whisper for speech-to-text conversion with Google's Gemini for intelligent summarization, delivered through an intuitive web interface.

# Features
Audio Transcription: Converts MP3, WAV, and M4A audio files into accurate text transcripts

AI Summarization: Generates bullet-point summaries highlighting decisions, action items, and key discussions

Local Processing: Whisper model runs locally for privacy and cost efficiency

User-Friendly Interface: Simple web interface built with Streamlit

# Technical Requirements
Python 3.8+

FFmpeg (for audio processing)

Google API key (for Gemini integration)

Minimum 4GB RAM (8GB recommended for longer recordings)

# Usage
Run the application:

streamlit run app.py
In your web browser:

Upload an audio file (MP3, WAV, or M4A format)

Wait for the transcription to complete

Click "Generate Summary" to create a concise meeting summary

# Configuration Options
Whisper model size can be adjusted in app.py (base, small, medium)

Summary prompt can be customized in the generate_summary() function

Debug mode can be enabled for troubleshooting file handling

# Troubleshooting
FFmpeg errors: Ensure FFmpeg is installed and in your system PATH

API errors: Verify your Google API key is valid and has sufficient quota

File not found errors: Check debug output for file path verification

# License
This project is licensed under the MIT License - see the LICENSE file for details.

# Acknowledgments
OpenAI for the Whisper speech recognition model

Google for the Gemini language model

Streamlit for the web application framework
