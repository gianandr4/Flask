from flask import Flask
from flask import request

app = Flask(__name__)



@app.route("/dsa")
def index():

    celsius = request.args.get("celsius", "")
    sex = request.args.get('sex',"")
    number = request.args.get('number',"")
    # number = request.args.getlist('number','')
    bool = request.args.get('bool',"")

    if not bool == True: bool='False'


    if celsius:
        fahrenheit = fahrenheit_from(celsius)
    else:
        fahrenheit = ""

    return (
            """<h1>Title</h1>
            <form action="" method="get">
            Celsius temperature: <input type="text" name="celsius">
            <br /><input checked="checked" name="sex" type="radio" value="male" /> Male <br /> 
            <input name="sex" type="radio" value="female" /> Female <br />

            <select name='number'>
            
            <option value="1">One</option>
            <option value="2">Two</option>
            <option value="3">Three</option>
            <option value="4">Four</option>
            </select>
            
            <input name="bool" type="checkbox" value="True" /> Checkbox<br /> 

            
            
            
            
            <input type="submit" value="Convert to Fahrenheit">
            </form>
            
            """
          + "<br>Fahrenheit:...." + fahrenheit
          + "<br>Sex:..........." + sex
          + "<br>Number:........" + number
          + "<br>Bool:.........." + bool
    )



def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    try:
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
        return str(fahrenheit)
    except ValueError:
        return "invalid input"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)










