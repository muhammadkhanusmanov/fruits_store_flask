from flask import Flask, request
from db import GroceryDB


app = Flask(__name__)
db = GroceryDB()


# view all grocery
@app.route('/grocery')
def all_grocery():
    """Get all grocery"""
    fruits = db.all()
    html ='<html>'
    html+='<style>table, th, td {border: 1px solid black;border-collapse: collapse;}th, td {padding: 5px;text-align: left;}</style>'
    html += '<head><title>Shop</title></head>'
    html += '<body>'
    html += '<h1>My shop products</h1>'
    html +='''<table>
                <tr>
                    <th>Name</th>
                    <th>Quantity</th>
                    <th>Price</th>
                    <th>Type</th>
                </tr>
            '''
    for fruit in fruits:
        html += f"<tr><th>{fruit['name']}</th><th>{fruit['quantity']}</th><th>{fruit['price']}</th><th>{fruit['type']}</th></tr>"
    html += '</table>'
    html += '</body>'
    html += '</html>'
    return html


# view add grocery
@app.route('/grocery/add', methods=['POST'])
def add_grocery():
    """Add a grocery"""
    product=request.get_json(force=True)
    db.add(product)
    return 'Done'


# view all grocery by type
@app.route('/grocery/type/<type>')
def all_grocery_by_type(type):
    """Get all grocery by type"""
    product=db.get_by_type(type)
    if product==[]:
        html=f"""<html>
        <head>
            <meta charset="UTF-8">
            <title>Products</title>
        </head>
        <body>
            <h2 style="color: red;">{type} type product was not found in our product database😥</h2>
        </body>
        </html>
        """
    else:
        html='<html>'
        html+='<style>table, th, td {border: 1px solid black;border-collapse: collapse;}th, td {padding: 5px;text-align: center;}</style>'
        html+='<head><meta charset="UTF-8"><title>Products</title></head>'
        html+=f'<body><h2><b>{type.title()}</b> type list of products</h2><table>'
        html+='''<tr>
                    <th>Name</th>
                    <th>Quantity</th>
                    <th>Price</th>
                    <th>Type</th>
                </tr>
                '''
        for i in product:
            html+=f'''<tr>
                    <th>{i['name']}</th>
                    <th>{i['quantity']}</th>
                    <th>{i['price']}</th>
                    <th>{i['type']}</th>
                </tr>
            '''
        html+='</table></body></html>'
    return html

# view all grocery by name
@app.route('/grocery/name/<name>')
def all_grocery_by_name(name):
    """Get all grocery by name"""
    product=db.get_by_name(name)
    if product==[]:
        html=f"""<html>
        <head>
            <meta charset="UTF-8">
            <title>Products</title>
        </head>
        <body>
            <h2 style="color: red;"><b>{name.title()}</b> name product was not found in our product database😥</h2>
        </body>
        </html>
        """
    else:
        html='<html>'
        html+='<style>table, th, td {border: 1px solid black;border-collapse: collapse;}th, td {padding: 5px;text-align: center;}</style>'
        html+=f'''<head>
            <meta charset="UTF-8">
            <title>Products</title>
        </head>
        <body>
            <h2 style="color: red;"{name.title()} name list of products</h2>
            <table>
                <tr>
                    <th>Name</th>
                    <th>Quantity</th>
                    <th>Price</th>
                    <th>Type</th>
                </tr>
        '''
        for i in product:
            html+=f'''<tr>
                    <th>{i['name']}</th>
                    <th>{i['quantity']}</th>
                    <th>{i['price']}</th>
                    <th>{i['type']}</th>
                </tr>
            '''
        html+='</table></body></html>'
    return html

# view all grocery by price
@app.route('/grocery/price/<float:price>')
def all_grocery_by_price(price):
    """Get all grocery by price"""
    product=db.get_by_price(price)
    if product==[]:
        html=f"""<html>
        <head>
            <meta charset="UTF-8">
            <title>Products</title>
        </head>
        <body>
            <h2 style="color: red;">No product found with a price of <b>${price}</b></h2>
        </body>
        </html>
        """
    else:
        html='<html>'
        html+='<style>table, th, td {border: 1px solid black;border-collapse: collapse;}th, td {padding: 5px;text-align: center;}</style>'
        html+=f'''<head>
            <meta charset="UTF-8">
            <title>Products</title>
        </head>
        <body>
            <h2>List of products priced at <b>${price}</b></h2>
            <table>
                <tr>
                    <th>Name</th>
                    <th>Quantity</th>
                    <th>Price</th>
                    <th>Type</th>
                </tr>
        '''
        for i in product:
            html+=f'''<tr>
                    <th>{i['name']}</th>
                    <th>{i['quantity']}</th>
                    <th>{i['price']}</th>
                    <th>{i['type']}</th>
                </tr>
            '''
        html+='</table></body></html>'
    return html



if __name__ == '__main__':
    app.run(debug=True)