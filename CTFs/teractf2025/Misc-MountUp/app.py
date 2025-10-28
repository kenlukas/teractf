from flask import Flask, request, render_template
import secrets

app = Flask(__name__)
app.config["SECRET_KEY"] = secrets.token_hex(32)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/view')
def view():
    filename = request.args.get('filename')
    if not filename:
        return "Do you want to view a file or not?", 400
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content, 200
    except FileNotFoundError:
        return "File not found", 404
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=5000, debug=True)
    app.run(host='0.0.0.0', port=5000, debug=False)

