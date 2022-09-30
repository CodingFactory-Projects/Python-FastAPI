from fastapi import FastAPI, HTTPException
import json

from classes.SneakersClass import EditedSneaker, Sneakers
from classes.UsersClass import User
from classes.ShopsClass import shops
from classes.OrdersClass import Order

app = FastAPI()


# Function to load data from json file
def load_data():
    with open('data.json') as f:
        return json.load(f)


data = load_data()


def write_data():
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=2, separators=(',', ': '))


# Function to get users from data.json
@app.get("/users/")
async def get_users():
    # Return users from data.json
    return data['users']


# Function to get user by id
@app.get("/users/{user_id}")
async def get_user_by_id(user_id: int):
    for user in data['users']:
        # If user_id is equal to user id
        if user_id == user['id']:
            # Return user
            return user


# Function to post users from data.json
@app.post("/users/")
async def create_user(user: User):
    """
    This function will create a new user and rewrite the data.json file
    :param user: User object
    :return: data['users']
    """

    data['users'].append(user.dict())
    write_data()
    return data['users']


# Function to delete users by id

@app.delete("/users/{user_id}")
async def delete_users(user_id: int):
    """
    This function will delete a user by id and rewrite the data.json file
    :param user_id: integer id
    :return: data
    """
    for user in data['users']:
        if user_id == user['id']:
            # Remove user from data['users'] if condition is true
            data['users'].remove(user)
            write_data()
            return data


# Function to modify 1 element of users info by id

@app.patch("/users/{user_id}")
async def update_user(user_id: int, user: User):
    """
    This function will update a user by id and rewrite the data.json file
    :param user_id: integer
    :param user: Base model
    :return: modified data
    """
    for users in data['users']:
        if user_id == users['id']:
            stored_user_data = users
            stored_user_model = User(**stored_user_data)
            update_data = user.dict(exclude_unset=True)  # exclude_unset=True will exclude the fields that are not set
            stored_user_model = stored_user_model.copy(update=update_data)  # Update user model with modified data
            users['username'] = stored_user_model.username
            users['money'] = stored_user_model.money
            write_data()
            return stored_user_model


@app.put("/users/{user_id}")
async def update_user_all(user_id: int, user: User):
    """
    This function will update a user by id and rewrite the data.json file
    :param user_id:
    :param user: Base model
    :return: modified data
    """
    for users in data['users']:
        if users['id'] == user_id:
            users['username'] = user.username or users['username']
            users['money'] = user.money or users['money']
            write_data()
            return "Sneaker as been updated"


# SHOP METHODS

@app.get("/shops")
async def get_shops():
    return data['shops']


# Get a specific shop by id
@app.get("/shop/{shop_id}")
async def get_shop(shop_id: int):
    for shop in data['shops']:
        if shop_id == shop['shop_id']:
            return shop


# Here we have the "post" methods
# We can create new shops
@app.post("/shops")
async def create_shop(shop: shops):
    data['shops'].append(shop.dict())
    write_data()
    return "shop"


# Here we have the "post" methods
# We can delete existing shops
# If the shop already exists, we can delete it, otherwise if it doesn't, we cannot delete it so an error is returned
@app.delete("/shops")
async def delete_shop(shop_id: int):
    for shop in data['shops']:
        if shop_id == shop['shop_id']:
            data['shops'].remove(shop)
            write_data()
            return data['shops']
    return HTTPException(status_code=404, detail="Shop doesnt exist")


# SNEAKERS METHODS

@app.get("/sneakers")
async def get_sneakers():
    return data['sneakers']


@app.get("/sneakers/{sneaker_id}")
async def get_sneaker(sneaker_id: int):
    # loop through the sneakers
    for sneaker in data['sneakers']:
        # if the sneaker id matches the id in the url return the sneaker info
        if sneaker_id == sneaker['id']:
            return sneaker
    return HTTPException(status_code=404, detail="Sneaker not found")


@app.get("/sneakers/name/{sneaker_id}")
async def get_sneaker_name(sneaker_id: int):
    # loop through the sneakers
    for sneaker in data['sneakers']:
        # if the sneaker id matches the id in the url return the sneakers name
        if sneaker_id == sneaker['id']:
            return sneaker["name"]
    return HTTPException(status_code=404, detail="Sneaker not found")


# POST METHOD
@app.post("/sneakers")
async def create_sneaker(new_sneaker: Sneakers):
    new_sneaker.id = data['sneakers'][-1]['id'] + 1
    # add the new sneaker to the data
    if new_sneaker.id not in [sneaker['id'] for sneaker in data['sneakers']]:
        data['sneakers'].append(new_sneaker.dict())
        write_data()
        return "Sneaker has been added"
    return HTTPException(status_code=404, detail="Sneaker already exists")


@app.put("/sneakers/{sneaker_id}")
async def update_sneaker(sneaker_id: int, edited_sneaker: EditedSneaker):
    # loop through the sneakers
    for sneaker in data['sneakers']:
        # if the sneaker id is the same as the sneaker id in the url
        if sneaker['id'] == sneaker_id:
            sneaker['name'] = edited_sneaker.name or sneaker['name']
            sneaker['img'] = edited_sneaker.img or sneaker['img']
            sneaker['description'] = edited_sneaker.description or sneaker['description']
            sneaker['colors'] = edited_sneaker.colors or sneaker['colors']
            sneaker['price'] = edited_sneaker.price or sneaker['price']
            sneaker['stock'] = edited_sneaker.stock or sneaker['stock']
            write_data()
            return "Sneaker as been updated"
    return HTTPException(status_code=404, detail="Sneaker not found")


@app.delete('/sneaker/{sneaker_id}')
async def delete_sneaker(sneaker_id: int):
    # loop through the sneakers and find the sneaker with the id given
    for sneaker in data['sneakers']:
        if sneaker_id == sneaker['id']:
            data['sneakers'].remove(sneaker)
            write_data()
            return "Sneaker has been deleted"
    return HTTPException(status_code=404, detail="Sneaker not found")


# ORDER METHODS


# Get all commands from json
@app.get("/orders")
async def read_orders():
    return data["orders"]


# Retrieves orders based on its id
@app.get("/orders/{id_order}")
async def get_orders_by_order_id(id_order: int):
    for x in data["orders"]:
        if x["id_order"] == id_order:
            return x
    return "Not found"


# Update command thanks to its id_order
@app.patch("/orders")
async def update_orders_by_order_id(order: Order):
    for x in data["orders"]:
        if x["id_order"] == order.id_order:
            order.total_price = order.products.price * order.products.quantity
            with open('data.json', 'w') as f:
                data["orders"].remove(x)
                data["orders"].append(order.dict())
                write_data()
                return order
    return "Not found"


# Allows you to create an order
@app.post("/orders")
async def create_order(order: Order):
    for x in data["orders"]:
        if x["id_order"] == order.id_order:
            return "Your id_order is already use. Try again"
        else:
            order.total_price = order.products.price * order.products.quantity
            data["orders"].append(order.dict())
            write_data()
        return "Your order has been registered "


# Allows you to delete an order
@app.delete("/orders/{id_order}")
async def delete_order(id_order: int):
    for x in data["orders"]:
        if x["id_order"] == id_order:
            data["orders"].remove(x)
            write_data()
    return "Your order has been deleted "


# Allows you to delete all order
@app.delete("/orders")
async def delete_all_orders():
    for x in data["orders"]:
        data["orders"].clear()
        write_data()
    return "Your orders has been deleted "
