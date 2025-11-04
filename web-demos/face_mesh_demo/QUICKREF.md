# Quick Reference Card

## 🚀 Quick Start Commands

```bash
# Navigate to demo directory
cd ~/insightface/web-demos/face_mesh_demo

# Option 1: Automated start (recommended)
./start_demo.sh

# Option 2: Manual start
source venv/bin/activate
python3 app.py

# Option 3: Command-line processing
python3 detect_mesh.py examples/t1.jpg
```

## 📊 Output Legend

| Color | Landmark | Description |
|-------|----------|-------------|
| 🔵 Blue | Eyes | Left and right eye centers |
| 🟢 Green | Nose | Nose tip |
| 🔴 Red | Mouth | Left and right mouth corners |
| 🟡 Yellow | Lines | Topology connections |
| 🟩 Green Box | Face | Face bounding box |

## 🔧 Common Tasks

### Test Installation
```bash
python3 test_setup.py
```

### Process Single Image
```bash
python3 detect_mesh.py image.jpg
```

### Process with Custom Output
```bash
python3 detect_mesh.py input.jpg -o output.jpg
```

### Start Web Demo
```bash
./start_demo.sh
# Then visit: http://localhost:7860
```

### Stop Web Demo
Press `Ctrl + C` in the terminal

### Deactivate Virtual Environment
```bash
deactivate
```

## 📋 Troubleshooting Quick Fixes

| Issue | Quick Fix |
|-------|-----------|
| Module not found | `pip install -r requirements.txt` |
| No faces detected | Use clear, frontal face images |
| Port already in use | Change port in app.py (line ~243) |
| Permission denied | `chmod +x start_demo.sh` |
| OpenCV error | `sudo apt install libgl1-mesa-glx` |

## 📦 Installation One-Liner

```bash
git clone https://github.com/deepinsight/insightface.git && \
cd insightface/web-demos/face_mesh_demo && \
./start_demo.sh
```

## 🎯 Key Features

- ✅ Single & multiple image processing
- ✅ Real-time face detection
- ✅ Facial landmark visualization
- ✅ Web-based interface (Gradio)
- ✅ Command-line tool included
- ✅ Example images provided
- ✅ Linux Mint optimized

## 📁 Important Files

| File | Purpose |
|------|---------|
| `app.py` | Web interface |
| `detect_mesh.py` | CLI tool |
| `start_demo.sh` | Quick start |
| `test_setup.py` | Test installation |
| `README.md` | Full documentation |

## 🌐 Web Interface Navigation

1. **Single Image Tab**: Process one image at a time
2. **Multiple Images Tab**: Process up to 3 images
3. **About Tab**: Documentation and info

## 💡 Pro Tips

- Use well-lit, frontal face images for best results
- The demo works on CPU by default (no GPU required)
- Check examples/ folder for sample images
- Use detect_mesh.py for batch processing
- Press F5 in browser to reload the interface

## 📞 Getting Help

1. Check README.md for detailed instructions
2. Run test_setup.py to verify installation
3. Check GitHub issues: github.com/deepinsight/insightface/issues
4. Visit InsightFace website: insightface.ai

---

**Quick Reference v1.0** | November 2025
