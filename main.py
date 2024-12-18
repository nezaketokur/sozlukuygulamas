import os
from flask import Flask, render_template, request

app = Flask(__name__)

# Çiçek isimlerini ve resim dosyalarını tanımlayan bir sözlük
data = {
    "lale": "static/images/lale.jpg",
    "zambak": "static/images/zambak.jpg",
    "papatya": "static/images/papatya.jpg",
    "sümbül": "static/images/sumbul.jpg",
    "gül": "static/images/gul.jpg",
    "manolya": "static/images/manolya.jpg",
    "lavanta": "static/images/lavanta.jpg",
    "orkide": "static/images/orkide.jpg",
    "yasemin": "static/images/yasemin.jpg",
    "zakkum": "static/images/zakkum.jpg"
}

@app.route("/arama")
def index():
    return render_template("arama.html")

@app.route("/search", methods=["POST"])
def search():
    query = request.form.get("query").lower()
    image_path = data.get(query, None)
    if image_path:
        return render_template("result.html", item=query, image=image_path)
    else:
        return render_template("result.html", item=None, image=None)

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
