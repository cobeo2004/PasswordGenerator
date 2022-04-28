
from PasswordGenerator.ProcessRandomPassword import RandomPassword

r = RandomPassword(25)
print(r.WithAllCases(_numbers=True, _symbol=True))