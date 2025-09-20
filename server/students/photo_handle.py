def convert_image(img_data):
    from PIL import Image
    import base64
    import io

    # Full base64 string (with data:image/png;base64, prefix removed)
    base64_str = img_data

    # Strip header if present
    if base64_str.startswith("data:image"):
        base64_str = base64_str.split(",")[1]

    # Fix padding issue
    missing_padding = len(base64_str) % 4
    if missing_padding:
        base64_str += "=" * (4 - missing_padding)

    # Decode and convert to Pillow
    image_data = base64.b64decode(base64_str)
    image = Image.open(io.BytesIO(image_data))
    return image

def face_compare(roll, img_data):
    from face_check import face_check
    import sqlalchemy
    conn=sqlalchemy.create_engine('sqlite:///../students/Databases/images.db', echo=False).connect()
    result=conn.execute(sqlalchemy.text(f"SELECT image FROM images WHERE roll='{roll}'"))
    result=result.fetchall()
    data=result[0][0]
    image1 = convert_image(img_data)
    image2 = convert_image(data)

    status = face_check(image1,image2)
    return status

