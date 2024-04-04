from flask import (
    Flask,
    request,
    redirect,
    url_for,
    render_template,
    make_response,
    session,
    abort,
)


app = Flask(__name__)
app.secret_key = "ASDASDASDASDASDASD"

# domen.kz/
# @app.route("/")
# def welcome():
#     return "Teacher`s Welcome Page"


# domen.kz/some-page
@app.route("/")
def index():
    return render_template("login.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session["username"] = request.form["username"]
        if request.form["username"] == "admin":
            return redirect(url_for("success"))
        else:
            abort(401)
    else:
        return redirect(url_for("index"))


@app.route("/success")
def success():
    return "logged in successfully"


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))


@app.route("/students/<name>/<age>")
def find_student(name, age):
    random_dict = {"phy": 50, "che": 60, "maths": 70}
    return render_template(
        "user.html",
        name=name,
        age=1,
        random_dict=random_dict,
    )


@app.route("/reviews/<float:rating>")
def find_reviews(rating):
    return f"Поиск отзывов с рейтингом - {rating}"


# @app.route("/login", methods=["POST", "GET"])
# def login():
#     if request.method == "POST":
#         # request.form - получают параметры из тела запроса вида x-www-form-urlencoded
#         username = request.form.get("username")
#         password = request.form.get("password")

#         return f"Отправился POST запрос. Отправлены данные: {username}, {password}"
#     elif request.method == "GET":

#         # request.args - получают QUERY PARAMS из ссылки запроса.
#         username = request.args.get("username")
#         password = request.args.get("password")

#         return f"Отправился GET запрос. Отправлены данные: {username}, {password}"


@app.route("/redirect-url")
def redirect_url():
    return redirect("https://google.com")


@app.route("/redirect-url-local")
def redirect_url_local():
    return redirect(url_for("some_page"))


@app.route("/login-page")
def login_page():
    return render_template("login.html")


@app.route("/my-page")
def my_page():
    return render_template("student.html")


@app.route("/set-cookie")
def set_cookie():
    response = make_response(render_template("cookie.html"))
    response.set_cookie("NAME", "Biba")
    return response


@app.route("/delete-cookie")
def delete_cookie():
    response = make_response(render_template("cookie.html"))
    response.delete_cookie("NAME")
    return response


@app.route("/get-cookie")
def get_cookie():
    name_cookie = request.cookies.get("NAME")
    return f"<h1>{name_cookie}</h1>"


@app.route("/static-example")
def static_example():
    return render_template("student.html")


@app.route("/name", methods=["get"])
def name_hmtl():
    response = make_response(render_template("name.html"))
    name = request.args.get("name")
    response.set_cookie("NAME", f"{name}")
    return response


@app.route("/welcome")
def welcome():
    name = request.cookies.get("NAME")
    return f"Привет, {name}!"


app.run(
    debug=True,
    host="0.0.0.0",
)
