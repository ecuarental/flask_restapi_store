"""Item resource definition."""
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    """Item class definition."""

    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help="This field cannot be left blank!")
    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help="Every item needs a store_id.")

    def get(self, name):
        """Get item by name."""
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def post(self, name):
        """Post item by name."""
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(
                name)}, 400

        data = Item.parser.parse_args()

        item = ItemModel(name, **data)

        try:
            item.save_to_db()
        except Exception:
            return {"message": "An error occurred inserting the item."}, 500

        return item.json(), 201

    def delete(self, name):
        """Delete item."""
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'message': 'Item deleted'}
        return {'message': 'Item not found.'}, 404

    def put(self, name):
        """Put item by name."""
        data = Item.parser.parse_args()

        item = self.find_by_name(name)

        if item:
            item.price = data['price']
        else:
            item = ItemModel(name, **data)

        item.save_to_db()

        return item.json()


class ItemList(Resource):
    """ItemList class definition."""

    def get(self):
        """Get items list."""
        return {'items': list(map(lambda x: x.json(),
                                  ItemModel.query.all()))}
