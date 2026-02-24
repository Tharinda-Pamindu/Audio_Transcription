"""
Audio Transcription App — Whisper + Liquid Glass UI
Transcribes audio files (Sinhala / English) using OpenAI Whisper large-v3.
"""

import os
import json
import tempfile
import traceback
from pathlib import Path

from flask import Flask, request, jsonify, render_template, send_from_directory

import whisper

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
UPLOAD_FOLDER = os.path.join(tempfile.gettempdir(), "audio_transcription_uploads")
ALLOWED_EXTENSIONS = {
    "mp3", "wav", "m4a", "ogg", "flac", "wma", "aac", "opus", "webm", "mp4"
}
DEFAULT_MODEL = "large-v3"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 500 * 1024 * 1024  # 500 MB max

# ---------------------------------------------------------------------------
# Model cache — lazy-loaded on first transcription
# ---------------------------------------------------------------------------
_models: dict = {}


def get_model(name: str = DEFAULT_MODEL):
    """Load (or return cached) Whisper model."""
    if name not in _models:
        print(f"[whisper] Loading model '{name}' — this may take a minute …")
        _models[name] = whisper.load_model(name)
        print(f"[whisper] Model '{name}' loaded ✓")
    return _models[name]


def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------
@app.route("/")
def index():
    """Serve the Liquid Glass UI."""
    return render_template("index.html")


@app.route("/transcribe", methods=["POST"])
def transcribe():
    """Accept an audio file and return its transcription."""
    # --- validate upload ------------------------------------------------
    if "audio" not in request.files:
        return jsonify({"error": "No audio file provided."}), 400

    file = request.files["audio"]
    if file.filename == "":
        return jsonify({"error": "Empty filename."}), 400
    if not allowed_file(file.filename):
        return jsonify({
            "error": f"Unsupported format. Allowed: {', '.join(sorted(ALLOWED_EXTENSIONS))}"
        }), 400

    # --- save temp file -------------------------------------------------
    ext = file.filename.rsplit(".", 1)[1].lower()
    tmp_path = os.path.join(UPLOAD_FOLDER, f"upload.{ext}")
    file.save(tmp_path)

    # --- transcribe -----------------------------------------------------
    model_name = request.form.get("model", DEFAULT_MODEL)
    language = request.form.get("language", None)  # None = auto-detect

    try:
        model = get_model(model_name)

        # Build transcribe options
        options = {
            "verbose": False,
        }
        if language and language != "auto":
            options["language"] = language

        result = model.transcribe(tmp_path, **options)

        segments = []
        for seg in result.get("segments", []):
            segments.append({
                "id": seg["id"],
                "start": round(seg["start"], 2),
                "end": round(seg["end"], 2),
                "text": seg["text"].strip(),
            })

        return jsonify({
            "text": result["text"].strip(),
            "language": result.get("language", "unknown"),
            "segments": segments,
            "model": model_name,
        })

    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

    finally:
        # cleanup temp file
        if os.path.exists(tmp_path):
            try:
                os.remove(tmp_path)
            except OSError:
                pass


@app.route("/models", methods=["GET"])
def models():
    """Return available Whisper model names and which are loaded."""
    available = ["tiny", "base", "small", "medium", "large", "large-v2", "large-v3"]
    loaded = list(_models.keys())
    return jsonify({"available": available, "loaded": loaded, "default": DEFAULT_MODEL})


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("\n╔══════════════════════════════════════════════════╗")
    print("║   Audio Transcription — Whisper + Liquid Glass   ║")
    print("║   Open:  http://127.0.0.1:5000                   ║")
    print("╚══════════════════════════════════════════════════╝\n")
    app.run(host="127.0.0.1", port=5000, debug=False)
