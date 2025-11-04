#!/usr/bin/env python3
"""
Test script for Face Mesh Demo
This script verifies that all dependencies are installed correctly.
"""

import sys

# Define package mappings
REQUIRED_PACKAGES = {
    "numpy": "numpy",
    "cv2": "opencv-python",
    "gradio": "gradio",
    "insightface": "insightface",
    "onnxruntime": "onnxruntime",
}


def check_imports():
    """Check if all required packages can be imported"""
    print("=" * 60)
    print("Testing Face Mesh Demo Dependencies")
    print("=" * 60)
    
    all_ok = True
    
    for module_name, package_name in REQUIRED_PACKAGES.items():
        try:
            # Dynamically import the module
            module = __import__(module_name)
            version = getattr(module, '__version__', 'unknown')
            print(f"✓ {package_name:20s} - OK (version: {version})")
        except ImportError:
            print(f"✗ {package_name:20s} - MISSING")
            print(f"  Install with: pip install {package_name}")
            all_ok = False
        except Exception as e:
            print(f"✗ {package_name:20s} - ERROR: {str(e)}")
            all_ok = False
    
    print("=" * 60)
    
    if all_ok:
        print("✓ All dependencies are installed correctly!")
        print("\nYou can now run the demo with:")
        print("  python3 app.py")
        return 0
    else:
        print("✗ Some dependencies are missing.")
        print("\nPlease install missing packages with:")
        print("  pip install -r requirements.txt")
        return 1


def test_basic_functionality():
    """Test basic InsightFace functionality"""
    print("\n" + "=" * 60)
    print("Testing Basic Functionality")
    print("=" * 60)
    
    try:
        from insightface.app import FaceAnalysis
        import numpy as np
        
        print("✓ Creating FaceAnalysis instance...")
        app = FaceAnalysis(allowed_modules=['detection'])
        print("✓ FaceAnalysis created successfully")
        
        print("✓ Preparing model (CPU mode)...")
        app.prepare(ctx_id=-1, det_size=(640, 640))
        print("✓ Model prepared successfully")
        
        # Create a dummy image
        dummy_image = np.zeros((480, 640, 3), dtype=np.uint8)
        print("✓ Testing detection on dummy image...")
        faces = app.get(dummy_image)
        print(f"✓ Detection test complete (found {len(faces)} faces in dummy image)")
        
        print("=" * 60)
        print("✓ Basic functionality test PASSED!")
        print("\nThe demo is ready to use!")
        return 0
        
    except Exception as e:
        print(f"✗ Functionality test FAILED: {str(e)}")
        print("\nPlease check your installation and try again.")
        return 1


if __name__ == "__main__":
    print("\n" + "🎭 Face Mesh Topology Demo - Dependency Check\n")
    
    # Check Python version
    print(f"Python version: {sys.version}")
    if sys.version_info < (3, 8):
        print("✗ Python 3.8 or higher is required!")
        sys.exit(1)
    
    # Check imports
    result1 = check_imports()
    
    if result1 == 0:
        # Test basic functionality
        result2 = test_basic_functionality()
        sys.exit(result2)
    else:
        sys.exit(result1)
