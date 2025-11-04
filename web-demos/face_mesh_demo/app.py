"""
Face Mesh Topology Demo - InsightFace
This demo showcases face mesh/topology detection from images using InsightFace's 3D face reconstruction.
"""

import gradio as gr
import cv2
import numpy as np
import sys
import os
from pathlib import Path

# Add parent directory to path to import insightface
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

try:
    from insightface.app import FaceAnalysis
    import insightface
    INSIGHTFACE_AVAILABLE = True
except ImportError:
    INSIGHTFACE_AVAILABLE = False
    print("InsightFace not installed. Please install it first.")


# Facial landmark indices (InsightFace 5-point landmarks)
LEFT_EYE = 0
RIGHT_EYE = 1
NOSE = 2
LEFT_MOUTH = 3
RIGHT_MOUTH = 4

# Color definitions for landmarks (BGR format for OpenCV)
LANDMARK_COLORS = {
    LEFT_EYE: (255, 0, 0),      # Blue
    RIGHT_EYE: (255, 0, 0),     # Blue
    NOSE: (0, 255, 0),          # Green
    LEFT_MOUTH: (0, 0, 255),    # Red
    RIGHT_MOUTH: (0, 0, 255),   # Red
}


def detect_and_visualize_face_mesh(image):
    """
    Detect faces and visualize face mesh topology.
    
    Args:
        image: Input image (numpy array)
    
    Returns:
        Annotated image with face mesh visualization
    """
    if not INSIGHTFACE_AVAILABLE:
        return None, "Error: InsightFace is not installed. Please run: pip install insightface"
    
    if image is None:
        return None, "Please upload an image"
    
    try:
        # Initialize face analysis
        app = FaceAnalysis(allowed_modules=['detection'])
        app.prepare(ctx_id=-1, det_size=(640, 640))  # Use CPU
        
        # Detect faces
        faces = app.get(image)
        
        if len(faces) == 0:
            return image, "No faces detected in the image"
        
        # Create output image
        output = image.copy()
        
        # Draw face bounding boxes and landmarks
        for idx, face in enumerate(faces):
            # Draw bounding box
            bbox = face.bbox.astype(int)
            cv2.rectangle(output, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 255, 0), 2)
            
            # Draw facial landmarks (5 keypoints)
            if face.kps is not None:
                kps = face.kps.astype(int)
                for i, (x, y) in enumerate(kps):
                    # Get color based on landmark type
                    color = LANDMARK_COLORS.get(i, (128, 128, 128))
                    cv2.circle(output, (x, y), 3, color, -1)
                
                # Draw topology connections
                # Connect eyes
                cv2.line(output, tuple(kps[LEFT_EYE]), tuple(kps[RIGHT_EYE]), (255, 255, 0), 1)
                # Connect nose to eyes
                cv2.line(output, tuple(kps[NOSE]), tuple(kps[LEFT_EYE]), (255, 255, 0), 1)
                cv2.line(output, tuple(kps[NOSE]), tuple(kps[RIGHT_EYE]), (255, 255, 0), 1)
                # Connect mouth corners
                cv2.line(output, tuple(kps[LEFT_MOUTH]), tuple(kps[RIGHT_MOUTH]), (255, 255, 0), 1)
                # Connect nose to mouth
                cv2.line(output, tuple(kps[NOSE]), tuple(kps[LEFT_MOUTH]), (255, 255, 0), 1)
                cv2.line(output, tuple(kps[NOSE]), tuple(kps[RIGHT_MOUTH]), (255, 255, 0), 1)
            
            # Add face number label
            cv2.putText(output, f'Face {idx+1}', (bbox[0], bbox[1]-10),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        
        info = f"✓ Detected {len(faces)} face(s)\n"
        info += "• Green boxes show face locations\n"
        info += "• Blue dots: Eyes\n"
        info += "• Green dot: Nose\n"
        info += "• Red dots: Mouth corners\n"
        info += "• Yellow lines: Face topology connections"
        
        return output, info
        
    except Exception as e:
        return None, f"Error processing image: {str(e)}"


def process_multiple_images(image1, image2, image3):
    """
    Process multiple images and return results.
    """
    results = []
    infos = []
    
    images = [img for img in [image1, image2, image3] if img is not None]
    
    if len(images) == 0:
        return None, None, None, "Please upload at least one image"
    
    combined_info = f"Processing {len(images)} image(s)...\n\n"
    
    for idx, img in enumerate(images):
        result, info = detect_and_visualize_face_mesh(img)
        results.append(result)
        combined_info += f"Image {idx+1}: {info}\n\n"
    
    # Pad results with None if needed
    while len(results) < 3:
        results.append(None)
    
    return results[0], results[1], results[2], combined_info


# Create Gradio interface
with gr.Blocks(title="Face Mesh Topology Demo - InsightFace") as demo:
    gr.Markdown("""
    # 🎭 Face Mesh Topology Detection Demo
    
    This demo showcases how to detect face topology (mesh structure) from images using **InsightFace**.
    
    ### Features:
    - 🔍 Automatic face detection
    - 📍 Facial landmark detection (eyes, nose, mouth)
    - 🕸️ Basic topology visualization
    - 📊 Support for single or multiple images
    
    ### How to use:
    1. Upload one or more images (JPG, PNG)
    2. Click "Detect Face Mesh" to process
    3. View the annotated results with face topology
    
    ---
    """)
    
    with gr.Tab("Single Image"):
        with gr.Row():
            with gr.Column():
                single_input = gr.Image(label="Upload Image", type="numpy")
                single_btn = gr.Button("🔍 Detect Face Mesh", variant="primary")
            
            with gr.Column():
                single_output = gr.Image(label="Result")
                single_info = gr.Textbox(label="Detection Info", lines=8)
        
        single_btn.click(
            fn=detect_and_visualize_face_mesh,
            inputs=[single_input],
            outputs=[single_output, single_info]
        )
        
        # Get example images
        example_dir = Path(__file__).parent / "examples"
        example_images = []
        if example_dir.exists():
            example_images = [str(f) for f in example_dir.glob("*.jpg")]
        
        if example_images:
            gr.Examples(
                examples=example_images,
                inputs=single_input,
                label="Example Images"
            )
        else:
            gr.Markdown("*No example images available. Upload your own images to test.*")
    
    with gr.Tab("Multiple Images"):
        gr.Markdown("Upload up to 3 images to process them together")
        
        with gr.Row():
            multi_input1 = gr.Image(label="Image 1", type="numpy")
            multi_input2 = gr.Image(label="Image 2 (Optional)", type="numpy")
            multi_input3 = gr.Image(label="Image 3 (Optional)", type="numpy")
        
        multi_btn = gr.Button("🔍 Detect Face Mesh in All Images", variant="primary")
        
        with gr.Row():
            multi_output1 = gr.Image(label="Result 1")
            multi_output2 = gr.Image(label="Result 2")
            multi_output3 = gr.Image(label="Result 3")
        
        multi_info = gr.Textbox(label="Detection Info", lines=10)
        
        multi_btn.click(
            fn=process_multiple_images,
            inputs=[multi_input1, multi_input2, multi_input3],
            outputs=[multi_output1, multi_output2, multi_output3, multi_info]
        )
    
    with gr.Tab("ℹ️ About"):
        gr.Markdown("""
        ## About This Demo
        
        This web demo demonstrates face topology detection using the **InsightFace** library.
        
        ### What is Face Topology?
        Face topology refers to the mesh structure and key points (landmarks) of a face. This includes:
        - Face boundaries (bounding boxes)
        - Key facial landmarks (eyes, nose, mouth)
        - Structural connections between landmarks
        
        ### Technology Used:
        - **InsightFace**: State-of-the-art 2D & 3D face analysis
        - **Gradio**: Modern web interface framework
        - **OpenCV**: Image processing
        
        ### Advanced 3D Reconstruction:
        For full 3D face mesh reconstruction with detailed topology, check out the JMLR (Joint Multi-view 
        Learning for Reconstruction) implementation in the `reconstruction/jmlr` directory of the InsightFace repository.
        
        ### Links:
        - [InsightFace GitHub](https://github.com/deepinsight/insightface)
        - [InsightFace Website](https://insightface.ai)
        
        ### Note:
        This demo uses basic face detection and landmark detection. For advanced 3D mesh reconstruction,
        additional models and processing are required (see JMLR method in the repository).
        """)


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860, share=False)
