from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello DevOps World! This is version 2.0"

if __name__ == '__main__':
    # قمنا بتغيير المنفذ هنا إلى 7860 ليتوافق مع الأنظمة السحابية
    app.run(host='0.0.0.0', port=7860)