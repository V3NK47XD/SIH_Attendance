def convert(img):
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

def face_check():
    import face_recognition

    img1_path = "facev3.heic"
    img2_path = "facev4.heic"

    # Convert HEIC → PNG
    img1_png = convert(img1_path)
    img2_png = convert(img2_path)

    # Load converted PNGs using absolute path
    img1 = face_recognition.load_image_file(img1_png)
    img2 = face_recognition.load_image_file(img2_png)

    enc1 = face_recognition.face_encodings(img1)[0]
    enc2 = face_recognition.face_encodings(img2)[0]

    results = face_recognition.compare_faces([enc1], enc2)
    distance = face_recognition.face_distance([enc1], enc2)[0]

    print("Same person? 👉", results[0])
    print("Similarity Score (lower = more similar):", distance)

face_check()
