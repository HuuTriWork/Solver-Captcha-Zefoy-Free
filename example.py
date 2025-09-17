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


if __name__ == "__main__":
    solver = CaptchaSolver()

    # Test từ file captcha.png
    print("🔹 Test với file:")
    result_file = solver.solve_captcha(path_to_file="captcha.png")
    print("Captcha giải được:", result_file)

    # Test từ base64
    print("\n🔹 Test với base64:")
    with open("captcha.png", "rb") as f:
        b64 = base64.b64encode(f.read()).decode("utf-8")
    result_b64 = solver.solve_captcha(b64=b64)
    print("Captcha giải được:", result_b64)
