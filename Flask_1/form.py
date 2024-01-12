from flask import Flask
from flask_opensearch import FlaskOpenSearch

app = Flask(__name__)

app.config['OPENSEARCH_HOST'] = "localhost"
app.config['OPENSEARCH_USER'] = "admin"
app.config['OPENSEARCH_PASSWORD'] = "admin"

opensearch = FlaskOpenSearch(
    app = app,
    use_ssl = True,
    verify_certs = False,
    ssl_assert_hostname = False,
    ssl_show_warn = False
)

@app.route('/')
def openSearch():
    with app.app_context():
       return str(opensearch.ping())


if __name__ == '__main__':
    app.run(debug=True)