from flask import Flask, request, abort
from main import Solution

app = Flask(__name__)



@app.route("/", methods=['GET', 'POST'])
def solve_pow():
    if request.method == 'POST':
        solver = Solution()
        x, n = request.form.get("x", None), request.form.get("n", None)
        try:
            x = float(x)
            n = int(n)
            result = solver.myPow(x, n)
        except (ValueError, TypeError):
            abort(400)

        return str(result)
    else:
        return "<html><head><title>This Is Test App Title</title></head>"\
               "<body><h1>This Is Test App Head</h1>" \
               "<form action='/result' method = 'POST'>" \
               "Type value X "\
               "<input type='text' name='x' id='x'/><br/>" \
               "Type value n " \
               "<input type='text' name='n' id='n'/><br/>" \
               "<input type='submit' id='submit'/>" \
               "<form>" \
               "</body></html>"


@app.route("/result", methods=['POST'])
def solve_result():
    if request.method == 'POST':
        solver = Solution()
        x, n = request.form.get("x", None), request.form.get("n", None)
        try:
            x = float(x)
            n = int(n)
            result = solver.myPow(x, n)
        except (ValueError, TypeError):
            result = "Incorrect data, try again"
           # abort(400)
        res = f"<html><head><title>This Is Test App Title</title></head>"\
              f"<body><h1>This Is Test App Head</h1>" \
              f"<form action='/result' method = 'POST'>" \
              f"Type value X "\
              f"<input type='text' name='x' id='x'/><br/>" \
              f"Type value n " \
              f"<input type='text' name='n' id='n'/><br/>" \
              f"<input type='submit' id='submit'/>" \
              f"<p></p>" \
              f"Result is " \
              f"<form><div id ='result'>{result}</div>" \
              f"</body></html>"
        return res, 200, {'Content-Type' : 'text/html; charset=utf-8'}
    return

if __name__ == "__main__":
    app.run(debug=True)