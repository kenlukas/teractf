from flask import Flask, render_template, request, redirect, url_for, send_file, make_response, send_from_directory

app = Flask(__name__, static_folder='static')

@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route('/')
def index():
    image_url = 'https://tenor.com/v5ZDFLHxgtW.gif'
    response = make_response(render_template('index.html', image_url=image_url))
    response.set_cookie('flag_part_3','Wh@t_c0uLd_g0_wr0ng?}', max_age=3600)
    return response
#    return render_template('index.html')

#@app.route('/hidden')
#def hidden():

#@app.route('/save_the_env', methods=['GET'])
#def save_the_env():
#    path = "../../../../../../../proc/self/environ"
#    #path = "../../../../../../../etc/passwd"
#    pic = "sad_flower.jpg"
#    filename = request.args.get('file')
#    content = ""
#    if filename in path:
#        with open(filename, "r") as file:
#            content = file.read()
#        return render_template("save_the_env.html", content=content)
#    elif filename in pic:
#        #return send_file(f'./static/{filename}')
#        return render_template("sad_flower.html")
#    else:
#        #return "<center><h1>You know the environment can't be saved with a click</h1></center>"
#        return render_template('not_the_env.html')
#
#
#@app.route('/save_the_env_img', methods=['GET'])
#def save_the_env_img():
##    return save_the_env_img(request, app)
#    image_path = f"{'static'}/{request.args.get('img')}"
#    #return send_file(image_path)
#    return image_path
#
#    return send_file(image_path)
#
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
