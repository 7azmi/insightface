#!/usr/bin/env python3
"""
Standalone Face Mesh Detection Script
This script demonstrates face mesh detection without the web interface.
Useful for testing and batch processing.
"""

import sys
import cv2
import numpy as np
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

try:
    from insightface.app import FaceAnalysis
    INSIGHTFACE_AVAILABLE = True
except ImportError:
    print("Error: InsightFace not available.")
    print("Please install it: pip install -e ../../python-package/")
    sys.exit(1)


def detect_face_mesh_standalone(image_path, output_path=None):
    """
    Detect face mesh from an image file.
    
    Args:
        image_path: Path to input image
        output_path: Path to save output image (optional)
    """
    print(f"Processing: {image_path}")
    
    # Read image
    img = cv2.imread(str(image_path))
    if img is None:
        print(f"Error: Could not read image: {image_path}")
        return None
    
    # Initialize face analysis
    print("Initializing face detection...")
    app = FaceAnalysis(allowed_modules=['detection'])
    app.prepare(ctx_id=-1, det_size=(640, 640))
    
    # Detect faces
    print("Detecting faces...")
    faces = app.get(img)
    
    if len(faces) == 0:
        print("No faces detected in the image")
        return None
    
    print(f"Found {len(faces)} face(s)")
    
    # Create output image
    output = img.copy()
    
    # Draw face bounding boxes and landmarks
    for idx, face in enumerate(faces):
        print(f"\nFace {idx+1}:")
        
        # Draw bounding box
        bbox = face.bbox.astype(int)
        print(f"  Bounding box: {bbox}")
        cv2.rectangle(output, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 255, 0), 2)
        
        # Draw facial landmarks
        if face.kps is not None:
            kps = face.kps.astype(int)
            print(f"  Landmarks: {len(kps)} keypoints")
            
            for i, (x, y) in enumerate(kps):
                # Different colors for different landmarks
                if i == 0 or i == 1:  # Eyes
                    color = (255, 0, 0)  # Blue
                    label = "eye"
                elif i == 2:  # Nose
                    color = (0, 255, 0)  # Green
                    label = "nose"
                else:  # Mouth corners
                    color = (0, 0, 255)  # Red
                    label = "mouth"
                
                cv2.circle(output, (x, y), 3, color, -1)
                print(f"    {label} {i}: ({x}, {y})")
            
            # Draw connections
            cv2.line(output, tuple(kps[0]), tuple(kps[1]), (255, 255, 0), 1)
            cv2.line(output, tuple(kps[2]), tuple(kps[0]), (255, 255, 0), 1)
            cv2.line(output, tuple(kps[2]), tuple(kps[1]), (255, 255, 0), 1)
            cv2.line(output, tuple(kps[3]), tuple(kps[4]), (255, 255, 0), 1)
            cv2.line(output, tuple(kps[2]), tuple(kps[3]), (255, 255, 0), 1)
            cv2.line(output, tuple(kps[2]), tuple(kps[4]), (255, 255, 0), 1)
        
        # Add face number label
        cv2.putText(output, f'Face {idx+1}', (bbox[0], bbox[1]-10),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    
    # Save output
    if output_path is None:
        input_path = Path(image_path)
        output_path = input_path.parent / f"{input_path.stem}_mesh{input_path.suffix}"
    
    cv2.imwrite(str(output_path), output)
    print(f"\nOutput saved to: {output_path}")
    
    return output


def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Face Mesh Detection - Standalone Script',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Process a single image
  python3 detect_mesh.py image.jpg
  
  # Process with custom output path
  python3 detect_mesh.py image.jpg -o result.jpg
  
  # Process example image
  python3 detect_mesh.py examples/t1.jpg
        """
    )
    
    parser.add_argument('image', type=str, help='Input image path')
    parser.add_argument('-o', '--output', type=str, default=None,
                       help='Output image path (default: input_mesh.jpg)')
    
    args = parser.parse_args()
    
    # Check if input file exists
    input_path = Path(args.image)
    if not input_path.exists():
        print(f"Error: Input file not found: {args.image}")
        sys.exit(1)
    
    # Process image
    result = detect_face_mesh_standalone(args.image, args.output)
    
    if result is not None:
        print("\n✓ Processing complete!")
    else:
        print("\n✗ Processing failed")
        sys.exit(1)


if __name__ == "__main__":
    main()
