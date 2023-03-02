from fastapi import Depends

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
