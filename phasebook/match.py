import time
from flask import Blueprint

from .data.match_data import MATCHES

bp = Blueprint("match", __name__, url_prefix="/match")

@bp.route("<int:match_id>")
def match(match_id):
    if match_id < 0 or match_id >= len(MATCHES):
        return "Invalid match id", 404

    fave_numbers_1, fave_numbers_2 = MATCHES[match_id]

    start = time.time()
    is_matched = is_match(fave_numbers_1, fave_numbers_2)
    end = time.time()

    msg = "Match found" if is_matched else "No match"

    return {"message": msg, "elapsedTime": end - start}, 200
def is_match(fave_numbers_1, fave_numbers_2):
    set_fave_numbers_1 = set(fave_numbers_1)
    set_fave_numbers_2 = set(fave_numbers_2)

    return set_fave_numbers_2 <= set_fave_numbers_1
