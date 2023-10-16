from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        pilihan = request.form['pilihan']
        if pilihan == 'ya':
            pilihan2 = request.form['pilihan2']
            if pilihan2 == 'ya':
                result = "Selamat, Anda berdua bisa pacaran!"
            else:
                result = "Sayangnya, dia tidak suka Anda. Mungkin suatu saat nanti!"
        elif pilihan == 'tidak':
            result = "Maaf, Anda tidak bisa bersama dengannya untuk selamanya."
        else:
            result = "Pilihan tidak valid. Silakan masukkan 'ya' atau 'tidak'."
        return render_template('index.html', result=result)
    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)
