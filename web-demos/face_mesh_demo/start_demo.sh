#!/bin/bash
# Quick start script for Face Mesh Demo

echo "========================================"
echo "Face Mesh Topology Demo - Quick Start"
echo "========================================"
echo ""

# Check if we're in the correct directory
if [ ! -f "app.py" ]; then
    echo "Error: Please run this script from the face_mesh_demo directory"
    echo "Usage: cd web-demos/face_mesh_demo && ./start_demo.sh"
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Creating one..."
    if ! python3 -m venv venv; then
        echo "Error: Failed to create virtual environment"
        echo "Please install python3-venv: sudo apt install python3-venv"
        exit 1
    fi
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Check if dependencies are installed
echo "Checking dependencies..."
if ! python3 -c "import gradio" 2>/dev/null; then
    echo "Dependencies not installed. Installing now..."
    pip install --upgrade pip
    
    if ! pip install -r requirements.txt; then
        echo "Error: Failed to install dependencies"
        exit 1
    fi
    
    # Install InsightFace from local package
    if [ -d "../../python-package" ]; then
        echo "Installing InsightFace from local package..."
        if ! pip install -e ../../python-package/; then
            echo "Warning: Failed to install local InsightFace package"
            echo "Installing InsightFace from PyPI..."
            pip install insightface
        fi
    else
        echo "Warning: Could not find python-package directory"
        echo "Installing InsightFace from PyPI..."
        pip install insightface
    fi
fi

echo ""
echo "========================================"
echo "Starting Face Mesh Demo..."
echo "========================================"
echo ""
echo "The demo will be available at:"
echo "  http://localhost:7860"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

# Run the demo
python3 app.py
