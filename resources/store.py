"""Store resource definition."""
from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):
    """Store class definition."""

    def get(self, name):
        """Get Store by name."""
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'Store not found'}, 404

    def post(self, name):
        """Post a store."""
        if StoreModel.find_by_name(name):
            return {'message':
                    "Store with the name '{}' already exists"
                    .format(name)}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except Exception:
            return {'message': 'An error ocurrend creating the store'}, 500

        return store.json(), 201

    def delete(self, name):
        """Delete store by name."""
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {'message': 'Store deleted'}


class StoreList(Resource):
    """StoreList class definition."""

    def get(self):
        """Get Storelist."""
        return {'stores': list(map(lambda x: x.json(),
                                   StoreModel.query.all()))}
