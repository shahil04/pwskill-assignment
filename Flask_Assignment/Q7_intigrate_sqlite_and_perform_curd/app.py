# 7. Integrate a SQLite database with Flask to perform CRUD operations on a list of items.

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)