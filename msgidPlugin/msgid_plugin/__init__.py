import uuid


def get_random_unique_msgid_plugin(uid, destination_cid):
    # Return a random message uuid
    return str(uuid.uuid4())
