# 🎭 Face Mesh Topology Detection Demo

A web-based demo that showcases face topology (mesh) detection from images using InsightFace's state-of-the-art face analysis technology.

![InsightFace](https://insightface.ai/assets/img/github/insightface_logo.jpg_320x320.webp)

## 📋 Features

- ✅ **Automatic Face Detection**: Detects faces in images automatically
- ✅ **Facial Landmark Detection**: Identifies key facial points (eyes, nose, mouth)
- ✅ **Topology Visualization**: Shows the mesh structure and connections between landmarks
- ✅ **Single & Multiple Image Support**: Process one or multiple images at once
- ✅ **Web-based Interface**: Easy-to-use Gradio interface accessible via browser
- ✅ **Real-time Processing**: Fast inference on CPU or GPU

## 🖥️ Installation Guide for Linux Mint

### Prerequisites

Before installing, make sure you have:
- Linux Mint (20.x or later recommended)
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Step 1: Update System Packages

```bash
sudo apt update
sudo apt upgrade -y
```

### Step 2: Install Python and Development Tools

```bash
# Install Python 3 and pip if not already installed
sudo apt install python3 python3-pip python3-dev -y

# Install build essentials and dependencies
sudo apt install build-essential cmake -y
sudo apt install libopencv-dev python3-opencv -y

# Verify Python version (should be 3.8+)
python3 --version
```

### Step 3: Clone the Repository

```bash
# Navigate to your desired directory
cd ~

# Clone the InsightFace repository
git clone https://github.com/deepinsight/insightface.git
cd insightface/web-demos/face_mesh_demo
```

### Step 4: Set Up Virtual Environment (Recommended)

```bash
# Install virtualenv if not already installed
sudo apt install python3-venv -y

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Your prompt should now show (venv)
```

### Step 5: Install Python Dependencies

```bash
# Upgrade pip to the latest version
pip install --upgrade pip

# Install the web demo dependencies
pip install -r requirements.txt

# Install InsightFace from the local python package
pip install -e ../../python-package/

# This will install:
# - gradio (web interface)
# - opencv-python (image processing)
# - numpy (numerical operations)
# - insightface (face analysis library from local package)
# - onnxruntime (model inference)
```

**Note**: The installation may take a few minutes as it downloads and installs all dependencies. The InsightFace package is installed from the local repository in "editable" mode.

### Step 6: Verify Installation

```bash
# Test if InsightFace is installed correctly
python3 -c "import insightface; print('InsightFace version:', insightface.__version__)"

# Test if Gradio is installed
python3 -c "import gradio; print('Gradio version:', gradio.__version__)"
```

## 🚀 Running the Demo

### Start the Web Server

```bash
# Make sure you're in the face_mesh_demo directory and virtual environment is activated
cd ~/insightface/web-demos/face_mesh_demo
source venv/bin/activate  # If not already activated

# Run the demo
python3 app.py
```

The demo will start and you should see output like:
```
Running on local URL:  http://127.0.0.1:7860
Running on public URL: https://xxxxx.gradio.live (if sharing is enabled)
```

### Access the Web Interface

1. Open your web browser (Firefox, Chrome, etc.)
2. Navigate to: **http://localhost:7860**
3. The Face Mesh Topology Demo interface should load

### Using the Demo

#### Single Image Processing:
1. Go to the "Single Image" tab
2. Click "Upload Image" and select a JPG or PNG image
3. Click "🔍 Detect Face Mesh"
4. View the annotated result with face topology

#### Multiple Images Processing:
1. Go to the "Multiple Images" tab
2. Upload up to 3 images
3. Click "🔍 Detect Face Mesh in All Images"
4. View all results simultaneously

### Stop the Server

To stop the demo server:
- Press `Ctrl + C` in the terminal where the app is running

### Deactivate Virtual Environment

When you're done:
```bash
deactivate
```

## 📁 Project Structure

```
face_mesh_demo/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 🔧 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'insightface'"

**Solution**: Make sure you're in the virtual environment and have installed requirements:
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Issue: "No faces detected in the image"

**Solution**: 
- Ensure the image contains visible faces
- Try images with frontal face views
- Check that the image is not too small or too blurry
- Lighting conditions should be reasonable

### Issue: OpenCV errors on Linux Mint

**Solution**: Install OpenCV system dependencies:
```bash
sudo apt install libgl1-mesa-glx libglib2.0-0 -y
```

### Issue: Permission denied when running app.py

**Solution**: Make the file executable:
```bash
chmod +x app.py
```

### Issue: Port 7860 already in use

**Solution**: Either:
1. Stop the other application using that port, or
2. Edit `app.py` and change the port number in the last line:
   ```python
   demo.launch(server_name="0.0.0.0", server_port=7861, share=False)
   ```

## 🎯 Advanced: 3D Face Mesh Reconstruction

This demo shows basic face detection and landmark topology. For advanced **3D face mesh reconstruction**, InsightFace provides the JMLR method:

### Location:
```
insightface/reconstruction/jmlr/
```

### Features:
- Full 3D face mesh with 1220+ vertices
- Perspective projection-based reconstruction
- Detailed facial geometry
- Eye gaze detection (optional)

### To use JMLR:
1. Follow the instructions in `reconstruction/jmlr/README.md`
2. Download pretrained models
3. Prepare the projection matrix and flip index files
4. Run inference with `inference_simple.py`

**Note**: JMLR requires additional setup and pretrained models (see the JMLR directory for details).

## 🔗 Related Resources

- **InsightFace GitHub**: https://github.com/deepinsight/insightface
- **InsightFace Website**: https://insightface.ai
- **Model Zoo**: https://github.com/deepinsight/insightface/wiki/Model-Zoo
- **Python Package Docs**: https://github.com/deepinsight/insightface/tree/master/python-package
- **JMLR Paper**: https://arxiv.org/abs/2208.07142

## 💡 Tips

1. **Image Quality**: Use clear, well-lit images for best results
2. **Face Size**: Faces should be reasonably sized in the image (not too small)
3. **Multiple Faces**: The demo can detect and process multiple faces in a single image
4. **GPU Acceleration**: To use GPU for faster processing, install `onnxruntime-gpu` instead of `onnxruntime`
   ```bash
   pip uninstall onnxruntime
   pip install onnxruntime-gpu
   ```
5. **Sharing**: To share your demo with others on your network, edit `app.py` and set `share=True` in the launch command

## 📝 System Requirements

### Minimum:
- CPU: Dual-core 2.0 GHz+
- RAM: 4 GB
- Disk: 2 GB free space
- OS: Linux Mint 20+ (or Ubuntu 20.04+)
- Python: 3.8+

### Recommended:
- CPU: Quad-core 3.0 GHz+
- RAM: 8 GB
- GPU: NVIDIA GPU with CUDA support (optional, for faster processing)
- Disk: 5 GB free space
- OS: Linux Mint 21+
- Python: 3.10+

## 🤝 Contributing

This is a demo application. For contributions to the main InsightFace project:
- Visit: https://github.com/deepinsight/insightface
- Check the contributing guidelines
- Submit issues or pull requests

## 📄 License

This demo is part of the InsightFace project and follows the same MIT License.
- Code: MIT License (free for commercial and academic use)
- Models: Non-commercial research use only

## 👥 Authors & Credits

- **InsightFace Team**: Jia Guo, Jiankang Deng, and contributors
- **Demo Author**: Created as part of InsightFace examples
- **Technology**: InsightFace, Gradio, OpenCV, PyTorch/ONNX

## 📧 Support

For issues specific to this demo:
- Open an issue on the GitHub repository

For general InsightFace questions:
- Check the documentation: https://insightface.ai
- Visit the GitHub issues page: https://github.com/deepinsight/insightface/issues

---

**Enjoy exploring face topology detection with InsightFace! 🎭**
