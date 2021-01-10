import ssl

from website.app import create_app


app = create_app({
    'SECRET_KEY': 'secret',
    'OAUTH2_REFRESH_TOKEN_GENERATOR': True,
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///db.sqlite',
    'OAUTHLIB_INSECURE_TRANSPORT':1

})

import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

#app.run()
#
# context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
# context.verify_mode = ssl.CERT_REQUIRED
# context.load_verify_locations("localhost.crt")
# context.load_cert_chain("localhost.crt", "localhost.key")

app.run(ssl_context="adhoc")
