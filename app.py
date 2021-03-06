"""Flask app for Cupcakes"""

from flask import Flask, request, redirect, jsonify, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "1234567890"

connect_db(app)
toolbar = DebugToolbarExtension(app)

#####################################################################
# -------------------------- Application -------------------------- #
#####################################################################


@app.route('/')
def show_cupcakes_and_form():
    """Show list of cupcakes and form to add new cupcakes."""
    cupcakes = Cupcake.query.all()
    return render_template('index.html', cupcakes=cupcakes)


#####################################################################
# -------------------------- API Requests ------------------------- #
#####################################################################

@app.route('/api/cupcakes')
def show_all_cupcakes():
    """Show all cupcake resources."""
    cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=cupcakes)


@app.route('/api/cupcakes/<int:id>')
def show_particular_cupcake(id):
    """Show a particular cupcake by cupcake id."""
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes', methods=['POST'])
def create_cupcake():
    """Create a new cupcake."""
    
    new_cupcake = Cupcake(
        flavor=request.json['flavor'],
        size=request.json['size'],
        rating=request.json['rating'],
        image=request.json['image'] or None,
    )

    # image = request.json.get('image', None)
    # if image != '' and image != None:
    #     new_cupcake['image'] = request.json['image']

    db.session.add(new_cupcake)
    db.session.commit()
    response_json = jsonify(cupcake=new_cupcake.serialize())
    return(response_json, 201)


@app.route('/api/cupcakes/<int:id>', methods=['PATCH'])
def update_cupcake(id):
    """Update a cupcake by cupcake id."""
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes/<int:id>', methods=['DELETE'])
def delete_cupcake(id):
    """Delete a cupcake by cupcake id."""
    cupcake = Cupcake.query.get_or_404(id)
    title = cupcake.flavor
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message=f"{title} cupcake deleted.")
