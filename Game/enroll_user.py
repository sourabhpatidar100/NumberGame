from cursor_object import cursor_obj, connection_obj

# username, new_first_name=None, new_score=None
class enrollment:
    def search_and_update_user(username):
        cursor_obj.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor_obj.fetchone()
        if user:
            return user[0]
        else:
            return None
        

    def register(username):

        is_user  = search_and_update_user(username)
        if not is_user:
            print("username not found in db please follow below steps to register: ")
            username = input("Enter Username: ")
            name = input("Enter First Name: ")

            cursor_obj.execute("INSERT INTO users (Username, First_Name) VALUES (?, ?)", (username, name))
            connection_obj.commit()
            is_user = search_and_update_user(username)


        return is_user
