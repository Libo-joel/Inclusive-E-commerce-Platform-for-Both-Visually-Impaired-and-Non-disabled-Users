from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import utils
import os
import random
import json

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        users = utils.load_users()

        for user in users:
            if user['email'] == email and user['password'] == password:
                isAdmin = True  # Set isAdmin to True for demonstration
                # return render_template('home.html')
                return redirect(url_for('men'))

        # User not found or incorrect credentials
        return render_template('login.html', error='Invalid email or password')

    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        confirmPassword = request.form['confirm-password']

        if password != confirmPassword:
            return render_template('register.html', error='Passwords do not match')

        users = utils.load_users()
        users.append({'email': email, 'password': password})
        utils.save_users(users)

        isAdmin = True  # Set isAdmin to True for demonstration
        return redirect(url_for('login'))

    return render_template('register.html')


@app.route('/get_data', methods=['GET'])
def getData():
    try:
        with open('dataset.json', 'r') as file:
            dataset = file.read()
            return jsonify(dataset)
    except FileNotFoundError:
        return jsonify({"error": "Dataset not found"}), 404


@app.route('/home')
def men():
    return render_template('men.html')


@app.route('/women')
def women():
    return render_template('women.html')


@app.route('/accessiroes')
def accessiroes():
    return render_template('accessiroes.html')


@app.route('/cart')
def cart():
    return render_template('cart.html')


@app.route('/save_cart', methods=['POST'])
def save_cart():
    try:
        data = request.json
        cart_items = data.get('cart', [])
        # Process and store the cart items as needed
        print('Received Cart Items:', cart_items)
        return jsonify({'message': 'Cart items received successfully'})
    except Exception as e:
        print('Error:', e)
        return jsonify({'error': 'Failed to process cart items'}), 500


@app.route('/remove_cart_item', methods=['POST'])
def remove_cart_item():
    try:
        data = request.json
        item_id_to_remove = data.get('itemId')
        cart_items = data.get('cart', [])

        # Assuming you have a cart_items list storing the current cart state
        for item in cart_items:
            if item['itemId'] == item_id_to_remove:
                cart_items.remove(item)
                print(f'Removed item with itemId {item_id_to_remove} from the cart.')
                return jsonify({'message': f'Item removed from the cart with itemId {item_id_to_remove}'}), 200

        # If the item with the specified itemId is not found
        return jsonify({'error': f'Item with itemId {item_id_to_remove} not found in the cart'}), 404

    except Exception as e:
        print('Error:', e)
        return jsonify({'error': 'Failed to remove cart item'}), 500


if __name__ == '__main__':
    app.run(debug=True)
