from flask import Flask, request, abort
from main import Solution

app = Flask(__name__)



@app.route("/", methods=['GET', 'POST'])
def solve_pow():
    if request.method == 'POST':
        solver = Solution()
        # x, n = request.form['x'], request.form['n']
        x, n = request.form.get("x", None), request.form.get("n", None)
        # print (f"x is '{x}', n is '{n}'")
        # r = type(x)
        # print(r)
        try:
            x = float(x)
            n = int(n)
            res = solver.myPow(x, n)
        except (ValueError, TypeError):
            abort(400)

        return str(res)
    else:
        return "<html><body><h1>THIS IS TEST APP</h1>" \
               "<form action='/' method = 'POST'>" \
               "Type value X "\
               "<input type='text' name='x'/><br/>" \
               "Type value n " \
               "<input type='text' name='n'/><br/>" \
               "<input type='submit' />" \
               "<form>" \
               "</body></html>"


if __name__ == "__main__":
    app.run(debug=True)