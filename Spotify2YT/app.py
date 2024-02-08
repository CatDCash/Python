from flask import flask, request, url_for, session, redirect
import spotipy
from spotipy.oauth2 import SpotifyOAuth

app = Flask(__name__)

app.secret_key = "tAFDGSt3423FDSA3cx"
app.config['SESSION_COOKIE_NAME'] = 'Keyla Cookie'
