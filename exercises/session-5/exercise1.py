from flask import Flask, render_template

app = Flask("Exercise 1")

def check_db_if_user_is_logged_in(user):
    if user == "Pepe" or user == "JJ":
        return True
    else:
        return False

@app.route("/")
def index():
    tweets_list = [
        {"name": "Pepe", "tweet": "Just setting up my twittr"},
        {"name": "Diego", "tweet": "Sloths grow moss"}]

    return render_template("tweets.html", tweets=tweets_list)


@app.route("/<name>/<height>")
def name_and_height(name, height):
    logged_in = check_db_if_user_is_logged_in(name)

    return render_template(
        "exercise1.html",
        name=name,
        height=height,
        logged_in=logged_in)

app.run(port=8080, debug=True)



def salute(name, last_name):
    print("hello " + name)


# salute("Felipe", "Fischel")
# salute("Felipe", last_name="Fischel") # correct
# salute(name="Felipe", "Fischel") # incorrect