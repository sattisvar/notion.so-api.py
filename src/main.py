from database import Databases
import settings

d = Databases(settings.settings['integration_token'])

print(d.databases[0])
