
def face_check(img1_png,img2_png):
    import face_recognition
    import numpy as np
    
    img1_png=img1_png.convert("RGB")
    img2_png=img2_png.convert("RGB")
    img1_np = np.array(img1_png)
    img2_np = np.array(img2_png)

    # Get face encodings
    enc1 = face_recognition.face_encodings(img1_np)
    enc2 = face_recognition.face_encodings(img2_np)

    if not enc1 or not enc2:
        print("No face found in one of the images 😢")
        return

    # Compare faces
    results = face_recognition.compare_faces([enc1[0]], enc2[0])
    distance = face_recognition.face_distance([enc1[0]], enc2[0])[0]

    print("Same person? 👉", results[0])
    print("Difference Score (lower = more similar):", distance)
    if results[0]:
        return "Face Matched"
    else:
        return "Face Not Matched"


def convertttt(img):
    from pillow_heif import register_heif_opener
    register_heif_opener()
    from PIL import Image
    import os

    img_open = Image.open(img)
    img_format = img_open.format

    # Ensure absolute path
    img_abs_path = os.path.abspath(img)
    dir_name = os.path.dirname(img_abs_path)       # folder path
    base_name = os.path.splitext(os.path.basename(img_abs_path))[0]  # filename without ext

    new_name = os.path.join(dir_name, base_name + ".png")  # full path to PNG

    # Save only if not already PNG
    if img_format != "PNG" or not os.path.exists(new_name):
        img_open.save(new_name, format="PNG")
        print("Saved as:", new_name)

    return new_name
