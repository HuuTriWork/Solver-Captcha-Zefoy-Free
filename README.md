# 🧩 Python OCR Captcha Solver

Hàm `solve_captcha` dùng để tự động nhận diện captcha thông qua API **OCR.Space**.  
Bạn có thể truyền vào **file ảnh captcha** hoặc **chuỗi base64**, hàm sẽ trả về text đã được nhận diện.  

---

## 📦 Cài đặt

1. Cài các thư viện cần thiết:
   ```bash
   pip install requests
   ```

---

## ⚙️ Cách sử dụng

### Import và gọi hàm
```python
import base64
import requests

class CaptchaSolver:
    def __init__(self):
        self.session = requests.Session()

    def solve_captcha(self, path_to_file=None, b64=None, delete_tag=['\n','\r']):
        if path_to_file:
            task = path_to_file
        else:
            open('temp.png', 'wb').write(base64.b64decode(b64))
            task = 'temp.png'

        request = self.session.post(
            'https://api.ocr.space/parse/image?K87899142388957',
            headers={'apikey': 'K87899142388957'},
            files={'task': open(task, 'rb')}
        ).json()

        solved_text = request['ParsedResults'][0]['ParsedText']
        for x in delete_tag:
            solved_text = solved_text.replace(x, '')

        return solved_text
```

---

## 🖼️ Ví dụ

### 1. Nhận diện captcha từ file ảnh
```python
solver = CaptchaSolver()
text = solver.solve_captcha(path_to_file="captcha.png")
print("Captcha giải được:", text)
```

### 2. Nhận diện captcha từ base64
```python
with open("captcha.png", "rb") as f:
    b64 = base64.b64encode(f.read()).decode("utf-8")

solver = CaptchaSolver()
text = solver.solve_captcha(b64=b64)
print("Captcha giải được:", text)
```

---

## 🔑 Lưu ý

- API key demo (`K87899142388957`) có thể bị giới hạn.  
- Bạn nên **tạo API key riêng** tại [OCR.Space](https://ocr.space/ocrapi) để dùng ổn định.  
- Nếu kết quả trả về rỗng, hãy thử **load captcha mới** hoặc kiểm tra lại chất lượng ảnh.

---

## 📜 License
MIT License – tự do sử dụng và chỉnh sửa.  
