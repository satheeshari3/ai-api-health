from models.endpoint import Endpoint
from extensions import db

def create_endpoint(name, url):
    endpoint = Endpoint(name=name, url=url)

    db.session.add(endpoint)
    db.session.commit()

    return endpoint


def get_all_endpoints():
    return Endpoint.query.all()