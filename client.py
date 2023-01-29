from flask import Flask, request, make_response

import subtitle

app = Flask(__name__)


@app.route('/')
def index():
    # A welcome message to test our server
    return "<h1>Welcome to our Xample API!</h1>"


@app.route('/subtitle', methods=['GET'])
def get_subtitle():
    word = request.args.get('word')
    url = subtitle.url + word
    subtitle_url_list = subtitle.getting_video_urls(url)
    json_obj = subtitle.jsonify(subtitle_url_list, word)
    print(json_obj)
    return make_response(
        json_obj
    )


if __name__ == "__main__":
    app.run(port=5000, threaded=True)
