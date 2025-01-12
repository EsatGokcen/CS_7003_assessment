import hashlib
import os

# Hashes a password with a random salt using PBKDF2-HMAC-SHA256.
# Returns the salt and hash combined as a single string.
def hash_password(password: str) -> str:
    salt = os.urandom(16)
    hashed_password = hashlib.pbkdf2_hmac(
        'sha256', password.encode('utf-8'), salt, 100000
    )
    return salt.hex() + ':' + hashed_password.hex()

# Verifies a provided password against a stored salt:hash password string.
def verify_password(stored_password: str, provided_password: str) -> bool:
    salt, hashed_password = stored_password.split(':')
    salt = bytes.fromhex(salt)
    provided_hash = hashlib.pbkdf2_hmac(
        'sha256', provided_password.encode('utf-8'), salt, 100000
    )
    return provided_hash.hex() == hashed_password
