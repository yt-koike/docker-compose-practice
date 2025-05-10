from PIL import Image
print("Hello!")

for i in range(10):
    print(i)
    
img = Image.new("RGB",(100,100),(128,0,128))
img.save("a.png")