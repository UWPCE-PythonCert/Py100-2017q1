
class Id:

    @staticmethod
    def _get_hash(string: str) -> str:
        from hashlib import md5
        return md5(string.encode()).hexdigest()
