import uuid


def get_random_unique_msgid_plugin(pdu_type, uid, source_cid, destination_cid):
    # Return a random message uuid
    return str(uuid.uuid4())
