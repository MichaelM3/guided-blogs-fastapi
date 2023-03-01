from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash:
    @classmethod
    def bcrypt(cls, password: str):
        return pwd_cxt.hash(password)

    @classmethod
    def verify(cls, hashed_password, plain_password):
        return pwd_cxt.verify(plain_password, hashed_password)
