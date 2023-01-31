# importing flask

from flask import Flask, request, render_template
from read_file import read_excel_file
from dropColumns import drop_columns
from nullcheck import drop_nan_values
from Encoding import label_encoder

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('DWT.html')


# route to html page - to show the options for User
@app.route('/data_wrangle', methods=["GET", "POST"])
def data_wrangle():
    if request.method == "POST":
        # getting file name from HTML form
        file_name = request.form.get("my_file")

        # read data from the source file
        df = read_excel_file(file_name)

        # drop na rows
        op_checked = request.form.get("null_Value")
        if op_checked is not None:
            df = drop_nan_values(df)

        # drop columns
        op_checked = request.form.get("drop_columns")
        if op_checked is not None:
            df = drop_columns(df)

        # Encoding
        op_checked = request.form.get("Encoding")
        if op_checked is not None:
            df = label_encoder(df)

    return render_template('DWT.html')


if __name__ == "__main__":
    app.run(host="localhost", port=int("5000"))
