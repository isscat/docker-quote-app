from flask import Flask, render_template, jsonify
import random

class QuoteApp(Flask):
    def __init__(self, import_name):
        super().__init__(import_name)
        self.quotes = [
            "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
            "The purpose of our lives is to be happy. - Dalai Lama",
            "Life is what happens when you’re busy making other plans. - John Lennon",
            "Get busy living or get busy dying. - Stephen King",
            "You have within you right now, everything you need to deal with whatever the world can throw at you. - Brian Tracy"
        ]
        self.route("/", methods=["GET"])(self.index)
        self.route("/quote", methods=["GET"])(self.get_quote)

    def index(self):
        return render_template("index.html")

    def get_quote(self):
        quote = random.choice(self.quotes)
        return jsonify({"quote": quote})

app = QuoteApp(__name__)
