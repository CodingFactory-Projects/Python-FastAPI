from fastapi import FastAPI
import json
from classes.UsersClass import User

app = FastAPI()


# Function to load data from json file
def load_data():
    with open('data.json') as f:
        return json.load(f)


data = load_data()


# Function to get users from data.json
@app.get("/users/")
async def get_users():
    return data['users']  # Return users from data.json


# Function to get user by id
@app.get("/users/{user_id}")
async def get_user_by_id(user_id: int):
    for user in data['users']:
        if user_id == user['id']:  # If user_id is equal to user id
            return user  # Return user


# Function to post users from data.json


@app.post("/users/")
async def create_user(user: User):
    """
    This function will create a new user and rewrite the data.json file
    :param user: User object
    :return: data['users']
    """

    with open('data.json', mode='w') as f:
        data['users'].append(user.dict())  # Append user to data.json if condition true
        f.write(json.dumps(data, indent=2, separators=(',', ': ')))
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
            data['users'].remove(user)  # Remove user from data['users'] if condition is true
            with open('data.json', mode="w") as f:
                f.write(json.dumps(data, indent=2, separators=(',', ': ')))
                print(data)
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
            with open('data.json', mode="w") as f:
                f.write(json.dumps(data, indent=2, separators=(',', ': ')))
                # Write modified data to data.json and separate with comma and colon
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
            with open('data.json', mode="w") as f:
                f.write(json.dumps(data, indent=2, separators=(',', ': ')))
                return "Sneaker as been updated"
