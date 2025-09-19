from deepface import DeepFace

img1=r"C:\Users\VenkatPrashad\Coding\Projects\AttendanceBackend\facev3.png"
img2=r"C:\Users\VenkatPrashad\Coding\Projects\AttendanceBackend\facev4.png"
result = DeepFace.verify(img1,img2,model_name="VGG-Face")
print(result)
