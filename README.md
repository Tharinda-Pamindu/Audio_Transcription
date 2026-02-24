# 🎙️ Audio Transcription

### AI-Powered Speech-to-Text with OpenAI Whisper

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Whisper-large--v3-412991?style=for-the-badge&logo=openai&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-2.0+-000000?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" />
</p>

<p align="center">
  <em>Transcribe Sinhala & English audio with world-class accuracy — beautiful Liquid Glass UI, drag-and-drop upload, timestamped segments, and one-click export. No command line needed.</em>
</p>

---

## 🎯 The Problem

Transcribing audio that mixes **Sinhala (සිංහල)** and **English** is notoriously difficult. Most transcription tools fail on Sinhala entirely, and code-switching between languages makes it even harder.

## ✅ The Solution

This app uses **OpenAI Whisper large-v3** — the state-of-the-art speech recognition model with excellent Sinhala support — wrapped in a stunning **Liquid Glass + Material Design** web interface. Upload your audio, get accurate transcriptions with timestamps, and download the results.

---

## ✨ Features

| Feature                 | Description                                                           |
| ----------------------- | --------------------------------------------------------------------- |
| 🧠 **Whisper large-v3** | Best-in-class multilingual speech recognition — excellent for Sinhala |
| 🌐 **Multi-Language**   | Auto-detects Sinhala, English, Tamil, or set it manually              |
| 🎛️ **Model Selection**  | Choose from `tiny` (fastest) to `large-v3` (most accurate)            |
| 📁 **Drag & Drop**      | Upload audio files by dragging onto the drop zone                     |
| 🔊 **Audio Preview**    | Built-in audio player to preview your files before transcribing       |
| ⏱️ **Timestamps**       | Toggle between plain text and timestamped segment view                |
| 📋 **Copy & Download**  | One-click copy to clipboard or download as `.txt`                     |
| 🎨 **Liquid Glass UI**  | Frosted glass panels, animated gradients, Material Design components  |
| 🎵 **All Formats**      | MP3, WAV, M4A, FLAC, OGG, AAC, OPUS, WebM, MP4, WMA                   |
| 🚀 **One-Click Launch** | Double-click `run.cmd` — everything sets up automatically             |

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+** — [Download](https://python.org)
- **FFmpeg** — Required for audio decoding ([Download](https://ffmpeg.org/download.html))
- **GPU (recommended)** — CUDA-compatible GPU dramatically speeds up transcription

### One-Click Launch (Windows)

```bash
# Just double-click:
run.cmd
```

This will:

1. ✅ Check for Python & FFmpeg
2. ✅ Create a virtual environment (`.venv`)
3. ✅ Install all dependencies
4. ✅ Open your browser to `http://127.0.0.1:5000`
5. ✅ Start the Flask server

### Manual Setup

```bash
# 1. Clone the repository
git clone https://github.com/Tharinda-Pamindu/Voice-Activity-Detector.git
cd Voice-Activity-Detector

# 2. Create & activate virtual environment
python -m venv .venv
.venv\Scripts\activate      # Windows
# source .venv/bin/activate  # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
```

Then open **http://127.0.0.1:5000** in your browser.

> **Note:** The first transcription will download the Whisper model (~3 GB). This is a one-time download.

---

## 📖 Usage

### 1. Upload Your Audio

Drag & drop an audio file onto the upload zone, or click to browse. Supports MP3, WAV, M4A, FLAC, OGG, AAC, OPUS, and more.

### 2. Configure Settings

| Setting      | Options                                                                  |
| ------------ | ------------------------------------------------------------------------ |
| **Model**    | `tiny` → `base` → `small` → `medium` → `large` → `large-v2` → `large-v3` |
| **Language** | Auto-detect · Sinhala (සිංහල) · English · Tamil (தமிழ்)                  |

> **Tip:** Use `large-v3` for the best Sinhala transcription accuracy.

### 3. Transcribe

Click the **Transcribe** button. The model loads on first use, then transcription runs automatically.

### 4. View & Export

- **Plain Text** — Full transcription as continuous text
- **Timestamps** — Segment-by-segment view with start/end times
- **Copy** — Copy to clipboard
- **Download** — Save as `transcription.txt` with embedded timestamps

---

## 📁 Project Structure

```
Audio-Transcription/
├── app.py                  # Flask backend + Whisper engine
├── run.cmd                 # One-click launcher (Windows)
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html          # Liquid Glass + Material Design UI
├── .gitignore
├── LICENSE                 # MIT License
├── CONTRIBUTING.md         # Contribution guidelines
└── README.md
```

---

## 🛠️ Tech Stack

| Component          | Technology                                                        |
| ------------------ | ----------------------------------------------------------------- |
| **Transcription**  | [OpenAI Whisper](https://github.com/openai/whisper) — large-v3    |
| **Backend**        | [Flask](https://flask.palletsprojects.com) — Python web framework |
| **ML Framework**   | [PyTorch](https://pytorch.org)                                    |
| **Audio Decoding** | [FFmpeg](https://ffmpeg.org)                                      |
| **UI Design**      | Liquid Glass + Material Design                                    |
| **Typography**     | [Inter](https://fonts.google.com/specimen/Inter) (Google Fonts)   |
| **Icons**          | [Material Symbols](https://fonts.google.com/icons)                |

---

## ⚙️ API

The app exposes a simple REST API:

| Endpoint      | Method | Description                                            |
| ------------- | ------ | ------------------------------------------------------ |
| `/`           | GET    | Serve the web UI                                       |
| `/transcribe` | POST   | Upload audio + get transcription (multipart/form-data) |
| `/models`     | GET    | List available/loaded Whisper models                   |

### POST `/transcribe`

**Form Data:**

- `audio` — Audio file (required)
- `model` — Whisper model name (default: `large-v3`)
- `language` — Language code: `auto`, `si`, `en`, `ta` (default: `auto`)

**Response:**

```json
{
  "text": "Full transcription text...",
  "language": "si",
  "model": "large-v3",
  "segments": [
    {
      "id": 0,
      "start": 0.0,
      "end": 4.52,
      "text": "Segment text..."
    }
  ]
}
```

---

## 🤝 Contributing

Contributions are welcome! Please read the [Contributing Guide](CONTRIBUTING.md) for details on:

- Setting up your development environment
- Our commit message conventions
- Code style guidelines
- How to submit pull requests

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [OpenAI Whisper](https://github.com/openai/whisper) — State-of-the-art speech recognition
- [Flask](https://flask.palletsprojects.com) — Lightweight Python web framework
- [PyTorch](https://pytorch.org) — Deep learning framework
- [Google Material Design](https://material.io) — Design system inspiration

---

<p align="center">
  Built with ❤️ by <a href="https://github.com/Tharinda-Pamindu">Tharinda Pamindu</a>
</p>
<p align="center">
  ⭐ Star this repo if you find it useful!
</p>
