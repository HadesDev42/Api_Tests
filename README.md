# Api_Tests
Little test with apis

Start the program with 

    uvicorn api:app --reload

Welcome to this basic API, you have 3 methods : GET, POST, DELETE.
           
           
            "GET :
            "To get all the items, you can use the following url : http://localhost:8000/items
            "To get a specific item, you can use the following url : http://localhost:8000/items/id=<item_id>

            "POST :
            "To add an item, you can use the following url : http://localhost:8000/items/add?name=<NAME>

            "DELETE :
            "To delete an item, you can use the following url : http://localhost:8000/items/delete?id=<item_id>
