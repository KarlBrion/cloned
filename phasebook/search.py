from flask import Blueprint, request
from .data.search_data import USERS

bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    results = []
    seen = set()

    for user in USERS:
        if 'id' in args and args['id'] == user['id']:
            results.append(user)
            seen.add(user['id'])
        elif 'name' in args and args['name'].lower() in user['name'].lower():
            if user['id'] not in seen:
                results.append(user)
                seen.add(user['id'])
        elif 'age' in args:
            try:
                age = int(args['age'])
                if age - 1 <= user['age'] <= age + 1:
                    if user['id'] not in seen:
                        results.append(user)
                        seen.add(user['id'])
            except ValueError:
                pass
        elif 'occupation' in args and args['occupation'].lower() in user['occupation'].lower():
            if user['id'] not in seen:
                results.append(user)
                seen.add(user['id'])

    return results
