from PIL import Image, ExifTags
import os

# 获取 EXIF 中 orientation 的字段编号
for orientation in ExifTags.TAGS.keys():
    if ExifTags.TAGS[orientation] == 'Orientation':
        ORIENTATION_TAG = orientation
        break

# 路径设置
input_folder = r'new_picture'
output_folder = r'fixed_new_picture'

if not os.path.exists(input_folder):
    print("❌ 输入路径不存在！请检查拼写或改成绝对路径。")
else:
    print("✅ 输入路径存在！可以开始处理图片。")
    
# 如果输出文件夹不存在，就创建
os.makedirs(output_folder, exist_ok=True)

# 遍历所有图片
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        try:
            image = Image.open(input_path)

            # 获取 EXIF 信息（有些图片没有）
            exif = image._getexif()
            if exif is not None and ORIENTATION_TAG in exif:
                orientation = exif[ORIENTATION_TAG]

                # 根据 orientation 值旋转图片
                if orientation == 3:
                    image = image.rotate(180, expand=True)
                elif orientation == 6:
                    image = image.rotate(270, expand=True)
                elif orientation == 8:
                    image = image.rotate(90, expand=True)

            image.save(output_path)
            print(f"✅ Fixed: {filename}")

        except Exception as e:
            print(f"❌ Failed: {filename}, reason: {e}")
